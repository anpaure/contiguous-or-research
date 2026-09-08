# Conveyor owner resolution: exact orbit statistics and the integral wall

Date: 2026-07-27

Scope: constant-one program; pure mathematics only.

## 0. Theorem-level outcome

Put
\[
 W=\binom{2m}{m},\qquad N=N_H=\binom{2m}{m-H},\qquad M=m+H,
\]
where \(H\) is the least integer such that
\(\lambda_H:=W/N_H\ge M\).  Thus
\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 \rho:=\frac{MN}{W}=1-O(H/m),\qquad MN=W-o(W).
\]

The owner-resolution problem is the following literal hypergraph
matching problem.  Its vertices are the rank-\(M\) tops and rank-\(m\)
middle owners.  A column is one full cyclic promotion frame: it contains
one top and its \(M\) cyclic \(m\)-windows.  Hence its growing uniformity
is
\[
 r=M+1=\Theta(m).
\]

A three-top conveyor has two shores, but both shores contain the same
three tops and the same \(3M\) owners.  Therefore the shores are parallel
columns in the owner projection.  Once a shore is signed, contracting a
bank of \(K\) disjoint conveyors deletes exactly \(3K\) tops and \(3MK\)
owners.  In particular
\[
 (W-3MK)-M(N-3K)=W-MN.                                      \tag{0.1}
\]
Thus shore choice creates no owner integrality condition and the packet
bank preserves the exact scalar slack.

The unconditioned frame hypergraph has exact degrees
\[
 D_{\rm top}=(M-1)!,\qquad
 D_{\rm own}=\binom mH m!H!,\qquad
 \frac{D_{\rm own}}{D_{\rm top}}=\rho.                       \tag{0.2}
\]
Giving every frame weight \(1/D_{\rm top}\) saturates every top and puts
load exactly \(\rho\le1\) on every owner.  This is the exact uniform
fractional point.

For two owners at Johnson distance \(d\), their codegree divided by
\(D_{\rm own}\) is
\[
 \frac{2}{\binom md^2}\quad(1\le d<H),\qquad
 \frac{m-H+1}{\binom mH^2}\quad(d=H),                        \tag{0.3}
\]
and is zero for \(d>H\).  Consequently
\[
 \frac{\Delta_2}{D_{\rm own}}=\frac2{m^2},\qquad
 r^2\frac{\Delta_2}{D_{\rm own}}=2+o(1).                    \tag{0.4}
\]
The maximum-codegree parameter is therefore exactly critical when the
uniformity is tracked.  Nevertheless the sum of normalized codegrees
over owner pairs inside one physical frame is
\[
 \frac2m+o(1),                                               \tag{0.5}
\]
so there is no pair-mass obstruction to a sharper structured nibble.
The previously proposed slow-bite trajectory is not such a proof: its
unconditional conclusion was retracted in
`MATH_AUDIT_REPAIRED_RING_BUFFERED_STOPPED_GENERATOR_ESCAPE_20260727.md`
because the dynamic repeated-edge and compensation-coin diagonal link
energies were uncontrolled.  Its surviving form assumes MDLE/ADLE.

The natural LP is genuinely nonintegral: three full promotion frames on
three distinct tops contain the literal minor
\[
 \begin{pmatrix}1&0&1\\1&1&0\\0&1&1\end{pmatrix},
\qquad |\det|=2.                                             \tag{0.6}
\]
The half-vector on these columns satisfies every top and owner capacity
row, while an integral matching selects at most one.  Thus fractional
feasibility cannot be rounded by total unimodularity or ordinary flow.
This is a local obstruction, not a macroscopic counterexample.

Finally, if \(\mathcal B\) is any occupied owner family, all but at most
\[
 \frac{\rho|\mathcal B|}{\eta}                               \tag{0.7}
\]
tops retain at least a \(1-\eta\) fraction of their cyclic-frame
catalogue.  For a dense conveyor bank,
\(|\mathcal B|=3MK\), \(K\le W/P_H\), and
\[
 P_H=9M^2+
 \left(9+256\sum_{q=1}^Hq^2\right)\frac WN
 =(256/3+o(1))MH^3.
\]
Hence the severely damaged tops have total owner capacity
\[
 \frac{3\rho M^2W}{\eta P_H}
 =O_\eta\!\left(\frac{M}{H^3}\right)W=o(W).                 \tag{0.8}
\]
The packet reservoir therefore cannot create a macroscopic zero-degree
exterior wall.

There remains one literal absorber wall: increasing the number of
covered tops by \(u\) necessarily consumes \(Mu\) previously uncovered
owners.  Deleting a packet frees three tops and exactly \(3M\) owners, so
a closed packet block cannot grow by even one top.  The shared-collar
splice theorem removes word-interface cost but creates no owner slack.

