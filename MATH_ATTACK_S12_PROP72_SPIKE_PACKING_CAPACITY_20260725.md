# Proposition 7.2 spike packing: an owner-preserving repair, exact capacity obstructions, and the floor-correct boundary ledger

Date: 2026-07-25

Method: pure mathematics only. No computation, search, solver, or web access is used.

## 0. Outcome

Put

\[
n=2m+1,
\qquad
W=\binom{n}{m},
\qquad
T=\binom{n}{m-1}=\frac{m}{m+2}W.
\]

Depth one is treated as the separately solved seed. This report concerns
\(q\ge2\).

There are two different conclusions.

First, the exact owner-disjointness problem has a positive local solution.
For a phase-\(A\) token with lower root \(S\), middle owner \(Y\), and upper
flag \(U_q\), the set

\[
R_q=U_q\setminus Y
\]

has size \(q\). If \(B\subset R_q\) is a pair and \(\theta\) exchanges
\(A\) and \(B\), then \(\theta\) fixes both \(S\) and \(Y\). Hence the
old token and the \(\theta\)-token are parallel central edges. Arbitrary
rootwise choices preserve lower saturation and middle simplicity exactly.
At a common depth-\(q\) spike, every pair of such innovations has Gram
inner product at least the depth-\(q\) weight. This removes the owner-release
defect in Proposition 7.2 for every fixed phase.

Second, this repair has an exact physical capacity ceiling. A common pair
\(B\) can lie in the future sets \(R_q\) of at most \(q-1\) consecutive
starts. Therefore an orientation-preserving interval atlas which touches
\(T_0\) roots requires at least

\[
\frac{T_0}{q-1}
\]

packets. Under the required \(o(W/H)\) packet budget and \(q\le H\), it can
touch only \(o(W)\) roots. Thus it cannot repair an arbitrary
positive-density bounded-load collision profile. It can still be efficient
on a small number of heavy spikes.

For one strict chart, the release defect can also be removed in the
coordinate-orbit model: its at most \(2s\le m+1\) old and alternate owners
can all be reserved, and the robust middle-level extension lemma constructs
one common background for every cube corner. This is an exact integral
single-chart theorem. Packing many charts is different: their union can
reserve far more than \(m+1\) owners, and the reserved sets may overlap.

The original owner-changing Proposition 7.2 charts have two sharper
arbitrary-profile obstructions.

1. Their existential size
   \(s=\lfloor(m+q)/(q+1)\rfloor\) is not available at an arbitrary existing
   spike. A phase-reachable spike may contain only \(q\) full priority pairs,
   and there are exact full token matchings with a load-\(m\) spike for which
   none of the \(m\) occurrences contains any full partner pair in its
   missing set.
2. With the background frozen, an owner-changing independent component must
   use one of the exactly
   \[
   W-T=\frac{2W}{m+2}
   \]
   unused middle owners. Collision loads do not encode this owner incidence.
   A finite exact construction below gives \(\lfloor m/3\rfloor\) individually
   legal two-occurrence charts whose alternate-owner sets are all the same
   two holes, so at most one chart is selectable.

The curvature ledger also has an exact finite-horizon correction. For
ambient full-word reciprocal floor weights, an upper flag at depth \(p\)
has weight

\[
w_p^+=\frac1{d_{p-1}},
\qquad
d_r=\left\lfloor
\frac{W}{\binom{n}{m-r}}
\right\rfloor.
\]

For a chart beginning at depth \(q\) and followed through depth \(J\), put

\[
C_{q,J}=\sum_{p=q}^{J}\frac1{d_{p-1}}.
\]

The maximal strict Proposition 7.2 chart has fair curvature credit

\[
\frac14s_q(s_q-1)C_{q,J},
\qquad
s_q=1+\left\lfloor\frac{m-1}{q+1}\right\rfloor,
\]

for at most \(2s_q\) selected-row runs and \(4s_q\) raw boundaries. With
the unbuffered horizon \(J=H=\lceil\sqrt m\,\omega\rceil\), the terminal
quantity \((s_H-1)C_{H,H}/H\) tends to zero. Thus the unbuffered certified
ledger is not uniformly super-\(H\). If instead

\[
J=H+\left\lfloor a\frac mH\right\rfloor,
\qquad
a>0,
\qquad
e^{\omega^2}\omega^3=o(\sqrt m),
\]

then uniformly for \(2\le q\le H\),

\[
\frac{(s_q-1)C_{q,J}}{H}\longrightarrow\infty.
\]

So buffering repairs the numerical curvature-per-boundary ledger for a
sufficiently slow diagonal. It does not repair owner selection, fixed-factor
compatibility, or the coherent-endpoint linear term. No constant-one
conclusion is claimed.

## 1. Token notation and the strict Proposition 7.2 chart

Let \(A\) be an omitted coordinate pair and let

\[
\pi=(x_0,\ldots,x_{2m-2})
\]

be an oriented cyclic row on \(Q_A=[n]\setminus A\). At start \(i\), write

\[
S_i=I_\pi(i,m-1),
\qquad
Y_i=I_\pi(i-1,m),
\]

and, for \(p\ge1\),

\[
L_p(i)=I_\pi(i+p-1,m-p),
\qquad
U_p(i)=I_\pi(i-1,m+p).
\]

Thus

\[
S_i\subset Y_i\subset U_p(i),
\qquad
|U_p(i)\setminus Y_i|=p.
\tag{1.1}
\]

The strict chart from Proposition 7.2 chooses one common
\((m+q)\)-set \(U\), one phase pair \(A\subset U^c\), pairwise disjoint
\((q+1)\)-sets \(D_i\subset U\), and distinct priority pairs
\(B_i\subset D_i\). It puts

\[
S_i=U\setminus D_i
\]

and orders \(D_i\) so that \(B_i\) supplies the predecessor and first upper
suffix coordinate. If \(\theta_i\) exchanges \(A\) and \(B_i\), the upper
innovation is

\[
(d_i)_p^+
=\mathbf e_{\theta_iU_p(i)}-\mathbf e_{U_p(i)}.
\tag{1.2}
\]

The lower flags are fixed. For arbitrary positive upper weights through
depth \(J\), direct expansion gives

