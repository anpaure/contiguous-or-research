# Lane U: exact antichain obstruction to reusable appended PBBS seam containers

Date: 2026-07-25

Pure mathematics only. No computation, finite search, solver, or external
input is used.

## 0. Outcome

Put

\[
N=2m+1,\qquad W=\binom Nm,\qquad B=\frac WN=\operatorname{Cat}_m.
\]

There is an exact obstruction to grouping many quotient cuts into a few
self-contained literal seam words.

> **Static seam-container theorem.** Choose \(K\) distinct quotient cut
> edges of the complement-projected PBBS factor. Their complete spatial
> decks have \(KN\) distinct rank-\(m\) depth-one crossing cores. If a
> collection of literal set-words internally represents all these cores by
> contiguous OR intervals, then its total length is at least
> \[
> \boxed{KN.}                                      \tag{0.1}
> \]

Thus grouping cuts by a common Dyck-sector, entropy, or abstract pattern
gives no literal depth-one saving in an appended, internally witnessed
catalogue. For one quotient cut and

\[
H_A=\lceil A\sqrt m\rceil
\]

with fixed \(A>0\),

\[
\boxed{
N=\left(\frac2{A^2}+o_A(1)\right)H_A^2.}          \tag{0.2}
\]

Consequently no standalone phase-deck seam packet can have total length
\(o(H_A^2)\). This conclusion is stronger than an entropy estimate: it is
an exact rank-antichain count.

The scope is decisive. The \(KN\) cores are themselves compulsory central
targets in the global width ledger. A coefficient-one construction may
recode and reuse those same \(KN\) principal positions to carry deeper
crossing targets. Therefore (0.1) is not an \(\Omega(KN)\) lower bound on
*excess* over the middle baseline. It closes appended reusable seam
catalogues, not integrated shared fusion. The correct surviving target is

\[
\boxed{\text{desired but unproved: total length }KN+o(KN)
\text{ on the assigned sector}}                               \tag{0.3}
\]

equivalently \(o(N)=o(H_A^2)\) excess per quotient packet after crediting
its \(N\) compulsory central positions.

There is also a uniform entropy theorem for the cyclic phase profiles. If

\[
\kappa(C)=\min_{0\ne t\in\mathbb Z_N}|C\triangle(C+t)|,
\]

then all but at most

\[
\boxed{N\,2^{17N/24}}                              \tag{0.4}
\]

central \(m\)-sets satisfy \(\kappa(C)\ge N/16\). Hence almost every phase
packet has linear cyclic translation distance in every nonzero direction;
no ordering of its phases is a Johnson-near path. This reinforces the
container obstruction, but by itself does not add a positive excess above
the exact baseline (0.1).

Finally, the purported Catalan-dense \(d=1\) *return* reservoir used to
motivate the requested fusion has been retracted: \(d=1\) does not imply a
return at gap \(2\operatorname{ht}(D)+1\). Thus this report proves a static
literal no-go and corrects the cost target; it does not prove or disprove
\((RP_A)\), and it does not prove coefficient one.

## 1. Equal-rank targets force an interval antichain

### Lemma 1.1 (one word)

Let

\[
w=(w_1,\ldots,w_L)
\]

be a word of subsets of an arbitrary ground set. Suppose \(T_1,\ldots,T_k\)
are distinct sets of one common cardinality, and for every \(i\) there is
an interval \(I_i=[a_i,b_i]\subseteq[L]\) such that

\[
T_i=\bigvee_{j\in I_i}w_j
=\bigcup_{j=a_i}^{b_i}w_j.                        \tag{1.1}
\]

Then

\[
\boxed{k\le L.}                                   \tag{1.2}
\]

### Proof

If \(I_i\subseteq I_j\), then (1.1) gives \(T_i\subseteq T_j\). Since the
two targets have equal cardinality, this forces \(T_i=T_j\), contrary to
distinctness. Thus the witness intervals form a containment antichain.

Two different intervals in that antichain cannot have the same left
endpoint, because then the one with smaller right endpoint is contained in
the other. Hence the \(k\) left endpoints are distinct members of
\([L]\), proving \(k\le L\). \(\square\)

No restriction on the letters is used. They may be repeated, may have
arbitrary ranks, and may serve arbitrarily many other target witnesses.
The only assumptions are literal contiguous OR, distinctness, and one
common target rank.

### Corollary 1.2 (many words)

Let \(\mathcal T\) be a family of \(M\) distinct equal-cardinality targets.
If every target is assigned a witness interval lying wholly inside one word
from a collection \(\{w_\alpha\}\), then

\[
\boxed{\sum_\alpha |w_\alpha|\ge M.}              \tag{1.3}
\]

