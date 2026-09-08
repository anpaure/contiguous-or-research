# Second-wave W: entropy structure of signed-subcube repair

This report is purely mathematical. It uses no web search, finite search, or
computer-assisted enumeration.

## Outcome

Fix a Gaussian window in one odd exact factor,

\[
n=2m+1,\qquad
W=\binom{n}{m},\qquad
K=\lceil A\sqrt m\rceil<m,
\]

where \(A>0\) is fixed. This report gives an exact answer, for the Poisson
signed-face functional, to the question of which restricted lower-hole
families have repair cost \(o(W)\). It also isolates the structural
information that a wreath or MTF construction would have to supply.

1. For arbitrary hole mass, including \(M\gg W\), the exact criterion is an
   entropy--capacity condition over every probability distribution on the
   holes. In the special regime \(M=O(W)\), this is equivalent to hereditary
   signed-face density tending to infinity in every linear-sized residual.
2. An explicit sufficient condition is antipodal trace condensation: after
   an \(o(W)\) leftover, partition the holes into proper signed cylinders
   \(C_i\), and require

   \[
   \sum_i\phi(|\mathcal G_i|,\gamma_i)=o(W),
   \]

   where \(\phi\) is computed exactly below. A depth-thick cylinder carrying
   a constant fraction of its one-rank capacity through \(L\) depths costs
   only \(O(\gamma(1+\log L))\), not its \(\Theta(L\gamma)\) hole count.
3. A persistent wreath full-cut kernel \(Z\) is precisely such a cylinder.
   For the abstract saturated family containing every relevant rank slice
   through \(Z\), and with \(|Z|=o(\sqrt n)\), its Poisson threshold is
   sharp:

   \[
   \Psi=o(W)
   \quad\Longleftrightarrow\quad
   |Z|-\log_2\log n\longrightarrow+\infty.
   \]

   In that saturated model the deterministic one-face threshold is only
   \(|Z|\to\infty\). For an arbitrary actual factor these are sufficient
   upper bounds only. The extra \(\log\log n\) is a Poissonization tax, not
   an intrinsic literal-word obstruction.
4. For a persistent MTF fence on \(d\) coordinates, trace-cell count alone
   gives a worst-case repair certificate only when the bad traces occupy
   few complementary pairs. Sparse families can be cheaper. For
   \(d=o(\sqrt n)\), the saturated \(J\)-pair model has

   \[
   \Psi=\Theta_A(J2^{-d}W\log n),\qquad
   D_{\rm det}=\Theta_A(J2^{-d}W).
   \]

   A single nested defect flag is, in contrast, exactly incompressible:

   \[
   \rho=\frac12,\qquad
   \Psi=D_{\rm frac}=D_{\rm det}=2|\Gamma|.
   \]
5. In the normalized \(A=1\) window there is a qualitatively sharp
   aligned-versus-rotating abstract obstruction along \(m=4^j\). It has
   \(\Theta(W/\sqrt m)\) holes at every rank, asymptotically correct point
   margins, and \(O_t(m^{-1/2})\) density in every fixed \(t\)-coordinate
   cylinder, yet every proper signed face has density at most \(12\), so

   \[
   \Psi\ge
   \left(
   \frac{1+\log24}{12}\int_0^1e^{-x^2}\,dx+o(1)
   \right)W.
   \]

   Reusing one trace rather than rotating the traces gives the same rank
   histogram and asymptotic point data but repair \(o(W)\). The missing
   invariant is cross-depth trace alignment, not rank totals, point balance,
   or bounded-coordinate pseudorandomness. A fixed dyadic subwindow gives
   the same positive obstruction for every fixed \(A>0\).

The analytic and extremal statements below are proved. What is not proved is
that the actual holes of one exact wreath factor, or the actual physical
holes of one low-reset adaptive-MTF construction after lower/upper
symmetrization (even allowing a safe declared complement-paired superset),
have the required trace condensation. That is the exact remaining geometric
bridge in this lane.

All logarithms without a subscript are natural; \(0\log0=0\), and terms
with \(\alpha_q=0\) in (3.9) are interpreted by continuity as zero. All signed-face costs are
costs of the canonical blocks defined next; they are not asserted to be
minimum costs among arbitrary words covering the same face.

## 1. Canonical proper signed faces and the restricted functional

Let

\[
\mathcal H=\bigsqcup_{q=1}^{K}\mathcal H_q,\qquad
\mathcal H_q\subseteq\binom{[n]}{m-q},\qquad
M_q=|\mathcal H_q|,\qquad
M=|\mathcal H|.
\]

For one exact factor, \(\mathcal H_q\) is its binary lower-hole family at
depth \(q\). The convex results apply to an arbitrary family with the same
rank support.

For disjoint \(P,N\subseteq[n]\), with \(P\cup N\ne\varnothing\), put

\[
U=[n]\setminus(P\cup N),\qquad s=|U|,
\]

and define the proper opposite signed face

\[
C(P,N)=
\{P\cup T:T\subseteq U\}
\cup
\{N\cup T:T\subseteq U\}.
\tag{1.1}
\]

Set \(\nu(0)=0\). If \(\nu(s)\) is the length of an available nonzero
OR-universal word on the \(s\) free coordinates, the canonical two-copy
block has length

\[
\gamma_C=
2\nu(s)+\mathbf1_{P\ne\varnothing}+\mathbf1_{N\ne\varnothing}.
\tag{1.2}
\]

Indeed, prefix one copy of the free word by \(P\), prefix the other by \(N\),
and add a literal anchor whenever the anchor is nonempty. This realizes every
relevant member of both branches internally. Formula (1.2) is exact for this
stated block. It is not proved minimal over all possible face-covering words.

When \(s=0\), taking \(P=S\), \(N=S^c\) gives the literal column
\(\{S,S^c\}\) of cost two. Restricted to lower holes it is incident only
with \(S\). The empty-anchor full cube \(P=N=\varnothing\) is excluded. Its
formal two-copy cost would be \(2\nu(n)\), whereas one economical copy costs
\(\nu(n)\); exclusion changes finite optimization but not \(o(W)\)
feasibility. Indeed, in an extended solution of cost \(o(W)\), its
full-cube intensity \(\lambda_*\) would satisfy
\(\nu(n)\lambda_*=o(W)\). Since \(\nu(n)\ge W\), this forces
\(\lambda_*=o(1)\). Deleting the full-cube column multiplies the residual
exponential term by only \(e^{\lambda_*}=1+o(1)\), so the total remains
\(o(W)\), even when \(M/W\) is unbounded.

There is one further endpoint convention. If \(s=0\) and exactly one anchor
is empty, (1.2) equals one and the corresponding one-letter block realizes
only the nonempty member of \(\{\varnothing,[n]\}\). This is exact for the
present incidence problem because \(K<m\) and the hole universe contains
only nonempty proper lower targets. It must not be reused unchanged if rank
zero is admitted.

Let \(\mathsf A_{S,C}=\mathbf1_{S\in C}\). The restricted Poisson functional
is

\[
\Psi_{\le K}(\mathcal H)
=
\inf_{\lambda\ge0}
\left[
\sum_C\gamma_C\lambda_C
+2\sum_{S\in\mathcal H}e^{-(\mathsf A\lambda)_S}
\right].
\tag{1.3}
\]

It is the exact value of this convex surrogate. It is not, in general, the
minimum deterministic signed-face repair cost.

For \(r\ge1\), we use the established constant-factor universal-word bound

\[
w(r):=\binom r{\lfloor r/2\rfloor}
\le\nu(r)\le C_0w(r)
\tag{1.4}
\]

for an absolute constant \(C_0\). All exact structural theorems are stated
in terms of \(\gamma_C\); (1.4) is used only to translate them into
codimension asymptotics.

## 2. Exact entropy--capacity characterization

