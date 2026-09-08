# Lane K: zero-winding carrier overlap and the critical trace-completion obstruction

Date: 2026-07-25

Pure mathematics only. No computation, finite search, solver, or external
input is used.

## 0. Outcome

Put

\[
 N=2r+1,\qquad B=\operatorname {Cat}_r,
\]

and let a genuine zero-winding PBBS return have \(s\) even-time quotient
steps.  In the audited notation

\[
 D_h=P_h1R_h0S_h,\qquad 0\le h\le s,
\]

let \(T_0,\ldots,T_{s-1}\) be the dual staircase words.  The identities
from `MATH_ATTACK_O_RP_A_ZERO_WINDING_PREFIX_CODE_20260725.md` imply that
the two endpoint certificates live in one common word of length
\(2r-1=N-2\).

This report proves three new statements.

1. **Overlap is compulsory.**  Define

   \[
   \begin{aligned}
   A&=(\overline T_{s-1}0)\cdots(\overline T_00),\\
   C&=(0S_s)(0S_{s-1})\cdots(0S_1).
   \end{aligned}                                      \tag{0.1}
   \]

   In the common carrier, \(A\) is a prefix and \(C\) is a suffix.  They
   overlap in a nonempty word \(O\).  Its length

   \[
      \kappa=|A|+|C|-(2r-1)                         \tag{0.2}
   \]

   is odd, and

   \[
      \operatorname {net}(O)=-1.                    \tag{0.3}
   \]

   Thus the forward and dual \(1/(s+1)\) fields can never be assigned to
   disjoint token regions.  The obstruction is universal, not confined to
   the fixed-height-three example in the earlier report.

2. **The lower bound \(\kappa\ge1\) is sharp at every height.**  For every
   two symmetric capped Dyck tuples displayed in Section 2 below, there is
   a literal PBBS orbit

   \[
      D_0\stackrel\tau\longmapsto D_1
      \stackrel\tau\longmapsto\cdots
      \stackrel\tau\longmapsto D_s                 \tag{0.4}
   \]

   which starts a first zero-winding return of gap \(2s+1\) and has
   \(\kappa=1\).  No argument may discard small carrier overlap as
   dynamically impossible.

3. **Minimal-overlap completion is Catalan-critical.**  Let
   \(Z_{r,s}^{(1)}\) be the number of roots in that explicit
   \(\kappa=1\) family.  It has the exact coefficient formula

   \[
      Z_{r,s}^{(1)}=[z^{r-s}]G_s(z),                \tag{0.5}
   \]

   where \(G_s\) is the product in (3.1).  There are absolute constants
   \(0<a<b<\infty\), \(c>0\), and infinitely many ranks \(r\) such that

   \[
      \boxed{
      \sum_{a\sqrt r\le s\le b\sqrt r}Z_{r,s}^{(1)}
      \ge c\,{B\over N}.}                          \tag{0.6}
   \]

   All but \(\exp(o(r))\) of these roots lie on quotient cycles longer
   than \(O(\sqrt r)\).

Consequently no terminal-completion argument which seeks to prove that the
**number** of actual Gaussian zero-winding starts is \(o(B/N)\) can be
correct.  The forward staircase, the dual staircase, their exact common
carrier, both endpoint Dyck constraints, and literal zero-winding dynamics
still permit Catalan-critical start mass.

This does not disprove \(RP_A\).  The starts in (0.6) may cluster on their
quotient cycles.  Within a proof which continues through the residence
packing gate, the missing gain must therefore be chronology-sensitive:
prove that these actual return intervals have packing \(o(B/N)\), or show
Pascal-weighted trace dispersion which excludes critical mass after
edge-disjointness is imposed.  Terminal completion alone supplies no
further factor \(\eta_{r,A}\to0\).  A global literal fusion which bypasses
\(RP_A\) remains a separate conditional fallback.

## 1. The common carrier and mandatory overlap

For a zero-winding return, put

\[
 d_h=|S_h|+1,
 \qquad L_h=\sum_{j<h}d_j,
 \qquad M_h=\delta(D_h)-L_h.                        \tag{1.1}
\]

The audited staircase theorem gives

\[
 S_0=\varnothing,
 \qquad L_s=\delta(D_s),
 \qquad M_s=0,                                     \tag{1.2}
\]

and, with

\[
 e_h=M_h-M_{h+1}=|T_h|+1,
\]

\[
 \sum_{h<s}e_h=M_0=\delta(D_0).                   \tag{1.3}
\]

The exact dual-tail identity is