The exact surviving gate is a near-perfect integral matching in the
residual \((M+1)\)-uniform frame hypergraph.  Neither a proof nor a
linear Hall obstruction is asserted here.

## 1. Hypergraph and shore contraction

Let
\[
 \mathcal U=\binom{[2m]}M,\qquad \mathcal X=\binom{[2m]}m.
\]
For a directed cyclic order
\(\pi=(a_i:i\in\mathbb Z_M)\) on \(U\in\mathcal U\), put
\[
 \mathcal O(U,\pi)=
 \bigl\{\{a_i,a_{i+1},\ldots,a_{i+m-1}\}:i\in\mathbb Z_M\bigr\}.
\]
These are \(M\) distinct owners.  Define
\[
 e(U,\pi)=\{U\}\mathbin{\dot\cup}\mathcal O(U,\pi).
\]
The hypergraph \(\mathcal H_{m,H}\) consists of these edges.

For a packet \(P\), write \(\mathcal U(P)\) for its three tops and
\(\mathcal O(P)\) for its common \(3M\)-owner support.  Introduce a packet
selector \(s_P\).  Its shore columns are
\[
 p_P^\epsilon=
 \{s_P\}\mathbin{\dot\cup}\mathcal U(P)
 \mathbin{\dot\cup}\mathcal O(P),\qquad \epsilon\in\{0,1\}.
\]
The exact-middle conveyor theorem says these two columns are identical
in this projection.  For a top- and owner-disjoint bank, contracting one
shore column per packet therefore leaves precisely the induced ordinary
hypergraph after deleting its packet tops and owners.  This proves
(0.1) and exact separation of shore signing from owner resolution.

There is also an exact coordinate identity.  For every \(c\in[2m]\),
\[
 \sum_{X\in\mathcal O(U,\pi)}{\bf1}_{c\in X}
 =m{\bf1}_{c\in U},                                         \tag{1.1}
\]
because a coordinate in \(U\) lies in exactly \(m\) cyclic
\(m\)-windows.  Thus packet contraction preserves every degree-one
coordinate equation, shore by shore.

If a resolution leaves top set \(\mathcal L_U\) and owner set
\(\mathcal L_X\), then, with \(d_0=W-MN\),
\[
 |\mathcal L_X|=d_0+M|\mathcal L_U|,                         \tag{1.2}
\]
and
\[
 |\{X\in\mathcal L_X:c\in X\}|
 =\frac{d_0}{2}+m|\{U\in\mathcal L_U:c\in U\}|.              \tag{1.3}
\]
Indeed every coordinate occurs in \(W/2\) owners and in
\(\binom{2m-1}{M-1}=MN/(2m)\) tops; subtract (1.1) over covered frames.
Thus the bank violates neither the scalar nor the degree-one lattice.

Minimality of \(H\) gives \(d_0=o(W)\): since
\[
 \frac{\lambda_H}{\lambda_{H-1}}
 =\frac{m+H}{m-H+1}=1+O(H/m)
\]
and \(\lambda_{H-1}<M-1\), one has
\(\lambda_H=M(1+O(H/m))\).

## 2. Exact degrees and codegrees

There are \((M-1)!\) directed cyclic orders modulo rotation on a fixed
top.  A fixed owner \(X\) has \(\binom mH\) top extensions.  For a fixed
extension \(U\supset X\), exactly
\[
 \frac{M!}{\binom MH}=m!H!
\]
cyclic orders contain \(X\) as a window.  This proves (0.2); equivalently
double counting gives
\[
 ND_{\rm top}M=WD_{\rm own}.
\]

Now let \(X,Y\) have Johnson distance \(d\).  A common top exists only
for \(d\le H\), and their number is
\(\binom{m-d}{H-d}\).  In one common top put
\(B=U\setminus X\), \(C=U\setminus Y\).  For \(d<H\), the overlapping
\(H\)-sets \(B,C\) are both cyclic intervals only when their starts are
separated by \(d\), in either direction.  The four consecutive regions
have sizes \(d,H-d,d,m-d\), so the number of orders is
\[
 2(d!)^2(H-d)!(m-d)!.
\]
Multiplying by the number of common tops yields
\[
 \deg(X,Y)=\frac{2(d!)^2(m-d)!^2}{(m-H)!}.                  \tag{2.1}
\]
If \(d=H\), the two complement blocks are disjoint.  Collapsing both
blocks gives
\[
 \deg(X,Y)=H!^2(m-H+1)!.                                    \tag{2.2}
\]
Since \(D_{\rm own}=m!^2/(m-H)!\), division proves (0.3)--(0.4).