For a probability distribution \(\pi\) on a nonempty \(\mathcal H\), write

\[
\operatorname{Ent}(\pi)=-\sum_{S\in\mathcal H}\pi_S\log\pi_S,\qquad
\pi(C)=\sum_{S\in\mathcal H\cap C}\pi_S,
\]

and define

\[
\delta(\pi)=
\max\left\{
\frac{\|\pi\|_\infty}{2},
\max_C\frac{\pi(C)}{\gamma_C}
\right\}.
\tag{2.1}
\]

### Theorem 2.1 (exact entropy dual)

If \(M>0\), then

\[
\boxed{
\Psi_{\le K}
=
\max_{\pi\in\mathcal P(\mathcal H)}
\frac{1+\operatorname{Ent}(\pi)+\log(2\delta(\pi))}
{\delta(\pi)}.}
\tag{2.2}
\]

Equivalently, put

\[
a(\pi)=\frac1{\delta(\pi)},\qquad
N_{\rm eff}(\pi)=e^{\operatorname{Ent}(\pi)}.
\]

Then

\[
\boxed{
\Psi_{\le K}
=\max_\pi
a(\pi)\left[1+\log\frac{2N_{\rm eff}(\pi)}{a(\pi)}\right].}
\tag{2.3}
\]

When \(M=0\), \(\Psi_{\le K}=0\) separately.

#### Proof

For \(x\ge0\), direct differentiation gives

\[
2e^{-x}
=\max_{0\le y\le2}
\left\{y\left(1+\log\frac2y\right)-xy\right\}.
\tag{2.4}
\]

Applying (2.4) coordinatewise and using finite-dimensional convex duality
gives

\[
\Psi_{\le K}
=
\max_{\substack{0\le y\le2\\ \mathsf A^Ty\le\gamma}}
\sum_{S\in\mathcal H}
y_S\left(1+\log\frac2{y_S}\right).
\tag{2.5}
\]

Indeed, there are at most \(3^n-1\) ordered proper anchor pairs and every
\(\gamma_C>0\). The \(y\)-domain is the compact cube
\([0,2]^{\mathcal H}\), while minimization over the nonnegative
\(\lambda\)-orthant leaves value zero exactly when
\(\mathsf A^Ty\le\gamma\) and value \(-\infty\) otherwise. Thus the stated
Fenchel/minimax exchange has no closure or attainment gap. Identical
columns from \((P,N)\) and \((N,P)\) may be retained or quotiented out.

For nonzero \(y\), put \(t=\sum_Sy_S\) and \(\pi=y/t\). The atom and face
constraints in (2.5) are exactly

\[
0<t\le
\min\left\{
\frac2{\|\pi\|_\infty},
\min_{C:\pi(C)>0}\frac{\gamma_C}{\pi(C)}
\right\}
=\frac1{\delta(\pi)}.
\]

The objective becomes

\[
t\left(1+\operatorname{Ent}(\pi)+\log\frac2t\right),
\]

whose derivative in \(t\) is

\[
\operatorname{Ent}(\pi)+\log\frac2t.
\]

Since \(\operatorname{Ent}(\pi)\ge-\log\|\pi\|_\infty\) and
\(t\le2/\|\pi\|_\infty\), the derivative is nonnegative throughout the
feasible interval. The maximum therefore occurs at
\(t=1/\delta(\pi)\), proving (2.2). Equation (2.3) is the same identity
after substituting \(a=1/\delta\). Notice that \(a\le2N_{\rm eff}\), so the
logarithm in (2.3) is nonnegative. \(\square\)

### Corollary 2.2 (the exact all-mass \(o(W)\) criterion)

For any sequence of nonempty fixed-window hole families,

\[
\boxed{
\Psi_{\le K}=o(W)
\quad\Longleftrightarrow\quad
\sup_{\pi\in\mathcal P(\mathcal H)}
\frac{a(\pi)}W
\left[1+\log\frac{2N_{\rm eff}(\pi)}{a(\pi)}\right]
\longrightarrow0.}
\tag{2.6}
\]

This has no assumption on \(M/W\). Every high-entropy distribution on the
holes must acquire enough mass in some economical proper signed face, or
else have a sufficiently small admissible scale through atom concentration.
The exact product in (2.6), not merely \(a(\pi)=o(W)\), is required when
the entropy factor diverges.

### Fractional and deterministic comparison

For \(M>0\), define

\[
D_{\rm frac}
=
\min_{\substack{x_C,z_S\ge0\\ \mathsf A x+z\ge\mathbf1}}
\left(\sum_C\gamma_Cx_C+2\sum_Sz_S\right),
\]

and let \(D_{\rm det}\) be the minimum cost of integral canonical face
blocks followed by literal repair. Linear programming duality and the same
reparametrization give

\[
\boxed{
D_{\rm frac}
=\max_\pi\frac1{\delta(\pi)}
=\frac1{\min_\pi\delta(\pi)},}
\tag{2.7}
\]

and independent selection of face \(C\) with probability
\(1-e^{-\lambda_C}\) gives

\[
\boxed{
D_{\rm frac}\le D_{\rm det}\le\Psi_{\le K}
\le D_{\rm frac}
\left(1+\log\frac{2M}{D_{\rm frac}}\right).}
\tag{2.8}
\]

For \(M=0\), all three quantities are zero. The last expression in (2.8) is
a sufficient upper bound, not an all-mass equivalence.

## 3. Residual density and a general level-set profile

For nonempty \(\mathcal G\subseteq\mathcal H\), put

\[
\rho(\mathcal G)
=\max\left\{\frac12,\max_C\frac{|\mathcal G\cap C|}{\gamma_C}\right\},
\qquad
f(r)=\frac{1+\log(2r)}r.
\tag{3.1}
\]

The \(1/2\) is attained by literal zero-free columns. Uniform \(\pi\) on
\(\mathcal G\) in (2.2) and (2.7) gives

\[
\boxed{
D_{\rm frac}\ge\frac{|\mathcal G|}{\rho(\mathcal G)},\qquad
\Psi_{\le K}\ge|\mathcal G|f(\rho(\mathcal G)).}
\tag{3.2}
\]

For \(0<t\le2\), define

\[
B(t)=
\max\left\{
|\mathcal G|:\varnothing\ne\mathcal G\subseteq\mathcal H,\
\rho(\mathcal G)\le1/t
\right\},
\tag{3.3}
\]

with value zero if no nonempty family qualifies.

### Theorem 3.1 (level-set profile upper bound)

\[
\boxed{
\Psi_{\le K}\le\int_0^2B(t)\log\frac2t\,dt.}
\tag{3.4}
\]

#### Proof

For a feasible \(y\) in (2.5), let
\(\mathcal G_t=\{S:y_S\ge t\}\). For every face \(C\),

\[
t|\mathcal G_t\cap C|
\le\sum_{S\in C}y_S\le\gamma_C.
\]

Since \(t\le2\), also \(1/2\le1/t\), and hence
\(\rho(\mathcal G_t)\le1/t\) whenever \(\mathcal G_t\ne\varnothing\).
If \(\mathcal G_t=\varnothing\), its cardinality is already zero. Thus in
all cases \(|\mathcal G_t|\le B(t)\). Finally,

\[
y\left(1+\log\frac2y\right)=\int_0^y\log\frac2t\,dt,
\]

so layer cake and (2.5) prove (3.4). \(\square\)

This is an upper bound, not an equality: the maximizing level sets for
different \(t\) need not be nested.

If every residual of size \(>u\) has \(\rho\ge R\ge1/2\), then

\[
\boxed{
D_{\rm det}\le2u+\frac MR,\qquad
\Psi_{\le K}\le2u+Mf(R).}
\tag{3.5}
\]