\[
 (\overline T_{s-1}0)\cdots(\overline T_00)R_0
 =R_s(0S_s)(0S_{s-1})\cdots(0S_1).                \tag{1.4}
\]

Using (0.1), call the common word in (1.4) \(Z\).  Since

\[
 D_0=P_01R_00,
 \qquad |P_01|=\delta(D_0)=|A|,
\]

one has

\[
 |Z|=|A|+|R_0|=2r-1.                               \tag{1.5}
\]

Likewise

\[
 |C|=\delta(D_s)+|S_s|,
 \qquad |R_s|+|C|=2r-1.                            \tag{1.6}
\]

### Theorem 1.1 (mandatory carrier overlap)

The prefix \(A\) and suffix \(C\) of \(Z\) overlap.  Writing their overlap
as \(O\),

\[
 A=R_sO,
 \qquad C=OR_0,                                    \tag{1.7}
\]

and

\[
 \boxed{\operatorname {net}(O)=-1.}               \tag{1.8}
\]

In particular \(\kappa=|O|\) is a positive odd integer.

#### Proof

Every block in \(A\) has net height \(-1\), and there are \(s\) blocks;
the same is true of \(C\).  Hence

\[
 \operatorname {net}(A)=\operatorname {net}(C)=-s. \tag{1.9}
\]

Suppose first that \(|A|+|C|\le|Z|\).  Then

\[
 Z=AUC
\]

for some word \(U\), and comparison with \(Z=AR_0\) gives

\[
 R_0=UC.
\]

The physical word \(R_0\), read immediately after the first attainment of
height \(s\) in \(D_0\), never rises above that height and has net height
\(-(s-1)\).  But (1.9) would force

\[
 \operatorname {net}(U)
 =\operatorname {net}(R_0)-\operatorname {net}(C)=1.
\]

Thus the prefix \(U\) of \(R_0\) would rise one unit above the already
attained global maximum, a contradiction.  Therefore the two regions
overlap.

For overlapping prefix and suffix regions, the word equality (1.4)
forces the literal decompositions (1.7).  Since \(R_s\), like \(R_0\),
goes from height \(s\) to height one,

\[
 \operatorname {net}(O)
 =\operatorname {net}(A)-\operatorname {net}(R_s)
 =-s+(s-1)=-1.
\]

Parity gives \(|O|\equiv-1\pmod2\), proving the final assertion.
\(\square\)

The theorem rules out the optimistic disjoint-field tensorization at its
source.  Even before counting, the two certificate regions must share a
chronological word of negative net height.

## 2. Every symmetric capped pair gives an exact overlap-one return

Fix \(s\ge2\).  Choose Dyck words

\[
 S_0=S_s=\varnothing,
 \qquad
 \operatorname {ht}(S_j)\le\min(j,s-j)
 \quad(1\le j<s),                                  \tag{2.1}
\]

and

\[
 \operatorname {ht}(T_h)\le\min(h,s-1-h)
 \quad(0\le h<s).                                  \tag{2.2}
\]

Thus \(T_0=T_{s-1}=\varnothing\).  Put

\[
 Q_h=(S_{h-1}1)\cdots(S_01),                       \tag{2.3}
\]

and

\[
 V_h=(\overline T_{s-1}1)
       (\overline T_{s-2}1)\cdots(\overline T_h1),
 \qquad V_s=\varnothing.                           \tag{2.4}
\]

Define \(P_h\) by

\[
 P_h1=Q_hV_h.                                      \tag{2.5}
\]

For \(0\le h<s\), define

\[
 R_h=(\overline T_{h-1}0)\cdots(\overline T_00)
      (0S_{s-1})\cdots(0S_{h+1}),                 \tag{2.6}
\]

with empty ranges omitted, and put

\[
 R_s=(\overline T_{s-1}0)\cdots
      (\overline T_10)\overline T_0.              \tag{2.7}
\]

Finally set

\[
 D_h=P_h1R_h0S_h.                                  \tag{2.8}
\]

### Theorem 2.1 (literal overlap-one trace)

Every word \(D_h\) in (2.8) is Dyck of height \(s\), the displayed
factorization is its canonical first-maximum factorization, and

\[
 \boxed{\tau D_h=D_{h+1}\qquad(0\le h<s).}         \tag{2.9}
\]

Moreover \(D_0\) starts a first zero-winding omitted-label return of gap
\(2s+1\), and its carrier overlap is exactly the one-bit word

\[
 \boxed{O=0.}                                      \tag{2.10}
\]

#### Proof

