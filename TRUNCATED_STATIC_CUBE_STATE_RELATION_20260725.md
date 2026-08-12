# Exact quotient-state relation across one truncated static-cube port

Date: 2026-07-25

This note fixes the missing phase convention in
`TRUNCATED_ROTOR_STATIC_CUBE_COMPILATION_20260725.md` and computes the
states

\[
A_j\longrightarrow B_j\longrightarrow D_j\longrightarrow C_j
\]

exactly. Here \(D_j\) is the unmarked state after the first of the two
cyclic moves from \(B_j\) to \(C_j\).

The main structural consequence is that the active row pair is in collar
slots \(r,r+1\) at \(A_j,B_j\), slots \(r+1,r+2\) at \(D_j\), and slots
\(r+2,r+3\) at \(C_j\), where

\[
r=Q-q_{ij}.
\]

Moreover, after accounting for the complement of all the other row signs,
the source-flush boundary bases at \(A_j\) and \(C_j\) do not agree. At
common hard ranks they differ by a fixed one-for-one exchange at the first
common rank and a fixed two-for-two exchange thereafter.

## 1. The phase convention which the compilation needs

Put \(n=2Q\), and let a cyclic order be

\[
\rho=(\rho_k:k\in\mathbb Z_M).
\]

For a directed cyclic interval write

\[
P_\rho[a,b]=\{\rho_a,\rho_{a+1},\ldots,\rho_b\}.
\]

The forward radius-\(Q\) quotient state compatible with the lower-flag
formula in the static-cube proof is

\[
S_s^Q(\rho)=(L_s^\rho;z_{s,1}^\rho,\ldots,z_{s,2Q}^\rho;R_s^\rho),
\tag{1.1}
\]

where

\[
L_s^\rho=P_\rho[s+Q,s+m-1],
\qquad
R_s^\rho=P_\rho[s+m,s-Q-1],
\tag{1.2}
\]

and

\[
z_{s,k}^\rho=\rho_{s+Q-k}\quad(1\le k\le Q),
\qquad
z_{s,Q+h}^\rho=\rho_{s-h}\quad(1\le h\le Q).
\tag{1.3}
\]

Thus, if

\[
F_h(S_s^Q(\rho))=L_s^\rho+\{z_{s,1}^\rho,\ldots,z_{s,h}^\rho\},
\]

then

\[
F_h=
\begin{cases}
P_\rho[s+Q-h,s+m-1],&0\le h\le Q,\\
P_\rho[s-(h-Q),s+m-1],&Q\le h\le2Q.
\end{cases}
\tag{1.4}
\]

In particular \(F_Q=P_\rho[s,s+m-1]\) is the owner and, at lower depth
\(q\), \(F_{Q-q}=P_\rho[s+q,s+m-1]\), exactly as used in the rectangle
calculation.

The update from phase \(s\) to phase \(s+1\) uses

\[
x=\rho_{s+Q},\qquad y=\rho_{s+m}.
\tag{1.5}
\]

Substitution in the rotor recurrence gives \(S_{s+1}^Q(\rho)\) exactly.

The original compilation only says that \(S_s^Q(\rho)\) has positional
interval flags. That does not by itself specify which endpoint is deleted,
which endpoint is used for the upper extension, or the order of the
\(2Q\) collar. Equations (1.1)--(1.3) should be made part of its definition.
They are the convention forced jointly by its displayed lower interval and
its claim that increasing phase is a forward rotor move.

## 2. Labels at one port

Write \(p_k=\pi_k\), with indices modulo \(M\). Let

\[
s=s_j=2j.
\]

For the row pair \(i\), put

\[
a=a_i=4t+2i,
\qquad
u=p_a,\quad v=p_{a+1}.
\tag{2.1}
\]

For the column pairs, put

\[
c_h=p_{m+2h-1},
\qquad
d_h=p_{m+2h}.
\tag{2.2}
\]

Thus \(\beta_h=(c_h\ d_h)\). At port \(j\),

