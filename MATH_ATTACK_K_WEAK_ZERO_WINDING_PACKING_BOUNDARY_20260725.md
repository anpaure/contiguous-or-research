# Lane K: the weak zero-winding packing gate after the sector retraction

Date: 2026-07-25

Method: pure mathematics only.  No web search, computation, finite search,
solver, or long-running job is used.

## 0. Outcome

Put

\[
 N=2r+1,\qquad B_r=\operatorname {Cat}_r,\qquad
 H=\lceil A\sqrt r\rceil ,
\]

where \(A>0\) is fixed.  Let
\(\overline\nu_H^{\,0}\) denote the maximum quotient-edge-disjoint packing
of genuine zero-winding PBBS residence intervals of duration at most
\(H-1\) on the long \(\tau=\phi^2\) quotient cycles.

The linear dominance seam needs only

\[
 \boxed{\overline\nu_H^{\,0}=o_A(B_r/H)}
 \tag{0.1}
\]

for the zero-winding branch.  This report proves one actual PBBS sector of
(0.1), and proves a sharp obstruction to obtaining the rest from the
present marginal chronology facts.

For an actual zero-winding return

\[
 D_j=P_j1R_j0S_j,\qquad 0\le j\le s,
\]

write

\[
 e_j=\delta(D_j)=|P_j|+1,\qquad
 \Lambda=e_0+e_s-2r.
 \tag{0.2}
\]

The audited phase-fusion kernel gives, uniformly in every cutoff \(H\),

\[
 \sum_{\substack{s<H\\ \Lambda=0}}e_{r,s}
 \le C\,\frac{4^r}{r^{5/2}},
 \tag{0.3}
\]

where \(e_{r,s}\) is the number of quotient roots which start such a
return.  Consequently

\[
 \boxed{
 \overline\nu_{H}^{\,0,\Lambda=0}
 =O(B_r/r)=o_A(B_r/H).}
 \tag{0.4}
\]

Thus the entire zero-excess endpoint-overlap sector is solved at a scale
stronger than the weak gate.  This sector contains the one-bit
common-carrier family from the terminal-completion obstruction.

There is an important correction to the overlap dictionary.  If
\(\kappa\) is the literal overlap length of the forward and dual
certificates in their common \((2r-1)\)-bit carrier, then

\[
 \boxed{\kappa=\Lambda+|S_s|+1,}
 \tag{0.5}
\]

not \(\kappa=\Lambda+1\).  Hence \(\kappa=1\) is a subclass of
\(\Lambda=0\), with \(S_s=\varnothing\); the two sectors need not be
equal.

For the remaining \(\Lambda>0\) sector, the following no-go is exact.
There are capacitated cyclic trace systems with:

1. an exact weak-composition Pascal fibre;
2. bijective common-base slot transport;
3. a phasewise literal slot prescription of density \(\Theta(1/H)\);
4. one invariant pruning-profile tag;
5. the strict zero-winding potential
   \(F_j=L_j-\delta_j=j-s\); and
6. pairwise edge-disjoint residence intervals

whose packing has size

\[
 \boxed{\Theta(B/H).}
 \tag{0.6}
\]

This is not a PBBS counterexample.  It is a theorem about the exact
capacitated projection relaxation: strict potential, profile invariance,
bijective slot transport, and every known marginal fan-capacity estimate
still permit residue-locked phase classes which tile the edge set at the
critical scale.

Therefore the precise surviving PBBS theorem is a common-base
cross-phase statement.  One must exclude residue locking for the actual
transported Pascal cells, or exploit an additional literal fusion.  The
false implication

\[
 d(D)=1\Longrightarrow
 \text{a return after }2\operatorname{ht}(D)+1
\]

is nowhere used.

## 1. Exact zero-winding chronology

For a genuine zero-winding return of step-two duration \(s\), put

\[
 d_j=|S_j|+1,\qquad
 L_j=\sum_{a<j}d_a,\qquad
 F_j=L_j-\delta(D_j).
 \tag{1.1}
\]

