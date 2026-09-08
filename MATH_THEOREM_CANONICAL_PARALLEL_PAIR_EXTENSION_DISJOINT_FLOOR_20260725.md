# A symbolic extension-disjoint floor for the canonical parallel-pair bridges

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

Let \(F_m^{\rm MSW}\) be the canonical exact wreath factor on
\(n=2m+1\) coordinates.  Consider either

\[
 \sigma_{\rm tr}=(2\ 3)(4\ 5)\cdots(2m-2\ \ 2m-1)
\tag{0.1}
\]

or the full parallel-pair involution

\[
 \sigma_{\rm full}=\sigma_{\rm tr}(2m\ \ 2m+1).
\tag{0.2}
\]

For every \(m\ge4\) for \(\sigma_{\rm tr}\), and every \(m\ge5\) for
\(\sigma_{\rm full}\), there are \(2\operatorname {Cat}_{m-4}\) disjoint
target orbits \(\{S,\sigma S\}\) on which the canonical first-shadow loads
are exactly

\[
 \boxed{(\mu_1(S),\mu_1(\sigma S))=(0,1).}
\tag{0.3}
\]

Consequently:

1. the covered member of every displayed orbit has empty pulled-back
   endpoint-extension set;
2. no diagonal replacement
   \((F\setminus A)\sqcup\sigma A\) can reduce the number of holes on any
   displayed orbit;
3. every such replacement retains at least
   \(2\operatorname {Cat}_{m-4}\) first-shadow holes.

This is only a \(\Theta(W/m)\) floor, so it does not rule out an
\(o(W)\)-defect bridge.  It does prove, symbolically, a genuine
extension-disjoint obstruction for both recursion-native parallel-pair
representatives.

## 1. The hereditary canonical hole family

Write incidence words on the \(2m\)-coordinate core, with one denoting
membership.  Put

\[
 B_0=11101101,
 \qquad B_1=10110111.
\tag{1.1}
\]

The complements of these two six-sets in the eight-coordinate core are,
respectively, \(47\) and \(25\).  The complete symbolic semilength-four
table of internal \(\Gamma\)-colours contains neither complement, so both
are absent from the base map.

### Lemma 1.1 (rank-six prefix localization)

Let \(Q\) be any eight-letter word with six ones, and let \(V\) be Dyck.
Every preimage of \(QV\) under the internal MSW map \(\Gamma\) has both
added coordinates in the first eight positions.  Consequently the
multiplicity of \(QV\) equals the base multiplicity of \(Q\).

### Proof

Write

\[
 \Gamma(x_i)=QV,
 \qquad x_i=QV\setminus\{a,b\},
\]

with \(a\) inserted by \(g\) and \(b\) deleted by the preceding
\(h\)-move.  The prefix \(Q\) ends at height four.  If \(a\) were in the
suffix, its target starting height would be at least four, and deletion of
the other added coordinate could lower it by at most two.  Its starting
height in \(x_i\) would therefore be at least two, whereas \(g\) selects
only a down-step starting at height zero or one.  Hence \(a\) lies in the
prefix.

The upper state supplied to \(h\) is \(QV\setminus\{a\}\).  Its prefix
ends at height two, and every up-step in the Dyck suffix starts at height at
least two.  Since \(h\) selects only among up-steps starting at height zero
or one, \(b\) also lies in the prefix.  Deleting \(a,b\) leaves a balanced
eight-letter state followed by the unchanged suffix.  The MSW
concatenation identity and uniqueness of the canonical owner identify it
with a base preimage followed by \(V\).  The converse is ordinary suffix
locality. \(\square\)

For every Dyck word \(V\) of semilength \(d=m-4\), put

\[
 T_i(V)=B_iV,
 \qquad i\in\{0,1\}.
\tag{1.2}
\]

The base table and Lemma 1.1 show that both targets are absent from the
internal second-upper map \(\Gamma\).  Under the exact
upper/lower complementation in one MSW row, the corresponding lower target
is

\[
 S_i(V)=\{2m+1\}\cup([2m]\setminus T_i(V)),
\tag{1.3}
\]

and

\[
 \boxed{\mu_1^{F_m^{\rm MSW}}(S_i(V))=0.}
\tag{1.4}
\]

Distinct suffixes give distinct targets.

