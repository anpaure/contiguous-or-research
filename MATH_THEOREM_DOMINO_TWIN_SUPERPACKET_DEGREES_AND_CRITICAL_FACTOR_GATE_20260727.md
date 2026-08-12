# Domino-twin superpackets: exact degrees, codegrees, and the critical factor gate

Date: 2026-07-27

## 0. Outcome

Let

\[
 n=2m,\qquad R=m-q_0,\qquad q_0=a\sqrt m+O(1),
\]

and restrict to the infinite parity subsequence on which \(R\) is odd.
For a labelled cyclic order \(P\), let \(P^\tau\) be obtained by swapping
the two entries in every consecutive position pair. The domino-twin
superpacket is

\[
 Q(P)=E_R(P)\,\dot\cup\,E_R(P^\tau).
\]

The two components are entrance-disjoint, so \(Q(P)\) is a \(2n=4m\)
uniform entrance edge. They share exactly \(n/2\) intervals of length
\(R-1\).

This note proves the full entrance degree and pair-codegree table of the
superpacket catalogue. With \(D^\square\) its vertex degree,

\[
 \boxed{D^\square=2nR!(n-R)!},                              \tag{0.1}
\]

\[
 \boxed{\frac{\Delta_2^\square}{D^\square}
       =\frac5{R(n-R)}=\frac{5+o(1)}{m^2},}                 \tag{0.2}
\]

and every superpacket has edge-local collision energy

\[
 \boxed{\eta^\square(Q)
 =\frac1{D^\square}\sum_{\{A,B\}\subset Q}d^\square(A,B)
 =\frac{25n}{R(n-R)}+O_a(m^{-3})
 =\frac{50+o(1)}m.}                                       \tag{0.3}
\]

Thus the twin catalogue has the same favorable *orders* as the ordinary
annular packet catalogue:

\[
 \Delta_2^\square/D^\square=\Theta(m^{-2}),\qquad
 \eta^\square=\Theta(m^{-1}).                              \tag{0.4}
\]

Under formal thinning to density \(z\), its local parameters are

\[
 \eta_z^\square=O((mz)^{-1}),\qquad
 \alpha_z^\square
 \le \frac{2n\Delta_2^\square}{D^\square z}
 =O((mz)^{-1}).                                            \tag{0.5}
\]

They are \(O(m^{-1/2})\) at \(z=m^{-1/2}\). There is no degree,
pair-codegree, edge-energy, fractional, or scalar divisibility obstruction
to a near-factor with leave \(O(N_{q_0}/\sqrt m)\).

Such a near-factor would be a genuine counterexample to the assertion that
every entrance matching automatically has
\(\sum_q\widetilde E_q=o(W)\): it would have

\[
 \widetilde E_{q_0+1}\ge(1/4-o(1))N_{q_0}=\Theta(W).       \tag{0.6}
\]

What remains open is precisely the same kind of growing-uniformity dynamic
regeneration theorem as for ordinary packets. The twin computation
therefore shows that no entrance-only theorem based on the local scales
(0.4)--(0.5) can prove the hereditary-repeat conclusion: if it is broad
enough to include this catalogue, it proves the opposite.

## 1. Labelled catalogue and the cross-position profile

Index columns by all bijections
\[
 x:\mathbb Z_n\longrightarrow[n].
\]
Put
\[
 P_x=(x_0,x_1,\ldots,x_{n-1}),
\]
and let
\[
 \tau(i)=
 \begin{cases}
 i+1,&i\text{ even},\\
 i-1,&i\text{ odd}.
 \end{cases}
\]
Then \(P_x^\tau=(x_{\tau(0)},\ldots,x_{\tau(n-1)})\). We retain all
\(n!\) labelled columns. This introduces only uniform multiplicity and
keeps every degree count literal.

For a start \(j\), write
\[
 I_j=\{j,j+1,\ldots,j+R-1\}\subset\mathbb Z_n,
\qquad
 J_j=\tau(I_j).
\]