The word \(Q_h\) first reaches height \(h\) at its last displayed
separator.  Starting there, the blocks of \(V_h\) successively raise the
running baseline from \(h\) to \(s\).  When the block indexed by \(j\) is
read, its complemented Dyck excursion descends by at most

\[
 \min(j,s-1-j),
\]

which is at most the number of preceding upward separators in \(V_h\).
Thus \(P_h1=Q_hV_h\) first reaches height \(s\) at its last symbol.

Read \(R_h\) from height \(s\).  In its initial \(T\)-part, the block
\(\overline T_j\) begins at height at least \(j+1\), so (2.2) keeps it
above zero.  After the \(T\)-part the height is \(s-h\).  In the
subsequent \(S\)-part, the complete block \(0S_j\) is based at height
\(j-h\); (2.1) keeps its maximum at most \(s\).  The last such block ends
at height one.  The same calculation, with the final separator deleted,
handles \(R_s\).  Hence \(R_h\) stays between heights one and \(s\), ends
at one, and the following displayed zero is the first return to zero.
The suffix \(S_h\) is Dyck of height at most \(s\).  This proves the
canonical factorization claim.

The definitions give the two literal identities

\[
 S_h1P_h=P_{h+1}1\overline T_h,                    \tag{2.11}
\]

and

\[
 \overline T_h0R_h=R_{h+1}0S_{h+1}.               \tag{2.12}
\]

Substitution into

\[
 \tau(P_h1R_h0S_h)=S_h1P_h0R_h
\]

proves (2.9).

Finally,

\[
 \sum_{h=0}^{s-1}(|S_h|+1)
 =|(S_{s-1}1)\cdots(S_01)|
 =|P_s1|=\delta(D_s).                              \tag{2.13}
\]

This is zero winding.  The strict first-passage theorem makes it the first
return.  In the carrier identity, (2.6)--(2.7) give

\[
 A=R_s0,
 \qquad C=0R_0,
\]

so the overlap is precisely the displayed zero.
\(\square\)

The construction is fully dynamic: no false static first-deepest-spine
iteration is used.

## 3. Exact enumeration of the overlap-one family

Let \(C_j(z)\) be the generating function for Dyck paths of height at most
\(j\), with semilength marked by \(z\).  Put

\[
\begin{aligned}
G_s(z)
&=\prod_{j=1}^{s-1}C_{\min(j,s-j)}(z)\\
&\qquad\cdot
  \prod_{h=0}^{s-1}C_{\min(h,s-1-h)}(z).           \tag{3.1}
\end{aligned}
\]

The tuple-to-root map is injective for a simpler dynamical reason.  The
root \(D_0\) determines every iterate \(\tau^hD_0\); each iterate has a
unique canonical first-maximum factorization and hence a unique suffix
\(S_h\).  Equation (2.11) then uniquely determines \(T_h\).  Thus two
tuples producing the same \(D_0\) coincide.  If \(|E|_{\rm e}\) denotes
Dyck semilength, direct reading of \(D_0\) gives

\[
 r=s+\sum_{j=1}^{s-1}|S_j|_{\rm e}
      +\sum_{h=0}^{s-1}|T_h|_{\rm e}.
\]

Therefore

\[
 \boxed{Z_{r,s}^{(1)}=[z^{r-s}]G_s(z).}            \tag{3.2}
\]

Families belonging to different values of \(s\) are disjoint as well:
Theorem 2.1 makes \(2s+1\) the first return gap, and one root cannot have
two different first return gaps.  Hence later sums over \(s\) count
distinct quotient roots, not repeated certificates of one root.

At the critical point

\[
 C_j(1/4)=\frac{2(j+1)}{j+2}.                      \tag{3.3}
\]

Define the normalized fixed-separator Kraft mass

\[
 K_s=4^{-s}G_s(1/4).                               \tag{3.4}
\]

If \(s=2t\), telescoping gives

\[
 \boxed{K_{2t}=\frac2{(t+1)^3(t+2)}.}              \tag{3.5}
\]

If \(s=2t+1\), it gives

\[
 \boxed{K_{2t+1}=\frac2{(t+1)(t+2)^3}.}            \tag{3.6}
\]

In particular

\[
 \boxed{K_s\asymp s^{-4}.}                        \tag{3.7}
\]

For each factor \(C_j\) in (3.1), let \(X_j\) have the critical
Boltzmann law

\[
 \Pr(X_j=n)=\frac{[z^n]C_j(z)\,4^{-n}}{C_j(1/4)}, \tag{3.8}
\]