\[
\|d_i\|^2=2\sum_{p=1}^{J}w_p^+,
\qquad
\langle d_i,d_k\rangle
=\sum_{p=q}^{J}w_p^+
\quad(i\ne k).
\tag{1.3}
\]

Indeed, before depth \(q\) the disjoint missing sets distinguish both old
targets and both images. From depth \(q\) onward the old targets coincide,
whereas the images omit different pairs \(B_i\). Every mixed old/image
equality is impossible because old targets avoid \(A\) and nontrivial images
meet \(A\).

The central owner claim is also exact inside the partial atlas. Choose the
predecessor \(b_i\in B_i\), with paired image \(a_i\in A\). Then

\[
Y_i=S_i\cup\{b_i\},
\qquad
\theta_iY_i=S_i\cup\{a_i\}.
\tag{1.4}
\]

The old owners are distinct, the alternate owners are distinct, and an old
owner cannot equal an alternate owner because the former is contained in
\(U\) whereas the latter meets \(A\subset U^c\). Thus arbitrary side choices
are a matching on the displayed roots.

What (1.4) does not by itself prove is compatibility with an already frozen
background. The embedding in the source proposition deletes every background
edge using one of the displayed owners and may release up to \(2s\) lower
roots. That particular embedding is not lower-saturating. There is, however,
an exact one-chart repair in the coordinate-orbit model.

### Proposition 1.1 (one strict chart has an exact common background)

For \(q\ge2\), every strict chart of maximal allowed size

\[
s\le s_q=1+\left\lfloor\frac{m-1}{q+1}\right\rfloor
\]

embeds into one full lower-saturating matching cube in the complete
coordinate-orbit token model. No lower root is released.

#### Proof

The chart has \(s\) roots and at most \(2s\) distinct old/alternate middle
owners. Since \(q\ge2\),

\[
2s\le2+2\left\lfloor\frac{m-1}{3}\right\rfloor\le m+1.
\]

Prescribe the \(s\) old chart edges and forbid the \(s\) alternate owners.
Lemma 3.1 applies because \(p+h=2s\le m+1\). Remove the prescribed old
edges from the completed matching. What remains matches every non-chart
root and avoids all \(2s\) old/alternate owners: the old owners were occupied
by the removed prescribed edges, and the alternate owners were forbidden.
At each chart root insert either its old or its alternate edge. Equations
(1.4) show that every side choice uses distinct reserved owners. Thus all
cube corners share one exact background. Every inclusion edge can be lifted
to a literal coordinate-orbit token. \(\square\)

This proposition does not place all rows in one preselected tuple of local
factors, and it does not pack several charts whose combined owner reserve is
large. Sections 3 and 5 isolate those failures.

## 2. The fixed-partition partner capacity

Fix disjoint priority pairs

\[
P_1,\ldots,P_m
\]

and one singleton \(z\). For an \((m+q)\)-set \(U\), let

\[
f(U)=\#\{j:P_j\subset U\},
\qquad
g(U)=\#\{j:P_j\subset U^c\},
\]

and put \(\varepsilon(U)=\mathbf1_{\{z\in U\}}\).

### Lemma 2.1 (exact full-pair balance)

For every \(U\in\binom{[n]}{m+q}\),

\[
\boxed{f(U)-g(U)=q-\varepsilon(U).}
\tag{2.1}
\]

If a phase pair \(A\) is contained in \(U^c\), then \(g(U)\ge1\), hence

\[
f(U)\ge q.
\tag{2.2}
\]

Equality is attainable.

#### Proof

Let \(h\) be the number of split priority pairs. Then

\[
f+g+h=m,
\qquad
2f+h+\varepsilon=m+q.
\]

Subtracting gives (2.1). If \(A\subset U^c\), then \(g\ge1\), and (2.2)
follows. To attain equality, put \(z\) in \(U\), put exactly one priority
pair \(A\) outside \(U\), put exactly \(q\) pairs inside \(U\), and split
all remaining pairs. Then \(\varepsilon=g=1\) and \(f=q\). \(\square\)

### Corollary 2.2 (strict-chart size at an existing spike)

Every strict Proposition 7.2 chart supported on an already prescribed spike
\(U\) satisfies

\[
\boxed{
s\le
\min\left\{
f(U),
\left\lfloor\frac{m+q}{q+1}\right\rfloor
\right\}.}
\tag{2.3}
\]

At a minimum-partner reachable spike, if \(q^2\le m\), this reduces to

\[
s\le q.
\tag{2.4}
\]

#### Proof

The distinct partners \(B_i\) must be full priority pairs contained in
\(U\), giving \(s\le f(U)\). Pairwise disjoint \(D_i\)'s give
\(s(q+1)\le m+q\). Finally,

\[
q\le\left\lfloor\frac{m+q}{q+1}\right\rfloor
\quad\Longleftrightarrow\quad
q^2\le m.
\]

This proves the claim. \(\square\)

The distinction is essential. Proposition 7.2 constructs \(U\) after
choosing many partner pairs. A packing theorem for an arbitrary collision
profile must use the \(U\)'s already present in that profile.

## 3. A full integral matching with a chart-invisible spike

We first record the exact extension fact needed to turn a local obstruction
into a full lower-saturating matching.

### Lemma 3.1 (robust middle-level extension)

Consider the simple inclusion graph between

\[
\binom{[n]}{m-1}
\quad\text{and}\quad
\binom{[n]}m.
\]

Let \(p\) pairwise disjoint inclusion edges be prescribed and let \(h\)
additional middle vertices be forbidden. If

\[
p+h\le m+1,
\tag{3.1}
\]

then the prescribed edges extend to a matching saturating every
\((m-1)\)-set while using none of the forbidden middle vertices.

#### Proof

We use the Lovasz form of the Kruskal--Katona shadow theorem. For every
nonempty family \(\mathcal X\subseteq\binom{[n]}{m-1}\), complement its
members into a family of \(r=m+2\)-sets. Write

\[
|\mathcal X|=\binom xr,
\qquad
r\le x\le n=2r-3,
\qquad
y=x-r+1\in[1,r-2].
\]

Kruskal--Katona gives

\[
|N(\mathcal X)|\ge\binom{x}{r-1}.
\]

The shadow surplus is therefore at least

\[
D_r(y)
=\binom{x}{r-1}-\binom xr
=\frac{(r-y)\prod_{j=1}^{r-1}(y+j)}{r!}.
\tag{3.2}
\]

