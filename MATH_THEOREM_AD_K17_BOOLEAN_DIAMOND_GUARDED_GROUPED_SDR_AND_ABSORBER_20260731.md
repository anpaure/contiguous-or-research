# The `K17` Boolean-diamond tail: guarded grouped SDR and label-only absorbers

Date: 2026-07-31  
Lane: AD  
Status: exact theorem conditional on a fixed repeat factor of the prescribed
diamond topology.  The theorem corrects the distinction between the raw
twenty choices at a new centre and the full choices after its two external
core endpoints are enforced.  No repeat factor or `K17` word is claimed.

## 1. Fixed-factor deletion semantics

Let `P` be a fixed maximum-degree-two Johnson path on rank-seven owners.
For a carrier edge `e=vw`, put

\[
                         C_e=v\cap w,\qquad |C_e|=6.       \tag{1.1}
\]

A unique edge emits the rank-six source `C_e`.  A repeat edge chooses
`g_e in C_e` and emits

\[
                         A_e=C_e-\{g_e\},\qquad |A_e|=5.  \tag{1.2}
\]

At every internal owner (and at every repeat-incidence owner in the port
factor) the two emitted sources must have union equal to the owner.  Global
path endpoints instead use their separately specified prefix/suffix boundary
source.  If an internal owner's incident facets are `v-{x}` and `v-{y}` with
`x!=y`, the union row says:

* one repeat followed by one unique edge: the repeat deletion is not the
  opposite missing coordinate;
* two repeats: neither deletion is the opposite missing coordinate and the
  two deletion labels are unequal.

If the incident facets coincide, both emitted sources lie in one proper
facet of `v`; the union equation is impossible.  Distinct Johnson edges and
a rank-nine three-owner union do not imply facet distinctness.

## 2. Raw diamonds versus guarded pair lists

Assume the fixed repeat topology has `1879` newly activated owners, every
one incident with two distinct repeat edges, no repeat edge joining two new
owners, each pair edge's non-new endpoint being a `K`-port incident with
exactly one unique-core edge, and every other repeat edge isolated between
two such unique-core ports.  This is a prescribed conditional topology, not an existence claim.  It
partitions the `4534` repeat edges into

\[
       1879\text{ two-edge groups}+776\text{ singleton groups}.          \tag{2.1}
\]

### Theorem 2.1 (exact guarded Boolean-diamond lists)

Consider a two-edge group `e,f` at a new centre `v`.  If its two centre
facets are distinct, write

\[
 C_e=S\cup\{y\},\qquad C_f=S\cup\{x\},qquad |S|=5.     \tag{2.2}
\]

The centre alone permits exactly

\[
               (g_e,g_f)\in S^2,qquad g_e\ne g_f,      \tag{2.3}
\]

and hence exactly `20` ordered pairs.

At the other endpoint of `e`, compare `C_e` with the adjacent unique-core
facet.  Equal facets make the whole group impossible.  Otherwise the
one-repeat union equation forbids one coordinate.  If that coordinate is
already excluded by (2.3), put `F_e=varnothing`; otherwise put the corresponding
singleton in `F_e subset S`.  Define `F_f` analogously.  Before filtering by
a prescribed rank-five bank, the full group list is exactly

\[
 \mathcal O_v=\{(g_e,g_f):g_e\in S\setminus F_e,
          g_f\in S\setminus F_f, g_e\ne g_f\}.          \tag{2.4}
\]

Its cardinality is

\[
\begin{array}{c|c}
(|F_e|,|F_f|)=(0,0)&20\\
\text{exactly one active singleton}&16\\
F_e=F_f\ne\varnothing&12\\
F_e,F_f\text{ distinct nonempty singletons}&13.
\end{array}                                             \tag{2.5}
\]

For a singleton repeat edge, equal facets at either endpoint again give an
empty list.  Otherwise its two endpoint guards leave exactly four labels
when distinct and five when equal, before a prescribed-bank filter.

#### Proof

At the new centre, the two-repeat union equation forces both labels into
the common five-set and forces them unequal, proving (2.3).  Each external
unique edge contributes the one-repeat forbidden equality, proving (2.4).
For allowed-set sizes `5,5`, `4,5`, `4,4` with the same excluded element,
and `4,4` with distinct excluded elements, subtracting the allowed diagonal
gives `20,16,12,13`.  The singleton statement is the same calculation in a
six-set with two endpoint guards. \(\square\)

If a target bank `B_5` is prescribed, retain from each list only the labels
whose emitted target or targets lie in `B_5`.  Such filtering can shrink a
list below (2.5), including to zero.  If the bank is an output of the tail,
there is no prior bank filter.

## 3. Exact grouped-SDR equivalence

For each pair group, replace every guarded label pair by its unordered
two-target set `{A_e,A_f}`.  For each singleton, replace every guarded label
by its one-target set.  The edge identities make these encodings injective.

### Theorem 3.1 (independent-transversal form)