For completeness, greedily choose a face \(C_i\) whose intersection
\(T_i\) with the current residual has density
\(r_i=|T_i|/\gamma_i\ge R\), delete \(T_i\), and stop with at most \(u\)
holes. The sets \(T_i\) are disjoint, so selecting all chosen faces costs
at most \(\sum_i|T_i|/R\le M/R\), proving the deterministic bound. For the
Poisson bound give \(C_i\) intensity \(\log(2r_i)\). Its face cost plus the
residual exponential charge assigned to \(T_i\) is

\[
 \gamma_i\log(2r_i)+2|T_i|e^{-\log(2r_i)}
 =|T_i|f(r_i)\le |T_i|f(R),
\]

because \(f\) decreases on \([1/2,\infty)\). Summing and repairing the final
residual literally proves (3.5). At \(R=1/2\), literal columns supply the
required density.

### Corollary 3.2 (exact \(M=O(W)\) characterization)

For a sequence with \(M\le CW\) eventually, the following are equivalent:

\[
\Psi_{\le K}=o(W),\qquad
D_{\rm frac}=o(W),\qquad
D_{\rm det}=o(W),
\tag{3.6}
\]

and

\[
\boxed{
\text{for every fixed }\varepsilon>0,\quad
\inf_{\substack{\mathcal G\subseteq\mathcal H\\
|\mathcal G|\ge\varepsilon W}}
\rho(\mathcal G)\longrightarrow\infty.}
\tag{3.7}
\]

The infimum of an empty family is \(+\infty\). Equivalently, in this regime,

\[
\sup_{\varnothing\ne\mathcal G\subseteq\mathcal H}
\frac{|\mathcal G|}{W}f(\rho(\mathcal G))\longrightarrow0.
\tag{3.8}
\]

Necessity is (3.2). Sufficiency follows from (3.5), first choosing a small
fixed \(\varepsilon\), then a large fixed \(R\). The hypothesis \(M=O(W)\)
is essential; (2.6), not (3.7), is the exact characterization for arbitrary
mass.

### Rank-profile duals

For any \(\alpha_q\ge0\) with \(\sum_{q=1}^K\alpha_q\le1\), the vector

\[
y_S=\alpha_q\qquad(S\in\mathcal H_q)
\]

is dual-feasible. One proper face meets each rank in at most its cost, and
\(y\le1\). Therefore

\[
\boxed{
\Psi_{\le K}\ge
\sum_{q=1}^KM_q\alpha_q
\left(1+\log\frac2{\alpha_q}\right).}
\tag{3.9}
\]

In particular,

\[
\Psi_{\le K}\ge(1+\log2)M_q.
\tag{3.10}
\]

For nonempty \(Q\subseteq\{1,\ldots,K\}\), put

\[
M_Q=\sum_{q\in Q}M_q,\qquad
L_Q=\min\{|Q|,\sqrt{2n}\}.
\]

The rank-throughput and free-dimension bounds give

\[
\boxed{
D_{\rm frac}\ge\frac{M_Q}{L_Q},\qquad
\Psi_{\le K}\ge
\frac{1+\log(2L_Q)}{L_Q}M_Q.}
\tag{3.11}
\]

For completeness, if a face has free dimension \(s\ge1\), its intersection
with one rank has size at most
\(2w(s)\le\gamma_C\), so its density on the ranks in \(Q\) is at most
\(|Q|\). Also

\[
|C|\le2^{s+1},\qquad
\gamma_C\ge2w(s)\ge\frac{2^{s+1}}{\sqrt{2(s+1)}},
\]

so its total density is at most
\(\sqrt{2(s+1)}\le\sqrt{2n}\). The \(s=0\) endpoint has density at most
\(1/2\). Thus \(\rho(\bigsqcup_{q\in Q}\mathcal H_q)\le L_Q\), and (3.11)
follows from (3.2).

Two necessary geometric consequences are worth recording. If a face has
hole density at least \(R\), then it must meet at least \(\lceil R\rceil\)
distinct depths, because its contribution at any one rank is at most its
cost. Moreover, if its free dimension is \(s\ge1\), then

\[
 R\le \frac{|C|}{\gamma_C}\le\sqrt{2(s+1)},
 \qquad\text{so}\qquad
 s\ge \frac{R^2}{2}-1.
\tag{3.12}
\]

Thus hereditary density tending to infinity necessarily comes from
genuinely depth-persistent, growing-dimensional faces; neither a bounded
depth packet nor a bounded free coordinate set can certify (3.7).

Thus a fixed Gaussian window permits at most
\(o(W\sqrt m/\log m)\) aggregate holes under \(\Psi=o(W)\), and every one
rank must have \(o(W)\) holes.

## 4. The exact signed-cylinder cluster certificate

Define, for \(M\ge0\) and \(\gamma>0\),

\[
\phi(M,\gamma)
=\min_{\lambda\ge0}\left(\gamma\lambda+2Me^{-\lambda}\right).
\tag{4.1}
\]

Direct differentiation gives

\[
\boxed{
\phi(M,\gamma)=
\begin{cases}
2M,&2M\le\gamma,\\[2mm]
\gamma\left(1+\log\dfrac{2M}{\gamma}\right),&2M\ge\gamma.
\end{cases}}
\tag{4.2}
\]

The expressions agree at equality.

### Theorem 4.1 (explicit cluster repair)

Suppose

\[
\mathcal H
=\mathcal H_0\mathbin{\dot\cup}
\mathcal G_1\mathbin{\dot\cup}\cdots
\mathbin{\dot\cup}\mathcal G_J,
\qquad
\mathcal G_i\subseteq C_i,
\]

where \(C_i\) is a proper signed face of cost \(\gamma_i\). Then

\[
\boxed{
\Psi_{\le K}(\mathcal H)
\le2|\mathcal H_0|+\sum_{i=1}^J\phi(|\mathcal G_i|,\gamma_i).}
\tag{4.3}
\]

If \(r_i=|\mathcal G_i|/\gamma_i\ge1/2\), its summand is

\[
\gamma_i(1+\log(2r_i))=|\mathcal G_i|f(r_i).
\tag{4.4}
\]

#### Proof

Use only the columns \(C_i\). Give \(C_i\) an intensity attaining (4.1), and
charge every hole of \(\mathcal G_i\) to that intensity. Other columns and
repeated occurrences of the same face can only add exposure; repeated faces
may equivalently receive the sum of their assigned intensities. Ignore
incidental exposure of \(\mathcal H_0\) and pay its literal residual cost.
This gives (4.3). \(\square\)

Discarding empty clusters, let \(Q_i\) be the nonempty set of depths
occupied by \(\mathcal G_i\). One
face meets one rank in at most \(\gamma_i\) holes, so
\(|\mathcal G_i|\le|Q_i|\gamma_i\). Consequently,

\[
\boxed{
\Psi_{\le K}
\le2|\mathcal H_0|
+\sum_i\gamma_i\left(1+\log(2|Q_i|)\right).}
\tag{4.5}
\]

This does not assume \(M=O(W)\).

### Signed-trace condensation

Fix a nonempty coordinate set \(D\). The unordered complementary trace
orbits

\[
[R]=\{R,D\setminus R\}\qquad(R\subseteq D)
\]

partition all traces. The cell

\[
\mathcal G_{[R]}=\{S\in\mathcal H:S\cap D\in[R]\}
\]

lies in \(C(R,D\setminus R)\). Hence Theorem 4.1 applies cell by cell.

Suppose \(M=O(W)\), \(R_m\to\infty\), and the total number of holes in cells
satisfying

\[
|\mathcal G_{[R]}|<R_m\gamma_{[R]}
\]

is \(o(W)\). Then

\[
\Psi_{\le K}\le o(W)+Mf(R_m)=o(W).
\tag{4.6}
\]

### Depth-thick corridors

