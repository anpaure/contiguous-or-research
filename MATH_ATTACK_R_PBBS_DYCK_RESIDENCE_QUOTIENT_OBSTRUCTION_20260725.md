# Lane R: the exact Dyck-quotient obstruction to PBBS residence packing

Date: 2026-07-25

No computation, finite search, or web search is used in this note.

## 0. Verdict

Put

\[
N=2r+1,
\qquad
A=\binom Nr,
\qquad
B=A/N=\operatorname{Cat}_r,
\]

and let \(f\) be the canonical parenthesis-flip permutation whose orbits
form the PBBS factor of \(KG(N,r)\).  The rotation quotient has exactly
\(B\) states, canonically represented by Dyck words of semilength \(r\).
The quotient dynamics and its forgotten spatial phase admit the exact
skew-product formula

\[
 f([a,D])=[a+\delta(D),R(D)].
\tag{0.1}
\]

This formula gives two new exact facts.

1. For every \(r\ge2\), PBBS has no omitted-label gap three.  Thus every
   nontrivial projected residence interval has at least four transition
   edges; in particular, the previously bounded depth-two rank excess is
   actually zero pointwise.

2. The hoped-for local injection of packed short returns into quotient
   states is false with an unbounded fibre.  For every \(r\ge3\), there is
   an explicit quotient three-cycle whose lift is one PBBS component of
   length \(3N\).  That component contains

   \[
   \boxed{r}
   \]

   pairwise projected-edge-disjoint gap-five residence intervals, all with
   the same return-start quotient state and the same three quotient
   transition edges.

More generally, if \(I\) is a \(k\)-edge return interval, \(C\) is its
projected PBBS cycle, and \(k<|C|/2\), the exact maximum number of
edge-disjoint spatial translates of \(I\) is

\[
\boxed{
 \alpha_\Gamma(I)
 =\frac Nh
   \left\lfloor
    \frac{h}{\lceil k/d\rceil}
   \right\rfloor,
 \qquad
 h=|\operatorname{Stab}_\Gamma(C)|,
 \quad d=|C|/h.}
\tag{0.2}
\]

In particular,

\[
 \alpha_\Gamma(I)\ge \frac{N}{2k}.
\tag{0.3}
\]

For residence at most \(H=o(N)\), every nonempty rotation orbit of short
returns therefore has an explicitly packable fibre of size
\(\Omega(N/H)\), although every member has the identical ordered Dyck
quotient trace.

Consequently, physical packedness does **not** force a distinct, or even
bounded-load, local quotient-state certificate.  The desired global bound

\[
 \nu_H(P_r)=O(\operatorname{Cat}_r)
\tag{0.4}
\]

is neither proved nor disproved here.  What is ruled out is the proposed
local proof mechanism.  A proof of (0.4) must use a global rarity or
cross-orbit phase-competition theorem for the bad quotient cocycles.  It
cannot charge each packed return locally to one of the quotient states or
edges visited by that return.

For the pair-omission application in which the local PBBS factor is
\(KG(2m-1,m-1)\), substitute \(r=m-1\), so that
\(B=\operatorname{Cat}_{m-1}\).  If the odd graph is parametrized directly
as \(KG(2m+1,m)\), substitute \(r=m\), and (0.4) is the requested
\(O(\operatorname{Cat}_m)\) statement.

## 1. The Catalan section and the exact phase cocycle

Coordinates are read cyclically modulo \(N\).  A one is an opening step and
a zero is a closing step.  Every rank-\(r\) word has one forward-unmatched
zero.  Let \(\rho\) be rotation by one coordinate in the direction of
reading, so that it increases the root coordinate by one.

The action of \(\langle\rho\rangle\cong\mathbb Z_N\) on rank-\(r\) states
is free.  Indeed, if a nontrivial subgroup of order \(s\) stabilized a
state, its support would be a union of coordinate orbits of size \(s\), so
\(s\mid r\) as well as \(s\mid N\).  Since \(\gcd(N,r)=1\), this forces
\(s=1\).

Rotate a state until its unique unmatched zero is at coordinate \(a\), and
read the next \(2r\) bits.  They form a Dyck word \(D\) of semilength \(r\).
Write the resulting state as

\[
 [a,D].
\]

