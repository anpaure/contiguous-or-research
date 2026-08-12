# Independent audit of the K17 H-source triple aperture factorization

**Date:** 2026-08-03  
**Scope:** proof audit of
`MATH_THEOREM_K17_DROP12_H_SOURCE_TRIPLE_APERTURE_JOIN_FACTORIZATION_20260803.md`
on the canonical drop-12 parent.  No broad triple search was run.

Canonical compressed/final SHA-256 values:

```text
e878bf19654d8478b4552451a3b5c9a54716e1383d2513c59d680091e10b5ffb
fa49188250bf194c8218d8afb5bf5f9220e4a73fd1267824bc7ed0b2868bbb7c
```

## 1. Verdict

The provider-atom factorization, the external-host necessity lemma, the
three-option natural join, and all three advertised support counts are
correct.  In particular,

\[
 48,\qquad 384,\qquad 2565
\]

have the stated meanings.  The indexed evaluation is lossless provided
that an index posting retains the physical atom identity in addition to its
value signature.  That identity requirement is the one correction/clarification
needed in the draft.

The factorization is an exact occurrence oracle only.  It does not imply a
supplier improvement or a K17 word.

## 2. Independent derivation of the provider factorization

For a phase \(\phi\), a provider atom must be an **occurrence-labelled**
object

\[
 \xi=(\operatorname{kind},\operatorname{mode},v,a,
       \operatorname{family},\operatorname{root},\operatorname{owner}),
\]

where \(v\) is the physical row and \(a\) is its flag.  A base atom has no
mode label; an installed-host atom records its installing mode.  Two atoms
with equal families, roots, owners, and flags but different rows are still
different atoms.

Let \({\cal B}^{\phi}\) be the parent long-atom bank after the exact
reservation filter:

* every one of the 7,213 private rows is absent;
* a row reserved in phase \(\phi\) is absent;
* an opposite-phase-only reserved row occurs only at its incumbent flag;
* the ten materialized incumbent LLR hosts remain eligible whenever the
  preceding rules permit them.

For six-endpoint-disjoint \(I=\{e,f,g\}\), materialization changes this
bank by exactly

\[
 {\cal P}^{\phi}_{I}
 =
 \bigl({\cal B}^{\phi}\setminus
       \{B^{\phi}(d_x,a):x\in I,\ 0\le a<4\}\bigr)
 \;\dot\cup\;
 \{H^{\phi}(x,a):x\in I,\ 0\le a<4\}.                 \tag{2.1}
\]

Endpoint disjointness makes the displayed atom families disjoint.  There
are no other long-row changes.

For role \(x\), phase \(\phi\), and key
\(k=(q,\alpha,\beta)\), let
\({\cal A}^{\phi}_{x}(k)\) be the universal relation of ordered provider
atom pairs satisfying all exact incoming, outgoing, and common five-cell
predicates, with flags \(\alpha,\beta\).  The universe must contain the
identity-labelled host atoms for every possible installing mode.  Then

\[
 {\cal T}^{\phi}_{x}(k;I)
 ={\cal A}^{\phi}_{x}(k)\cap
   \bigl({\cal P}^{\phi}_{I}\times{\cal P}^{\phi}_{I}\bigr). \tag{2.2}
\]

This proves the donor-delete/host-insert factorization.  Notice that (2.2)
retains every physical tuple, not merely its declared key or provider-state
value.

A two-phase option for role \(x\) is a same-key pair
\((t_x^0,t_x^1)\) whose row-to-flag maps have a single-valued union.  Three
options form a packing exactly when their footprints are pairwise disjoint
inside each phase and the union of all six flag maps is a function.  The
reservation compatibility with the ten incumbent options has already been
compiled into (2.1).  This is precisely the natural join in the theorem
under audit, so its forward and reverse implications are exact.

## 3. Why the source must use \(h_f\) or \(h_g\)

Let \(e\) be one of the 468 authenticated unary-empty H sources.  Suppose a
triple option for \(e\) used neither installed external host.  Since the
triple bank has deleted \(d_f,d_g\), none of its tuples uses either deleted
row.  Removing \(f,g\) therefore changes none of the atoms used by the
option: the same two phase tuples, key, capacities, and coalesced flags give
an option in the unary child for \(e\).  This contradicts unary emptiness.
Thus

\[
 \{\phi:h_f\in F(t_e^\phi)\}\cup
 \{\phi:h_g\in F(t_e^\phi)\}\ne\varnothing.            \tag{3.1}
\]

The conclusion is a two-phase disjunction.  It does not say that every
phase uses an external host, that both external hosts are used, or that the
other provider is nonbase.

## 4. Independent support-pattern census

### 4.1 Unphased digraphs

There are six off-diagonal arcs on \(\{e,f,g\}\).  Equation (3.1) says that
at least one of \(e\to f,e\to g\) is present.  The other four arcs are free,
so the count is

\[
 (2^2-1)2^4=3\cdot16=48.                               \tag{4.1}
\]