Indeed, assign each target to one chosen witnessing word and apply Lemma
1.1 inside every word.

## 2. The PBBS depth-one core map is a bijection

Let \((A_i)\) be the canonical PBBS odd-graph factor on rank-\(m\) sets and
put

\[
X_i=[N]\setminus A_i.
\]

The complement-projected step-two sequences are Johnson cycles on the
rank-\((m+1)\) owners \(X_i\). For the transition from \(X_i\) to
\(X_{i+2}\), its depth-one lower crossing core is

\[
C_i=X_i\cap X_{i+2}.                              \tag{2.1}
\]

Adjacent odd-graph states are disjoint, and the PBBS three-state identity
gives

\[
\boxed{
X_i\cap X_{i+2}
=[N]\setminus(A_i\cup A_{i+2})
=A_{i+1}.}                                       \tag{2.2}
\]

Explicitly, \(A_i\) and \(A_{i+2}\) are distinct \(m\)-subsets of the
\((m+1)\)-set \([N]\setminus A_{i+1}\): each is disjoint from the
intermediate odd-graph state \(A_{i+1}\). Their union is therefore that
whole complement, which proves the last equality in (2.2).

The factor owns every rank-\(m\) set exactly once. Therefore (2.2) proves:

### Lemma 2.1 (exact core ownership)

The directed physical step-two edges are in bijection with
\(\binom{[N]}m\) through their depth-one crossing cores.

The physical deck acts by cyclic coordinate translation. Hence the \(N\)
lifts of one quotient edge have cores

\[
\{C+t:t\in\mathbb Z_N\}.                          \tag{2.3}
\]

These \(N\) sets are distinct. Indeed, if \(C+t=C\) for nonzero \(t\),
let \(\ell>1\) be the order of \(t\) in \(\mathbb Z_N\). The invariant set
is a union of \(\ell\)-cycles, so \(\ell\mid |C|=m\), while also
\(\ell\mid N=2m+1\). This contradicts \(\gcd(N,m)=1\).

It follows that quotient edges are in bijection with cyclic necklaces of
rank-\(m\) sets, and decks of distinct quotient edges are disjoint. Thus
\(K\) distinct quotient cuts give exactly \(KN\) distinct cores.

## 3. Proof and literal scope of the static seam theorem

Cutting a physical step-two edge destroys its canonical depth-one crossing
witness. A self-contained repair of the complete spatial deck of a
quotient cut must restore the \(N\) masks in (2.3) by intervals internal to
the appended repair word or words.

For \(K\) quotient cuts, Lemma 2.1 gives \(KN\) distinct rank-\(m\)
targets. Corollary 1.2 gives total repair-word length at least \(KN\). This
proves (0.1).

The theorem allows:

* arbitrarily many seam words;
* arbitrary assignment of cuts and phases among them;
* arbitrary letters and arbitrary target occurrence multiplicity;
* arbitrary witness ordering; and
* arbitrary grouping by sector, return length, entropy profile, or packet
  label.

It assumes that the restored core witnesses lie wholly inside the appended
seam words. Two constructions escape:

1. **Baseline integration.** Keep or recode the \(KN\) compulsory central
   positions and make the deeper crossing witnesses use those positions.
   Then \(KN\) is principal length, not appended overhead.
2. **Cross-packet intervals.** Use witness intervals which cross nominal
   packet or seam boundaries in one global word. Such witnesses cannot be
   assigned to internally complete seam blocks, so Corollary 1.2 does not
   price them as appended charts.

This is why (0.1) does not imply a coefficient-one lower bound. It says
that an entropy catalogue cannot be appended cheaply; it must be compiled
into the central baseline.

## 4. Uniform cyclic-profile entropy deficit

For \(C\in\binom{\mathbb Z_N}m\), define

\[
\kappa(C)=\min_{0\ne t\in\mathbb Z_N}
|C\triangle(C+t)|.
\]

### Theorem 4.1 (hard cores are overwhelming)

Let

\[
\mathcal E_N=
\left\{
C\in\binom{\mathbb Z_N}m:
\kappa(C)<\frac N{16}
\right\}.
\]

Then

\[
\boxed{|\mathcal E_N|\le N\,2^{17N/24}.}          \tag{4.1}
\]

Consequently, for every fixed \(K\),

\[
\frac{|\mathcal E_N|}{\binom Nm}
=o(m^{-K}).                                       \tag{4.2}
\]

### Proof

Fix \(0\ne t\in\mathbb Z_N\). Translation by \(t\) has

\[
d=\gcd(N,t)
\]

cycles. Since \(N\) is odd, every nontrivial translation cycle has odd
length at least three, so

\[
d\le\frac N3.                                     \tag{4.3}
\]