Every state has a unique representation of this form.  Hence the rotation
quotient is the set \(\mathcal D_r\) of Dyck words, and

\[
 |\mathcal D_r|
 =\frac1N\binom Nr
 =\frac1{r+1}\binom{2r}{r}
 =\operatorname{Cat}_r.
\tag{1.1}
\]

For a Dyck word \(D\), let \(p(D)\) be the first position at which its
height attains its global maximum.  Write

\[
 D=U\,1\,V
\tag{1.2}
\]

at that up-step, so \(p(D)=|U|+1\).  If \(\overline W\) denotes bitwise
complement, define

\[
 R(D)=\overline V\,0\,\overline U,
 \qquad
 \delta(D)=p(D)=|U|+1.
\tag{1.3}
\]

### Theorem 1.1 (exact quotient PBBS skew product)

For every \(a\in\mathbb Z_N\) and \(D\in\mathcal D_r\),

\[
\boxed{
 f([a,D])=[a+\delta(D),R(D)].}
\tag{1.4}
\]

In particular, \(R\) is a permutation of \(\mathcal D_r\), and the omitted
label of the factor edge leaving \([a,D]\) is exactly \(a\).

#### Proof

Cut immediately after the unmatched zero.  Every bit of \(D\) is matched.
The parenthesis flip therefore leaves the root zero fixed and complements
all bits of \(D\), giving the cyclic word

\[
 0\,\overline D.
\]

Relative to this cut, the prefix height after the first zero and the first
\(j\) bits of \(\overline D\) is

\[
 -1-h_D(j),
\]

where \(h_D(j)\) is the height of the first \(j\) bits of \(D\).  The first
attainment of the global minimum is therefore the complement of the up-step
where \(D\) first attains its global maximum, namely position \(p(D)\).
That zero is the new forward-unmatched zero.  Cutting there gives

\[
 0\,\overline V\,0\,\overline U,
\]

so the new Dyck root is \(R(D)=\overline V0\overline U\), and the physical
root moves by \(p(D)\).  This is (1.4).  Since \(f\) is a permutation and
commutes with rotation, its quotient map \(R\) is a permutation.  The root
zero is precisely the coordinate omitted by both endpoints of the PBBS
odd-graph edge.  \(\square\)

For \(g\ge1\), put

\[
 S_g(D)=\sum_{j=0}^{g-1}\delta(R^jD)\pmod N.
\tag{1.5}
\]

Equation (1.4) immediately gives the exact return criterion

\[
 \lambda_i=\lambda_{i+g}
 \quad\Longleftrightarrow\quad
 S_g(D_i)=0.
\tag{1.6}
\]

The occurrences are consecutive precisely when \(S_j(D_i)\ne0\) for
\(1\le j<g\).  The criterion is independent of the initial phase \(a\).
Thus every quotient return has all \(N\) spatial lifts.

If

\[
 g(D)=\min\{g\ge1:S_g(D)=0\},
\tag{1.7}
\]

then the exact number \(G_g\) of physical consecutive omitted-label gaps of
size \(g\), summed over the PBBS factor, is

\[
\boxed{
 G_g=N\,|\{D\in\mathcal D_r:g(D)=g\}|.}
\tag{1.8}
\]

Indeed, each quotient state has exactly \(N\) labelled lifts, and (1.6)
gives the same next-return gap on all of them.

## 2. Gap three is impossible

The quotient formula permits a complete symbolic analysis of the first
possible odd gap.

### Theorem 2.1 (no PBBS gap three)

For every \(r\ge2\) and every PBBS orbit in \(KG(2r+1,r)\),

\[
\boxed{\lambda_i\ne\lambda_{i+3}\quad\text{for every }i.}
\tag{2.1}
\]

Consequently every consecutive omitted-label gap is at least five.

#### Proof

Let \(D\in\mathcal D_r\), let \(H\) be its maximum height, and refine
(1.2) as

\[
 D=A\,1\,C\,0\,E.
\tag{2.2}
\]

Here the displayed one is the first step reaching height \(H\), and the
displayed zero is the first subsequent return from height one to height
zero.  Thus:

- \(A\) goes from height zero to height \(H-1\) without reaching \(H\);
- between the displayed one and zero, the path \(C\) stays between heights
  one and \(H\);
- \(E\) is a Dyck word.

