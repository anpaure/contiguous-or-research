# Audit: orbitwise coordinate homomesy for the periodic box-ball map

Date: 2026-07-24

## Verdict

The stated coordinate-homomesy theorem is **valid** for (0<N<L/2), and the
Kneser-cycle consequences stated with it are valid.  The theta-function proof
does cover repeated soliton amplitudes.  No unproved genericity or
distinct-amplitude assumption is being smuggled into the argument.

There is one bridge that should be stated in the manuscript rather than left
implicit: the cyclic parenthesis-flip map (f) is the periodic box-ball
evolution (T_l) for any carrier capacity (l) at least the largest soliton
amplitude (in particular, (l=N) suffices).  A short proof of this bridge is
included below.

The audit used the primary sources:

- A. Kuniba and R. Sakamoto, *Combinatorial Bethe ansatz and ultradiscrete
  Riemann theta function with rational characteristics*, arXiv:nlin/0611046v2.
- A. Merino, T. Mütze and Namrata, *Kneser graphs are Hamiltonian*,
  arXiv:2212.03918v4.
- J. Petr and P. Turek, *The wreath matrix*, arXiv:2501.07269v2.

This is a mathematical audit, not a bibliographic-priority determination.

## 1. Parenthesis flip equals the infinite-capacity PBBS evolution

Interpret a 1-bit as a ball and a 0-bit as an empty box.  Because (L>2N),
cyclic parenthesis matching pairs every 1 with a 0 and leaves (L-2N) zeroes
unmatched.

Choose a cyclic cut immediately after an unmatched zero.  Starting with an
empty carrier and scanning from this cut, pick up a ball at every 1 and, at a
0, drop a ball exactly when the carrier is nonempty.  The carrier load is the
usual parenthesis height.  Thus the zeroes at which a ball is dropped are
exactly the matched zeroes.  At the end of the scan the carrier is empty again.
Consequently the update changes every 1 to 0, every matched 0 to 1, and leaves
the unmatched zeroes unchanged: this is precisely the map (f).

The carrier never holds more than (N) balls, so capacity (l=N) is already
infinite for this state.  Both the periodic-carrier rule and (f) commute with
cyclic rotation, so the choice of the cut does not alter the resulting labelled
cyclic state.  This identifies (f) with (T_l) for (l\ge N), hence with the
flow denoted (T_\infty) in the theta-function argument.

## 2. The Kuniba--Sakamoto formula applies with repeated amplitudes

For a fixed action variable, let the distinct soliton amplitudes be indexed by
ℐ, with multiplicities (m_i\ge1).  In the notation of arXiv:nlin/0611046,

\[
 F_{ij}=\delta_{ij}p_i+2\min(i,j)m_j,
 \qquad M=\operatorname{diag}(m_i),
 \qquad \Omega=MF.
\]

The paper explicitly states that its Theorem 5.1 covers all states and extends
the earlier distinct-amplitude formula.  Repeated amplitudes enter through the
rational characteristics and the correction
χ\((s;\widetilde I)\).  Under (T_\infty), every rigging having amplitude
(i) is translated by the same amount (i).  Therefore all differences
(I_{i,\beta}-I_{i,\alpha}), and hence χ, are invariant.  Meanwhile the bundled
angle variable is translated by (M h_\infty).  Thus the time-dependent tau
function really has the form

\[
 \tau_t(j)=\max_{s\in\mathbb Z^g/M\mathbb Z^g}
 \left\{
 \Theta_{M^{-1}s}(z_{t,j})+\chi(s;\widetilde I)
 \right\},
 \quad
 z_{t,j}=I+M\left(t h_\infty-jh_1-\frac p2\right),
\]

and the state bit is

\[
 x_{j,t}=\tau_t(j)-\tau_t(j-1)-\tau_{t+1}(j)+\tau_{t+1}(j-1).
\]

No multiplicity-one hypothesis is used here.

## 3. The determinant translation is a genuine period

Let

\[
 D=\det F>0,
 \qquad u=\operatorname{adj}(F)h_\infty\in\mathbb Z^g.
\]

Then (Fu=Dh_\infty), and hence

\[
 z_{t+D,j}-z_{t,j}=DMh_\infty=MFu=\Omega u.
\]

Kuniba--Sakamoto's quasi-periodicity formula is, for any
(v\in\Omega\mathbb Z^g),

\[
 \Theta_a(z+v)=\Theta_a(z)+v^{\mathsf T}\Omega^{-1}
 \left(z+\frac v2\right).
\]

With (v=\Omega u), the additive term is

\[
 u^{\mathsf T}z+\frac12u^{\mathsf T}\Omega u,
\]

independent of the rational characteristic (a).  It therefore passes through
the maximum over characteristics, giving

\[
 \tau_{t+D}(j)-\tau_t(j)
 =u^{\mathsf T}z_{t,j}+\frac12u^{\mathsf T}\Omega u.
\]