\[
c_j=p_{s+m-1},\qquad d_j=p_{s+m},
\tag{2.3}
\]

and

\[
c_{j+1}=p_{s+m+1},\qquad d_{j+1}=p_{s+m+2}.
\tag{2.4}
\]

Let

\[
\gamma=\alpha_{x^j},
\qquad
\overline\gamma=\alpha_{\mathbf1-x^j}.
\]

The row transpositions act only in the lower half of the collar at all
three phases \(s,s+1,s+2\). Consequently they change collar order but not
the unordered core or tail.

## 3. Exact formulas for \(A_j,B_j,D_j,C_j\)

Abbreviate the base phase-\(s\) data by

\[
L=L_s^\pi,
\qquad
R=R_s^\pi,
\qquad
\mathbf z=\mathbf z_s^\pi.
\]

Then

\[
\boxed{
A_j=(L;\gamma\mathbf z;R).}
\tag{3.1}
\]

At phase \(s\), only \(\beta_j\) crosses the owner boundary. Therefore

\[
\boxed{
B_j=(L-c_j+d_j;\overline\gamma\mathbf z;R-d_j+c_j).}
\tag{3.2}
\]

After one cyclic move no column pair crosses the owner boundary: both
labels of \(\beta_j\) are in the core and both labels of \(\beta_{j+1}\) are
in the tail. Hence the intermediate state is exactly

\[
\boxed{
D_j=S_{s+1}^Q(\overline\gamma\beta\pi)
=(L_{s+1}^\pi;\overline\gamma\mathbf z_{s+1}^\pi;R_{s+1}^\pi).}
\tag{3.3}
\]

At phase \(s+2\), only \(\beta_{j+1}\) crosses. Thus

\[
\boxed{
C_j=(L_{s+2}^\pi-c_{j+1}+d_{j+1};
\overline\gamma\mathbf z_{s+2}^\pi;
R_{s+2}^\pi-d_{j+1}+c_{j+1}).}
\tag{3.4}
\]

The two literal cyclic updates are also explicit. The first uses

\[
x_0=p_{s+Q},\qquad y_0=c_j,
\tag{3.5}
\]

and the second uses

\[
x_1=p_{s+Q+1},\qquad y_1=d_{j+1}.
\tag{3.6}
\]

Finally,

\[
A_{j+1}=(L_{s+2}^\pi;
\alpha_{x^{j+1}}\mathbf z_{s+2}^\pi;
R_{s+2}^\pi).
\tag{3.7}
\]

It follows that the routed exchange \(A_j\to B_j\) removes \(c_j\) from
the core and inserts \(d_j\), whereas the routed exchange
\(C_j\to A_{j+1}\) removes \(d_{j+1}\) and inserts \(c_{j+1}\).

## 4. The two-step source-state relation

Put

\[
w_0=p_{s+Q},\quad w_1=p_{s+Q+1},
\qquad
\ell_0=p_{s-Q},\quad\ell_1=p_{s-Q+1}.
\tag{4.1}
\]

As unordered blocks, (3.1) and (3.4) satisfy

\[
\boxed{
L(C_j)=L(A_j)-\{w_0,w_1\}+\{d_j,d_{j+1}\},}
\tag{4.2}
\]

\[
\boxed{
R(C_j)=R(A_j)-\{d_j,d_{j+1}\}+\{\ell_0,\ell_1\}.}
\tag{4.3}
\]

For the base collar order,

\[
\boxed{
\mathbf z_{s+2}^\pi=(w_1,w_0,z_{s,1}^\pi,\ldots,z_{s,n-2}^\pi).}
\tag{4.4}
\]

Thus the two cyclic moves transfer \(w_0,w_1\) from core to the front of
the collar, transfer \(\ell_0,\ell_1\) from the end of the collar to the
tail, and, after the two column-boundary effects are included, transfer
\(d_j,d_{j+1}\) from tail to core.

Let

\[
\mathsf A=\prod_{h=0}^{p-1}\alpha_h.
\]