Inside one frame, for each \(1\le d<H\) there are exactly \(M\)
unordered owner pairs at distance \(d\); all remaining pairs have
distance \(H\).  Therefore the physical normalized pair mass equals
\[
 2M\sum_{d=1}^{H-1}\binom md^{-2}
 +\left(\binom M2-M(H-1)\right)
   \frac{m-H+1}{\binom mH^2}
 =\frac2m+o(1),
\]
which proves (0.5).

## 3. Literal determinant-two full-frame minor

Choose disjoint sets
\[
 |C|=m-H,\qquad |A_1|=|A_2|=|A_3|=H;
\]
they fit because \(m\ge2H\).  Put
\[
 X_i=C\cup A_i,\qquad
 U_{12}=C\cup A_1\cup A_2,\quad
 U_{23}=C\cup A_2\cup A_3,\quad
 U_{31}=C\cup A_3\cup A_1.
\]
On \(U_{ij}\), choose a cyclic order in which \(A_i,A_j\) are contiguous
\(H\)-blocks, for instance the concatenation \(A_i,A_j,C\).  Complements
of these two \(H\)-blocks are \(X_j,X_i\), so the frame on \(U_{ij}\)
contains exactly the two displayed owners among \(X_1,X_2,X_3\).
The three columns therefore induce (0.6).

No owner occurs in all three columns, since it would be an \(m\)-subset
of
\[
 U_{12}\cap U_{23}\cap U_{31}=C,
\]
but \(|C|=m-H\).  Thus the half-vector loads every owner by at most one;
the three top selectors are distinct and have load \(1/2\).  Every pair
of columns shares one \(X_i\), so an integral matching selects at most
one.  This proves both non-TU and the claimed local integrality gap.

## 4. The reservoir cannot kill linearly many catalogues

For an occupied owner family \(\mathcal B\), write
\[
 b_U=|\mathcal B\cap\binom Um|.
\]
Every forbidden owner in a fixed top occurs in \(m!H!\) of its
\((M-1)!\) frames.  Hence at least
\[
 (M-1)!-b_Um!H!
 =(M-1)!\left(1-\frac{b_U}{\tau}\right),\qquad
 \tau=\frac{\binom MH}{M},                                  \tag{4.1}
\]
frames survive.  In particular, losing more than an \(\eta\) fraction
requires \(b_U\ge\eta\tau\).

Every owner is contained in exactly \(\binom mH\) tops, so
\[
 \sum_U b_U=|\mathcal B|\binom mH.
\]
The number of \(\eta\)-severe tops is therefore at most
\[
 \frac{|\mathcal B|\binom mH}{\eta\tau}
 =\frac{\rho|\mathcal B|}{\eta},
\]
proving (0.7).  Substitution of \(|\mathcal B|=3MK\),
\(K\le W/P_H\), and
\(P_H=(256/3+o(1))MH^3\) proves (0.8).

## 5. Exact closed-absorber obstruction

Every ordinary frame uses \(M\) owners per top; every conveyor packet
uses \(3M\) owners per three tops.  Thus any owner-disjoint family
satisfies
\[
 \#\{\text{covered owners}\}
 =M\,\#\{\text{covered tops}\}.                              \tag{5.1}
\]
If an augmentation deletes a block covering \(r\) tops and \(Mr\)
owners, then replaces it while covering \(r+u\) tops, it needs
\(M(r+u)\) owners.  If only the freed owners and \(E\) previously
uncovered owners are available, then
\[
 Mr+E\ge M(r+u),\qquad\text{hence}\qquad E\ge Mu.            \tag{5.2}
\]
This proves the literal exterior wall.  It does not preclude a global
augmentation: a matching leaving \(\ell\) tops leaves exactly
\(d_0+M\ell\) owners by (1.2).  The unresolved issue is routing that
global supply through disjoint cyclic frames.

## 6. Exact boundary

Proved here:

1. the owner-resolution hypergraph and exact shore contraction;
2. the uniform fractional point with all degrees exact;
3. the exact critical codegree parameter \(r^2\Delta_2/D_{\rm own}=2+o(1)\);
4. the sharper physical pair mass \(2/m+o(1)\);
5. a literal determinant-two triangle in three complete promotion frames;
6. only \(o(W)\) owner capacity can suffer severe catalogue loss from the
   \(W/P_H\) packet reservoir; and
7. every absorber gaining \(u\) tops must import \(Mu\) exterior owners.

Not proved:

1. a matching covering all but \(o(N)\) residual tops;
2. the MDLE/ADLE dynamic diagonal-energy estimate for a slow nibble;
3. an absorber routing the global leave;
4. a macroscopic odd-set obstruction; or
5. coefficient one.