Suppose a cluster \(\mathcal G_i\subseteq C_i\) has \(L_i\) distinct depths
at which it contains at least \(\alpha_i\gamma_i\) holes. Then

\[
r_i=\frac{|\mathcal G_i|}{\gamma_i}\ge\alpha_iL_i.
\tag{4.7}
\]

For clusters with \(\alpha_iL_i\ge1/2\), an \(o(W)\) leftover and

\[
\sum_i|\mathcal G_i|f(\alpha_iL_i)=o(W)
\tag{4.8}
\]

suffice. If all nonliteral clusters are thick on the same \(L\) depths with
\(\alpha_i\ge c>0\), then

\[
\Psi_{\le K}
=O_c\left(|\mathcal H_0|+\frac{M(1+\log L)}{L}\right).
\tag{4.9}
\]

For families supported on those \(L\) depths, put

\[
L_*:=\min\{L,\sqrt{2n}\}.
\]

The exact lower-bound parameter in (3.11) is \(L_*\), so \(\Psi=o(W)\)
forces
\(M=o(WL_* /(1+\log L_*))\). In the fixed-window range
\(L\le K=O_A(\sqrt m)\), one has \(L_*=\Theta_A(L)\); hence, for
\(L\to\infty\), the order is \(o_A(WL/\log L)\). Full depth-thick signed
cylinders therefore saturate, up to constants depending only on \(A\), the
maximum aggregate defect allowed by the entropy dual.

### Codimension ledger

Let \(d=n-s=|P|+|N|\). If \(s\to\infty\), the central-binomial asymptotic and
(1.4) give

\[
\gamma_C
=\Theta\left(2^{-d}W\sqrt{\frac n{n-d}}\right).
\tag{4.10}
\]

An exact lower bound follows from convolution:

\[
W=\binom n{\lfloor n/2\rfloor}\le2^dw(n-d).
\]

Hence, for \(s\ge1\),

\[
\boxed{\gamma_C\ge2w(s)\ge2^{1-d}W.}
\tag{4.11}
\]

If \(M\le CW\) and a face has density at least \(R\), then

\[
d\ge1+\log_2(R/C).
\tag{4.12}
\]

Thus bounded-coordinate localization cannot provide unbounded residual
density for a linear hole family. A growing anchor/fence is forced.

## 5. Persistent full-cut kernels in an exact wreath factor

For an exact middle wreath factor \(F\), let

\[
\mathcal H_q(F)
=\left\{S\in\binom{[n]}{m-q}:\mu_q^F(S)=0\right\}.
\]

Call a coordinate \(z\) a full depth-\(q\) covering cut when every
\((m-q)\)-set avoiding \(z\) occurs in the factor.

### Theorem 5.1 (full-cut kernel identity)

If \(\mathcal H_q(F)\ne\varnothing\), the full covering coordinates are

\[
\boxed{
C_q(F)=\bigcap_{S\in\mathcal H_q(F)}S.}
\tag{5.1}
\]

If \(\mathcal H_q(F)=\varnothing\), every coordinate covers.

#### Proof

A coordinate \(z\) covers exactly when no missing \((m-q)\)-set avoids
\(z\), which is equivalent to \(z\) belonging to every hole. \(\square\)

Thus a set \(Z\ne\varnothing\) of persistent full cuts over a nonempty set
of depths \(Q\)
satisfies

\[
\bigsqcup_{q\in Q}\mathcal H_q(F)
\subseteq C(Z,\varnothing).
\tag{5.2}
\]

Put

\[
\mathcal H_Q(F)=\bigsqcup_{q\in Q}\mathcal H_q(F),\qquad
M_Q=\sum_{q\in Q}|\mathcal H_q(F)|,\qquad
\gamma_Z=2\nu(n-|Z|)+1.
\]

The cluster theorem gives

\[
\boxed{
\Psi(\mathcal H_Q(F))
\le\phi(M_Q,\gamma_Z)
\le\gamma_Z\left(1+\log(2|Q|)\right).}
\tag{5.3}
\]

More generally, partition the depths into \(Q_j\), permit a different
persistent kernel \(Z_j\) on each block, and sum (5.3).

If \(t=|Z|=o(n)\), then

\[
\gamma_Z
=\Theta\left(W2^{-t}\sqrt{\frac n{n-t}}\right).
\tag{5.4}
\]

For the entire Gaussian window \(Q=\{1,\ldots,K\}\), (5.3) implies

\[
t-\log_2\log n\longrightarrow+\infty
\quad\Longrightarrow\quad
\Psi_{\le K}=o(W).
\tag{5.5}
\]

Independently of Poissonization, selecting \(C(Z,\varnothing)\) once gives
\(D_{\rm det}\le\gamma_Z\). Under the same \(t=o(n)\) hypothesis, a
persistent kernel with merely \(t\to\infty\) already gives deterministic
\(o(W)\) canonical repair.

This is much weaker than asking for \(\Theta(\log m)\) common cuts. It is
also genuinely cross-depth: a different one-coordinate kernel at each
depth gives no large density certificate from those kernels alone. This
does not exclude some other, hidden high-codimension face alignment.

### Theorem 5.2 (sharp saturated common-kernel model)

Fix \(A>0\). Let \(1\le t=o(\sqrt n)\), choose a fixed \(t\)-set \(Z\), and
define the abstract family

\[
\mathcal H_q^Z
=\left\{S\in\binom{[n]}{m-q}:Z\subseteq S\right\},
\qquad 1\le q\le K.
\tag{5.6}
\]

Write \(\mathcal H^Z=\bigsqcup_{q=1}^K\mathcal H_q^Z\).

Put \(s=n-t\) and \(w_s=w(s)\). Then

\[
\boxed{
\Psi_{\le K}(\mathcal H^Z)
=\Theta_A(w_s\log K)
=\Theta_A(W2^{-t}\log n),}
\tag{5.7}
\]

and

\[
\boxed{
D_{\rm frac}(\mathcal H^Z),
D_{\rm det}(\mathcal H^Z)
=\Theta_A(w_s)
=\Theta_A(W2^{-t}).}
\tag{5.8}
\]

#### Proof

The exact slice count is

\[
|\mathcal H_q^Z|
=\binom{s}{m-q-t}
=\binom{s}{\lfloor s/2\rfloor-q-\lceil t/2\rceil}.
\tag{5.9}
\]

Since \(q\le K=A\sqrt m+O(1)\) and \(t=o(\sqrt n)\), elementary
central-binomial product estimates give, uniformly in \(q\),

\[
|\mathcal H_q^Z|=\Theta_A(w_s).
\]

Therefore \(M=\Theta_A(Kw_s)\), while
\(\gamma_Z=2\nu(s)+1=\Theta(w_s)\). The chosen face
\(C(Z,\varnothing)\) has density \(\Theta_A(K)\). Conversely every proper
face meets each rank in at most its cost, and the family is supported on
only \(K\) ranks, so

\[
\rho(\mathcal H^Z)=\Theta_A(K).
\]

The lower bound (3.2) and the one-face upper bound (4.2) give (5.7).
Likewise \(D_{\rm frac}\ge M/K=\Omega_A(w_s)\), while one deterministic
copy of \(C(Z,\varnothing)\) costs \(O(w_s)\), proving (5.8). Finally,

\[
\frac{w_s}{W}
=(1+o(1))2^{-t}\sqrt{\frac n{n-t}}
=\Theta(2^{-t}).
\]

\(\square\)

Consequently, in this saturated model,

\[
\boxed{
\Psi=o(W)
\Longleftrightarrow
2^{-t}\log n\to0
\Longleftrightarrow
t-\log_2\log n\to+\infty,}
\tag{5.10}
\]

whereas

\[
D_{\rm det}=o(W)\Longleftrightarrow t\to\infty.
\tag{5.11}
\]