Moreover,

\[
\frac{d}{dy}\log D_r(y)
=-\frac1{r-y}+\sum_{j=1}^{r-1}\frac1{y+j}
\ge
-\frac1{r-y}+\frac{r-1}{y+r-1}.
\]

The last expression is nonnegative because

\[
(r-1)^2-ry\ge1
\qquad(1\le y\le r-2).
\]

Hence \(D_r(y)\ge D_r(1)=r-1=m+1\), and so

\[
|N(\mathcal X)|-|\mathcal X|\ge m+1
\tag{3.3}
\]

for every nonempty \(\mathcal X\).

Delete the \(p\) prescribed lower vertices, their \(p\) prescribed middle
owners, and the \(h\) forbidden owners. For every family of remaining lower
vertices, (3.3) shows that deleting at most \(p+h\le m+1\) neighbors leaves
at least as many neighbors as lower vertices. Hall's theorem completes the
matching. \(\square\)

### Theorem 3.2 (exact load-\(m\) spike of strict incidence zero)

For every

\[
2\le q\le m-2,
\]

there is a full lower-saturating matching in the coordinate-symmetric orbit
token support and a target \(U\in\binom{[n]}{m+q}\) such that

\[
\mu_{q,U}=m,
\tag{3.4}
\]

but none of the \(m\) occurrences at \(U\) has a full priority pair in its
missing set \(U\setminus S\). Consequently no strict Proposition 7.2 atom
is incident with this spike.

#### Proof

Choose a minimum-partner reachable \(U\) from Lemma 2.1, with one empty
phase pair \(A\), exactly \(q\) full pairs, every other pair split, and the
singleton in \(U\). Choose an \(m\)-set \(R\subset U\) containing the
singleton and exactly one coordinate from every nonempty priority-pair
class. Thus \(R\) contains no full priority pair.

Cyclically order

\[
R=(r_0,\ldots,r_{m-1}).
\]

For \(i\in\mathbb Z/m\mathbb Z\), let \(D_i\) be the cyclic
\((q+1)\)-interval beginning at \(r_i\), put \(d_i=r_i\), and define

\[
S_i=U\setminus D_i,
\qquad
Y_i=U\setminus(D_i\setminus\{d_i\}).
\tag{3.5}
\]

The \(D_i\)'s are distinct because \(q+1<m\). Hence the \(S_i\)'s are
distinct. The complements \(D_i\setminus\{d_i\}\) are the distinct cyclic
\(q\)-intervals beginning at \(r_{i+1}\), so the \(Y_i\)'s are also
distinct. Therefore the \(m\) edges \(S_i\subset Y_i\) form a matching.

Each edge lifts to a phase-\(A\) token with upper depth-\(q\) flag \(U\):
use \(d_i\) as predecessor and the other \(q\) elements of \(D_i\) as the
upper suffix. Every such cyclic row is present in a coordinate image of an
exact local factor on \(Q_A\).

Apply Lemma 3.1 with \(p=m\) and \(h=0\) to extend the central edges. Every
residual inclusion edge \(S\subset Y\) can be lifted with upper target
different from \(U\). If \(Y\not\subset U\), this is automatic. If
\(Y\subset U\), replace one coordinate of \(U\setminus Y\) by a coordinate
outside \(U\), then choose an omitted pair in the complement of the new
target. The complement has size \(m+1-q\ge3\). Thus no residual token adds
another occurrence at \(U\), proving (3.4).

Finally every \(D_i\subset R\), and \(R\) contains no full priority pair.
So no occurrence supports the partner required by the strict chart.
\(\square\)

The theorem is integral and every token is literal. It does not assert that
the resulting tokens occupy \(o(W/H)\) source-row runs. Its implication is
exactly that collision loads alone cannot imply strict-chart incidence.

### Theorem 3.3 (linear weighted collision can be strictly chart-invisible)

Suppose a full token matching is phase-labelled by the fixed priority
pairs, so every selected token has an omitted pair \(A\) which its middle
owner avoids. For every

\[
2\le q\le\left\lfloor\frac{m-2}{2}\right\rfloor,
\]

one may re-lift every central edge, preserving its lower root, middle owner,
and phase, so that its depth-\(q\) missing set contains no full priority
pair.

Let

\[
M_q=\binom{n}{m+q}.
\]

For the resulting load vector,

\[
\sum_U\mu_U(\mu_U-1)
\ge T\left(\frac{T}{M_q}-1\right).
\tag{3.6}
\]

With the ambient full-word weight

\[
w_q^+=\frac1{\lfloor W/M_q\rfloor},
\]

one has

\[
w_q^+\sum_U\mu_U(\mu_U-1)
\ge
\frac{T^2}{W}-\frac{TM_q}{W}.
\tag{3.7}
\]

In particular, if

\[
q=H=\lfloor\sqrt m\,\omega(m)\rfloor,
\qquad
\omega\to\infty,
\qquad
H=o(m),
\]

then the right side of (3.7) is \((1-o(1))W\), while the strict
Proposition 7.2 incidence is identically zero.

#### Proof

Fix one token with edge \(S\subset Y\), predecessor \(d=Y\setminus S\),
and phase pair \(A\). The set \(Q_A\setminus Y\) has \(m-1\) coordinates.
Discard the pair class containing \(d\). Among the remaining coordinates
there are at least

\[
\left\lfloor\frac{m-2}{2}\right\rfloor
\]

distinct priority-pair classes. Choose the \(q\) upper suffix coordinates
from distinct such classes. Then

\[
D=(Y\setminus S)\cup(U_q\setminus Y)
\]

contains at most one coordinate from every priority pair. The cyclic order
can be completed inside \(Q_A\), giving a literal orbit token with the same
central edge and phase. Perform this independently at every root. Central
matching legality is unchanged.

Every occurrence is now ineligible for the strict chart. On the other hand,
\(\sum_U\mu_U=T\), so Cauchy gives

\[
\sum_U\mu_U^2\ge\frac{T^2}{M_q},
\]

which is (3.6). Since

\[
\frac1{\lfloor W/M_q\rfloor}\ge\frac{M_q}{W},
\]

(3.7) follows.

At upper depth \(q\), complementation gives