with the repeated factors represented by independent copies.  Let \(Y_s\)
be their sum.  Equations (3.2)--(3.4) give the exact probability identity

\[
 \boxed{
 Z_{r,s}^{(1)}=4^rK_s\Pr(Y_s=r-s).}                \tag{3.9}
\]

This separates the two effects exactly: \(s^{-4}\) is the joint symmetric
endpoint-field mass, while the fixed total semilength is the lattice
probability in (3.9).

## 4. The critical size window has uniformly positive probability

We need no local limit theorem for the lower bound (0.6).  A first moment
and one spectral lower bound suffice.

### Lemma 4.1 (mean size)

Under (3.8),

\[
 \mathbb E X_j=\frac j3.                            \tag{4.1}
\]

Consequently

\[
 c_1s^2\le\mathbb E Y_s\le c_2s^2                 \tag{4.2}
\]

for absolute positive constants \(c_1,c_2\).

#### Proof

The continued-fraction recurrence

\[
 C_j(z)=\frac1{1-zC_{j-1}(z)}
\]

and (3.3) give, after logarithmic differentiation at \(z=1/4\),

\[
 \mu_j=\frac{j}{j+2}(1+\mu_{j-1}),
 \qquad \mu_0=0.
\]

Induction yields \(\mu_j=j/3\).  The sum of the caps in (3.1) is
\(\Theta(s^2)\), proving (4.2).
\(\square\)

### Lemma 4.2 (one macroscopic block)

There are constants \(0<\alpha<\beta<\infty\) and \(c_3>0\) such that,
for every sufficiently large \(s\), at least \(c_3s\) independent factors
in (3.1) obey

\[
 \Pr(\alpha s^2\le X_j\le\beta s^2)\ge\frac{c_3}{s}. \tag{4.3}
\]

#### Proof

At least a fixed positive fraction of the caps in (3.1) lie between
\(s/4\) and \(s/2\).  For such a cap \(j\), the exact path-graph spectral
formula is

\[
 [z^n]C_j(z)
 =\frac2{j+2}\sum_{q=1}^{j+1}
   \sin^2\!\frac{\pi q}{j+2}
   \left(2\cos\frac{\pi q}{j+2}\right)^{2n}.      \tag{4.4}
\]

All summands are nonnegative.  For
\(\alpha s^2\le n\le\beta s^2\), the \(q=1\) term gives

\[
 [z^n]C_j(z)\ge c_{\alpha,\beta}\frac{4^n}{s^3}.  \tag{4.5}
\]

Since \(C_j(1/4)\le2\), each individual value in that interval has
probability at least \(c/s^3\).  Summing over \(\Theta(s^2)\) values of
\(n\) proves (4.3).
\(\square\)

### Lemma 4.3 (uniform critical window)

There are constants \(0<a_0<b_0<\infty\) and \(c_0>0\) such that

\[
 \boxed{
 \Pr(a_0s^2\le Y_s\le b_0s^2)\ge c_0}             \tag{4.6}
\]

for every sufficiently large \(s\).

#### Proof

By Lemma 4.2 and independence, the probability that at least one of the
\(c_3s\) displayed factors lies in its macroscopic interval is at least

\[
 1-(1-c_3/s)^{c_3s}\ge c_4>0.                     \tag{4.7}
\]

On that event \(Y_s\ge\alpha s^2\).  By (4.2) and Markov's inequality,
choose \(b_0\) so large that

\[
 \Pr(Y_s>b_0s^2)\le c_4/2.
\]

Taking \(a_0=\alpha\) gives (4.6).
\(\square\)

## 5. Catalan-critical mass on Gaussian subsequences

### Theorem 5.1 (critical terminal-completion obstruction)

There are constants \(0<a<b<\infty\), \(c>0\), and infinitely many
integers \(r\) for which

\[
 \boxed{
 \sum_{a\sqrt r\le s\le b\sqrt r}Z_{r,s}^{(1)}
 \ge c\frac{\operatorname {Cat}_r}{2r+1}.}         \tag{5.1}
\]

#### Proof

Fix a large integer scale \(S\) and sum (4.6) over

\[
 S\le s\le2S.
\]

Put explicitly

\[
 I_S=
 \left[
  \left\lfloor a_0S^2+S\right\rfloor,
  \left\lceil4b_0S^2+2S\right\rceil
 \right]\cap\mathbb Z.
\]

For every \(S\le s\le2S\), the event in (4.6), after adding \(s\) to
the value of \(Y_s\), lies inside \(I_S\).  Therefore

