# Exact even-equivariant `(c,t)` normal form at `k=16`

Date: 2026-07-29  
Status: exact central-carrier normal form and exact `q1` ledger.  This note
does not assert existence of a shadow-complete or compiler-ready carrier.

## 1. Parameters and action

Let the old coordinates be `X=Z_15`, let `z` be the sixteenth coordinate,
and put

\[
 L=\binom{16}{8}=12870=15N,
 \qquad N=858.
\]

Let `rho(x)=x+1` on `X` and let `rho(z)=z`.  Consider a voltage-one cyclic
equivariant indexed deck

\[
 T_{i+N}=\rho T_i,
 \qquad i\in\mathbb Z_L.
\tag{1.1}
\]

Any unit voltage is reduced to (1.1) by multiplying the old coordinate
labels by the inverse voltage modulo 15.  Conversely, a Hamilton deck on
these two shores can only have unit voltage: ranks seven and eight have free
`C_15` action, so a nonunit voltage would repeat a physical owner before all
fifteen members of its orbit were visited.

Define

\[
 t_j={\bf1}_{\{z\in T_j\}}
 \quad(j\in\mathbb Z_N),
 \qquad
 c_i={\bf1}_{\{0\in T_i\}}
 \quad(i\in\mathbb Z_L).
\tag{1.2}
\]

## 2. Reconstruction and rank

### Theorem 2.1 (even-equivariant binary normal form)

The map (1.2) is a bijection between indexed decks satisfying (1.1) and
pairs

\[
 (c,t)\in\{0,1\}^{\mathbb Z_L}\times
          \{0,1\}^{\mathbb Z_N}
\]

under the reconstruction

\[
 \boxed{
 T_i=
 \bigl(\{z\}\text{ if }t_{i\bmod N}=1\bigr)
 \cup
 \{x\in\mathbb Z_{15}:c_{i-xN}=1\}.}
\tag{2.1}
\]

Every `T_i` has rank eight if and only if

\[
 \boxed{
 \sum_{x\in\mathbb Z_{15}}c_{j-xN}=8-t_j
 \qquad(j\in\mathbb Z_N).}
\tag{2.2}
\]

#### Proof

If (1.1) holds, then

\[
 x\in T_i
 \iff 0\in\rho^{-x}T_i=T_{i-xN},
\]

which gives (2.1).  Conversely, (2.1) gives

\[
 x\in T_{i+N}
 \iff c_{i+N-xN}=c_{i-(x-1)N}=1
 \iff x-1\in T_i,
\]

while the `z` bit is `N`-periodic.  Thus it gives (1.1), and (1.2) recovers
the pair uniquely.  Summing the old-coordinate indicators in (2.1) gives
(2.2).  ∎

## 3. Johnson seams and the exact transversal exceptions

For `j in Z_N`, define the old-coordinate run-start and run-end counts

\[
\begin{aligned}
 S_j&=\sum_{x\in\mathbb Z_{15}}
       (1-c_{j-xN})c_{j+1-xN},\\
 E_j&=\sum_{x\in\mathbb Z_{15}}
       c_{j-xN}(1-c_{j+1-xN}).
\end{aligned}
\tag{3.1}
\]

### Theorem 3.1 (even run-transversal Johnson theorem)

Under the rank equations (2.2), every seam `T_j,T_(j+1)` is a Johnson edge
if and only if

\[
 \boxed{
 S_j=1-(1-t_j)t_{j+1},
 \qquad
 E_j=1-t_j(1-t_{j+1})}
\tag{3.2}
\]

for every `j in Z_N`.

Equivalently, the four seam types have

\[
\begin{array}{c|cccc}
 (t_j,t_{j+1})&00&01&10&11\\ \hline
 (S_j,E_j)&(1,1)&(0,1)&(1,0)&(1,1).
\end{array}
\tag{3.3}
\]

Thus the old-coordinate run-start transversal has exactly the `z`-entry
positions missing, and the run-end transversal has exactly the `z`-exit
positions missing.  There are no other exceptions.

#### Proof

Let

\[
 C_j=\sum_xc_{j-xN}=8-t_j.
\]

Counting old-coordinate insertions and deletions gives

\[
 C_{j+1}-C_j=S_j-E_j=t_j-t_{j+1}.
\tag{3.4}
\]

The full symmetric difference across the seam has size

\[
 S_j+E_j+|t_{j+1}-t_j|.
\tag{3.5}
\]

For a Johnson edge this equals two.  Solving (3.4)--(3.5) in the four
binary cases gives exactly (3.3), hence (3.2).  Conversely, (3.2) gives
one deletion and one insertion in total, with the `z` event supplying the
missing old event at a cross seam.  Therefore every seam is Johnson.  ∎

If `t` is nonconstant, let `R` be its number of cyclic one-runs and put
`n_1=sum_j t_j`, `n_0=N-n_1`.  Then

\[
 \#01=\#10=R,
 \qquad
 \#00=n_0-R,
 \qquad
 \#11=n_1-R.
\tag{3.6}
\]

Under the middle-Hamilton census of Theorem 4.1, `n_0=n_1=429`, so the last
two counts both equal `429-R`.

and the old trace `c` has exactly

\[
 \sum_jS_j=\sum_jE_j=858-R
\tag{3.7}
\]

cyclic one-runs.

## 4. Hamilton ownership is two separate orbit bijections

For `j in Z_N`, put

\[
 M_j=\{x\in\mathbb Z_{15}:c_{j-xN}=1\}.
\tag{4.1}
\]

When these quotient masks are used to evaluate seams, the wrap is twisted:

\[
 M_N=\rho M_0,
\tag{4.1a}
\]