Applying (1.3) gives

\[
 R(D)=\overline C\,1\,\overline E\,0\,\overline A.
\tag{2.3}
\]

The prefix \(\overline C\) rises from zero to \(H-1\) and never reaches
\(H\).  The displayed one first reaches height \(H\).  The word
\(\overline E\) starts at height \(H\) and never rises above it; after the
displayed zero, \(\overline A\) stays below \(H\) and returns to zero.
Hence the displayed one in (2.3) is the first global-maximum step of
\(R(D)\).  A second use of (1.3) therefore yields

\[
 R^2(D)=E\,1\,A\,0\,C.
\tag{2.4}
\]

Moreover,

\[
 \delta(D)+\delta(RD)
 =|A|+|C|+2
 =2r-|E|.
\tag{2.5}
\]

Suppose that the old omitted coordinate returned after three steps.  By
(1.6),

\[
 2r-|E|+\delta(R^2D)\equiv0\pmod{2r+1}.
\tag{2.6}
\]

Since \(1\le\delta(R^2D)\le2r\), the only possible multiple of \(N=2r+1\)
in (2.6) is \(N\); the multiple \(2N\) would require
\(\delta(R^2D)=N+1+|E|>2r\).  Therefore

\[
 \delta(R^2D)=|E|+1.
\tag{2.7}
\]

Let \(H_E\) be the maximum height of \(E\).  In the word
\(E1A0C\), the global maximum is \(\max(H_E,H)\).

If \(H_E\ge H\), its first global maximum occurs inside \(E\), and hence

\[
 \delta(R^2D)\le |E|,
\]

contradicting (2.7).

If \(H_E<H\), the first global maximum occurs in \(1A\), at position

\[
 |E|+1+t,
\]

where \(t\) is the first time at which \(A\) reaches height \(H-1\).
Equality (2.7) forces \(t=0\), and therefore \(H=1\).  Then \(A\) is empty,
because it cannot reach height one before the first global maximum;
\(H_E<1\) forces \(E\) to be empty; and \(C\) is empty because it must stay
at height one while every nonempty bit changes the height.  Thus \(D=10\)
and \(r=1\), contrary to the hypothesis.

Both cases are impossible, proving (2.1).  \(\square\)

For completeness, the audited step-two recurrence

\[
 A_{i+2}=A_i-\{\lambda_{i+1}\}+\{\lambda_i\}
\]

excludes two consecutive equal labels, since they would repeat a factor
vertex.  After an edge labelled \(x\), coordinate \(x\) is absent at two
successive vertices and then toggles until the next \(x\)-labelled edge;
hence consecutive occurrences of \(x\) have odd gap.  The only possible gap
below five was therefore three, which Theorem 2.1 excludes.

### Corollary 2.2 (pointwise depth-two exactness)

For \(r\ge2\), every three-state parity intersection satisfies

\[
\boxed{
 |A_i\cap A_{i+2}\cap A_{i+4}|=r-2.}
\tag{2.8}
\]

Equivalently, the PBBS rank-excess variable \(\eta_{i,2}\) vanishes for
every \(i\), not merely in aggregate:

\[
 E_2(P_r)=0.
\tag{2.9}
\]

#### Proof

The exact gap formula at depth two charges only consecutive omitted-label
gaps of size three.  Theorem 2.1 rules all of them out.  \(\square\)

For the complement-projected residence intervals, a gap \(g=2s+1\) has
residence length \(s+1\) and contains \(s+2\) projected transition edges.
Theorem 2.1 therefore implies

\[
\boxed{|I|\ge4}
\tag{2.10}
\]

for every nonempty positive residence interval when \(r\ge2\).

## 3. An all-r gap-five quotient collision

The lower bound (2.10) is sharp in every dimension from \(r=3\) onward.
More importantly, the sharp example has an unbounded deck fibre.

### Theorem 3.1 (explicit quotient three-cycle and gap-five return)

Let \(r\ge3\), put \(t=r-3\), and define

\[
\begin{aligned}
D_0&=110100(10)^t,\\
D_1&=1011(01)^t00,\\
D_2&=(10)^t110010.
\end{aligned}
\tag{3.1}
\]

Then \(D_0,D_1,D_2\) are distinct Dyck words of semilength \(r\), and