\[
 \sum_{s=S}^{2S}
 \sum_{r\in I_S}\Pr(Y_s=r-s)\ge c_0S.             \tag{5.2}
\]

The interval is contained in \([c_5S^2,c_6S^2]\) for fixed positive
constants and has \(O(S^2)\) members.  By averaging, some
\(r=r(S)\in I_S\) satisfies

\[
 \sum_{s=S}^{2S}\Pr(Y_s=r-s)\ge\frac{c_7}{S}.     \tag{5.3}
\]

For these \(s\), (3.5)--(3.7) give \(K_s\ge c_8/S^4\).  Therefore (3.9)
and (5.3) yield

\[
 \sum_{s=S}^{2S}Z_{r,s}^{(1)}
 \ge c_9\frac{4^r}{S^5}.                          \tag{5.4}
\]

Since \(r\asymp S^2\), the Wallis estimates give

\[
 \frac{\operatorname {Cat}_r}{2r+1}
 \asymp\frac{4^r}{r^{5/2}}
 \asymp\frac{4^r}{S^5}.                           \tag{5.5}
\]

Equations (5.4)--(5.5) prove (5.1), with fixed \(a,b\) obtained from
\(r\asymp S^2\).  Letting \(S\to\infty\) supplies infinitely many ranks.
\(\square\)

The standard short-cycle itinerary bound says that the number of quotient
roots on cycles of length at most \(O(\sqrt r)\) is

\[
 \exp(O(\sqrt r\log r))=\exp(o(r)).                \tag{5.6}
\]

The right side of (5.1) is \(\exp(r\log4-o(r))\).  Removing all short-cycle
roots therefore preserves (5.1), after changing \(c\).

## 6. What this proves about the Pascal/trace gate

Theorem 5.1 is an obstruction to **counting sparsity**, not a counterexample
to residence packing.  A greedy interval selection from (5.1) may lose a
factor \(O(\sqrt r)\), and the theorem does not exclude much stronger
clustering on the actual quotient cycles.

Its consequence for the requested entropy route is nevertheless exact.
The following implication is false:

\[
 \left.
 \begin{array}{c}
 \text{forward staircase field}\\
 \text{dual staircase field}\\
 \text{terminal Dyck completion}\\
 \text{exact zero-winding chronology}\\
 \text{long quotient cycle}
 \end{array}
 \right\}
 \Longrightarrow
 o(B/N)\text{ possible starts}.                   \tag{6.1}
\]

The overlap-one family satisfies every premise on the left and has
\(\Omega(B/N)\) starts on the subsequence of Theorem 5.1.  In particular,
there is no universal extra completion factor

\[
 \eta_{r,A}\longrightarrow0                       \tag{6.2}
\]

at the level of actual-start enumeration.

For an edge-disjoint packed family, an additional factor may still come
from how the intervals occupy their quotient cycles.  The conditional
packing statement left by this obstruction is therefore narrower than the
former joint-completion lemma:

> **Chronology-sensitive clustering gate.**  Prove that the actual
> overlap-one traces in Section 2, and the larger-overlap traces not covered
> by that normal form, have aggregate quotient interval packing
> \(o_A(B/N)\), despite their Catalan-critical start count; equivalently,
> prove that their Pascal slot vectors or their two-child predecessor
> passages collide on quotient edges by a factor tending to infinity beyond
> the universal interval-conflict bound.

The inverse-pruning harmonic tower permits a constant fraction of fibres
even after bounded seam constraints, so the required factor cannot come
from multiplying independent slot probabilities.  It must use the order of
the transported slot vectors along the complete trace.

## 7. Exact boundary and caveats

Proved here:

1. the universal common carrier, compulsory overlap, and net-height law
   (1.7)--(1.8);
2. a literal dynamically valid overlap-one return for every symmetric
   capped pair of Dyck tuples;
3. exact enumeration and exact critical Kraft masses (3.2)--(3.7);
4. the positive critical size-window probability (4.6); and
5. Catalan-critical \(\Omega(B/N)\) long-cycle start mass on infinitely
   many ranks.

Not proved here:

1. that these starts contain an \(\Omega(B/N)\) edge-disjoint quotient
   subfamily;
2. failure of \(RP_A\);
3. a trace-clustering theorem for the overlap-one family;
4. constant one.

Thus the sought additional \(o(1)\) does not exist in terminal completion
or endpoint correlation alone.  If one continues through \(RP_A\), its
remaining possible location is the edge-disjoint chronology of the
complete transported Pascal trace.  This does not exclude a global
owner-injective literal fusion which bypasses the packing gate.