Because \(R\) is odd,
\[
 I_j\ne J_k\quad\text{for all }j,k,
\]
and hence the two component traces of \(Q(P_x)\) are disjoint.

### Lemma 1.1 (cross intersection table)

Put \(g=n-2R>0\). For \(0\le t\le R-1\), let
\[
 c_t=|\{(j,k)\in\mathbb Z_n^2:|I_j\cap J_k|=t\}|.
\]
Then

\[
 \boxed{
 \frac{c_t}{n}=
 \begin{cases}
 g,&t=0,\\
 3,&t=1\text{ or }t=R-1,\\
 2,&2\le t\le R-2.
 \end{cases}}                                             \tag{1.1}
\]

#### Proof

Write \(R=2r+1\). If \(k\) is even, then
\[
 J_k=[k,k+R-2]\cup\{k+R\};
\]
if \(k\) is odd, then
\[
 J_k=\{k-1\}\cup[k+1,k+R-1].
\]
Fixing the parity of \(j\), move \(k-j\) once around the circle. For
ordinary overlap sizes \(2,\ldots,R-2\), the left and right approaches
give two relative starts. At overlap \(1\) and \(R-1\), the displaced
singleton supplies one additional relative start. There are \(g\) starts
with zero intersection. The same list occurs for each parity of \(j\).
Multiplying by the \(n\) translates gives (1.1).

As a check,
\[
 g+3+3+2(R-3)=n.
\]
\(\square\)

The ordinary within-component pair profile is:
there are \(n\) unordered pairs with intersection \(t\) for every
\(1\le t\le R-1\), and \(n(g+1)/2\) disjoint pairs.

## 2. Exact degree and pair codegree

Let
\[
 D_R=R!(n-R)!
\]
be the degree of an \(R\)-target in the directed cyclic-order catalogue
modulo rotation, and let
\[
 \lambda_R(t)=
 \begin{cases}
 R!^2(g+1)!,&t=0,\\
 2(R-t)!^2t!(g+t)!,&1\le t\le R-1
 \end{cases}                                               \tag{2.1}
\]
be its ordinary pair codegree.

### Theorem 2.1 (superpacket degree)

Every \(R\)-target has degree
\[
 D^\square=2nD_R.                                         \tag{2.2}
\]

#### Proof

For one component, a fixed target is an interval in \(nD_R\) full
labellings: choose its unique start, then label the inside and outside.
It cannot occur in both components because the two traces are disjoint.
The two components therefore contribute \(2nD_R\). \(\square\)

### Theorem 2.2 (full pair-codegree table)

Let \(A,B\) be distinct \(R\)-sets and put \(t=|A\cap B|\). For
\(1\le t\le R-1\), define
\[
 a_t=
 \begin{cases}
 3,&t=1\text{ or }t=R-1,\\
 2,&2\le t\le R-2.
 \end{cases}
\]
Then

\[
 d^\square(A,B)=
 \begin{cases}
 2n\,\dfrac{2g+1}{g+1}\,\lambda_R(0),&t=0,\\[3mm]
 n(2+a_t)\lambda_R(t),&1\le t\le R-1.
 \end{cases}                                               \tag{2.3}
\]

Equivalently,

\[
 \frac{d^\square(A,B)}{D^\square}
 =
 \begin{cases}
 \dfrac{2g+1}{g+1}\,\dfrac{\lambda_R(0)}{D_R},&t=0,\\[3mm]
 \dfrac{2+a_t}{2}\,\dfrac{\lambda_R(t)}{D_R},&1\le t\le R-1.
 \end{cases}                                               \tag{2.4}
\]

#### Proof

The two same-component choices contribute \(2n\lambda_R(t)\).

For a cross-component choice, fix starts \(j,k\). If the two position
sets have intersection \(t\), the number of labellings realizing
\(A,B\) on them is
\[
 f_t=t!(R-t)!^2(n-2R+t)!.
\]
Lemma 1.1 gives \(c_t\) possible start pairs. There are two cross
orientations.

