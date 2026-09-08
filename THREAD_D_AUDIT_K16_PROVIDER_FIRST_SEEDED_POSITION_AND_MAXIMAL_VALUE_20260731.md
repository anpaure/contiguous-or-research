# Audit of the seeded provider-first position reduction and maximal second value

Date: 2026-07-31  
Lane: D  
Source audited: `scratch/search_k16_provider_first_seeded_exact_20260730.cpp`  
Status: proof of the candidate-position reduction; correction required before the maximal-value optimization

## 1. Verdict

Within its advertised **provider-first** branch, the source-seed plus
affected-component reduction of the second position is sound and complete.
It also retains mixed one-site/both-site interactions: after the first edit,
the exact pair delta contains the `p`-only, `q`-only, and both-site interval
classes, so the reduction is not a sequential-independence assumption.

The proposed collapse of the second-value interval is exact only after one
replaces the source variable called `upper` by the true target core

\[
 J_Z(q)=\bigcap\{t:\hbox{ every current }t\hbox{-witness in }Z
                         \hbox{ contains }q\}.
\]

The current source's `upper` is only the intersection of the intermediate
holes.  Testing that value alone is not complete: a represented target can
have every witness through `q`, impose an additional zero bit on the second
value, and be destroyed by the larger hole-intersection value.  Thus the
patch must compute the full forced-through target set (or an exactly
equivalent multiplicity test), not merely replace the existing submask loop
by one call at its current `upper`.

## 2. Exact provider bank

Fix a deletion word `W`, an original hole `h`, and a first site `p`.  An
interval containing `p` consists of a suffix ending at `p-1`, the new value
`x`, and a prefix starting at `p+1`.  If their fixed OR is `s`, it realizes
`h` exactly when

\[
 s\subseteq h,\qquad h\setminus s\subseteq x\subseteq h.
\]

`contexts_at` enumerates every such suffix/prefix OR, and `service_values`
enumerates exactly this Boolean interval of nonzero `x`.  Taking the union
over the input holes therefore enumerates every genuine first edit that by
itself supplies at least one deletion hole.  This is the full provider-first
bank, including partial providers.

## 3. Proof of the seeded second-position reduction

After a first edit `p:W_p -> x`, write the materialized word as `Z`.  For a
target `t` and prospective second site `q`, let `C_Y(q,t)` be the OR of the
maximal `t`-compatible run immediately left of `q` and the maximal
`t`-compatible run immediately right of `q` in a word `Y`, with the cell at
`q` omitted.  A value `y subseteq t` can make a through-`q` witness of `t`
if and only if

\[
 t\setminus y\subseteq C_Z(q,t).                    \tag{3.1}
\]

Let `D` be the exact hole set after the first edit and put

\[
 U=\bigcap_{d\in D}d.
\]

Every completing second value obeys `y subseteq U`.  Select any seed debt
`t in D` and put `R=t\setminus U`.  From (3.1), every completing position
must satisfy

\[
 R\subseteq C_Z(q,t).                               \tag{3.2}
\]

The cached source set is exactly the set of `q` satisfying
`R subseteq C_W(q,t)`.  It remains to locate sites where (3.2) changes truth
after editing `p`.

Changing one cell can alter `C_Y(q,t)` only if `p` belongs to one of the two
maximal compatible runs adjacent to `q`, or if changing the compatibility of
`p` merges or splits those runs.  Consequently every changed context lies
in the union of

* the old `t`-compatible component containing `p`, with its two adjacent
  boundary sites;
* the new `t`-compatible component containing `p`, with its two adjacent
  boundary sites;
* when `p` is an incompatible separator, the compatible components on its
  two sides, again with their boundary sites.

`add_affected_component` adds precisely a (possibly nonminimal) superset of
this union in both the source and edited states.  Hence a site satisfying
(3.2) is either already in the cached source set or is added by the affected
component routine.  The candidate-position reduction is complete.  Choosing
the seed with maximum `popcount(t & ~U)` changes only pruning strength, not
the proof.

This argument remains valid after the maximal-value patch.  The true core
`J_Z(q)` is a subset of `U`, so every feasible `J_Z(q)` witness still forces
`t\setminus U subseteq C_Z(q,t)`.

## 4. Mixed joint interactions are retained

For fixed `p<q`, `exact_pair_complete` removes and re-adds exactly the three
disjoint affected interval classes:

1. intervals containing `p` but not `q`;
2. intervals containing `q` but not `p`;
3. intervals containing both sites.

The third class uses `x OR interior OR y`; therefore it includes all cross
terms.  A first edit need only supply one original hole alone.  Remaining
original holes and newly ejected targets may be supplied by intervals
containing both edits.  The only excluded solutions are those in which no
changed site alone supplies any original hole; those are exactly the
separately stated all-joint branch.

## 5. Correct maximal-value patch

For the first-edited word `Z`, define

\[
 \mathcal R_Z(q)=\{t:\hbox{every }t\hbox{-witness in }Z
                         \hbox{ contains }q\},
 \qquad J_Z(q)=\bigcap_{t\in\mathcal R_Z(q)}t.
\]

Absent targets belong to `R_Z(q)` at every site.  A represented target
belongs exactly when the intersection of all its witness intervals contains
`q`; equivalently its total multiplicity equals its through-`q`
multiplicity.  These characterizations give two exact implementations.

If a value `y` completes at `q`, then `y subseteq J_Z(q)`.  If a fixed
context `s` has `s OR y=t`, then

\[
 y\subseteq J_Z(q)\subseteq t \quad\Longrightarrow\quad
 s\mathbin\vee J_Z(q)=t.
\]

Thus a completing value exists if and only if the single maximal value
`J_Z(q)` completes.  Testing it with `exact_pair_complete` (and literal
replay on a zero row) is sufficient.

By contrast, the current variable

\[
 U=\bigcap_{d\in D}d
\]

omits represented targets forced through `q`.  There is no implication
`U subseteq t` for such a target.  A smaller feasible value can preserve
`t` while `U` introduces a forbidden bit and destroys it.  Therefore a
literal patch that tests only the current `upper=U` is incomplete.

## 6. Incumbent/coatom corner

For a fixed true core `J`, feasible values form an upset inside `2^J`.  If
`J` equals the incumbent, any proper feasible value lies below a feasible
coatom `J\{b}`; testing at most 16 coatoms is a generally valid fail-closed
rule.

In the present provider-first census the intermediate word still has a
nonempty exact debt set (the empty-debt row is handled as a one-edit
completion).  Hence the incumbent cannot itself pass the forced-through
test: that would already witness every intermediate hole.  Monotonicity then
implies no smaller coatom can pass either.  With the frozen one-substitution
no-go, coatoms are therefore redundant, although retaining them is harmless
and makes the routine valid without relying on that frozen theorem.

## 7. Safe implementation contract

A patched exhaustive run may claim the provider-first branch only if it:

1. retains the current complete partial-provider enumeration;
2. retains the source-seed plus old/new affected-component position union;
3. computes `R_Z(q)` over **all 65535 nonzero targets**, not only first-edit
   holes;
4. tests `J_Z(q)` (and, if desired, the incumbent coatoms), rather than the
   old debt intersection `U`;
5. applies the exact two-site multiplicity delta and literal replay;
6. composes its result explicitly with the separately authenticated
   all-joint branch before claiming a full arbitrary two-substitution no-go.