Since \(\overline\gamma=\mathsf A\gamma\), the ordered relation is

\[
\boxed{
\mathbf z(C_j)
=(w_1,w_0,
\mathsf A(\gamma z_{s,1}),\ldots,
\mathsf A(\gamma z_{s,n-2})).}
\tag{4.5}
\]

This global complement twist is important: \(C_j\) is not merely a
two-slot shift of \(A_j\); every other row-pair orientation is complemented
as well.

## 5. Exact active-pair positions

The rectangle depth is

\[
q=q_{ij}=a-s+1.
\]

Put

\[
r=Q-q=Q-a+s-1.
\tag{5.1}
\]

By (1.3), at phase \(s\),

\[
z_{s,r}=v,
\qquad
z_{s,r+1}=u.
\tag{5.2}
\]

At the four successive states the same pair occupies

\[
\begin{array}{c|c|c}
\text{state}&\text{collar slots}&\text{row orientation}\\ \hline
A_j&r,r+1&x_i^j\\
B_j&r,r+1&1-x_i^j\\
D_j&r+1,r+2&1-x_i^j\\
C_j&r+2,r+3&1-x_i^j.
\end{array}
\tag{5.3}
\]

Here “orientation \(0\)” means the base order \((v,u)\) and orientation
\(1\) means \((u,v)\). Consequently a bit toggle reverses the \(A_j\)
edge and all three \(B_j,D_j,C_j\) edges in opposite orientation.

## 6. Comparison of the source-flush boundary bases

Consider the route \(A_j\to B_j\). Its exchange tail label is \(d_j\),
and the active pair starts at boundary \(r\). Let \(K_h^A\) be the
boundary bases from equation (2.5) of
`TRUNCATED_STATIC_CUBE_CONNECTOR_AUDIT_20260725.md`.

The route \(C_j\to A_{j+1}\) has exchange tail label \(c_{j+1}\), and the
active pair starts at boundary \(r+2\). Let its boundary bases be \(K_h^C\).

Fix all other row bits and put

\[
\Theta_i=\prod_{h\ne i}\alpha_h.
\tag{6.1}
\]

The complement convention means that the \(C_j\) edge, after its active
\(\alpha_i\) orientation is removed, uses the \(\Theta_i\)-image of the
other-row orientation at \(A_j\). The exact structural comparison is

\[
\boxed{
K_{r+2}^C
=\bigl(\Theta_iK_{r+2}^A-\{\ell_0\}\bigr)+\{d_{j+1}\},}
\tag{6.2}
\]

and, for every

\[
r+3\le h\le n,
\]

\[
\boxed{
K_h^C
=\bigl(\Theta_iK_h^A-\{\ell_0,\ell_1\}\bigr)
+\{c_{j+1},d_{j+1}\}.}
\tag{6.3}
\]

To verify this, note first that the \(C_j\) prefix before its active pair is

\[
\{w_1,w_0\}+\Theta_i\{z_{s,1},\ldots,z_{s,r-1}\}.
\]

Combining it with (4.2) restores the original core \(L\) and leaves the two
new core labels \(d_j,d_{j+1}\). At the initial \(C_j\) boundary
\(h=r+2\), its reload label \(c_{j+1}\) has not yet entered the core. The
\(A_j\) boundary at the same rank has instead acquired the final old collar
label \(\ell_0\), proving (6.2). From \(h=r+3\) onward the \(C_j\) flush has
inserted \(c_{j+1}\). Its shifted collar suffix is the corresponding
\(A_j\) suffix with the last two old collar labels
\(\ell_0,\ell_1\) deleted, proving (6.3).

There is no \(C_j\) boundary term at rank \(h=r+1\), while the \(A_j\)
source has one. Thus even before the special split-core states are
considered, the two source boundary traces do not telescope term by term.
At \(h=r+2\) their bases differ by a genuine one-for-one exchange, and at
all later common ranks by a genuine two-for-two exchange. All six labels
in these exchanges are disjoint from the active row pair.