For \(t>0\), \(\lambda_R(t)=2f_t\), so the two cross orientations
contribute \(n a_t\lambda_R(t)\). For \(t=0\),
\[
 \lambda_R(0)=(g+1)f_0,
\]
and the two cross orientations contribute
\[
 2ngf_0=\frac{2ng}{g+1}\lambda_R(0).
\]
Adding the same-component contribution proves (2.3), and division by
(2.2) proves (2.4). \(\square\)

### Corollary 2.3 (maximum pair codegree)

For \(q_0=a\sqrt m+O(1)\),
\[
 \frac{\Delta_2^\square}{D^\square}
 =\frac5{R(n-R)}=\frac{5+o(1)}{m^2}.                      \tag{2.5}
\]

#### Proof

At \(t=R-1\),
\[
 \frac{\lambda_R(R-1)}{D_R}=\frac2{R(n-R)}
\]
and \(a_{R-1}=3\), giving (2.5). As in the ordinary packet catalogue,
the \(t=1\) and disjoint endpoints are
\(\exp[-\Omega_a(\sqrt m\log m)]\) smaller, while the interior sequence
is log-convex toward its endpoints. \(\square\)

## 3. Edge-local collision energy

Inside one superpacket, let \(b_t\) be the number of unordered target
pairs with intersection \(t\). The two within-component profiles and
Lemma 1.1 give

\[
 b_t=
 \begin{cases}
 n(2g+1),&t=0,\\
 n(2+a_t),&1\le t\le R-1.
 \end{cases}                                               \tag{3.1}
\]

The check
\[
 \sum_{t=0}^{R-1}b_t=\binom{2n}{2}
\]
is immediate.

### Theorem 3.1 (exact leading collision energy)

\[
 \eta^\square(Q)
 :=\frac1{D^\square}\sum_{\{A,B\}\subset Q}d^\square(A,B)
 =\frac{25n}{R(n-R)}+O_a(m^{-3}).                         \tag{3.2}
\]

#### Proof

The \(t=R-1\) term equals
\[
 b_{R-1}\frac{d^\square(R-1)}{D^\square}
 =5n\cdot\frac5{R(n-R)}
 =\frac{25n}{R(n-R)}.
\]
The \(t=R-2\) term is \(O(m^{-3})\); successive interior terms decrease
by two further powers until the opposite endpoint. The \(t=1\) and
disjoint terms are superpolynomially small in the Gaussian regime.
\(\square\)

## 4. Small-order higher spread

For two members of one superpacket, use Johnson distance
\[
 \partial(A,B)=R-|A\cap B|.
\]

### Lemma 4.1 (balls in a twin superpacket)

For \(1\le h\le R-2\), every Johnson ball of radius \(h\), intersected
with one superpacket, has at most
\[
 4h+2                                                   \tag{4.1}
\]
vertices.

#### Proof

In the same component cycle there are at most \(2h+1\) vertices within
distance \(h\), including the centre. In the opposite component,
Lemma 1.1 gives three vertices at distance one and two at every further
distance through \(h\), hence at most \(2h+1\). Their union has at most
\(4h+2\) vertices. \(\square\)

### Corollary 4.2 (higher codegree)

Let \(j\ge7\), and put
\[
 h_j=\left\lfloor\frac{j-3}{4}\right\rfloor.
\]
Any \(j\) distinct vertices contained in one superpacket include a pair
at Johnson distance at least \(h_j+1\). Consequently

\[
 \frac{\Delta_j^\square}{D^\square}
 \le
 \frac5{\binom R{h_j+1}\binom{n-R}{h_j+1}}.                \tag{4.2}
\]

#### Proof

Fix one of the \(j\) vertices. If all the others were at distance at most
\(h_j\), Lemma 4.1 would give \(j\le4h_j+2\), contrary to the definition
of \(h_j\). Apply (2.4) to the resulting pair; the multiplier relative to
the ordinary equal-rank codegree is at most \(5/2\). \(\square\)

This is the same factorial small-order spread mechanism as for one
ordinary packet, with only a constant loss.

## 5. Slow-bite scales