At \(t=\log_2\log n+O(1)\), the Poisson cost is \(\Theta(W)\) while one
deterministic face costs \(o(W)\). This is a sharp warning against treating
\(\Psi\) as the deterministic optimum when \(M\ne O(W)\).

The family (5.6) is abstract; it is not proved to be the hole family of an
exact factor. It shows that (5.5) is the worst-case sharp Poisson threshold
deducible from common-kernel information alone. Sparse subfamilies can do
better.

A point-transitive exact factor cannot have a nonempty intermediate kernel:
at a fixed depth, (5.1) is invariant, so it is either empty or all of
\([n]\); the latter forces no holes. Thus the common-kernel route requires
deliberate symmetry breaking or exact completion of the affected depths.

## 6. Complementary trace pairs and MTF fences

Let \(D\subseteq[n]\), \(|D|=d\ge1\), and let

\[
\mathscr R=\{[R_1],\ldots,[R_J]\},\qquad
[R_i]=\{R_i,D\setminus R_i\},
\]

be distinct unordered complementary trace orbits. Thus
\(1\le J\le2^{d-1}\). Any defect family whose traces lie in these cells
partitions into the faces

\[
C_i=C(R_i,D\setminus R_i),
\]

of costs

\[
\gamma_i=
2\nu(n-d)
+\mathbf1_{R_i\ne\varnothing}
+\mathbf1_{D\setminus R_i\ne\varnothing}.
\tag{6.1}
\]

Therefore (4.3) is an exact sufficient certificate. If all cells occupy at
most \(K\) depths,

\[
\Psi_{\le K}
\le2|\mathcal H_0|
+\sum_{i=1}^J\gamma_i(1+\log(2K)).
\tag{6.2}
\]

When \(d=o(n)\), (1.4) makes the following a convenient sufficient
condition:

\[
|\mathcal H_0|=o(W),\qquad
J2^{-d}\log n=o(1).
\tag{6.3}
\]

This is the natural numerical target for a fixed-coordinate MTF fence: the
fence dimension helps only to the extent that the bad trace entropy is
smaller than \(d\).

### Theorem 6.1 (sharp saturated \(J\)-trace model)

Assume \(d=o(\sqrt n)\). Define

\[
\mathcal H_q(D,\mathscr R)
=\left\{
S\in\binom{[n]}{m-q}:
S\cap D\in\bigcup_{i=1}^J[R_i]
\right\},
\qquad 1\le q\le K.
\tag{6.4}
\]

Then

\[
\boxed{
\Psi_{\le K}
=\Theta_A(JW2^{-d}\log n),\qquad
D_{\rm frac},D_{\rm det}
=\Theta_A(JW2^{-d}).}
\tag{6.5}
\]

#### Proof

Put \(s=n-d\). For \(r_i=|R_i|\), the two trace slices at depth \(q\) have
sizes

\[
\binom{s}{m-q-r_i},\qquad
\binom{s}{m-q-(d-r_i)}.
\]

Their offsets from \(\lfloor s/2\rfloor\) have absolute value at most
\(K+\lceil d/2\rceil\). Since \(d=o(\sqrt n)\), each is
\(\Theta_A(w(s))\), uniformly over all selected patterns and depths.
Distinct trace cells are disjoint, so

\[
M=\Theta_A(JK w(s)).
\]

Every \(\gamma_i=\Theta(w(s))\). The cluster upper bound gives
\(O_A(Jw(s)\log K)\). The whole family is supported on \(K\) ranks, so
\(\rho\le K\), and (3.2) gives the matching lower bound. The same argument
with (2.7), together with selecting all \(J\) faces once, gives the
deterministic order. Finally \(w(s)/W=\Theta(2^{-d})\). \(\square\)

Thus the exact Poisson criterion in the saturated model is

\[
\boxed{
J2^{-d}\log n=o(1)
\quad\Longleftrightarrow\quad
d-\log_2J-\log_2\log n\to+\infty.}
\tag{6.6}
\]

If all \(2^{d-1}\) complementary trace cells occur densely at all depths,
then \(\Psi=\Theta(W\log n)\): a large tied block by itself gives no
compression. Trace sparsity and cross-depth reuse are the relevant data.

The converse in (6.5) uses the saturated model. An arbitrary sparse MTF
defect family has only the cluster upper bound, not this threshold converse.

### Theorem 6.2 (one nested defect flag is exactly incompressible)

Let \(\Gamma\ne\varnothing\) be a strict inclusion chain of nonempty proper
sets contained in the lower fixed window. Then

\[
\boxed{
\rho(\Gamma)=\frac12,\qquad
\Psi(\Gamma)=D_{\rm frac}(\Gamma)
=D_{\rm det}(\Gamma)=2|\Gamma|.}
\tag{6.7}
\]

#### Proof

Fix a proper face \(C(P,N)\) with free dimension \(s\).

If both anchors are nonempty, its two branches are mutually incomparable,
so \(\Gamma\) meets at most one branch. A chain in that branch has at most
\(s+1\) members. For \(s\ge1\),

\[
\gamma_C\ge2w(s)+2\ge2s+2,
\]

and the density is at most \(1/2\). The \(s=0\) endpoint has the same bound.

If exactly one anchor is empty, the union of the two branches is
order-isomorphic to a Boolean lattice on \(s+1\) atoms, one atom
representing the nonempty anchor. The empty and full endpoints correspond
to \(\varnothing\) and \([n]\), neither of which belongs to \(\Gamma\).
Hence the intersection has at most \(s\) members. For \(s\ge1\),

\[
\gamma_C\ge2w(s)+1\ge2s+1,
\]

so its density is strictly below \(1/2\). When \(s=0\), the face is
\(\{\varnothing,[n]\}\) and meets \(\Gamma\) trivially. Literal columns
attain \(1/2\), so
\(\rho(\Gamma)=1/2\). Equations (3.2) give the lower bounds
\(2|\Gamma|\), while literal repair and \(\lambda=0\) give the matching
upper bounds. \(\square\)

If a residual is the union of at most \(r\) inclusion chains, then every
face meets it in at most \(r\gamma_C/2\). Therefore

\[
\rho(\mathcal G)\le r/2,\qquad
\Psi\ge|\mathcal G|f(r/2)
=\frac{2(1+\log r)}r|\mathcal G|.
\tag{6.8}
\]

Thus a bounded number of long vertical histories still has a linear repair
toll. The positive counterpart is a parallel flag bundle: if
\(\Theta(\gamma_C)\) distinct histories share one complementary trace cell
and each remains defective for \(\ell\to\infty\) depths, their union has
density \(\Theta(\ell)\) and is compressible by Theorem 4.1.

Known MTF state theorems provide nested covered flags and reset accounting.
They do not prove that the complementary hole family is a union of few
chains, nor that \(\Theta(\gamma_C)\) hole trajectories align in one trace
cell. Collision-created holes in particular have no known canonical
assignment to an MTF trajectory. That bridge is unproved.

## 7. A bounded-dispersion obstruction

The next theorem shows that cross-depth rotation of a bounded trace alphabet
destroys every economical signed face.

### Theorem 7.1 (marker-dispersion lemma)

Fix a marker set \(D\subseteq[n]\). For each depth \(q\), let
\(\mathcal B_q\subseteq2^D\), and define

\[
\mathcal G_q
=\left\{S\in\binom{[n]}{m-q}:S\cap D\in\mathcal B_q\right\},
\qquad
\mathcal G=\bigsqcup_q\mathcal G_q.
\tag{7.1}
\]

Assume

\[
|\mathcal B_q|\le L\quad\text{for every }q,\qquad
\left|\{q:B\in\mathcal B_q\}\right|\le a
\quad\text{for every }B\subseteq D,
\tag{7.2}
\]

where \(a,L\ge1\). Then every proper signed face satisfies