The three loops are independent at this raw unphased level, giving

\[
 48\cdot2^3=384.                                       \tag{4.2}
\]

These 384 objects are only coarse support labels.  For example, a host with
three distinct incoming role arcs cannot be packed into two unit-capacity
phases.  Hence 384 must not be reported as a physical-support census.

### 4.2 Phase-labelled capacity supports

In one phase, each of the three installed host rows is assigned to one of
the three roles or is unused.  This gives \(4^3=64\) functions.  A role has
only two provider positions, so the three functions assigning all hosts to
one role are impossible.  Thus there are

\[
 64-3=61                                                   \tag{4.3}
\]

phase supports.

If source \(e\) uses neither external host in that phase, columns \(h_f,h_g\)
each have only three choices (unused, \(f\), or \(g\)), while \(h_e\) has
four.  Of the resulting \(4\cdot3^2=36\), the all-to-\(f\) and all-to-\(g\)
functions violate the two-provider bound.  Therefore 34 phase supports do
not rescue \(e\).  The phases are ordered, and (3.1) excludes exactly the
pairs in which neither phase rescues \(e\).  Hence

\[
 61^2-34^2=3721-1156=\boxed{2565}.                     \tag{4.4}
\]

This count prices installed-host capacity only.  Base-row capacity and all
cross-phase flag equalities remain predicates of the exact natural join.

## 5. Indexed host-aperture evaluation

The proposed index is exact with the following implementation discipline.

1. A **bucket key** may omit the row identity and use only
   \((\phi,a,\operatorname{family},\operatorname{root},
   \operatorname{owner})\).
2. Every posting in that bucket must still carry the installing mode,
   physical host row, donor row, tuple side, role, key, complete footprint,
   and flag map.
3. Every base posting carries its physical row as a kill label.  After
   selecting \(e,f,g\), discard a posting using any of
   \(d_e,d_f,d_g\).
4. Join a role's phases on its own declared key and flag consistency; do not
   join keys between different roles.
5. Before emission, enforce the six-endpoint condition, all three
   same-phase footprint constraints, and one global flag map.

Without item 2, two installed hosts with identical value signatures would
be coalesced.  That loses the distinction between a legal use of two
different physical rows and an illegal double use of one row, and it also
breaks endpoint filtering.  Thus the signature displayed in the draft is a
bucket signature, not by itself an exact provider-atom signature.  One may
instead repair the display by including \((y,h_y)\) in it.

Anchoring on a source posting using \(h_f\) or \(h_g\) is lossless by
(3.1).  If the source uses the two helpers in different phases, the two
postings must be joined on the source key and complete flag map.  If it uses
both in one phase, retain the two-host tuple posting.  A source using only
one helper does not determine the second helper; that helper must be found
from the remaining role relations.  These cases exhaust the exact join.

## 6. Sharp quadratic-output warnings

There are two separate quadratic phenomena.

### 6.1 Quadratically many helper-pair outputs

Consider an abstract occurrence instance obeying exactly the atom, capacity,
and coalescing semantics above.  Give one unary-empty source \(e\), and give
\(N\) helpers pairwise disjoint endpoints and indistinguishable compatible
host bucket signatures.  For every helper \(i\), let the source have a
same-key two-phase option which uses \(h_i\) at one fixed flag.  Let helper
\(i\) have a two-phase option on rows private to \(i\), and let every donor
row be absent from all these footprints.  All other rows are private, so
capacities never collide.

The source remains unary-empty because none of the \(h_i\) exists in its
unary child.  For every unordered pair \(\{i,j\}\), choose the source option
using \(h_i\) and the two private helper options.  This is a complete triple
packing.  Therefore the exact projected output has

\[
 \binom N2=\Theta(N^2)                                  \tag{6.1}
\]

records.  No explicit lossless enumeration can have subquadratic worst-case
output time under unary emptiness alone.

### 6.2 Quadratically many options behind one host aperture

Even for one installed helper host and one declared source key, suppose the
host-anchored phase-0 tuple list has \(r\) alternatives and the compatible
phase-1 list has \(s\) alternatives.  Give every alternative a private
nonhost row and the same flag on the shared helper host.  Then every
phase-0/phase-1 pair is a distinct exact source option, producing

\[
 rs                                                     \tag{6.2}
\]

option records.  For \(r=s=N\), the aperture output itself is quadratic.
Fixed tuple arity and constant-size state delta therefore do not imply a
constant-time or linear-output query.

The indexed construction remains valuable: it is output-sensitive and
avoids a blind \(468\times112621^2\) materialization.  It cannot promise an
unconditional subquadratic explicit output bound.

## 7. Proof-safe conclusion

After adding the atom-identity clarification, the audited theorem is exact:

\[
 \text{triple occurrence packing}
 \iff
 \text{one of the 2,565 labelled aperture joins is nonempty}.
\]

A negative complete join is an occurrence no-go.  A positive join must
retain a literal six-tuple witness, be jointly materialized, and undergo a
fresh supplier replay before any deficiency claim.