The signs are opposite, because \(A_j\) uses \(x_i^j\) and \(C_j\) uses
\(1-x_i^j\). Equations (6.2)--(6.3), however, show that opposite sign is
not equality of support.

## 7. What remains unspecified

The special split-core bases \(J_h\) depend on the ordered buffer lists

\[
x_1,\ldots,x_{n}
\]

chosen separately in Theorem 2.1. The compilation theorem specifies only
their existence. It gives neither

* a deterministic buffer rule, nor
* a coupling between the buffers on \(A_j\to B_j\) and those on
  \(C_j\to A_{j+1}\).

Therefore the quotient states force (6.2)--(6.3) for the boundary terms,
but they do not determine any relation between \(J_h^A\) and \(J_h^C\).
In particular, a claimed full cross-port telescope cannot be audited until
a buffer coupling is supplied.

The intermediate cyclic state \(D_j\) contributes a row-transposition edge
only at prefix \(h=r+1\), while \(B_j\) and \(C_j\) contribute only at
\(h=r\) and \(h=r+2\), respectively. Incoming target reloads are confined
to prefixes at most \(r\). Hence none of those fixed states can cancel the
common-rank boundary mismatch (6.3) for \(h\ge r+3\). Any cancellation
there must come from the buffer-dependent split-core \(J\)-chains or from a
genuinely nonlocal pairing across other ports or carriers.

This is the exact residual question.

## 8. A buffer-independent full-path residue on every high prefix

There is a stronger consequence of (4.2)--(4.4). For every

\[
h\ge r+3,
\]

all four masks in the \(A_j\to B_j\) source-flush difference at prefix
\(h\)

* contain \(\ell_0,\ell_1\), and
* omit \(c_{j+1},d_{j+1}\).

Indeed, the \(K_h^A\) suffix contains the final two old collar labels once
\(h\ge r+3\), while the \(J_h^A\) core contains the entire fixed suffix
\(z_{r+2},\ldots,z_n\). Neither next-column label is in the source core,
collar, exchange label, or a legal buffer.

At the same prefixes, all four masks in the \(C_j\to A_{j+1}\)
source-flush difference have the opposite invariant:

* they contain \(c_{j+1},d_{j+1}\), and
* omit \(\ell_0,\ell_1\).

Here \(d_{j+1}\) belongs to the \(C_j\) source core and \(c_{j+1}\) is its
exchange tail label; the two old trailing-collar labels have already moved
to the tail and cannot be buffers.

Thus the two source differences have disjoint supports at every common
prefix \(r+3\le h\le n-1\), independently of all buffer choices. Each
individual source trace has squared norm \(4\) there by the one-route
calculation. Incoming and outgoing target reloads are confined to prefixes
at most \(r\), and the fixed states \(B_j,D_j,C_j\) contribute only at
\(r,r+1,r+2\). Therefore, for every interior port,

\[
\boxed{
\|\Delta_{ij}^{(m-Q+h)}\|_2^2=8
\qquad(r+3\le h\le n-1).}
\tag{8.1}
\]

Consequently

\[
\boxed{
\sum_{h=r+3}^{n-1}
\|\Delta_{ij}^{(m-Q+h)}\|_2^2
=8(n-r-3)=\Omega(Q).}
\tag{8.2}
\]

At the final port there is no outgoing \(C_j\to A_{j+1}\) route. The
\(A_j\to B_j\) source trace alone gives

\[
\boxed{
\|\Delta_{i,t-1}^{(m-Q+h)}\|_2^2=4
\qquad(r+1\le h\le n-1),}
\tag{8.3}
\]

and hence total squared norm \(4(n-r-1)=\Omega(Q)\).

This proves that the complete unpadded path has no exact single-bit
cross-port telescope, not merely that the two boundary \(K\)-chains fail to
cancel term by term.

### 8.1 Direct next-to-top check

Although the complete \(J\)-chains depend on the unspecified buffers, their
next-to-top member does not, except for one harmless buffer label in the
case \(r=1\).