For a binary indicator \(1_C\), define the \(t\)-boundary

\[
\partial_tC=
\{x:1_C(x)\ne1_C(x-t)\}.                          \tag{4.4}
\]

Its size is exactly

\[
|\partial_tC|=|C\triangle(C+t)|.
\]

Given \(\partial_tC\) and one initial bit on each of the \(d\) translation
cycles, all bits of \(C\) are determined by propagating around those
cycles. Therefore

\[
\#\left\{
C:|C\triangle(C+t)|\le\frac N{16}
\right\}
\le
2^d\sum_{j\le N/16}\binom Nj.                    \tag{4.5}
\]

The binary entropy estimate gives

\[
\sum_{j\le N/16}\binom Nj
\le2^{NH_2(1/16)}.
\]

Moreover,

\[
H_2(1/16)
=\frac14+\frac{15}{16}\log_2\frac{16}{15}
\le\frac14+\frac1{16\log 2}
<\frac38.                                        \tag{4.6}
\]

Combining (4.3)--(4.6) gives at most

\[
2^{N/3+3N/8}=2^{17N/24}
\]

exceptional sets for one \(t\). A union bound over fewer than \(N\)
nonzero translations proves (4.1).

Finally,

\[
\binom Nm\ge\frac{2^N}{N+1},
\]

so

\[
\frac{|\mathcal E_N|}{\binom Nm}
\le N(N+1)2^{-7N/24},
\]

which proves (4.2). \(\square\)

### Corollary 4.2 (no Johnson-near phase ordering)

If \(C\notin\mathcal E_N\), then for every ordering
\(t_1,\ldots,t_N\) of \(\mathbb Z_N\),

\[
\boxed{
\sum_{i=1}^{N-1}
|(C+t_i)\triangle(C+t_{i+1})|
\ge\frac{N(N-1)}{16}.}                            \tag{4.7}
\]

Thus any chronology which moves directly between successive phase cores
by one-coordinate Johnson exchanges needs \(\Omega(N^2)\) such exchanges.
At Gaussian scale this is \(\Omega(H_A^4)\). A literal contiguous-OR word
may bypass direct Johnson motion, so (4.7) is a chronology obstruction,
not an additional word-length lower bound.

## 5. Implication for a Catalan-scale packet family

The core necklaces partition the \(W\) central sets into \(B=W/N\)
quotient packets. Equation (4.1) shows that only exponentially few packets
can contain a cyclicly soft core. Hence any proposed family of quotient
cuts of Catalan-polynomial density contains hard packets except for a
negligible subfamily.

This statement is conditional only at the point where one identifies a
given Dyck-sector family with *actual return cuts*. The primitive \(d=1\)
class is Catalan-positive as a class of roots, but the claimed return law
for it is false. It therefore cannot be inserted into this theorem as a
Catalan-positive residence family.

For any genuine return family supplied by a future theorem, the conclusions
are exact:

* every appended internally complete deck packet costs at least \(N\);
* almost every packet has cyclic translation distance at least \(N/16\);
* grouping packets by a low-entropy abstract template does not reduce the
  number of actual rank-\(m\) core positions; and
* the only possible coefficient-one use of such grouping is carrier reuse
  inside a global \(W+o(W)\) word.

## 6. Independent audit and exact boundary

1. **No multiplicity shortcut.** Corollary 1.2 assigns each target to one
   chosen occurrence. Additional occurrences do not reduce the
   containment-antichain lower bound.
2. **No necklace collision.** The PBBS core map is a physical bijection,
   and \(\gcd(N,m)=1\) makes every rotation orbit free. Distinct quotient
   cuts therefore contribute disjoint target decks.
3. **Correct scale.** For fixed \(A\),
   \(H_A^2=A^2m+o_A(m)\) and \(N=2m+1\), proving (0.2).
4. **Entropy constant.** Oddness of \(N\) gives the exact divisor bound
   \(d\le N/3\); (4.6) gives \(1/3+3/8=17/24\).
5. **Cost scope.** The lower bound is on total length of standalone
   internally witnessed seam blocks. It is not an excess lower bound after
   crediting the compulsory central positions.
6. **Current frontier.** The literal target which survives this report is
   an integrated carrier theorem: for a selected sector of \(K\) quotient
   cuts, build one word of length \(KN+o(KN)\) whose \(KN\) central
   positions also support every required deeper crossing mask. No such
   theorem is proved here.

The entropy/container idea therefore has an exact verdict. It cannot
compress a reusable appended seam catalogue below the quadratic
\(H_A^2\) scale. It remains potentially useful only as a rule for assigning
deeper witnesses to already compulsory central carriers in a genuinely
global fusion.