The strict first-passage theorem, in its sign convention
\(M_j=\delta(D_j)-L_j\), says

\[
 M_j\ge s-j,\qquad 0\le j<s,\qquad M_s=0.
 \tag{1.2}
\]

Equivalently,

\[
 \boxed{
 F_0<F_1<\cdots<F_s=0,\qquad
 F_{j+1}-F_j\ge1.}
 \tag{1.3}
\]

The increments have the exact dual form

\[
 F_{j+1}-F_j
 =\delta(D_j)+d_j-\delta(D_{j+1})
 =|T_j|+1.
 \tag{1.4}
\]

Thus the forward lengths \(d_j\) partition the accumulated-deficit
interval, while the positive increments in (1.4) partition the dual
potential interval.  This proves first return and gives two ordered
staircases.  It does not constrain the locations of different return
starts around a quotient cycle.

Peak deletion semiconjugates \(\tau\), so the complete pruning-rank
profile

\[
 \bigl(r_0(D),r_1(D),\ldots\bigr),\qquad
 r_a(D)=\tfrac12|\partial^aD|,
 \tag{1.5}
\]

is constant around a quotient orbit.  The audited Pascal fan transports
its phase-local adjacency conditions to prescribed coordinates in one
common inverse-tower fibre.  For a fixed good profile and a depth \(K\),
the compatible start fraction is at most

\[
 Q_K(\mathbf r)\le\frac{2e}{K+1}.
 \tag{1.6}
\]

A slow diagonal gives \(K=K(r)\to\infty\) and hence vanishing start
density.  Neither (1.3), (1.5), nor (1.6) relates the compatible fibre
cell at phase \(i\) to the compatible cell at phase \(i+s+2\).  That
missing relation is exactly where an edge-packing gain would have to
enter.

## 2. The solved \(\Lambda=0\) sector

### Theorem 2.1

For every fixed \(A>0\), with \(H=\lceil A\sqrt r\rceil\),

\[
 \boxed{
 \overline\nu_{H}^{\,0,\Lambda=0}
 =O(B_r/r)
 =o_A(B_r/H).}
 \tag{2.1}
\]

The constant \(C\) is absolute.

#### Proof

The phase-fusion kernel counts genuine first zero-winding starts with
\(\Lambda=0\).  Its killed-path estimate gives

\[
 \sum_{1\le s<H}e_{r,s}
 \le C_0\frac{4^r}{r^{5/2}}
 \tag{2.2}
\]

uniformly in \(H\).  Every member of a quotient-edge-disjoint packing has
a distinct start root, so

\[
 \overline\nu_{H}^{\,0,\Lambda=0}
 \le \sum_{s<H}e_{r,s}.
 \tag{2.3}
\]

Wallis' estimate

\[
 B_r\asymp\frac{4^r}{r^{3/2}}
 \tag{2.4}
\]

turns (2.2) into \(O(B_r/r)\).  Finally,

\[
 \frac{B_r/r}{B_r/H}=\frac Hr=O_A(r^{-1/2})\to0.
 \tag{2.5}
\]

This proves (2.1). \(\square\)

The theorem is a start-count argument, but here that is sufficient because
the start count already lies a full factor \(H\) below the weak packing
scale.  No rarity-times-length multiplication occurs.

## 3. Correct relation between \(\Lambda\) and common-carrier overlap

For a zero-winding return define

\[
 A=(\overline T_{s-1}0)\cdots(\overline T_00),
 \qquad
 C=(0S_s)(0S_{s-1})\cdots(0S_1).
 \tag{3.1}
\]

The dual-tail identity places them as a prefix and a suffix of one word
\(Z\) of length \(2r-1\):

\[
 Z=AR_0=R_sC.
 \tag{3.2}
\]

Their lengths are

\[
 |A|=e_0,\qquad |C|=e_s+|S_s|.
 \tag{3.3}
\]

Therefore their overlap has length