not `M_N=M_0`.  The scalar indices in (3.1) already incorporate this twist.

The rotation action of `C_15` is free on both
`binom(X,7)` and `binom(X,8)`.  Indeed, a subset fixed by a nontrivial
rotation is a union of coordinate cycles of length three, five, or fifteen,
whereas neither seven nor eight is divisible by any of these lengths.

There are therefore exactly

\[
 \frac1{15}\binom{15}{7}
 =\frac1{15}\binom{15}{8}=429
\tag{4.2}
\]

orbits on each shore.

### Theorem 4.1 (middle Hamilton criterion)

The reconstructed deck `(T_i)` enumerates all `12870` rank-eight subsets
exactly once if and only if:

1. `t` has exactly 429 zeros and 429 ones;
2. the masks `M_j` at the 429 positions with `t_j=0` represent all 429
   rotation orbits of `binom(X,8)` exactly once;
3. the masks `M_j` at the 429 positions with `t_j=1` represent all 429
   rotation orbits of `binom(X,7)` exactly once.

#### Proof

For `0<=j<N` and `0<=s<15`, (2.1) gives

\[
 T_{j+sN}=\rho^sT_j.
\]

Every old-set orbit on either shore is free and has size fifteen.  Hence one
quotient representative produces exactly its full physical orbit, and the
two `z` shores are disjoint.  The three displayed conditions are therefore
necessary and sufficient.  ∎

In particular, Hamilton ownership is not implied by class sums or the seam
transversals.  It is exactly two independent 429-orbit all-different rows.

## 5. Residence and fixed-window traces

The `z`-coordinate trace is `t` repeated fifteen times.  Every old-coordinate
trace is a cyclic shift of `c`.  Therefore depth-three residence is exactly

\[
 \boxed{
 \text{every cyclic one-run of }t\text{ and of }c
 \text{ has length at least four}.}
\tag{5.1}

Bi-residence is obtained by adding the same lower bound for cyclic zero-runs
of both words.

All fixed-window flags are literal Boolean windows.  For every old
coordinate `x`,

\[
\begin{aligned}
 x\in\bigcap_{h=0}^{q}T_{i+h}
 &\iff \bigwedge_{h=0}^{q}c_{i+h-xN}=1,\\
 x\in\bigcup_{h=0}^{q}T_{i+h}
 &\iff \bigvee_{h=0}^{q}c_{i+h-xN}=1,
\end{aligned}
\tag{5.2}
\]

while `z` belongs precisely according to the corresponding AND/OR window of
`t`.  These identities reduce every fixed-depth target audit to the 858
quotient starts.  They do not replace arbitrary-width upper interval
coverage.

## 6. Exact first-shadow palettes

Write a no-`z` owner as `A` and a `z` owner as `{z} union B`.  A cross seam
is Johnson exactly when `B subset A`; its lower colour is `B` and its upper
colour is `{z} union A`.  Consequently the quotient seam types supply:

\[
\begin{array}{c|c|c}
\text{seam type}&\text{lower colour}&\text{upper colour}\\ \hline
AA&A\cap A'\in\binom X7&A\cup A'\in\binom X9\\
BB&\{z\}\cup(B\cap B'),\ B\cap B'\in\binom X6
  &\{z\}\cup(B\cup B'),\ B\cup B'\in\binom X8\\
AB/BA&B\in\binom X7&\{z\}\cup A,\ A\in\binom X8.
\end{array}
\tag{6.1}
\]

Thus first-shadow completeness is four separate target-orbit cover systems:

- lower no-`z`: `AA` plus cross seams, rank seven;
- lower with `z`: `BB` seams only, old rank six;
- upper no-`z`: `AA` seams only, old rank nine;
- upper with `z`: `BB` plus cross seams, old rank eight.

None follows from middle Hamiltonicity.

There are 429 rotation orbits at old ranks seven and eight.  Burnside gives
335 rotation orbits at ranks six and nine:

\[
 \frac1{15}\left(\binom{15}{6}+2\binom52\right)=335.
\tag{6.2}
\]

The two extra fixed terms come from the two nonidentity rotations of order
three; equivalently there are two short target orbits of size five.

Under the middle-Hamilton census `n_0=n_1=429`, (3.6) gives the numbers of
available seam orbits in the four palettes:

\[
\begin{array}{c|cccc}
&L_{\bar z}&L_z&U_{\bar z}&U_z\\ \hline
\text{seam orbits}&429+R&429-R&429-R&429+R.
\end{array}
\tag{6.3}
\]

Hence exact `q1` coverage has the unconditional necessary capacity bound

\[
 \boxed{R\le94.}
\tag{6.4}
\]

Indeed the two hard palettes each need 335 distinct target orbits, while
`429-R` seam orbits are available.  The weaker physical occurrence count
would give only `R<=95`; it misses the two short target orbits.

## 7. Exact proved/remaining boundary

The following are completely encoded by `(c,t)`:

1. equivariance and rank, by (2.1)--(2.2);
2. every Johnson seam, by (3.2);
3. middle Hamiltonicity, by the two orbit bijections of Theorem 4.1;
4. depth-three residence or bi-residence, by run constraints;
5. every fixed-window lower and upper trace, by (5.2);
6. first-shadow coverage, by the four explicit palettes (6.1).

The normal form does **not** itself prove:

1. any of the four first-shadow cover rows;
2. protected lower `q2/q3` coverage;
3. arbitrary-width upper interval coverage;
4. a safe linear cut or preservation after opening;
5. feasibility of the exact unrestricted `COMP_3` compiler;
6. a literal length-12873 universal word.

These must remain exact eager rows or fail-closed physical CEGAR audits.
