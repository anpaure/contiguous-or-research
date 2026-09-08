# Independent audit: capped lower-shadow compression and the partial-colex obstruction

**Date:** 2026-08-04  
**Verdict:** **GO AFTER ONE SCOPE CORRECTION.**  The complement identity,
compression theorem, capped Kruskal--Katona inequalities, partial-colex
census, heavy-facet deduction, and co-small formula are all correct.  The
original summary overextended the heavy-facet conclusion to every
low-slack family, although the proved theorem requires `m>=144` and
`|F|>=2m`.  The theorem has been patched to state those hypotheses in all
summary occurrences.  No mathematical formula or proved implication was
changed.

No computation, search, or solver result is used in this audit.

## 1. Artifact lineage

The original theorem audited had SHA-256

`43500aabc13cef9ecd54a3fbb93212255ebbae3e95a60985682dfa1fb1ede09c`.

After the scope-only correction, the final theorem

`MATH_THEOREM_CAPPED_LOWER_SHADOW_COMPRESSION_AND_PARTIAL_COLEX_OBSTRUCTION_20260804.md`

has SHA-256

`6e138117e2310bcc8087d3cc67cb07bd1702f0674b1ac1369298205b4fc1610f`.

The author self-audit was independently read and has SHA-256

`00d317714a412fcd46efd7c00e878a0f517ecab452dfe50e87bbb7c0e9f974fe`.

It was not used as evidence for the checks below.

## 2. Complement and capped-shadow identity

On `n=2m-1` points, complementation maps a lower vertex `X` of rank
`m-1` to an `m`-set and an owner `U` of rank `m` to an `(m-1)`-set.  Thus

\[
 X\subset U
 \quad\Longleftrightarrow\quad
 [n]\setminus U\subset[n]\setminus X,
\]

so `a_U=d_F([n]\setminus U)` exactly.  If `S=|partial F|` and `q_1` is
the number of degree-one facets, then

\[
 \Psi_2(F)=q_1+2(S-q_1)=2S-q_1.
\]

Since complementation preserves cardinality,

\[
 \sigma(A)=\Psi_2(F)-2|F|=2(S-|F|)-q_1.
\]

This verifies every part of Theorem 1.1.

## 3. Capped Kruskal--Katona bound

Every member of an `m`-uniform family has `m` facets, and any one facet
has at most `m` extensions on a `2m-1` point ground set.  Hence, writing
`f=|F|`,

\[
 mf=\sum_Dd_F(D)
 \le q_1+m(S-q_1),
\]

and therefore

\[
 q_1\le {m(S-f)\over m-1}.
\]

Substitution into the exact capped identity gives

\[
 \Psi_2(F)-2f
 \ge {m-2\over m-1}(S-f).
\]

Equality holds exactly when every positive nonunique facet degree is the
maximum `m`, equivalently all positive degrees lie in `{1,m}`.  Applying
ordinary Kruskal--Katona gives (2.3), and its real-binomial Lovasz form
gives (2.4).  On the two-covered face `q_1=0`, the identity reduces to

\[
 \Psi_2(F)-2f=2(S-f)\ge2(KK_m(f)-f).
\]

Every initial colex segment that is itself two-covered has
`S=KK_m(f)`, so it attains this bound.  The statement does not claim that
an initial colex segment is two-covered for every cardinality.

## 4. Compression monotonicity

For an `(i,j)` shift, facets containing neither shift coordinate retain
their extension degree: only the two extensions obtained by adding `i`
or `j` can move, and their total occupancy is unchanged.  Facets containing
both coordinates are untouched.

Every remaining facet belongs to a pair `C+i,C+j`.  Excluding their common
possible extension `C+i+j`, let `R_i,R_j` record the outside coordinates
that extend the two facets.  Coordinate shifting changes these to

\[
 R_i\cup R_j,qquad R_i\cap R_j.
\]

The common extension contributes the same additive zero or one to both
degrees.  Thus the new degree pair has the same sum and majorizes the old
pair.  Since `min(2,t)` is concave on the nonnegative integers, its sum on
the pair cannot increase.  Summing proves

\[
 \Psi_2(S_{ij}F)\le\Psi_2(F).
\]

Repeated shifts terminate and preserve cardinality, so a minimizer may be
chosen shifted.  Nothing in this argument asserts colex extremality, in
agreement with the theorem's scope warning.

## 5. Partial-colex staircase

For

\[
 F_{t,u}=\binom{[t]}m\ \dot\cup\
 \bigl(\{z\}+\binom{[u]}{m-1}\bigr),
 \qquad z=t+1,
\]

the positive facet types and degrees are

| facet | degree |
|---|---:|
| `D subset [t]`, `D not subset [u]` | `t-m+1` |
| `D subset [u]`, `|D|=m-1` | `t-m+2` |
| `{z}+J`, `J in binom([u],m-2)` | `u-m+2` |

All are at least two under `m+1<=t` and `m<=u<=t-1`.  Hence the family is
two-covered and its shadow is exactly

\[
 \binom{[t]}{m-1}\ \dot\cup\
 \bigl(\{z\}+\binom{[u]}{m-2}\bigr).
\]

This gives (4.3)--(4.4).  The binomial expression for its size is the
canonical colex expansion, so the shadow is exactly `KK_m(f)`.  The first
block is connected, and replacing `z` in any second-block member by any
point of `[t]\setminus H` joins it to the first block.  Thus connectivity
is also exact.