For one source route whose active pair occupies slots \(r,r+1\), put

\[
T=K_n=J_n
=A+b+\bigl(\{z_1,\ldots,z_n\}-\{u,v\}\bigr).
\tag{8.4}
\]

At prefix \(h=n-1\),

\[
K_{n-1}=T-\{z_{r+2}\},
\tag{8.5}
\]

whereas

\[
J_{n-1}=
\begin{cases}
T-\{z_{r-1}\},&r\ge2,\\
T-\{x_1\},&r=1.
\end{cases}
\tag{8.6}
\]

The deleted labels in (8.5) and (8.6) are distinct, so the aggregate
source-flush transposition difference at this rank has squared norm exactly
\(4\), for every legal buffer choice.

For the \(A_j\to B_j\) source route, every one of the four masks in this
rank-\((m+Q-1)\) difference contains

\[
\ell_0,\ell_1
\]

and omits

\[
c_{j+1},d_{j+1}.
\]

For the \(C_j\to A_{j+1}\) source route, every one of its four masks has the
opposite invariant: it contains \(c_{j+1},d_{j+1}\) and omits
\(\ell_0,\ell_1\).  This remains true in the \(r=1\) case because \(x_1\)
must lie in the source core and must be distinct from the exchanged core
label.

Consequently the two rank-\((m+Q-1)\) source differences have disjoint
supports. Their opposite orientations cannot cancel. Neither a target
reload nor one of the states \(B_j,D_j,C_j\) contributes at this prefix:
their row-pair boundaries are at most \(r+2\le Q+2<n-1\) in the calibrated
range.

In particular, for the unpadded path of Theorem 4.2 and an interior port
\(j<t-1\), toggling one bit has the exact buffer-independent next-to-top
residue

\[
\boxed{
\|\Delta_{ij}^{(m+Q-1)}\|_2^2=8.}
\tag{8.7}
\]

At the last port, where there is no outgoing \(C_j\to A_{j+1}\) route, the
corresponding value is

\[
\boxed{
\|\Delta_{i,t-1}^{(m+Q-1)}\|_2^2=4.}
\tag{8.8}
\]

Equations (8.1)--(8.3) and (8.7)--(8.8) are one-bit influence statements,
not by themselves
a covariance lower bound for the full Boolean cube: different bit
influences may live in higher-order Walsh components. They do, however,
give an exact \(\Omega(Q)\) full-incidence influence for every bit and rule
out an exact cross-port telescope of the complete incidence difference,
independently of how the flush buffers are coupled. An additional
\(E\)-dependent padding rule could add further terms; it is not part of the
audited compilation and would itself require a cancellation proof.

## 9. Exact row and column sign relations

Let \(E^{\mathrm{row}\ i}\) be obtained by toggling \(E_{ij}\) for every
port \(j\). Since all \(\alpha\)'s commute and are disjoint from all
\(\beta\)'s, equations (3.1)--(3.7) give

\[
A_j(E^{\mathrm{row}\ i})=\alpha_iA_j(E),\qquad
B_j(E^{\mathrm{row}\ i})=\alpha_iB_j(E),
\tag{9.1}
\]

and likewise

\[
D_j(E^{\mathrm{row}\ i})=\alpha_iD_j(E),\qquad
C_j(E^{\mathrm{row}\ i})=\alpha_iC_j(E).
\tag{9.2}
\]

Thus, if the buffer rule on every route is coordinate-equivariant, the
entire unpadded compiled path is sent to its \(\alpha_i\)-image. This
recovers the full-row relation

\[
P(E^{\mathrm{row}\ i})=\alpha_iP(E).
\tag{9.3}
\]

This assertion is conditional on an equivariant buffer rule; Theorem 2.1
alone only chooses buffers existentially.

Now complement one complete column \(x^j\). Put

\[
\mathsf A=\prod_i\alpha_i.
\]

The four local states at that port obey