\[
 \begin{aligned}
 \kappa
 &=|A|+|C|-|Z|\\
 &=e_0+e_s+|S_s|-(2r-1)\\
 &=\Lambda+|S_s|+1.
 \end{aligned}
 \tag{3.4}
\]

This proves (0.5).  The mandatory-overlap theorem gives
\(\kappa\ge1\), while the phase-fusion endpoint equations independently
give \(\Lambda\ge0\).  Consequently

\[
 \kappa=1\Longrightarrow
 \Lambda=0,\quad S_s=\varnothing,
 \tag{3.5}
\]

whereas

\[
 \Lambda=0\Longrightarrow \kappa=|S_s|+1.
 \tag{3.6}
\]

Thus the overlap-one family is safely included in Theorem 2.1, but it does
not exhaust that theorem's sector.

For \(\Lambda>0\), the common certificate extends beyond the mandatory
terminal block by \(\Lambda\) bits.  Since both \(\kappa\) and
\(|S_s|+1\) are odd, \(\Lambda\) is even.  It is tempting to delete this
balanced extra word and reduce to \(\Lambda=0\).  That is not presently a
proof: the extra word may cross several \(S/T\) block boundaries, and
deleting it has not been shown to preserve the canonical first-maximum
factorizations or the actual \(\tau\)-chronology.  No bounded-overlap
extension is claimed here.

## 4. A sharp capacitated residue obstruction

The next theorem isolates exactly why the facts in Section 1 do not imply
the little-oh packing gain.

### Theorem 4.1 (strict-potential Pascal residue saturation)

Let \(h\ge6\), put \(q=h+2\), and let \(L\) be a multiple of \(q\).
There is a finite cyclic capacitated trace system with total state mass
\(\mathcal B\) and a family \(\mathcal P\) such that:

1. every member of \(\mathcal P\) has \(q=h+2\) consecutive transition
   edges;
2. all members of \(\mathcal P\) are pairwise edge-disjoint;
3. every start carries the exact scalar zero-winding data

   \[
   d_j=1,\quad L_j=j,\quad\delta_j=h,\quad
   F_j=j-h\qquad(0\le j\le h);
   \tag{4.1}
   \]

4. every state has one common invariant profile tag;
5. the transported start condition is contained in one exact
   weak-composition slot hyperplane, and its density at every phase is
   between \(1/(48q)\) and \(1/(24q)\); and
6. nevertheless

   \[
   \boxed{
   |\mathcal P|\ge\frac{\mathcal B}{48q}
   =\Theta(\mathcal B/h).}
   \tag{4.2}
   \]

#### Proof

Choose an odd integer \(p\ge q\), put \(y=pq\), and take the exact
weak-composition simplex

\[
 \Omega=
 \left\{(n_0,\ldots,n_{p-1})\in\mathbb Z_{\ge0}^{p}:
       \sum_an_a=y\right\}.
 \tag{4.3}
\]

Its size is

\[
 F=|\Omega|=\binom{y+p-1}{p-1}.
 \tag{4.4}
\]

For \(0\le z<q\), the literal slot hyperplane

\[
 H_z=\{\mathbf n\in\Omega:n_0=z\}
 \tag{4.5}
\]

has size

\[
 K_z=\binom{y-z+p-2}{p-2}.
 \tag{4.6}
\]

First,

\[
 \frac{K_0}{F}
 =\frac{p-1}{p(q+1)-1}
 \ge\frac1{3q}.
 \tag{4.7}
\]

Moreover,

\[
 \frac{K_{z+1}}{K_z}
 =\frac{y-z}{y+p-2-z}
 =1-\frac{p-2}{y+p-2-z}
 \ge1-\frac1q,
 \tag{4.8}
\]

because \(z\le q-2\le p-2\) and \(y=pq\).  Hence

\[
 K_z\ge K_0(1-1/q)^q\ge\frac{F}{12q}.
 \tag{4.9}
\]

Choose pairwise disjoint subsets