## 6. The `m=4q` counterfamily

Put `t=5q`, `u=5q-1`, and `f_0=binom(5q,4q)`.  Direct binomial ratios give

\[
 {f_1\over f_0}={4\over5},
 \qquad
 {\binom{5q}{4q-1}\over f_0}={4q\over q+1},
 \qquad
 {\binom{5q-1}{4q-2}\over f_1}={4q-1\over q+1}.
\]

Therefore `f=(9/5)f_0` and

\[
 {\sigma\over f}
 ={2(27q-13)\over9(q+1)}
 ={54m-104\over9m+36}
 =6-{320\over9m+36}<6.
\]

Also

\[
 f={9\over5}\binom{5q}q
 \le {9\over5}(5e)^q
 <2^{m+1}.
\]

All positive facet degrees are `q+1` or `q+2`, hence lie strictly between
one and `m`; after complementation the clique-closure defect is positive.
Complementation preserves Johnson adjacency, so the lower family remains
connected.

The second block has size

\[
 f_1={4\over9}f.
\]

Deleting it therefore costs a fixed fraction of the family.  Completing
to the next support costs

\[
 \binom{5q-1}{4q-2}
 ={4q-1\over q+1}f_1>f_1,
\]

so both adjacent complete-support profiles are macroscopically distant.

For the geometric description, `C_0=[n]\setminus[t]` contains `z`, while
`C_1=[n]\setminus([u]\cup\{z\})` replaces `z` by `t`; the cores differ by
one exchange.  Complements of second-block members are precisely the
members of the `C_1` star omitting `z`.  The remaining members of that star
contain `C_0` and already belong to the `C_0` star.  Hence

\[
 A_q=\mathcal A_{C_0}\cup\mathcal A_{C_1}.
\]

This confirms both the obstruction and the theorem's warning that it is a
two-centre Hamming-one union rather than a new isolated geometry.

For `t=alpha m+O(1)` and `u=t-1`, both shadow-to-member ratios tend to
`1/(alpha-1)`, yielding

\[
 {\sigma\over|A|}\longrightarrow
 {2(2-\alpha)\over\alpha-1}.
\]

This is below 15 exactly when `alpha>19/17`.  Stirling's formula gives
size exponent `alpha H_2(1/alpha)`; if that exponent is below one the
family is exponentially inside `O(m^2 2^m)`, and at equality the usual
`m^{-1/2}` prefactor still puts it inside that localization window.

## 7. Heavy-facet concentration

Assume the hypotheses actually used by Theorem 5.1:

\[
 m\ge144,qquad f\ge2m,qquad \Psi_2(F)-2f<15f+2m.
\]

Then `Psi_2(F)<18f`.  With `L=ceil(m/72)`, the number of positive facets
is at most `Psi_2(F)`, and each light facet has degree at most `L-1<m/72`.
Thus light raw incidence is strictly less than

\[
 {m\over72}\,18f={mf\over4}.
\]

More than `3mf/4` incidences are heavy.  If at most half the members had
at least `m/2` heavy facets, the heavy incidence total would be at most
`3mf/4`, a contradiction.  For every resulting heavy member `Y`, each
Johnson neighbor is counted at its unique common facet, so

\[
 d_{J[F]}(Y)=\sum_{D\subset Y}(d_F(D)-1)
 \ge {m\over2}(L-1).
\]

For `m>=144`, `L-1>=m/144`, giving `m^2/288`.

The original summary omitted `m>=144` and `f>=2m` when saying that
“every” violating family has this property.  That unqualified assertion is
false: a singleton has low capped slack but induced Johnson degree zero.
The final theorem now includes the two hypotheses in its opening summary,
the post-Theorem-5.1 interpretation, and the programme summary.

## 8. Co-small identity

Let `A=L\setminus C`, and at an owner let `d` be the number of deleted
facets.  Then `a=m-d`.  Using `|U|=|L|=W`, one may compute directly:

\[
\begin{aligned}
 \sigma(A)
 &=\sum_U\min\{2,m-d_U\}-2(W-c)\\
 &=2c+\sum_U\bigl(\min\{2,m-d_U\}-2\bigr).
\end{aligned}
\]

The correction is zero for `d<=m-2`, minus one for `d=m-1`, and minus
two for `d=m`.  Complementation identifies these `d` values with facet
degrees in `G`, proving

\[
 \sigma(L\setminus C)=2c-n_{m-1}(G)-2n_m(G)\le2c.
\]

Thus the co-small warning and its restriction to the two highest
multiplicity tails are exact.

## 9. Final scope verdict

After the stated scope correction, the theorem proves exactly:

1. capped-shadow equivalence under complementation;
2. shift monotonicity and the KK lower bound, sharp on every two-covered
   initial-colex profile;
3. a connected, localized continuum of low-slack partial-colex
   obstructions;
4. dense Johnson neighborhoods for low-slack families only under
   `m>=144` and `|F|>=2m`; and
5. the exact co-small high-multiplicity formula.

It does not prove protected Ore extension or classify the protected loss
on these staircases.  The proposed protected-crossing theorem remains a
genuine open next step.

**Final verdict: GO** for theorem SHA
`6e138117e2310bcc8087d3cc67cb07bd1702f0674b1ac1369298205b4fc1610f`.