The right-hand side is separately affine in (t) and (j).  Its mixed finite
difference vanishes, so the four-term tau formula gives
(x_{j,t+D}=x_{j,t}).  Therefore (D) is an orbit period.  (For the trivial
(N=0) state, homomesy is immediate and this action-variable discussion can be
omitted.)

## 4. Telescoping proves site homomesy

Summing the four-term expression from (t=0) through (D-1) gives

\[
\begin{aligned}
 S_j
 &=\sum_{t=0}^{D-1}x_{j,t}\\
 &=\tau_0(j)-\tau_0(j-1)-\tau_D(j)+\tau_D(j-1)\\
 &=u^{\mathsf T}(z_{0,j-1}-z_{0,j})
 =u^{\mathsf T}Mh_1,
\end{aligned}
\]

which is independent of (j).  Each of the (D) time slices has (N) balls,
so summing over the (L) sites yields

\[
 S_j=\frac{DN}{L}.
\]

If (P) is the fundamental period, then (P\mid D), and the first (D)
iterates are (D/P) repetitions of the fundamental orbit.  Dividing by
(D/P) proves

\[
 \sum_{t=0}^{P-1}(T^t x)_j=\frac{PN}{L}
\]

for every site (j).  Integrality is equivalent to

\[
 \frac{L}{\gcd(L,N)}\mid P.
\]

## 5. Three-state refinement

Every 1 is matched, so at any time there are exactly (N) matched ones.  A
site is a matched zero at time (t) exactly when it is occupied at time
(t+1).  Hence each site is a matched one and a matched zero exactly (PN/L)
times over a fundamental orbit.  The remaining count is

\[
 P-2\frac{PN}{L}=\frac{P(L-2N)}{L},
\]

which is the unmatched-zero count at that site.

## 6. Kneser-cycle consequences

Merino--Mütze--Namrata prove directly that (f) is invertible and that its
orbits form a cycle factor of (K(n,k)).  Adjacent supports are disjoint because
all old 1s are flipped to 0 and only matched zeroes become 1.

Put

\[
 g=\gcd(n,k),\qquad M_0=n/g,\qquad s=k/g.
\]

For a parenthesis orbit (C) of length (P), the theorem gives

\[
 M_0\mid P,
 \qquad P=\ell M_0,
 \qquad d_v(C)=Pk/n=\ell s
\]

for every ground point (v).  Thus every individual cycle is point-regular.
Summing its lengths over the cycle factor gives

\[
 \sum_C\ell_C=\frac1{M_0}\binom nk
 =\frac gn\binom nk,
\]

the number of wreaths required by a decomposition.

## 7. Critical-diagonal reconstruction is correct

Assume

\[
 n=(2s+1)g,\qquad k=sg,
\]

and let (A_0,A_1,\ldots,A_{2s}) be a point-regular
(C_{2s+1}) in (K(n,k)).  Point regularity forces every point to occur in
exactly (s) of the (A_i).

For a point (x), its occurrence positions are an independent (s)-set in
the odd cycle (C_{2s+1}).  Such an independent set has exactly one edge whose
two endpoints are both absent: its cyclic binary word has (s) isolated ones
and (s+1) zeroes, hence exactly one run of two zeroes and all other zero-runs
have length one.

Set

\[
 B_i=[n]\setminus(A_i\cup A_{i+1}).
\]

Every point lies in exactly one \(B_i\), and \(|B_i|=n-2k=g\), so the
(B_i) partition the ground set.  If (x\in B_j), its occurrence positions
must be

\[
 j+2,j+4,\ldots,j+2s.
\]

Consequently

\[
 A_i=B_{i-2}\cup B_{i-4}\cup\cdots\cup B_{i-2s}.
\]

Because multiplication by `-2` permutes `Z/(2s+1)Z`, put
`P_c=B_{-2c}`.  Writing `i=-2a`, the last display becomes

\[
 A_{-2a}=P_{a+1}\cup\cdots\cup P_{a+s}.
\]

Thus the family is precisely all cyclic windows of `s` consecutive
`g`-blocks.  This is an `(n,k)`-wreath under the Petr--Turek/Baranyai
definition (successive wreath starts advance by `k=sg`, i.e. by `s`
blocks, and `gcd(s,2s+1)=1`).

It follows in particular that every minimum-length parenthesis orbit on this
diagonal is a wreath.

## 8. Audited examples and scope

A light independent enumeration reproduces the stated parenthesis orbits

\[
 13,24,35,46,15,26
\]

at ((n,k)=(6,2)), and

\[
 135,246,357,468,157,268,137,248
\]

at ((8,3)).  It also reproduces exactly the claimed cycle-length set at
((13,6)):

\[
 13,39,65,91,117,273.
\]

The two examples correctly show that point regularity alone does not split a
long orbit into wreaths and does not characterize wreaths away from the
critical diagonal.  Therefore the proposed balanced inter-orbit switching step
is still genuinely missing, and the Wreath Conjecture is not proved by the
homomesy theorem.

One small expository issue remains: if the finite-capacity-(2) counterexample
is retained, the manuscript should name its initial state (or print the orbit),
so the displayed alternating occupation vector is reproducible from the note
itself.