\[
(A_j,B_j,D_j,C_j)(E^{\mathrm{col}\ j})
=\mathsf A(A_j,B_j,D_j,C_j)(E).
\tag{9.4}
\]

However, \(C_{j-1}\) and \(A_{j+1}\) are unchanged. Therefore the incoming
route \(C_{j-1}\to A_j\) has only its target transformed, while the outgoing
route \(C_j\to A_{j+1}\) has only its source transformed. A column sign
update is consequently not the coordinate image of the whole compiled
path, even with equivariant buffers. Its two boundary routes are the exact
locations where a separate telescope or pairing theorem would be needed.

## 10. The natural slot-equivariant routing has \(\Omega(MQ)\) variance

The preceding influence lower bound becomes a covariance lower bound for
the slot-equivariant routing prescribed in Section 6.2 of the compilation
note.

Assume:

1. buffer slots are fixed independently of all row-pair orientations;
2. the target collar is reloaded in its target slot order; and
3. no \(E\)-dependent padding is appended.

Let \(\widetilde I(E)\) be the complete aggregate hard-flag incidence
vector of the unpadded compiled path, and let the \(pt\) bits of \(E\) be
independent and fair.

### Lemma 10.1 (degree two)

Every coordinate of \(\widetilde I(E)\), as a Boolean function of the
matrix bits, has Walsh degree at most \(2\).

#### Proof

During a source flush, all row pairs initially occupy adjacent two-slot
blocks in one collar. At any time:

* at most one row pair is split between core and tail, because the two
  adjacent labels are processed consecutively; and
* a flag-prefix boundary splits at most one further adjacent row pair.

Every other row pair has both labels in the flag or neither label in it, so
its orientation is invisible. Hence one flag mask depends on at most two
bits of the source column.

At the end of the flush all source-collar labels are in the unordered core,
so source orientation has disappeared completely. During target reload the
same argument applies in reverse: at most one target pair is split between
core and collar and at most one further pair is split by the flag-prefix
boundary. Thus one reload flag depends on at most two bits of the target
column.

In a route \(C_j\to A_{j+1}\), the flush part therefore depends only on
column \(j\), while the reload part depends only on column \(j+1\); no
single state depends on both columns. The two cyclic states depend only on
column \(j\) and split at most one pair.

The indicator of any particular mask at any particular state is therefore
a Boolean function of at most two bits. Summing these indicators over all
states preserves Walsh degree at most \(2\). \(\square\)

### Theorem 10.2 (variance obstruction)

For vector-valued Walsh expansion

\[
\widetilde I(E)=\sum_{S\subseteq[pt]}\widehat I_S\chi_S(E),
\]

one has

\[
\sum_b\mathbb E\|
\widetilde I(E^{\oplus b})-\widetilde I(E)\|_2^2
=4\sum_S |S|\|\widehat I_S\|_2^2
\le8\,\operatorname{tr}\operatorname{Cov}(\widetilde I(E)),
\tag{10.1}
\]

where Lemma 10.1 was used in the inequality.

For every bit, (8.2)--(8.3) give

\[
\mathbb E\|
\widetilde I(E^{\oplus b})-\widetilde I(E)\|_2^2
\ge4(Q-3)
\tag{10.2}
\]

for all sufficiently large \(Q\). Consequently

\[
\boxed{
\operatorname{tr}\operatorname{Cov}(\widetilde I(E))
\ge \frac{pt(Q-3)}2
=\left(\frac1{32}-o(1)\right)MQ.}
\tag{10.3}
\]

Thus the independent-fair static cube, after the proposed literal
slot-equivariant compilation, does not have coefficient-scale
\(O(M)\) variance in its full physical load. Its complete variance is
larger by a factor \(\Omega(Q)\).

This does not rule out a different randomized law on cube vertices, a
non-slot-equivariant routing whose buffer choices introduce high Walsh
degree, or a multi-carrier signed pairing. It does close the claimed
independent-fair \(O(1)\)-step interpretation for the natural compiled
kernel.