\[
\boxed{
 R(D_0)=D_1,\qquad
 R(D_1)=D_2,\qquad
 R(D_2)=D_0,}
\tag{3.2}
\]

with displacements

\[
\boxed{
 \delta(D_0)=2,\qquad
 \delta(D_1)=4,\qquad
 \delta(D_2)=N-5.}
\tag{3.3}
\]

Starting from quotient state \(D_1\), the next occurrence of the same
omitted label is exactly five PBBS steps later.

#### Proof

The height sequences are explicit.

- \(D_0\) has heights \(1,2,1,2,1,0\), followed by \(t\) excursions
  \(1,0\).
- \(D_1\) has initial heights \(1,0,1,2\); each following \(01\) lowers
  the height to one and returns it to two; the final \(00\) returns through
  one to zero.
- \(D_2\) has \(t\) excursions \(1,0\), followed by suffix heights
  \(1,2,1,0,1,0\).

Thus all three words are Dyck, and their first global maxima occur at
positions

\[
 2,\qquad4,\qquad2t+2=N-5,
\tag{3.4}
\]

respectively.  Formula (1.3) gives

\[
\begin{aligned}
R(D_0)
 &=1011(01)^t00=D_1,\\
R(D_1)
 &=(10)^t110010=D_2,\\
R(D_2)
 &=11010(01)^t0
  =110100(10)^t
  =D_0.
\end{aligned}
\tag{3.5}

The equality in the last line uses \((01)^t0=0(10)^t\).  This proves
(3.2)--(3.3).  The words are distinct: \(D_0\) begins \(11\), whereas
\(D_1\) begins \(10\); direct comparison at the first displayed suffix
separates \(D_2\) from both, including the case \(t=0\).

Starting at \(D_1\), the first five phase increments are

\[
 4,\quad N-5,\quad2,\quad4,\quad N-5.
\tag{3.6}
\]

Their proper partial sums are

\[
 4,\qquad N-1,\qquad N+1,\qquad N+5,
\tag{3.7}
\]

which are congruent to \(4,-1,1,5\pmod N\).  None is zero because
\(N\ge7\).  The fifth partial sum is \(2N\).  The return criterion (1.6)
therefore gives a consecutive omitted-label gap exactly equal to five.
\(\square\)

### Theorem 3.2 (exact r-fold packed collision)

For every \(r\ge3\), the gap-five return in Theorem 3.1 has \(N\) spatial
translates whose conflict graph is the odd cycle \(C_N\).  Hence exactly

\[
\boxed{
 \left\lfloor\frac N2\right\rfloor=r}
\tag{3.8}
\]

of those translates can be chosen pairwise disjoint as sets of projected
transition edges.  In particular,

\[
\boxed{\nu_3(P_r)\ge r.}
\tag{3.9}
\]

All \(r\) intervals have the same return-start quotient state \(D_1\), the
same ordered quotient-tail trace

\[
 (D_0,D_2,D_1,D_0),
\tag{3.10}
\]

and the same three quotient transition edges.

#### Proof

Let the return begin at time \(i\), rotate so \(\lambda_i=0\), and put
\(X_j=[N]\setminus A_j\).  Write

\[
 e_j:X_j\longrightarrow X_{j+2}
\]

for the canonically oriented complement-projected step-two transition.
For a gap at positions \(i,i+5\), the residence convention gives

\[
 I_i={e_{i-1},e_{i+1},e_{i+3},e_{i+5}\}.
\tag{3.11}
\]

The four quotient tails and root phases are

\[
\begin{array}{c|c|c}
\text{transition tail}&\text{quotient state}&\text{phase}\pmod N\\ \hline
i-1&D_0&-2\\
i+1&D_2&4\\
i+3&D_1&1\\
i+5&D_0&0.
\end{array}
\tag{3.12}
\]

The first row follows because the displacement from \(D_0\) to \(D_1\)
is two; the other rows are the partial sums in (3.7) and the final zero sum.
In particular,

\[
 A_{i+5}=\rho^2A_{i-1}.
\]

Equivariance of \(f^2\) and complementation then gives

\[
 e_{i+5}=\rho^2e_{i-1}.
\tag{3.13}
\]

The quotient endpoint pairs of the four transitions are, in order,

\[
 \{D_0,D_2\},\quad
 \{D_2,D_1\},\quad
 \{D_1,D_0\},\quad
 \{D_0,D_2\}.
\tag{3.14}
\]

They are pairwise distinct except for the first and last.  Thus treating
the cut edges as undirected introduces no additional collision: a spatial
rotation cannot reverse the repeated quotient edge, because it preserves
the quotient source state.

For \(a\in\mathbb Z_N\), put \(I^a=\rho^aI_i\).  On the repeated
\(D_0\)-edge orbit, \(I^a\) uses phases \(a-2\) and \(a\); on each of the
other two edge orbits it uses one phase.  Rotation acts freely on every
projected edge orbit, since it already acts freely on its rank-\(r\) tail.
Therefore, for \(a\ne b\),

\[
 I^a\cap I^b\ne\varnothing
 \quad\Longleftrightarrow\quad
 a-b\equiv\pm2\pmod N.
\tag{3.15}
\]

The conflict graph is \(\operatorname{Cay}(\mathbb Z_N,\{\pm2\})\).  Since
\(N\) is odd, multiplication by two permutes \(\mathbb Z_N\), so this graph
is \(C_N\).  Its independence number is \(\lfloor N/2\rfloor=r\), proving
(3.8)--(3.9).  Quotienting (3.12)--(3.14) proves (3.10).  \(\square\)

### Corollary 3.3 (the obstruction occurs in one level-three component)

The three quotient displacements have total

\[
 2+4+(N-5)=N+1\equiv1\pmod N.
\tag{3.16}
\]

Consequently the lift of the quotient three-cycle is one PBBS component of
length \(3N\), and all \(r\) intervals in Theorem 3.2 lie in that one
component.

#### Proof

After three applications of \(f\), the quotient state returns and the phase
advances by one.  Hence all \(N\) phases lie in one orbit, whose length is
\(3N\).  Since \(3N\) is odd, \(f^2\) also acts as one cycle on these states.
\(\square\)

Thus even the stronger prospective componentwise estimate

\[
 \text{packing in a PBBS component of level }\ell=O(\ell)
\]

is false: the explicit component has level \(3\) and packing number at
least \(r\).

The rotor reduction assumes \(H\le(r+1)/2\).  The choice \(H=3\) lies in
that range for \(r\ge5\).  The packing statement itself, (3.9), is valid
already for every \(r\ge3\).

## 4. Exact packing of the spatial-translate fibre

The preceding example is one instance of a general deck-packing formula.

Let

\[
 \Gamma=\langle\rho\rangle\cong C_N,
 \qquad T=f^2.
\]

Complementation identifies the directed \(T\)-cycles with the directed
complement-projected transition cycles.  Let \(I\) be \(k\) consecutive
transition edges of one such directed cycle \(C\), and put

\[
 M=|C|,
 \qquad
 S=\operatorname{Stab}_\Gamma(C),
 \qquad
 h=|S|,
 \qquad
 d=M/h.
\tag{4.1}
\]

Every projected PBBS cycle has length divisible by \(N\).  Indeed, an
\(f\)-cycle has length \(\ell N\); if it has odd length, \(f^2\) has the
same cycle, and if it has even length, \(f^2\) splits it into two cycles of
length \(\ell N/2\), with \(\ell\) even.  In either case \(M\ge N\).

### Theorem 4.1 (spatial translate-packing formula)

Assume \(k<M/2\).  Among the \(N\) spatial translates of \(I\), the exact
maximum size of a pairwise edge-disjoint subfamily is

\[
\boxed{
 \alpha_\Gamma(I)
 =\frac Nh
   \left\lfloor
    \frac{h}{\lceil k/d\rceil}
   \right\rfloor.}
\tag{4.2}
\]

Consequently,

\[
\boxed{
 \alpha_\Gamma(I)
 \ge \frac{N}{2\lceil k/d\rceil}
 \ge \frac{N}{2k}.}
\tag{4.3}
\]

If \(k\le d\), all \(N\) translates are pairwise edge-disjoint.

#### Proof

Every element of \(S\) commutes with \(T\), so it acts as an
orientation-preserving shift of the directed cycle \(C\).  The action is
free on the vertices of \(C\), because spatial rotation is free on rank-\(r\)
states.  Its image is therefore the unique order-\(h\) subgroup of the
shift group \(\mathbb Z_M\), namely

\[
 d\mathbb Z_M.
\]

The \(N\) translates of \(C\) form \(N/h\) distinct directed cycles.  On
each such cycle, the corresponding \(h\) translates of \(I\) start at the
\(h\) positions spaced by \(d\) edges.

Put

\[
 a=\lceil k/d\rceil.
\]

Two of these \(k\)-edge arcs are disjoint exactly when the circular distance
between their start indices in \(\mathbb Z_h\), in both directions, is at
least \(a\).  If \(q\) start indices are selected, their \(q\) circular
gaps therefore have sum \(h\) and are each at least \(a\), giving

\[
 q\le\lfloor h/a\rfloor.
\]

Conversely, the starts

\[
 0,a,2a,\ldots,(\lfloor h/a\rfloor-1)a
\]

have every circular gap at least \(a\), so the bound is attained.  Multiply
by the \(N/h\) distinct cycles to obtain (4.2).

Since \(a\le h\), one has \(\lfloor h/a\rfloor\ge h/(2a)\).  Also
\(d\ge1\), so \(\lceil k/d\rceil\le k\).  These give (4.3).  If \(k\le d\),
then \(a=1\), and (4.2) equals \(N\).  \(\square\)

Every spatial translate in Theorem 4.1 has the identical ordered trace in
the Dyck/rotation quotient.  For a residence interval of length at most
\(H\),

\[
 k\le H+1.
\]

If \(H=o(N)\), then eventually \(k<M/2\), and (4.3) gives

\[
\boxed{
 \alpha_\Gamma(I)\ge\frac{N}{2(H+1)}.}
\tag{4.4}
\]

In the target range

\[
 H=\sqrt r\,\omega(r),
 \qquad
 \omega(r)\to\infty,
 \qquad
 \omega(r)=o\!\left(\frac{\sqrt r}{\log^2r}\right),
\tag{4.5}
\]

the lower bound in (4.4) is

\[
 \Omega\!\left(\frac{\sqrt r}{\omega(r)}\right)\to\infty.
\tag{4.6}
\]

Thus the loss of the spatial phase is not a constant-fibre defect at the
Gaussian scale.

For the explicit component in Section 3, \(M=3N\), \(h=N\), \(d=3\), and
\(k=4\).  Formula (4.2) becomes

\[
 \alpha_\Gamma(I)=\left\lfloor\frac N2\right\rfloor=r,
\]

in agreement with the direct conflict-graph proof.

## 5. The exact quotient-Hall boundary

Let \(\mathcal E\) be the canonically oriented projected transition-edge
set.  Rotation acts freely on \(\mathcal E\), because it acts freely on the
tail state of every edge.  Hence

\[
 |\mathcal E/\Gamma|=A/N=B=\operatorname{Cat}_r.
\tag{5.1}
\]

For a residence interval \(I\), let

\[
 Q(I)\subseteq\mathcal E/\Gamma
\]

be the set of quotient transition edges visited by \(I\).  Let
\(\mathcal P\) be a pairwise physical-edge-disjoint family of residence
intervals.

### Theorem 5.1 (capacitated quotient-certificate criterion)

For an integer \(C\ge1\), there is an assignment

\[
 c:\mathcal P\longrightarrow\mathcal E/\Gamma
\]

such that

\[
 c(I)\in Q(I)
\]

for every \(I\), and every quotient edge receives at most \(C\) intervals,
if and only if

\[
\boxed{
 |\mathcal A|
 \le C\left|\bigcup_{I\in\mathcal A}Q(I)\right|
 \quad\text{for every }\mathcal A\subseteq\mathcal P.}
\tag{5.2}
\]

Whenever (5.2) holds,

\[
 |\mathcal P|\le C\operatorname{Cat}_r.
\tag{5.3}
\]

#### Proof

Make a bipartite graph with left vertices \(\mathcal P\), right vertices
\(\mathcal E/\Gamma\), and adjacency \(I\sim q\) exactly when \(q\in Q(I)\).
Replace every right vertex by \(C\) identical copies.  Hall's theorem on the
cloned graph is exactly (5.2), and a matching is exactly the required
assignment.  Summing the right capacities and using (5.1) gives (5.3).
\(\square\)

Physical edge-disjointness alone gives only the volume inequality

\[
\boxed{
 \sum_{I\in\mathcal A}|I|
 \le
 N\left|\bigcup_{I\in\mathcal A}Q(I)\right|.}
\tag{5.4}
\]

Indeed, the intervals on the left use distinct physical edges, while each
quotient edge on the right has exactly \(N\) physical lifts.  By (2.10),

\[
 |\mathcal A|
 \le
 \frac N4
 \left|\bigcup_{I\in\mathcal A}Q(I)\right|.
\tag{5.5}
\]

Thus the bare volume argument supplies only an order-\(N\) Hall load.

The explicit packing in Theorem 3.2 has \(r\) intervals and exactly three
quotient edges in the union of their supports.  Hence every local
quotient-edge certificate for that packing has maximum load at least

\[
\boxed{\left\lceil\frac r3\right\rceil.}
\tag{5.6}
\]

The same bound holds if certificates are chosen from the three quotient
states in the interval trace.  If the certificate is required to be the
return-start quotient state, all \(r\) intervals receive \(D_1\), so the
fibre is exactly \(r\).  Any deterministic certificate depending only on
the ordered unphased quotient trace likewise has fibre \(r\).

Therefore no constant \(C\) can make (5.2) follow from physical packedness.
This is an exact obstruction, not a missing estimate.

## 6. What remains possible

Let \(\overline T=R^2\) act on the quotient transition tails.  Its cycles
partition the \(B\) quotient edges.  The full spatial lifts of distinct
\(\overline T\)-cycles are edge-disjoint invariant blocks, and every
residence interval remains inside one such block.  Consequently the global
packing number is the sum of the packing numbers in these lifted quotient
blocks.

The example in Section 3 is one quotient block of size three with physical
packing number at least \(r\).  Hence a uniform blockwise estimate

\[
 \nu_H(\text{lift of }O)=O(|O|)
\]

is also false.

This does not contradict a global Catalan estimate, because the exhibited
bad quotient block is only one block among \(B\) quotient states.  A global
proof could still show that high phase-packing ratios occur on sufficiently
few quotient blocks, or that different return patterns inside most lifted
blocks compete for the same physical phases.  In the notation (1.5)--(1.7),
such a proof must use the distribution and overlap geometry of the cocycle
partial sums

\[
 \sum_{j<u}\delta(R^jD)\pmod N.
\]

For comparison, the stronger assertion that the **total number** of returns
through residence \(H\) is \(O(B)\) would, by (1.8), require the rare-state
estimate

\[
 \left|
  \{D\in\mathcal D_r:g(D)\le2H-1\}
 \right|
 =O(B/N).
\tag{6.1}
\]

Packing permits many more short returns than (6.1), but Theorems 3.2 and 4.1
show that it still needs information beyond the unphased quotient trace.

What has been closed is the proposed implication

\[
 \text{physical edge-disjointness}
 \quad\Longrightarrow\quad
 \text{distinct or bounded-load local quotient certificates}.
\]

Theorems 3.2, 4.1, and 5.1 show exactly why it fails and quantify the lost
deck phase.  The global bound \(\nu_H(P_r)=O(\operatorname{Cat}_r)\), and
hence the PBBS residence route to the constant-one contiguous-OR theorem,
remain open beyond this obstruction.

## 7. Independent audit of the decisive step

The decisive collision calculation can be checked without any structural
PBBS input beyond (1.4):

1. The quotient three-cycle has increments \(2,4,N-5\), whose cycle sum is
   \(N+1\equiv1\pmod N\).  Hence its lift is one \(3N\)-cycle.
2. Starting at \(D_1\), the five partial sums are
   \(4,N-1,N+1,N+5,2N\); exactly the last is zero modulo \(N\).
3. The residence edge tails occur at times \(-1,1,3,5\), with quotient
   states \(D_0,D_2,D_1,D_0\) and phases \(-2,4,1,0\).
4. Only the first and fourth quotient edges can coincide under rotation,
   and their phase difference is two.  Therefore two translated intervals
   meet exactly at phase difference \(\pm2\).
5. Since \(N\) is odd, the \(\pm2\) Cayley graph is one \(N\)-cycle, whose
   exact independence number is \(r\).

This separately verifies the unbounded-fibre obstruction and its constants.