\[
\frac{M_q}{W}
=\prod_{j=1}^{q-1}\frac{m+1-j}{m+1+j}
\le
\exp\left(-\frac{q(q-1)}{m+1}\right).
\tag{3.8}
\]

Thus \(M_H/W=o(1)\), while \(T/W=m/(m+2)=1-o(1)\), proving the final
claim. \(\square\)

The re-lifting in Theorem 3.3 generally destroys the audited low-run trace
and need not stay in the originally chosen fixed local factors. Therefore
it refutes a theorem whose hypotheses contain only the collision profile;
it does not refute a theorem which uses the full fixed-factor low-run trace.

## 4. The owner-preserving late-pair atlas

The preceding obstruction is specific to the strict chart, which chooses
its partner in \(U_q\setminus S\) and changes the middle owner. At
\(q\ge2\), the partner can instead be chosen wholly after the middle owner.

### Theorem 4.1 (rootwise owner-preserving spike atlas)

Fix

\[
2\le q\le J\le m-2
\]

and one omitted pair \(A\). Let \(\mathcal T\) be any collection of
phase-\(A\) tokens with distinct lower roots and distinct middle owners.
For \(e\in\mathcal T\), put

\[
R_q(e)=U_q(e)\setminus Y(e).
\]

Choose any pair

\[
B_e\in\binom{R_q(e)}2
\]

and let \(\theta_e\) exchange \(A\) with \(B_e\), coordinatewise. Then:

1. \(\theta_e\) fixes the lower root, middle owner, and every lower flag;
2. arbitrary rootwise choices between \(e\) and \(\theta_e e\) form a
   lower-saturating, middle-simple matching with exactly the original owner
   map;
3. for distinct tokens \(e,f\) and every upper depth \(p\),
   \[
   \langle(d_e)_p^+,(d_f)_p^+\rangle\ge0;
   \tag{4.1}
   \]
4. if \(U_q(e)=U_q(f)\), then
   \[
   \langle d_e,d_f\rangle
   \ge w_q^+.
   \tag{4.2}
   \]

Consequently, for a depth-\(q\) spike of load \(s\),

\[
\boxed{
\mathfrak A-\mathfrak V\ge s(s-1)w_q^+.}
\tag{4.3}
\]

Fair independent component bits have curvature credit at least

\[
\boxed{\frac{s(s-1)}4w_q^+.}
\tag{4.4}
\]

relative to the average of the two coherent endpoint quadratic energies.

#### Proof

By (1.1), \(|R_q(e)|=q\), so the choice of \(B_e\) is possible exactly
because \(q\ge2\). Both \(S(e)\) and \(Y(e)\) avoid \(A\cup B_e\). Thus
\(\theta_e\) fixes both central endpoints. Every lower flag is a subset of
\(S(e)\), so it too is fixed. This proves the first two assertions.

At a fixed upper depth, write

\[
(d_e)_p^+
=\mathbf e_{\theta_eU_p(e)}-\mathbf e_{U_p(e)}.
\]

If \(U_p(e)\) avoids \(B_e\), this vector is zero. Otherwise its image
meets \(A\), whereas every old phase-\(A\) target avoids \(A\). Hence both
mixed old/image equalities are impossible. For two nonzero innovations,

\[
\langle(d_e)_p^+,(d_f)_p^+\rangle
=\mathbf1_{\{U_p(e)=U_p(f)\}}
+\mathbf1_{\{\theta_eU_p(e)=\theta_fU_p(f)\}}
\ge0.
\tag{4.5}
\]

At depth \(q\), both coordinates of \(B_e\) have entered \(U_q(e)\). If
the old targets coincide, the first indicator in (4.5) equals one. Summing
with positive weights proves (4.1)--(4.2). Finally

\[
\mathfrak A-\mathfrak V
=2\sum_{e<f}\langle d_e,d_f\rangle,
\]

which gives (4.3), and the standard fair-cube identity gives (4.4).
\(\square\)