\[
\boxed{
\frac{|\mathcal G\cap C|}{\gamma_C}
\le6\max\{a,L\}.}
\tag{7.3}
\]

Consequently, if \(\mathcal G\) is a residual subset of a hole family, then

\[
\boxed{
D_{\rm frac}\ge\frac{|\mathcal G|}{6\max(a,L)},\qquad
\Psi\ge
\frac{1+\log(12\max(a,L))}{6\max(a,L)}
|\mathcal G|.}
\tag{7.4}
\]

#### Proof

Fix \(C(P,N)\), let \(U\) be its free set, and write

\[
s=|U|,\qquad r=|D\cap U|,\qquad t=s-r.
\]

On one branch, exactly \(2^r\) marker traces are compatible. Each occurs at
at most \(a\) depths, so there are at most \(a2^r\) compatible pairs
\((q,B)\). Independently, one branch spans only \(s+1\) sizes, and there are
at most \(L\) traces per depth, giving at most \(L(s+1)\) pairs. Once \(q\)
and the full marker trace are fixed, the remaining choice is one layer of
the \(t\) unmarked free coordinates, of size at most \(w(t)\). Accounting
for both branches,

\[
|\mathcal G\cap C|
\le2\min\{a2^r,L(s+1)\}w(s-r).
\tag{7.5}
\]

For \(s\ge1\), divide by \(\gamma_C\ge2w(s)\). With
\(M_0=\max(a,L)\), the quotient is at most \(M_0B(s,r)\), where

\[
B(s,r)=\min\{2^r,s+1\}\frac{w(s-r)}{w(s)}.
\]

The elementary bounds

\[
\frac{2^u}{\sqrt{2(u+1)}}\le w(u)\le\frac{2^u}{\sqrt{u+1}}
\]

give

\[
B(s,r)\le
\sqrt{\frac{2(s+1)}{s-r+1}}
\min\{1,(s+1)2^{-r}\}.
\tag{7.6}
\]

If \(r\le s/2\), (7.6) is \(<2\). If \(r>s/2\) and \(s\le15\), it is
\(<\sqrt{32}<6\). If \(r>s/2\) and \(s\ge16\), it is at most

\[
\sqrt2(s+1)^{3/2}2^{-s/2}<1,
\]

and this expression decreases from \(s=16\). This proves (7.3) for
\(s\ge1\).

For \(s=0\), if both anchors are nonempty the face is \(\{P,N\}\), at most
one member can lie in the lower central band, and \(\gamma_C=2\). If one
anchor is empty, the face is \(\{\varnothing,[n]\}\) and meets no
restricted lower hole. Thus (7.3) also holds at the endpoint.

Finally \(y=1/(6M_0)\) on \(\mathcal G\), zero elsewhere, is dual-feasible.
Substitution in the linear and entropy duals proves (7.4). \(\square\)