On the fixed factor, a literal rank-five deletion assignment exists if and
only if one can select one option from every group so that all selected
target sets are pairwise disjoint.  If `B_5` is prescribed with size `4534`,
the resulting injection is a bijection onto `B_5`; if it is not prescribed,
the selected union is the output bank.

Equivalently, make a graph `Gamma` whose vertices are guarded options, whose
parts are the groups, and whose cross-part edges join options sharing a
target.  Feasibility is exactly the existence of an independent transversal
of `Gamma`.

#### Proof

Theorem 2.1 has already compiled every owner-local union equation into the
guarded lists.  What remains is exactly injectivity of the emitted rank-five
targets.  Disjoint option sets are equivalent to that injectivity, and are
equivalent to an independent transversal by the definition of `Gamma`.
The prescribed-bank statement follows from equal finite cardinalities.
\(\square\)

For a group family `X`, let `N(X)` be the union of every target appearing in
an option of a group in `X`, and put

\[
             d(X)=2|X_{\rm pair}|+|X_{\rm single}|.     \tag{3.1}
\]

Then `|N(X)|>=d(X)` is necessary.  It is not sufficient for an arbitrary
grouped-choice system: the two pair lists

\[
        \{\{a,b\},\{c,d\}\},\qquad
        \{\{a,c\},\{b,d\}\}                           \tag{3.2}
\]

pass all union-size demands but have no disjoint pair of options.  This is
an abstract warning; (3.2) is not asserted to embed in the restricted
Boolean-diamond family.

## 4. Two exact sufficient absorber criteria

### Theorem 4.1 (option-load criterion)

For a target `T` and group `i`, let `rho(T,i)` be the number of options in
all groups other than `i` that contain `T`, and set

\[
                         \rho=\max_{T,i}\rho(T,i).       \tag{4.1}
\]

If every guarded group list has size at least

\[
                         \max\{1,4\rho\},               \tag{4.2}
\]

then the grouped SDR exists.

#### Proof

An option contains at most two targets, so its degree in `Gamma` is at most
`2rho`.  Haxell's independent-transversal theorem applies when every part
has size at least twice the maximum degree; for degree zero, explicit
nonemptiness is necessary and sufficient.  Thus (4.2) gives an independent
transversal, and Theorem 3.1 completes the proof. \(\square\)

The raw singleton bound four would require `rho<=1`; no such load estimate
is presently known for the `K17` factor.

### Theorem 4.2 (label-only augmenting-linkage absorber)

Suppose first that the unary occurrence-to-target graph has an injective
matching `M` saturating every repeat occurrence.  Its edges have already
passed bank membership, facet distinctness, centre-side unary restrictions,
and both external endpoint guards.  A pair centre is then bad exactly when
its two matched deletion labels coincide.

For each bad centre `b`, let `L_b` be a nonempty list of `M`-alternating
paths or cycles such that toggling a member:

1. preserves occurrence-to-target injectivity and every unary restriction;
2. makes `b` good;
3. creates no new bad centre; and
4. changes no physical carrier edge.

Treat the vertices of the selector as part-labelled copies `(b,L)`; if the
same physical linkage occurs in several lists, its copies conflict through
their shared support.  Join two linkage options when their
occurrence/target supports overlap or their simultaneous toggles fail any
listed row, and let `Delta_L` be the maximum degree of this complete conflict
graph.  If

\[
                         |L_b|\ge\max\{1,2\Delta_L\}     \tag{4.3}
\]

for every bad centre, then all bad centres can be repaired simultaneously.

#### Proof

Haxell gives one conflict-free linkage per bad centre.  Their toggles have
disjoint supports, preserve the injection, and commute.  Rows 1--3 leave
every pair centre good.  Row 4 shows the repeat path, its q8/h9 resources,
and its topology are unchanged. \(\square\)

When the target universe has unused vertices, linkage options may be
correctly oriented alternating reassignment paths ending at unused targets,
whose symmetric difference preserves saturation of every occurrence.  For
an exactly prescribed full bank they are alternating cycles.

## 5. Exact boundary

The following remain unproved:

* a clean acyclic unique-provider core;
* the `4534`-edge fresh-q8/injective-h9 repeat factor with the prescribed
  no-new-to-new diamond topology;
* nonempty guarded lists after a prescribed-bank filter;
* either quantitative condition (4.2) or (4.3); and
* residence, higher shadows, prefix/common-cap compatibility, or a `K17`
  word.

Thus the old undifferentiated common-cap gate is replaced at tail rank five
by an exact grouped-SDR/absorber gate **after topology**, but is not solved.

## 6. Independent local replay

The dependency-free audit

```text
scratch/audit_ad_k17_boolean_diamond_guarded_sdr_20260731.py
scratch/ad_k17_boolean_diamond_guarded_sdr_20260731.audit.json
```

enumerates the four sizes in (2.5), the singleton sizes `4/5`, a
distinct-edge/rank-nine equal-facet zero-domain fixture, and the abstract
counterexample (3.2).  Its canonical payload is

```text
28e02bb8a1ce7c3194f518044b453d473f81634416ea5c49c24e0f7837d46616
```