## 2. Action of the parallel-pair involutions

Every nonempty Dyck word begins with one and ends with zero.  For \(m\ge5\), the pair
\((8,9)\) therefore sees two ones in either concatenation \(B_iV\), while the
full final pair \((2m,2m+1)\) sees two zeroes in the upper-core
representation (the distinguished coordinate \(2m+1\) is absent).

Inside the suffix, define

\[
 \eta_t=(2t\ \ 2t+1),\qquad1\le t\le d-1,
\tag{2.1}
\]

acting on suffix positions.  Each \(\eta_t\) preserves the Dyck family:
equal adjacent steps are unchanged; changing down-up to up-down raises the
intermediate height; changing up-down to down-up lowers an odd positive
intermediate height by two and therefore keeps it nonnegative.  The
\(\eta_t\)'s commute, so

\[
 V'=\eta_1\eta_2\cdots\eta_{d-1}V
\tag{2.2}
\]

is again Dyck.

The first three active pairs in the eight-letter prefixes change

\[
 11101101\longmapsto11110011,
 \qquad
 10110111\longmapsto11001111.
\]

Put

\[
 B'_0=11110011,
 \qquad B'_1=11001111.
\tag{2.3}
\]

The boundary and final pairs noted above act trivially.  Hence, in the
stated ranges, for either
involution in (0.1)--(0.2),

\[
 \boxed{\sigma T_i(V)=B'_iV'.}
\tag{2.4}
\]

Equivalently,

\[
 \boxed{\sigma S_i(V)=
 \{2m+1\}\cup([2m]\setminus B'_iV').}
\tag{2.5}
\]

For the full involution, both \(2m\) and \(2m+1\) belong to the lower set
in (1.3), so their final swap is again harmless.

## 3. The image families have canonical load exactly one

The complements of \(B'_0,B'_1\) inside the eight-coordinate core are
\(\{5,6\}\) and \(\{3,4\}\), respectively.  The symbolic
semilength-four table has exactly one occurrence of each internal
\(\Gamma\)-colour: complement \(56\) occurs at \(i=2\) in the row rooted
at \(11100100\), while complement \(34\) occurs at \(i=2\) in the row
rooted at \(11011000\).

Lemma 1.1 therefore gives

\[
 \boxed{\#\Gamma^{-1}(B'_iV')=1.}
\tag{3.1}
\]

After upper/lower complementation,

\[
 \boxed{\mu_1^{F_m^{\rm MSW}}(\sigma S_i(V))=1.}
\tag{3.2}
\]

Together with (1.4), this proves (0.3).

## 4. Extension-disjoint and orbit-mass consequences

Since \(E_1^F(S_i(V))=\varnothing\) and \(\sigma^2=1\),

\[
 \sigma E_1^F(\sigma^{-1}\sigma S_i(V))
 =\sigma E_1^F(S_i(V))
 =\varnothing.
\tag{4.1}
\]

Thus the covered target \(\sigma S_i(V)\) has no pulled-back witnessing
middle extension.  It is an explicit extension-disjoint target.

Its load is one, so its occurrence-owner support consists of a single row
and cannot be split by a row cut.  The involution orbit-mass identity says
that every diagonal replacement preserves total load one on
\(\{S_i(V),\sigma S_i(V)\}\).  Exactly one member therefore remains a hole at
every cut.

The map \(V\mapsto V'\) is a bijection of \(\mathcal D_{m-4}\), and all
the targets \(S_i(V)\) are distinct.  The two base families are disjoint,
and a hole target cannot equal a load-one target, so the displayed orbits are
distinct and prove the floor

\[
 \boxed{H_1((F\setminus A)\sqcup\sigma A)
 \ge2\operatorname {Cat}_{m-4}.}
\tag{4.2}
\]

Finally,

\[
 {2\operatorname {Cat}_{m-4}\over W}
 ={1+o(1)\over128(2m+1)}
 ={1+o(1)\over256m}.
\tag{4.3}
\]

Thus (4.2) is a genuine algebraic obstruction, but only of order
\(W/m\).  A linear extension-disjoint floor for the full or truncated
parallel-pair bridge would require suspending this seed across
\(\Theta(m)\) disjoint contexts; that further packing theorem is not proved
here.