\[
 C_z\subseteq H_z,\qquad
 |C_z|=M:=\left\lfloor\frac{F}{24q}\right\rfloor.
 \tag{4.10}
\]

For \(q\ge8\), \(F\ge48q\), so

\[
 \frac{F}{48q}\le M\le\frac{F}{24q}.
 \tag{4.11}
\]

Let the state set be

\[
 \mathcal X=\mathbb Z_L\times\Omega,
 \qquad
 \tau(i,\mathbf n)=(i+1,\mathbf n),
 \tag{4.12}
\]

and index its transition edges by the same pairs.  Thus

\[
 \mathcal B=|\mathcal X|=LF.
 \tag{4.13}
\]

Attach one fixed pruning-profile tag to every state.  At phase \(i\),
declare \((i,\mathbf n)\) eligible precisely when

\[
 \mathbf n\in C_{i\bmod q}.
 \tag{4.14}
\]

This is an exact common-base transported slot prescription: every eligible
vector lies in

\[
 n_0=i\bmod q.
 \tag{4.15}
\]

Its phasewise density is \(M/F\), which lies in the interval asserted in
item 5.

For an eligible start define its transition-edge interval by

\[
 I(i,\mathbf n)
 =\{(i-1+t,\mathbf n):0\le t<q\},
 \tag{4.16}
\]

with the first coordinate taken modulo \(L\).  Fix
\(\mathbf n\in C_z\).  Its eligible starts are exactly the phases

\[
 i\equiv z\pmod q.
 \tag{4.17}
\]

The corresponding half-open \(q\)-edge intervals partition its
\(\mathbb Z_L\)-cycle.  Intervals with different vectors use disjoint
product edges.  Hence every eligible interval is edge-disjoint from every
other one.

There are \(qM\) selected vectors and \(L/q\) starts for each.  Therefore

\[
 |\mathcal P|
 =qM\frac Lq
 =LM
 \ge\frac{LF}{48q}
 =\frac{\mathcal B}{48q}.
 \tag{4.18}
\]

Finally assign to every interval the data (4.1).  Then

\[
 \sum_{j<h}d_j=h=\delta_h,
 \qquad
 F_0=-h,\quad F_h=0,\quad F_{j+1}-F_j=1.
 \tag{4.19}
\]

Thus the scalar chronology is an exact zero-winding strict-potential
chronology.  The assignments do not conflict, because the trace intervals
are already disjoint.  This proves every assertion. \(\square\)

### Corollary 4.2

No theorem of the form

\[
 \overline\nu_H^{\,0}=o(B_r/H)
 \tag{4.20}
\]

can be deduced solely from:

1. the strict scalar potential (1.3);
2. invariance of a profile label under \(\tau\);
3. bijectivity of slot transport;
4. a phasewise compatible-fibre fraction \(o(1)\), even
   \(O(1/H)\); and
5. the universal edge-capacity ledger.

#### Proof

Theorem 4.1 satisfies all five statements and has packing
\(\Theta(\mathcal B/H)\). \(\square\)

The theorem uses an exact Pascal simplex and exact integral intervals.
Its transport is an abstract capacitated transport, not the actual PBBS
slot permutation of a Dyck core.  It models an \(O(1/H)\) phasewise
compatible-cell fraction and one literal transported Pascal hyperplane;
it does **not** model every detailed equation in the triangular
multilevel PBBS fan.  It therefore does not refute the desired PBBS
inequality.  Its role is to show that the missing theorem must identify a
PBBS-specific cross-phase or multilevel restriction; no rearrangement of
the present marginal inequalities can supply the little-oh.

The residue obstruction is also compatible with the qualitative
harmonic-pruning theorem.  Its eligible start density is \(1/\Theta(H)\),
which tends to zero, and hence lies below every sufficiently slow
diagonal \(O(1/K(r))\).  The strict potential does not prevent the
eligible cells from recurring exactly one interval length apart.

## 5. Exact remaining PBBS boundary

Decompose an actual zero-winding packing as