Every residual \(\mathcal G'\subseteq\mathcal G\) inherits (7.3). Thus a
linear subfamily of a bounded-dispersion schedule defeats hereditary
dense-face peeling at the first step.

### Theorem 7.2 (rotating complement-pair obstruction)

For this theorem take the normalized window \(A=1\); equivalently, when the
ambient fixed window has \(A\ge1\), use its first \(\sqrt m\) depths.
Let \(m=4^j\), \(n=2m+1\), and

\[
K=2^j=\sqrt m,\qquad d=j+1.
\]

Choose a \(d\)-set \(D\subseteq[n]\). There are exactly
\(2^{d-1}=K\) unordered complementary pairs in \(2^D\). Bijection them
with the depths \(q=1,\ldots,K\), writing the pair at depth \(q\) as
\([B_q]=\{B_q,D\setminus B_q\}\). Define

\[
\mathcal H_q^{\rm rot}
=\left\{S\in\binom{[n]}{m-q}:S\cap D\in[B_q]\right\},
\qquad
\mathcal H^{\rm rot}
=\bigsqcup_{q=1}^K\mathcal H_q^{\rm rot}.
\tag{7.7}
\]

Then, uniformly for \(1\le q\le K\),

\[
\boxed{
|\mathcal H_q^{\rm rot}|
=(1+o(1))\frac WK e^{-q^2/m}.}
\tag{7.8}
\]

Consequently,

\[
\boxed{
\frac{|\mathcal H^{\rm rot}|}{W}
\longrightarrow
c_*:=\int_0^1e^{-x^2}\,dx.}
\tag{7.9}
\]

Moreover every proper signed face satisfies

\[
|\mathcal H^{\rm rot}\cap C|\le12\gamma_C,
\tag{7.10}
\]

and hence

\[
\boxed{
\liminf_{j\to\infty}
\frac{\Psi(\mathcal H^{\rm rot})}{W}
\ge
c_*\frac{1+\log24}{12}>0.}
\tag{7.11}
\]

In fact, as order statements,

\[
\Psi(\mathcal H^{\rm rot})=\Theta(W),\qquad
D_{\rm frac}(\mathcal H^{\rm rot}),
D_{\rm det}(\mathcal H^{\rm rot})=\Theta(W).
\tag{7.12}
\]

#### Proof

Let \(k_q=|B_q|\). The exact count is

\[
|\mathcal H_q^{\rm rot}|
=
\binom{n-d}{m-q-k_q}
+\binom{n-d}{m-q-(d-k_q)}.
\tag{7.13}
\]

Uniform falling-factorial expansion, using \(d=O(\log m)\) and
\(q\le\sqrt m\), gives

\[
\frac{\binom{n-d}{m-q-k}}{W}
=2^{-d}e^{-q^2/m}(1+o(1))
\]

uniformly for \(0\le k\le d\). The complementary branch has the same
asymptotic. Since \(2^{1-d}=1/K\), this proves (7.8). Summing the Riemann
sum proves (7.9).

Here each depth uses \(L=2\) traces and each trace occurs at only \(a=1\)
depth. Theorem 7.1 gives (7.10), and \(y=1/12\) on all holes gives (7.11).
Literal repair is \(O(W)\), while (7.4) gives linear lower bounds for both
fractional and deterministic canonical repair. \(\square\)

The family also has strong local balance. Uniformly in \(q\le K\) and
\(x\in[n]\),

\[
\frac{|\{S\in\mathcal H_q^{\rm rot}:x\in S\}|}
{|\mathcal H_q^{\rm rot}|}
=\frac{m-q}{n}+O\left(\frac d{\sqrt m}\right)
=\frac{m-q}{n}+o(1).
\tag{7.14}
\]

For \(x\in D\), the two complementary branch sizes have ratio
\(1+O(d/\sqrt m)\); for \(x\notin D\), the sharper error is \(O(d/n)\).
Every pair outside \(D\) has joint inclusion probabilities within \(O(d/n)\)
of the rank-hypergeometric values, so this holds for \(1-o(1)\) of all
coordinate pairs.

For each fixed integer \(t\), uniformly over all \(t\)-sets
\(L\subseteq[n]\), all patterns \(\sigma\subseteq L\), and all \(q\le K\),

\[
\frac{
|\mathcal H_q^{\rm rot}\cap\{S:S\cap L=\sigma\}|
}{
|\binom{[n]}{m-q}\cap\{S:S\cap L=\sigma\}|
}
\le\frac{2^t+o_t(1)}K.
\tag{7.15}
\]

The denominator is nonzero for all large \(m\). This is only an upper
nonconcentration statement; some cylinders have no holes. To prove it, put
\(\ell=|L\cap D|\). Conditional on the rank and the fixed pattern on \(L\),
each compatible completion to one full marker trace has relative mass

\[
(1+o_t(1))2^{-(d-\ell)}
\]

uniformly in all choices. If \(\ell=0\), at most the two complementary
traces survive; if \(\ell>0\), at most one of them survives. Hence the
conditional hole density is at most
\((1+o_t(1))/K\) in the first case and
\((2^{\ell-1}+o_t(1))/K\) in the second, both bounded by (7.15).

Thus small one-rank defect, asymptotically correct point margins, averaged
pair balance, and absence of concentration in every fixed-coordinate
cylinder do not imply \(\Psi=o(W)\).

### Aligned comparison

Keep the same \(m,K,d,D\), choose one fixed nontrivial complementary pair
\([B]=\{B,D\setminus B\}\), and reuse it at every depth:

\[
\mathcal H_q^{\rm al}
=\left\{S\in\binom{[n]}{m-q}:S\cap D\in[B]\right\}.
\tag{7.16}
\]

Write
\(\mathcal H^{\rm al}=\bigsqcup_{q=1}^K\mathcal H_q^{\rm al}\).

The rank counts, point margins, and bounded-coordinate nonconcentration are
asymptotically the same as in (7.8), (7.14), and (7.15). But the whole
family lies in one face \(C(B,D\setminus B)\), whose cost is

\[
\gamma=\Theta(W/K).
\]

The chosen face and the universal \(K\)-rank cap give
\(\rho(\mathcal H^{\rm al})=\Theta(K)\). Therefore

\[
\boxed{
\Psi(\mathcal H^{\rm al})
=\Theta\left(\frac{W\log K}{K}\right)=o(W),\qquad
D_{\rm det}(\mathcal H^{\rm al})
=\Theta\left(\frac WK\right).}
\tag{7.17}
\]

The aligned and rotating families have opposite repair behavior because one
reuses the same trace through \(K\) depths and the other spends every trace
only once. This is the sharp structural distinction sought in this lane.

The same obstruction lies inside every fixed \(A>0\) window. Let \(r\ge0\)
be the least integer for which the dyadic number

\[
\alpha=2^{-r}\le\min\{A,1\}.
\]

Along \(m=4^j\), for \(j>r\), put

\[
K_\alpha=\alpha\sqrt m=2^{j-r},\qquad d_\alpha=j-r+1.
\]

There are exactly \(2^{d_\alpha-1}=K_\alpha\) complementary trace pairs;
rotate them over depths \(1,\ldots,K_\alpha\). The proof above, with
\(K_\alpha\) in place of
\(K\), gives uniformly

\[
|\mathcal H_q^{\rm rot}|
=(1+o(1))\frac{W}{K_\alpha}e^{-q^2/m},
\]

and hence

\[
\frac{|\mathcal H^{\rm rot}|}{W}
\longrightarrow
c_\alpha:=\frac1\alpha\int_0^\alpha e^{-x^2}\,dx>0.
\tag{7.18}
\]

The density bound \(12\) is unchanged, so

\[
\liminf_{j\to\infty}\frac{\Psi(\mathcal H^{\rm rot})}{W}
\ge c_\alpha\frac{1+\log24}{12}>0.
\tag{7.19}
\]

For every fixed cylinder dimension \(t_0\), its conditional hole density is
\(O_{A,t_0}(m^{-1/2})\). Thus the obstruction is available for every fixed
\(A>0\). The constant \(12\) is an explicit uniform constant, not claimed
optimal; “sharp” here refers to the aligned-versus-rotating change from
\(\Theta(W)\) to \(o(W)\) repair at the same one-rank scales. Indeed,
reusing one trace pair over the same \(K_\alpha\) depths gives

\[
\Psi=\Theta_A\!\left(\frac{W\log m}{\sqrt m}\right)=o(W),
\qquad
D_{\rm det}=\Theta_A\!\left(\frac W{\sqrt m}\right).
\tag{7.20}
\]

Both families are abstract. They are not claimed to be realizable as the
holes of an exact factor or a canonical MTF construction. Theorem 7.1,
however, applies verbatim to actual holes whenever such a dispersed trace
residual can be verified.

## 8. Architecture-local fixed-frame MTF obstruction

There is a second, more specialized obstruction linking the one-rank entropy
dual to the audited fixed-coordinate matching capacity theorem.

Work on \([2m]\), put \(W_e=\binom{2m}{m}\),
\(H=\lceil A\sqrt m\rceil\),
\(N_q=\binom{2m}{m-q}\), and fix one perfect coordinate
matching \(\mathcal P\). Consider a canonical \(H\)-saturated lower-MTF
forest with \(p\) post-cut components, in the specific sense that every
component carries the whole radius-\(H\) certified flag, so the number of
component boundaries relevant at every \(q\le H\) is exactly \(p\), and
each component pays the exact initialization toll \(2H+1\). Suppose
\(s_{\rm ex}\) selected arcs do not flip a pair of \(\mathcal P\), while all
other arcs do. At depth \(q\le H\), define

\[
V_f=\frac{m!}{f!^2(m-2f)!}2^{m-2f},
\qquad
T_{f,q}=
\frac{m!}{f!(f+q)!(m-2f-q)!}2^{m-2f-q},
\]

with \(T_{f,q}=0\) outside its natural range, and put

\[
D_{m,q}=\sum_f(T_{f,q}-V_f)_+.
\tag{8.1}
\]

For a non-saturated forest with \(P_q\) components still active at depth
\(q\), the exact replacement in (8.2) is
\((D_{m,q}-q(s_{\rm ex}+P_q))_+\), and its reset ledger must use the
corresponding weighted component toll rather than \((2H+1)p\).

Let \(\widetilde M_q^-\) be the number of missing declared canonical lower
flags at depth \(q\). The fixed-frame type-capacity argument gives

\[
\widetilde M_q^-
\ge\left(D_{m,q}-q(s_{\rm ex}+p)\right)_+.
\tag{8.2}
\]

Indeed, a pure \(q\)-window preserves its full-pair type \(f\), so distinct
sources can hit at most
\(\sum_f\min(V_f,T_{f,q})=N_q-D_{m,q}\) distinct targets. Each exceptional
arc and each component boundary contaminates at most \(q\) windows.

Let \(\widetilde\Psi\) be the signed-face Poisson functional on these
declared holes. The one-rank dual (3.10), with
\(a_0=1+\log2<2\), and the physical reset charge give

\[
\boxed{
(2H+1)p+\widetilde\Psi
\ge
a_0\left(D_{m,q}-qs_{\rm ex}\right)_+.}
\tag{8.3}
\]

To check (8.3), put \(X=D_{m,q}-qs_{\rm ex}\) and \(b=qp\). The left side
is at least \(2b+a_0(X-b)_+\), which is at least \(a_0X_+\) because
\(a_0<2\).

For \(q=\lfloor x\sqrt m\rfloor\), fixed \(x\in(0,A]\), the audited Gaussian
capacity limit is

\[
\frac{D_{m,q}}{W_e}
\longrightarrow
\delta(x)
:=e^{-x^2}\Phi_{\rm G}(x/2)-\Phi_{\rm G}(-3x/2)>0.
\tag{8.4}
\]

Here \(\Phi_{\rm G}\) is the standard normal distribution function.

For completeness, (8.4) follows from uniform Stirling. Writing

\[
f=\frac m4+X\sqrt m,
\]

one has, uniformly for bounded \(X\),

\[
\frac{V_f}{W_e}
=\frac4{\sqrt{2\pi m}}e^{-8X^2}(1+o(1)),
\]

and

\[
\frac{T_{f,q}}{W_e}
=\frac4{\sqrt{2\pi m}}
e^{-8(X+x/2)^2-x^2}(1+o(1)).
\]

Both type laws have uniformly tight Gaussian tails. Their densities cross
where \(X=-3x/8\). Summing the positive difference on
\(X<-3x/8\) gives

\[
e^{-x^2}\Phi_{\rm G}(x/2)-\Phi_{\rm G}(-3x/2),
\]

which proves (8.4). Positivity follows because the target density exceeds
the source density on that nonempty half-line.

Hence

\[
s_{\rm ex}=o(W_e/\sqrt m)
\quad\Longrightarrow\quad
\liminf
\frac{(2H+1)p+\widetilde\Psi}{W_e}
\ge(1+\log2)\delta(x)>0.
\tag{8.5}
\]

This theorem has deliberately narrow scope. It leaves
\(\Theta(W_e/\sqrt m)\) mixed-frame arcs as an escape, permits changing
pair frames and nonlocal pivots, and concerns the declared canonical
support. The full emitted word can have incidental intervals covering some
declared holes; without a separate bound on that incidental coverage,
(8.5) does not obstruct every physical fixed-frame word. It does show that
signed-face entropy repair cannot by itself rescue the canonical one-frame
ledger.

## 9. What wreath and MTF geometry actually supplies

The proved structural information from the existing lanes falls short in a
specific way.

* The full-cut kernel identity (5.1) is exact, but no exact factor with a
  growing persistent kernel through the Gaussian window is known.
  Point-transitive factors cannot have such an intermediate kernel.
* Core-rainbow cuts are much stronger than full cuts and are bounded in
  number; they are not the right source of a growing kernel.
* Known wreath cycle towers and vertical occurrence ledgers provide counts,
  nested occurrences, and one-step support relations. They do not prove
  that the holes repeat one complementary trace across many depths.
* The adaptive MTF construction supplies nested lower flags, adaptive upper
  recency flags, and reset accounting. Theorem 6.2 shows that one nested
  hole flag would not be compressible anyway. What is needed is massive
  alignment of many parallel histories into the same growing-coordinate
  trace cell.
* Fixed one-coordinate seams, four-label profile trades, and one
  transposition visibly localize defects in only \(O(1)\) coordinates. By
  (4.12), that localization information alone cannot certify unbounded face
  density for a linear residual; it does not preclude additional hidden
  high-codimension alignment.
* The known MSW fixed-prefix hole subfamily is only \(\Theta(W/m)\) in size.
  Literal repair is already \(o(W)\); it gives no theorem for the remaining
  holes.

The rotating construction proves that no theorem based only on Gaussian
rank counts, asymptotic point balance, average pair balance, or
bounded-coordinate nonconcentration can bridge this gap. Even exact
nonnegative fractional point-margin equations can be supported outside the
rotating holes: complement symmetry gives marker mean \(1/2\), and mixing a
lower Hamming-weight trace layer adjusts every marker mean to \((m-q)/n\).
More explicitly, for large \(d\) choose \(k<d/2\) different from the two
forbidden trace weights; the entire uniform weight-\(k\) layer is allowed,
and a convex mixture with the complement-invariant uniform distribution on
all allowed traces hits the required marker mean exactly. Once the expected
marker weight is \(d(m-q)/n\), outside-coordinate symmetry and the fixed
total set size give the same mean on every outside coordinate. Scaling gives
total fractional mass \(W\). This is a fractional observation, not an
integral factor realization, but it rules out point margins alone as the
missing invariant.

## 10. Exact remaining trace-condensation lemma

A concrete route-specific sufficient theorem that would close this
second-wave lane is the following. It is not asserted to be necessary or
minimal.

> **UNPROVED TRACE-CONDENSATION LEMMA \(\mathrm{TC}_A\).** For every fixed
> \(A>0\), choose either
>
> 1. one exact middle wreath factor, with its actual restricted binary hole
>    family; or
> 2. one canonical adaptive-MTF forest whose already audited physical reset
>    and seam charge is \(o(W)\), with the symmetrized physical demand
>
>    \[
>    \mathcal H_q=
>    \mathcal H_q^-
>    \cup
>    \{[n]\setminus T:T\in\mathcal H_q^+\},
>    \]
>
>    where \(\mathcal H_q^-\) and \(\mathcal H_q^+\) are the actual lower-
>    and upper-rank holes after all incidental and seam-crossing witnesses
>    are counted. A declared complement-paired superset containing this
>    demand is also safe,
>
> so that the holes admit a disjoint partition
>
> \[
> \mathcal H
> =\mathcal H_0
> \mathbin{\dot\cup}\mathcal G_1
> \mathbin{\dot\cup}\cdots
> \mathbin{\dot\cup}\mathcal G_J,
> \qquad
> \mathcal G_i\subseteq C_i,
> \]
>
> into proper antipodal trace cylinders satisfying
>
> \[
> \boxed{
> 2|\mathcal H_0|
> +\sum_i\phi(|\mathcal G_i|,\gamma_i)
> =o(W).}
> \tag{10.1}
> \]

By Theorem 4.1, \(\mathrm{TC}_A\) gives \(\Psi_{\le K}=o(W)\).
Randomized face selection then gives an actual integral collection of
canonical blocks of total cost \(o(W)\), followed by literal repair of the
residual. Every proper signed face is complement-closed, so the same blocks
repair the corresponding upper-band defects represented in the symmetrized
demand. Every witness lies internally in a literal block. Thus the argument
remains integral inside one exact factor in the wreath version, and directly
constructs a literal OR word in the MTF version.

Condition (10.1) is strictly weaker than \(\sum_qM_q=o(W)\). Depth-thick
corridors allow \(\Theta(W)\) holes, and up to the order-sharp scale
\(o(W\sqrt m/\log m)\), while still having \(\Psi=o(W)\).

If \(\mathrm{TC}_A\) were proved for every fixed \(A\), slow
diagonalization in \(A\), together with the already audited seams and outer
tails, would give a literal coefficient-one construction. One fixed \(A\)
alone does not remove the Gaussian outer-tail constant.

No current wreath occurrence theorem or MTF state theorem proves
\(\mathrm{TC}_A\), even in a quantitatively weaker sufficient form. The
decisive missing step is cross-depth, growing-coordinate, hereditary trace
alignment.

## 11. Implication scope and audit status

The exact implications established here are

\[
\mathrm{TC}_A
\Longrightarrow
\Psi_{\le K}=o(W)
\Longrightarrow
D_{\rm det}=o(W)
\Longrightarrow
\text{literal fixed-window signed-face repair}.
\]

They do not prove MWB, balanced multiplicities, or labelled common-owner
synchronization. The hole functional sees binary absence only. Conversely,
failure of \(\Psi=o(W)\) directly obstructs the Poisson certificate. It
obstructs deterministic canonical signed-face repair when \(M=O(W)\), by
Corollary 3.2, and in the rotating example by the explicit fractional lower
bound. Without such an additional argument, \(D_{\rm det}\le\Psi\) gives no
general converse; Theorem 5.2 exhibits the possible logarithmic gap.

Nothing here obstructs arbitrary contiguous-OR words outside the additive
proper signed-face architecture. The fixed-frame theorem is still narrower:
it concerns one declared canonical MTF support and does not count incidental
interval coverage unless that coverage is separately controlled.

The decisive analytic steps were independently rederived and adversarially
audited:

* the exact Fenchel and entropy reparametrization, including the \(M=0\),
  \(s=0\), and full-cube endpoints;
* the exact cluster optimizer \(\phi\);
* the common-kernel and \(J\)-trace thresholds, including all
  local-central-binomial offsets and the hypotheses \(t,d=o(\sqrt n)\);
* the marker-dispersion constant \(6\max(a,L)\), its analytic small-\(s\)
  split, and the \(s=0\) endpoint;
* the rotating-pair Riemann-sum constant, point-margin quantifiers,
  fixed-cylinder upper bound, and aligned comparison;
* the distinction between Poisson, deterministic canonical repair, and an
  unrestricted literal word.

The report therefore closes the analytic W2 question. The remaining issue
is not entropy duality. It is the unproved factor/MTF trace-condensation
lemma (10.1).