The superpacket rank is
\[
 K^\square=2n=4m.
\]
For a fixed superpacket \(Q\), let \(c(Q)\) be the number of other
superpackets meeting it. As usual,

\[
 K^\square D^\square-D^\square\eta^\square(Q)
 \le c(Q)+1\le K^\square D^\square.                       \tag{5.1}
\]

Marking each column with probability
\[
 p=\frac{\gamma}{K^\square D^\square}
\]
therefore gives
\[
 \Pr(Q\text{ is isolated and retained})
 =\frac{\gamma e^{-\gamma}}{K^\square D^\square}
   \bigl(1+O_a(m^{-2})\bigr).                              \tag{5.2}
\]

Under independent thinning to vertex density \(z\),
\[
 \eta_z^\square=\frac{\eta^\square}{z}=O((mz)^{-1}),       \tag{5.3}
\]
and the maximum relative one-column influence on a surviving vertex link
is at most
\[
 \alpha_z^\square
 \le\frac{K^\square\Delta_2^\square}{D^\square z}
 =O((mz)^{-1}).                                            \tag{5.4}
\]

Both are \(O(m^{-1/2})\) at \(z=m^{-1/2}\). The residual degree remains
factorially large there.

The max-based variable-rank expression remains critical rather than
vanishing:
\[
 K^\square\frac{\Delta_2^\square}{D^\square}\log N_{q_0}
 =40\log2+o(1).                                            \tag{5.5}
\]
As for ordinary packets, the edge-local profile (3.2), not (5.5), is the
favorable statistic.

## 6. Fractional normalization and exact necessary leave ledger

Relabelling acts transitively on entrance targets and all columns have
size \(2n\). Therefore the uniform weight \(1/D^\square\) is an exact
fractional perfect matching.

Every ordinary cyclic packet contains each coordinate in exactly \(R\)
of its entrance intervals. Hence every twin superpacket contains each
coordinate in exactly \(2R\) entrance targets. If a matching of \(T\)
superpackets has leave \(\mathcal L\), then necessarily

\[
 |\mathcal L|=N_{q_0}-2nT,\qquad
 \deg_{\mathcal L}(x)=\binom{n-1}{R-1}-2RT
 =\frac{R|\mathcal L|}{n}                                  \tag{6.1}
\]
for every \(x\in[n]\).

The divisibility \(n\mid R|\mathcal L|\) is automatic, since
\(n\mid RN_{q_0}\). Thus (6.1) is the same regular-leave condition as in
the ordinary packet problem, not a new obstruction. At the target leave
scale \(N_{q_0}/\sqrt m\), regular \(R\)-uniform leave families have ample
scalar capacity.

The hypergeometric central-slice transversal also persists: every
component packet meets it, hence every twin superpacket meets it at least
twice. Its density is \(\Theta(m^{-1/2})\), so it explains why a theorem
uniform over all residuals is impossible, but it does not rule out a
trajectory stopping at the same critical density.

## 7. Exact status

Proved:

1. the twin superpacket has two entrance-disjoint ordinary packets and
   \(n/2\) common first-deeper targets;
2. exact regularity and the complete pair-codegree table;
3. maximum relative codegree \((5+o(1))/m^2\);
4. edge-local collision energy \((50+o(1))/m\);
5. factorial small-order higher spread;
6. the same formal \(z=m^{-1/2}\) slow-bite scales as ordinary packets;
7. no fractional, divisibility, or scalar leave obstruction.

Not proved:

1. dynamic regeneration of the link/mixed-diagram hierarchy for
   \(\Theta(m\log m)\) bites;
2. a near-perfect integral twin-superpacket matching;
3. therefore, a literal near-spanning counterexample to the universal
   entrance-matching implication.

The strongest exact conclusion is a dichotomy:

> Either the catalogue-specific annular slow-bite theorem fails even for
> the locally favorable twin catalogue, or entrance matching alone does
> not control hereditary repeat excess.

In particular, a proof of the positive annular programme must couple
matching with deeper-colour compensation from the first bite. Entrance
regeneration cannot be proved as a black box and then composed with the
repeat estimate.