This theorem is per phase. Across two different omitted pairs \(A,A'\), an
image from one phase can equal an old target from the other and create a
negative mixed term. Also, if one insists on one preselected exact factor
\(F_B\) for every omitted pair \(B\), then the relation

\[
F_B=\theta_{A,B}F_A
\]

can be imposed simultaneously for all partners of one source phase \(A\),
but generally not for several source phases at once. In the orbit-token
formulation every displayed row is literal; global fixed-factor
compatibility remains a separate condition.

### Theorem 4.2 (legal interval packetization and exact packet count)

Consider one selected physical run of length \(\ell\) in a phase-\(A\)
row. Partition it into consecutive blocks of length at most \(q-1\). For
each block choose a common pair

\[
B\subseteq\bigcap_{e\text{ in the block}}R_q(e)
\]

and switch the whole block to the same paired row in
\(\theta_{A,B}F_A\). Then arbitrary packet-side choices are integral,
lower-saturating, and middle-simple. Each selected packet adds at most two
selected-row runs and at most four raw \(0/1\) boundaries.

For every pair \(B\) which is reused, fix one coordinatewise orientation
\(\theta_{A,B}\) globally and use the one factor
\(F_B=\theta_{A,B}F_A\). Different orientations for repeated uses of the
same \(B\) are not included in the theorem.

If a phase contains \(N_A\) selected tokens in \(J_A\) source runs, the
number of packets satisfies

\[
\boxed{
K_{A,q}\le\frac{N_A}{q-1}+J_A.}
\tag{4.6}
\]

For the depth-\(q\) load profile of these tokens,

\[
\boxed{
\mathfrak A-\mathfrak V
\ge
w_q^+\sum_U\mu_{A,q,U}(\mu_{A,q,U}-1).}
\tag{4.7}
\]

#### Proof

The future sets \(R_q(i)\) are consecutive cyclic \(q\)-windows. For
\(t\le q-1\) consecutive starts,

\[
\left|\bigcap_{j=0}^{t-1}R_q(i+j)\right|=q-t+1\ge2.
\tag{4.8}
\]

Choose \(B\) in this intersection. Theorem 4.1 fixes every central endpoint
in the block. The old and paired rows have the same orientation, so this is
an orientation-preserving interval packet of the audited kind. Removing one
interval from the old row and inserting one interval in the paired row
increases the selected-run count by at most two and the raw boundary count
by at most four.

A run of length \(\ell\) uses at most

\[
\left\lceil\frac{\ell}{q-1}\right\rceil
\le\frac{\ell}{q-1}+1
\]

packets. Summing over source runs gives (4.6).

All cross-token Gram entries are nonnegative by (4.5). Two equal
depth-\(q\) upper targets cannot arise at different starts of one physical
row, because \(U_q\) is a proper cyclic window. Hence every unordered
collision pair lies in two different packets and contributes at least
\(w_q^+\) to their packet Gram. Multiplying by two gives (4.7). \(\square\)

For fair packet bits, (4.7) gives the exact certified aggregate ledger

\[
G_{A,q}
\ge
\frac{w_q^+}{4}
\sum_U\mu_{A,q,U}(\mu_{A,q,U}-1),
\qquad
B_{A,q}^{\rm run}\le2K_{A,q}.
\tag{4.7a}
\]

Thus the certified credit per charged selected-row run is at least

\[
\frac{w_q^+
\sum_U\mu_{A,q,U}(\mu_{A,q,U}-1)}
{8K_{A,q}}.
\tag{4.7b}
\]

For one isolated spike of load \(s\), this has order \(s w_q^+\): the
curvature is quadratic in \(s\), while the occurrence/packet charge is
linear. This is the precise sense in which heavy spikes remain viable even
though dispersed bounded loads fail the packet-capacity test below.

### Theorem 4.3 (sharp interval-capacity obstruction)

Within the owner-preserving common-partner interval family, a nontrivial
packet has length at most \(q-1\). Consequently any such atlas which touches
\(T_0\) roots has

\[
\boxed{K\ge\frac{T_0}{q-1}.}
\tag{4.9}
\]

If \(q\le H\) and \(K=o(W/H)\), then

\[
\boxed{T_0=o(W).}
\tag{4.10}
\]

#### Proof

A common partner must be contained in every future set of its packet. The
intersection in (4.8) has size \(q-t+1\), so it can contain a pair only if
\(t\le q-1\). This bound is attained when \(t=q-1\). Summing packet lengths
gives (4.9). Finally

\[
T_0\le(q-1)K\le HK=o(W),
\]

which is (4.10). \(\square\)

Thus arbitrary-profile packing fails for this repaired family whenever a
positive density of bounded-load spikes must be changed. The obstruction is
not merely formal: such integral profiles exist.

### Proposition 4.4 (literal positive-density doubleton profile)

Let

\[
q_m=\left\lfloor\frac{\sqrt m}{4}\right\rfloor.
\]

For all sufficiently large \(m\), there is a full lower-saturating orbit
token matching whose depth-\(q_m\) upper loads are at most two and for which
at least

\[
T-\binom{n}{m+q_m}
=\left(1-e^{-1/16}+o(1)\right)W
\tag{4.11}
\]

targets have load two.

#### Proof

Start with any matching saturating the lower rank in the central inclusion
graph, and let \(\mathcal Y\) be its \(T\) used middle owners. Join
\(Y\in\mathcal Y\) to every \((m+q_m)\)-set \(U\supset Y\). The left
degree is

\[
\ell_q=\binom{m+1}{q},
\]

and the degree of a right target in the full owner layer is

\[
r_q=\binom{m+q}{q}.
\]

For every \(\mathcal X\subseteq\mathcal Y\), edge counting gives

\[
\ell_q|\mathcal X|\le r_q|N(\mathcal X)|.
\]

Moreover

\[
\log\frac{r_q}{\ell_q}
=\sum_{i=1}^{q}
\log\frac{m+i}{m+2-i}
\le\frac{q(q-1)}{m+2-q}<\log2
\]

for \(q=q_m\) and all sufficiently large \(m\). Thus

\[
2|N(\mathcal X)|\ge|\mathcal X|.
\]

Capacitated Hall assigns every used owner to an upper target, with target
capacity two. Lift each central token edge to a literal row having its
assigned \(U_q\); this preserves the central matching.

If \(a\) targets have load two and \(b\) have load one, then

\[
2a+b=T,
\qquad
a+b\le\binom{n}{m+q}.
\]

Therefore \(a\ge T-\binom{n}{m+q}\). Finally

\[
\frac1W\binom{n}{m+q_m}
\longrightarrow e^{-1/16},
\qquad
\frac TW\longrightarrow1,
\]

because, with \(r=q_m-1\),

\[
-\log\left(\frac1W\binom{n}{m+q_m}\right)
=2\sum_{k=1}^{r}\operatorname{artanh}\frac{k}{m+1}
=\frac{r(r+1)}{m+1}+o(1)
\longrightarrow\frac1{16}.
\]

This proves (4.11). \(\square\)

For \(H=\sqrt m\,\omega(m)\), one has \(q_m/H\to0\). Repairing all the
doubletons in Proposition 4.4 with the late-pair interval family requires
touching at least one root per doubleton. Theorem 4.3 therefore forces
\(\Omega(W/q_m)\) packets, which is \(\omega(W/H)\). This is a literal
arbitrary-profile obstruction for that family, not for every conceivable
switch language. As in Theorem 3.3, the constructed profile is not asserted
to have the special first-avoided low-run trace.

In fact the ambient floor at this depth is eventually one, because

\[
\frac{W}{\binom{n}{m+q_m}}\longrightarrow e^{1/16}<2.
\]

Thus the displayed doubletons carry \(\Theta(W)\) floor-weighted collision.
Reducing it to \(o(W)\) with this family requires touching
\(\Theta(W)\) roots, so the same packet lower bound remains necessary even
when exact elimination of every last doubleton is not demanded.

## 5. Exact owner capacity for the original owner-changing charts

Let \(M\) be a matching saturating every lower root, and write

\[
\mathcal F
=\binom{[n]}m\setminus\operatorname{im}M
\]

for its free middle owners.

### Lemma 5.1 (free-owner capacity)

The free set has exact size

\[
\boxed{
|\mathcal F|=W-T=\frac{2W}{m+2}.}
\tag{5.1}
\]

Suppose owner-changing components are to be independently switchable while
the background is frozen. Then every alternate owner must lie in
\(\mathcal F\), and distinct components must have distinct alternate owners.
Thus at most \(2W/(m+2)\) components can be packed.

#### Proof

The count follows from \(T/W=m/(m+2)\). If an alternate owner is used by a
background edge, the cube corner which switches only that component has a
middle collision. If two components share an alternate owner, the corner
which switches both has a collision. These are also sufficient obstructions
for disjoint two-owner supports. \(\square\)

Alternating paths and cycles can evade Lemma 5.1 by displacing the owner
currently occupying an alternate target. But that requires the directed
owner-incidence graph, which is absent from the collision load vector. It is
the exact dynamic-fusion term.

More generally, if a chart \(\mathcal C\) has alternate-owner set
\(A_{\mathcal C}\), every owner-disjoint chart selection satisfies the
capacity inequalities

\[
\sum_{\mathcal C:z\in A_{\mathcal C}}x_{\mathcal C}\le1
\qquad(z\in\tbinom{[n]}m).
\tag{5.2}
\]

The next construction shows that these inequalities are not controlled by
the spike loads.

### Proposition 5.2 (many individually legal charts with one common owner bottleneck)

Assume

\[
2\le q\le m/3,
\qquad
t=\lfloor m/3\rfloor.
\]

In the coordinate-symmetric orbit token system there is a full
lower-saturating matching with distinct load-two spikes

\[
U_1,\ldots,U_t
\]

such that every spike individually admits a strict \(s=2\) chart, every
such chart is an exact lower-saturating switch, but all \(t\) charts have
the same two alternate owners. Hence at most one chart can be selected.

#### Proof

Choose distinct fixed priority pairs

\[
B,C,E,A_1,\ldots,A_t
\]

and \(q-1\) further pairs. This is possible for the stated range once \(m\)
is sufficiently large. Choose an \(m\)-set \(Z\) which contains the
singleton and both coordinates of \(C\), avoids \(B\cup E\), contains one
coordinate \(a_i\) of every \(A_i\), contains one coordinate \(x_j\) of
every further pair, and splits all remaining pairs. Put

\[
Q=\{x_1,\ldots,x_{q-1}\},
\qquad
R=\{\text{the mates of }x_1,\ldots,x_{q-1}\}.
\]

For each \(i\), define

\[
S_i=Z\setminus\{a_i\},
\qquad
U_i=S_i\cup B\cup R,
\]

and

\[
T_i=U_i\setminus(C\cup Q).
\tag{5.3}
\]

Then \(|S_i|=|T_i|=m-1\), \(|U_i|=m+q\), and the two missing sets are

\[
U_i\setminus S_i=B\cup R,
\qquad
U_i\setminus T_i=C\cup Q.
\tag{5.4}
\]

Their only full priority pairs are respectively \(B\) and \(C\). Both
lower roots avoid \(A_i\). Choose predecessors \(b_i\in B\) and
\(c_i\in C\), with the fixed coordinatewise swaps
\(A_i\leftrightarrow B\) and \(A_i\leftrightarrow C\) sending
\(b_i,c_i\) to \(a_i\). The old owners are

\[
Y_i=S_i\cup\{b_i\},
\qquad
X_i=T_i\cup\{c_i\}.
\]

They are all distinct. The two alternate owners are

\[
Z
\quad\text{and}\quad
Z'=(Z\setminus(C\cup Q))\cup B\cup R,
\tag{5.5}
\]

independently of \(i\).

Prescribe these \(2t\) old central edges and forbid \(Z,Z'\). Since

\[
2t+2\le m+1,
\]

Lemma 3.1 extends them to a full matching which leaves \(Z,Z'\) free.
Lift residual edges with depth-\(q\) targets outside
\(\{U_1,\ldots,U_t\}\). This is possible because every middle owner has
\(\binom{m+1}{q}>t\) rank-\((m+q)\) supersets, while every such target has
complement size at least two. Thus every displayed spike has exact load two.

Switching either displayed chart replaces its two old owners by the two free
owners \(Z,Z'\), so it is an exact full matching. Switching two charts would
use both \(Z\) and \(Z'\) twice. Hence (5.2) permits at most one chart.
\(\square\)

Each displayed \(s=2\) chart has strict coherent-minus-independent
curvature

\[
2C_{q,J}
\]

and fair credit \(C_{q,J}/2\). Without owner conflicts the \(t\) charts
would therefore supply \(2tC_{q,J}\) curvature and \(tC_{q,J}/2\) fair
credit. The exact owner constraints reduce these figures to
\(2C_{q,J}\) and \(C_{q,J}/2\).

The construction fixes the coordinatewise orientations of the displayed
orbit tokens. It does not prove that all source/partner relations can be
realized simultaneously by one globally preselected family of local factors
\(F_P\). Its certified conclusion is an orbit-token owner-capacity
obstruction. The \(O(m)\) displayed singleton rows are negligible compared
with \(W/H\), so this finite obstruction is purely an owner obstruction,
not a boundary obstruction. Its total curvature is sublinear in \(W\), and
it is not by itself a constant-one lower bound.

### Corollary 5.3 (background-hole curvature ceiling at depth two)

At a minimum-partner depth-two profile, every strict chart has size at most
two. If all owner-changing components must use the frozen background holes,
then the total strict-chart curvature is at most

\[
\frac{2W}{m+2}C_{2,J},
\tag{5.6}
\]

and the total fair credit is at most

\[
\frac{W}{2(m+2)}C_{2,J}.
\tag{5.7}
\]

In particular, if \(J=o(m)\), then both are \(o(W)\).

#### Proof

By (2.4), \(s\le2\) at a minimum-partner depth-two spike. Every nontrivial
chart therefore consumes two alternate owners and has curvature
\(2C_{2,J}\). Lemma 5.1 supplies at most \(2W/(m+2)\) alternate owners, so
there are at most \(W/(m+2)\) charts. This gives (5.6), and division by four
gives (5.7). Since every reciprocal floor weight is at most one,
\(C_{2,J}\le J\), proving the last assertion. \(\square\)

## 6. Floor-correct curvature per boundary

Define, for \(0\le r\le m-1\),

\[
N_r=\binom{n}{m-r},
\qquad
d_r=\left\lfloor\frac{W}{N_r}\right\rfloor,
\qquad
\rho_r=\frac{N_r}{W}.
\tag{6.1}
\]

An upper flag of size \(m+p\) has the same rank cardinality as rank
\(m-(p-1)\), so its ambient full-word reciprocal floor weight is

\[
w_p^+=\frac1{d_{p-1}}.
\tag{6.2}
\]

This is the ambient coefficient-one weight, not the autonomous token-core
floor. For the token core of mass \(T\), the first upper floor is zero; no
reciprocal token-core weight is used here.

For a chart beginning at depth \(q\) and followed through depth \(J\), put

\[
C_{q,J}=\sum_{p=q}^{J}\frac1{d_{p-1}}.
\tag{6.3}
\]

The maximal size allowed by the disjoint-missing-set construction is

\[
s_q
=\left\lfloor\frac{m+q}{q+1}\right\rfloor
=1+\left\lfloor\frac{m-1}{q+1}\right\rfloor.
\tag{6.4}
\]

This is an existential designer maximum. Sections 2 and 3 show that an
existing profile may support fewer components or none.

For this maximal synthetic chart, abbreviate

\[
E_{q,J}:=(s_q-1)C_{q,J}.
\tag{6.4a}
\]

### Proposition 6.1 (exact certified strict-chart efficiency)

For a legal exact owner-disjoint strict chart of size \(s\),

\[
\Delta_{q,J}=s(s-1)C_{q,J}
\tag{6.5}
\]

is the coherent-minus-independent curvature, and fair independent bits have
credit

\[
G_{q,J}=\frac14s(s-1)C_{q,J}.
\tag{6.6}
\]

The chart has certified charges

\[
B_{\rm run}\le2s,
\qquad
B_{\rm raw}\le4s.
\tag{6.7}
\]

At \(s=s_q\), the corresponding guaranteed credits per charged run and per
raw boundary are

\[
\frac{(s_q-1)C_{q,J}}8
\quad\text{and}\quad
\frac{(s_q-1)C_{q,J}}{16}.
\tag{6.8}
\]

For a chart \(\mathcal C\) of size \(s_{\mathcal C}\), define

\[
E_{\mathcal C}
=(s_{\mathcal C}-1)C_{q_{\mathcal C},J}.
\]

If

\[
E_{\mathcal C}\ge R
\qquad\text{for every selected chart},
\]

then

\[
B_{\rm run}\le\frac8R\sum_{\mathcal C}G_{\mathcal C},
\qquad
B_{\rm raw}\le\frac{16}{R}\sum_{\mathcal C}G_{\mathcal C}.
\tag{6.9}
\]

Thus activated curvature of order \(W\) has \(o(W/H)\) certified boundary
charge whenever \(R/H\to\infty\).

#### Proof

Equations (6.5)--(6.6) are (1.3) summed over unordered component pairs.
Each component removes at most one singleton interval from its old row and
inserts at most one in its alternate row, giving (6.7). Equations
(6.8)--(6.9) are algebraic rearrangements. \(\square\)

The word ``credit'' is essential. The fair-cube identity is

\[
\mathbb E\mathcal Q(M_{\boldsymbol\epsilon})
=\frac{\mathcal Q(M_0)+\mathcal Q(M_1)}2
-\frac14(\mathfrak A-\mathfrak V).
\tag{6.10}
\]

Without control of the coherent endpoint gap
\(\mathcal Q(M_1)-\mathcal Q(M_0)\), positive curvature alone does not prove
descent from \(M_0\). The rankwise energy-flat endpoint hypothesis used in
the audited adjacent-priority packet cube is absent here.

### Lemma 6.2 (exact capacity-weight bounds)

For every \(r\),

\[
\rho_r
=\prod_{k=1}^{r}\frac{m+1-k}{m+1+k},
\qquad
\rho_r\le\frac1{d_r}\le2\rho_r,
\tag{6.11}
\]

and

\[
-\log\rho_r
=2\sum_{k=1}^{r}
\operatorname{artanh}\frac{k}{m+1}.
\tag{6.12}
\]

Consequently

\[
\exp\left[
-\frac{r(r+1)}{m+1}
\frac1{1-(r/(m+1))^2}
\right]
\le\rho_r
\le
\exp\left[-\frac{r(r+1)}{m+1}\right].
\tag{6.13}
\]

#### Proof

The product is the exact ratio of adjacent binomial coefficients. Since
\(d_r=\lfloor1/\rho_r\rfloor\) and \(x/2\le\lfloor x\rfloor\le x\) for
\(x\ge1\), (6.11) follows. Taking logarithms of
\((1-x)/(1+x)\) gives (6.12). Finally

\[
x\le\operatorname{artanh}x
\le\frac{x}{1-x^2}
\]

and summation give (6.13). \(\square\)

### Theorem 6.3 (the unbuffered terminal term)

Let

\[
H=\lceil\sqrt m\,\omega(m)\rceil,
\qquad
\omega\to\infty,
\qquad
H=o(m).
\]

With \(J=H\),

\[
C_{H,H}=\frac1{d_{H-1}}
\]

and

\[
\boxed{
\frac{E_{H,H}}H
\le
\frac{2m}{H(H+1)}
\exp\left[-\frac{(H-1)H}{m+H}\right]
\longrightarrow0.}
\tag{6.14}
\]

If in addition \(H^3/m^2=o(1)\), then more precisely,

\[
\frac{E_{H,H}}H
=(1+o(1))\frac{e^{-\omega^2}}{\omega^2}.
\tag{6.15}
\]

Under only the displayed hypotheses of the theorem, the always-valid form is

\[
\frac{E_{H,H}}H
=\frac1{\omega^2}
\exp\bigl(-(1+o(1))\omega^2\bigr).
\tag{6.15a}
\]

Thus the unbuffered Proposition 7.2 component ledger does not certify a
uniform super-\(H\) curvature-per-boundary ratio through its terminal depth.

#### Proof

From (6.4),

\[
s_H-1\le\frac{m}{H+1}.
\]

Equations (6.11) and (6.13), with \(r=H-1\), give

\[
\frac1{d_{H-1}}
\le2\exp\left[-\frac{(H-1)H}{m+H}\right].
\]

Multiplying and dividing by \(H\) proves (6.14). The hypotheses imply the
standard relative-exponent expansion

\[
\rho_{H-1}=\exp\bigl(-(1+o(1))H^2/m\bigr),
\]

and the floor is asymptotically negligible because
\(1/\rho_{H-1}\to\infty\). Together with
\(s_H-1=(1+o(1))m/H\), this gives (6.15a). If
\(H^3/m^2=o(1)\), the additive error in the logarithm is \(o(1)\), which
gives (6.15). \(\square\)

Theorem 6.3 is a failure of this certified finite-horizon ledger, not a
lower bound on every possible physical grouping.

### Theorem 6.4 (a natural buffer repairs the numerical ledger)

Fix \(a>0\), and assume

\[
e^{\omega^2}\omega^3=o(\sqrt m).
\tag{6.16}
\]

Put

\[
J=H+\left\lfloor a\frac mH\right\rfloor.
\tag{6.17}
\]

Then \(J\le m-2\) eventually, \(J=(1+o(1))H\), and

\[
\boxed{
\frac{\min_{2\le q\le H}E_{q,J}}H
=(1+o(1))
\frac{1-e^{-2a}}2
\frac{\sqrt m\,e^{-\omega^2}}{\omega^3}
\longrightarrow\infty.}
\tag{6.18}
\]

Consequently the strict-chart curvature ledger, conditional on exact legal
activation and endpoint-gap control, is quantitatively strong enough for
\(o(W/H)\) boundaries at every target depth \(2\le q\le H\).

Here ``strict chart'' means the synthetic Proposition 7.2 chart with all of
its occurrences aligned on the prescribed common upper tail through depth
\(J\). An arbitrary collision only at depth \(q\) guarantees the single
\(w_q^+\) Gram term, not the tail sum \(C_{q,J}\).

The ranks \(H+1,\ldots,J\) are auxiliary potential ranks in this statement.
If \(J\) is promoted to the required coverage cutoff, its own top layer
\(q=J\) is unbuffered again. If they remain auxiliary, a global proof must
still control their coherent endpoint and floor-recentering terms.

#### Proof

Both \(s_q-1\) and \(C_{q,J}\) are nonincreasing in \(q\). Hence
\(E_{q,J}\ge E_{H,J}\) for \(q\le H\).

Let \(L=J-H+1\). Uniformly over this buffer, (6.11)--(6.13) and (6.16) give

\[
\frac1{d_{p-1}}
=(1+o(1))e^{-p^2/m}.
\]

Therefore the geometric Gaussian tail is

\[
C_{H,J}
=(1+o(1))
\frac{\sqrt m}{2\omega}
e^{-\omega^2}(1-e^{-2a}).
\tag{6.19}
\]

Also

\[
s_H-1=(1+o(1))\frac{\sqrt m}{\omega}.
\]

Multiply (6.19) by this last expression and divide by
\(H=(1+o(1))\sqrt m\,\omega\). This gives (6.18). Condition (6.16) makes
the right side diverge. \(\square\)

For a general terminal parameter \(q=t\sqrt m\), with \(t\to\infty\),
\(q=o(m^{3/4})\), and \(L=J-q+1\), the same calculation gives

\[
C_{q,J}
=(1+o(1))
\frac{m}{2q}e^{-q^2/m}
\left(1-e^{-2qL/m}\right),
\tag{6.20}
\]

and

\[
\frac{E_{q,J}}H
=(1+o(1))
\frac{\sqrt m}{2\omega t^2}e^{-t^2}
\left(1-e^{-2tL/\sqrt m}\right).
\tag{6.21}
\]

This displays the exact finite-tail factor omitted by an infinite-tail
heuristic.

## 7. Precise proved and conditional boundary

The following statements are proved.

1. The strict Proposition 7.2 Gram formula is correct. Its source embedding
   with deleted background edges is relaxed, but Proposition 1.1 supplies an
   exact common lower-saturating background for every single chart in the
   coordinate-orbit token model. A common fixed-factor tuple is not supplied.
2. At an existing phase-reachable spike, fixed-partition partner capacity is
   bounded by (2.3), and strict incidence may be zero even at a load-\(m\)
   spike in a full integral token matching.
3. Collision loads alone can carry \((1-o(1))W\) weighted collision while
   every strict chart is absent. This is a profile-only no-go; the example
   does not preserve the special low-run fixed-factor trace.
4. For every \(q\ge2\), the late-pair construction gives a literal,
   owner-preserving, nonnegative-Gram spike atlas within one phase.
5. Its common-partner interval packets have the sharp length ceiling
   \(q-1\). Hence \(o(W/H)\) such packets touch only \(o(W)\) roots for
   every \(q\le H\). A literal positive-density doubleton profile therefore
   lies outside this packet capacity.
6. Original owner-changing independent charts have only
   \(2W/(m+2)\) free background owners. The explicit common-bottleneck
   construction shows that even negligible boundary count does not imply
   owner-disjoint selection.
7. The unbuffered terminal strict-chart ledger is not uniformly super-\(H\).
   A buffer of length \(\Theta(m/H)\) repairs the numerical ledger for the
   synthetic charts whose occurrences share the prescribed common tails,
   under the slow-diagonal condition (6.16). An arbitrary depth-\(q\)
   collision supplies only its depth-\(q\) Gram term and need not supply this
   tail.

The following statements remain unproved and are necessary before this lane
can imply constant one.

1. A theorem exploiting the actual first-avoided low-run trace, rather than
   only its collision histogram, must show that all but \(o(W)\) relevant
   roots lie in efficiently packetizable heavy spikes, or provide a
   different long packet family.
2. Owner-changing charts which hit occupied owners must be closed into
   alternating paths/cycles. The collision profile does not determine this
   dynamic owner graph.
3. Partner factors selected from several source phases need a simultaneous
   fixed-factor compatibility theorem, or the argument must be compiled
   directly into one literal word with its full boundary ledger.
4. Positive Gram curvature must be combined with a floor-correct coherent
   endpoint comparison. Neither the strict chart nor the late-pair chart has
   the audited global energy-flat endpoint property by itself.
5. Lower flags and all other invariant sectors still require their own
   exact treatment.

Accordingly the arbitrary-profile owner-disjoint Proposition 7.2 packing
claim is false. The strongest surviving positive statement is the
owner-preserving late-pair atlas on a trace class whose active roots are
\(o(W)\) or concentrated in sufficiently heavy spikes, together with the
buffered conditional ledger of Theorem 6.4. This does not prove
\(\nu(k)\le(1+o(1))W(k)\).