\[
 \mathcal P=\mathcal P_{\Lambda=0}
             \,\dot\cup\,\mathcal P_{\Lambda>0}.
 \tag{5.1}
\]

Theorem 2.1 gives

\[
 |\mathcal P_{\Lambda=0}|=O(B_r/r)
 =o_A(B_r/H).
 \tag{5.2}
\]

Therefore the weak zero-winding gate is now exactly

\[
 \boxed{
 |\mathcal P_{\Lambda>0}|=o_A(B_r/H).}
 \tag{5.3}
\]

The audited start-density theorem gives only
\(o_A(B_r)\) for this larger class.  The reciprocal-height trace gives
only \(O_A(B_r/H)\).  Theorem 4.1 proves that these two marginal facts
cannot be multiplied.

A sufficient common-base assertion may be phrased as follows.  In a fixed
invariant pruning-profile fibre, let \(\mathcal E_i\) be the exact set of
inverse-tower vectors satisfying all transported Pascal equations for a
return beginning at phase \(i\).  Prove that, after restricting to
\(\Lambda>0\), no edge-disjoint family can follow a residue tiling:

\[
 \sum_{I\in\mathcal P}|I|
 =o_A\!\left(\sum_{\text{profile base edges }e}F(e)\right)
 \tag{5.4}
\]

uniformly for every Gaussian-height packed family.  Since
\(|I|\asymp_A H\), (5.4) gives (5.3).

Equivalently, one may prove a two-phase or multi-phase incidence estimate
which forces the common transported cells
\(\mathcal E_i,\mathcal E_{i+|I|},\ldots\) to lose a factor tending to
zero relative to the residue model.  The estimate must use the actual
first-maximum/peak-deletion chronology.  Profile invariance by itself
helps the residue construction: it keeps all phases in the same fibre.

Global literal phase fusion remains a separate fallback.  The packet and
block compilers survive the retraction as conditional theorems, but no
dense compatible packet family has been proved.

## 6. Adversarial self-audit

1. **No false converse.**  The actual PBBS theorem in Section 2 begins
   with genuine first zero-winding starts.  The abstract model explicitly
   assigns chronology data and is not called a PBBS realization.

2. **Correct weak scale.**  For \(H=\Theta_A(\sqrt r)\),
   \(B_r/r=o_A(B_r/H)\).  No factor \(N\) belongs in the quotient
   statement.

3. **No rarity-times-length multiplication.**  Theorem 2.1 uses start
   count alone.  Section 4 shows why the general start-density and edge
   ledgers cannot be multiplied.

4. **Overlap dictionary.**  The suffix certificate has the extra
   \(|S_s|\) symbols.  Omitting them gives the false formula
   \(\kappa=\Lambda+1\).  Equations (3.4)--(3.6) are the corrected
   quantifiers.

5. **Pascal floors.**  Equations (4.4)--(4.9) use the exact
   stars-and-bars fibre and the exact hyperplane cardinalities.  The floor
   in (4.10) loses only the explicit factor two in (4.11).

6. **Packing is integral.**  For each selected vector the \(q\)-edge
   intervals tile one base cycle.  Different vectors use disjoint edges.
   No fractional selection or randomized rounding is used.

7. **Scope of the obstruction.**  The abstract transport need not be a
   Dyck/PBBS transport and does not satisfy the complete multilevel fan or
   unlisted literal word identities.  It realizes the exact
   weak-composition fibre, one transported slot hyperplane, the
   \(O(1/H)\) compatible-cell marginal, and the scalar/profile/edge
   ledgers.  It proves insufficiency of those audited marginal facts, not
   failure of (5.3).

8. **What has actually advanced.**  The whole \(\Lambda=0\) PBBS sector,
   including every \(\kappa=1\) start, satisfies the weak packing gate.
   The only unsolved zero-winding branch in this lane is
   \(\Lambda>0\), where a PBBS-specific cross-phase incidence theorem or
   a literal block fusion is still required.
