# From nested Hoffman flags to long locally geodesic paths: the exact port-Hall gate

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

Put

\[
 {\cal M}=\binom{[2m]}m,\qquad W=|{\cal M}|,
 \qquad 1\le H\le C_0\sqrt{m\log m}.
 \tag{0.1}
\]

The simultaneous mixed-frame face-Hall theorem and the layered Hoffman
theorem do not by themselves imply a long path cover. There is one further
integral matching layer.

There is also a prior assignment-identification gap: the polynomial
simultaneous-Hall assignment and the augmented exact-SCD/Hoffman assignment
are different integral outputs. No theorem currently transports the
former one's type-bin and collision ledgers to the latter one's nested
flags. Accordingly the formulation below minimizes over whichever
integral Hoffman-feasible state selections actually exist; it does not
silently identify those two assignments.

For fixed integral physical flag states \(x\) and a total order
\(\prec\) on the retained middle owners, form the split-copy bridge graph
\(B_\prec(x)\). Its left and right shores are copies of the owners, and
\(X_LY_R\) is an edge exactly when the state at \(X\) can be followed by
the state at \(Y\), with all length-\(H\) overlaps agreeing, and
\(X\prec Y\). Then

\[
 \boxed{
 p(x,\prec)
 =|U|-\nu(B_\prec(x))
 =\max_{{\cal S}\subseteq U}
   \bigl(|{\cal S}|-|N_{B_\prec(x)}({\cal S})|\bigr),}
 \tag{0.2}
\]

where \(U\) is the retained owner set and \(p(x,\prec)\) is the minimum
number of compatible directed paths covering \(U\). Consequently the exact
joint gate is

\[
 \boxed{
 \min_{\substack{x\ {\rm integral}\\
                 x\ {\rm Hoffman\!-\!feasible}}}
 \ \min_\prec\
 \max_{{\cal S}\subseteq U}
 \bigl(|{\cal S}|-|N_{B_\prec(x)}({\cal S})|\bigr)
 =o(W/H).}
 \tag{0.3}
\]

Hoffman's inequalities certify only that the outer feasible set in (0.3)
is nonempty. They do not imply its port-Hall inequalities.

There is a sharp explicit dual cut. Every state has an ordered exit port
\(r(\omega)\) and entrance port \(\ell(\omega)\), and every legal bridge
obeys

\[
                         r(\omega)=\ell(\eta).
 \tag{0.4}
\]

If \(R_x,L_x\) are the two port histograms, then every cover which discards
\(e\) owners and uses \(p\) paths satisfies

\[
 \boxed{
 e+p\ge {1\over2}\|R_x-L_x\|_1.}
 \tag{0.5}
\]

This cut is linearly independent of the complete layered Hoffman system.
Inside one actual balanced pair frame, the signed difference between even
and odd orders of \(H\) split directions has zero incidence in every
owner and target-throughput row at every depth, but has nonzero pairing
with (0.5).

The failure is also integral. There is a pairwise \(o(m)\)-separated
catalogue of

\[
 J=O\!\left(m^2\,4^H\exp(CH^2/m)\right)=W^{o(1)}
 \tag{0.6}
\]

frames, exact literal two-sided SCD flags, and an owner-frame assignment
for which

* every lower and upper target through depth \(H\) occurs exactly once;
* both layered Hoffman flows are explicit and integral; but
* no two Johnson-adjacent middle owners have the same assigned frame.

Thus the frame-local transition graph is empty and its path-cover number
is exactly \(W\).

For the original polynomial mixed-frame assignment, the same phenomenon
is quantitative: it can be chosen simultaneously Hall-good and with only

\[
 O(Wm/J)=o(W/H)
 \tag{0.7}
\]

same-frame pair-flip edges. Hence the existing independent owner rounding
cannot be postprocessed into long frame-local paths.

Cross-frame bridges are a possible escape, but they introduce a separate
seam count. If a path forest has \(p\) components and \(s\) frame-changing
arcs, cutting those arcs gives \(p+s\) frame-local paths. Without a new
zero-cost exterior-moving seam theorem, coefficient one requires

\[
                         p+s=o(W/H).
 \tag{0.8}
\]

Conditionally, if (0.3) holds after deleting
\(e=o(W/H)\) owners, the selected flags do compile into paths with
\(O(Hp)=o(W)\) collar cost and unchanged internal target incidences.
Thus the new minimal lemma is a **port-sensitive integral
Hoffman circulation**, not another depthwise target Hall theorem.

## 1. Physical flag states and bridge overlap

The lower and upper Hoffman networks are separate single-commodity
networks. An integral solution gives one lower prefix and one upper prefix
at each owner, but those two prefixes need not be the two shadows of one
middle trajectory. We therefore state explicitly the local object needed
for path fusion.

### Definition 1.1 (physical \(H\)-state)

A physical \(H\)-state \(\omega\) over a middle owner \(X\) consists of

1. its assigned pair frame;
2. a locally geodesic middle germ

   \[
    G(\omega)=(X_0,X_1,\ldots,X_H),\qquad X_0=X;
    \tag{1.1}
   \]

3. the literal target traces

   \[
    L_q(\omega)=\bigcap_{i=0}^qX_i,\qquad
    U_q(\omega)=\bigcup_{i=0}^qX_i
    \quad(1\le q\le H);
    \tag{1.2}
   \]

4. any past queue, radius label, or frame tag required by the chosen
   compiler.

Locally geodesic means that the \(q\) transitions in every displayed
subgerm of length \(q\le H\) change \(q\) distinct coordinates or pair
directions. Hence

\[
 |L_q(\omega)|=m-q,\qquad |U_q(\omega)|=m+q.
 \tag{1.3}
\]

If the application uses lower traces from the past and upper traces from
the future, replace (1.1) by a centered germ
\((X_{-H},\ldots,X_0,\ldots,X_H)\). Everything below is unchanged after
enlarging the overlap port.

Let \(\Omega_X\) be the menu of physical states over \(X\) compatible with
the fixed target-frame Hoffman data. It may be empty: separate integral
lower and upper flows do not themselves prove a common-germ lift.

### Definition 1.2 (bridge)

For \(\omega\in\Omega_X\) and \(\eta\in\Omega_Y\), write
\(\omega\to\eta\) when

\[
 Y=X_1,\qquad
 (Y_0,\ldots,Y_{H-1})=(X_1,\ldots,X_H),
 \tag{1.4}
\]

and every additional frame, queue, and target-state interface agrees.
For a frame-local bridge also require that \(X\) and \(Y\) have the same
assigned frame and that their transition is a pair flip in that frame.

Define the full physical ports

\[
 r(\omega)=(X_1,\ldots,X_H;\ {\rm interface\ data}),
 \tag{1.5}
\]

\[
 \ell(\eta)=(Y_0,\ldots,Y_{H-1};\ {\rm interface\ data}).
 \tag{1.6}
\]

Then

\[
                  \omega\to\eta\quad\Longrightarrow\quad
                  r(\omega)=\ell(\eta).
 \tag{1.7}
\]

Conversely, the interface record may be defined to include all local data,
so that equality in (1.7) is sufficient as well.

A chain of bridge-compatible states splices into one middle path. Every
length-\(H\) segment of that path is one of its selected germs, so the
whole path is locally geodesic through the protected depth.

## 2. Exact split-copy path-cover theorem

First fix one state \(\omega_X\in\Omega_X\) for every owner in
\(U\subseteq{\cal M}\). Let \(D(x)\) be their directed bridge graph.

Fix a total order \(\prec\) on \(U\), and retain only bridge arcs
\(X\to Y\) with \(X\prec Y\). Form a bipartite graph

\[
 B_\prec(x)=(U_L,U_R;E_\prec)
 \tag{2.1}
\]

by replacing an allowed directed arc \(X\to Y\) by the edge \(X_LY_R\).

### Theorem 2.1 (ordered path cover equals Hall deficiency)

The minimum number of directed compatible paths covering all vertices of
\(U\), using only \(\prec\)-increasing arcs, is

\[
 \boxed{
 p(x,\prec)=|U|-\nu(B_\prec(x))
 =\max_{{\cal S}\subseteq U}
 \bigl(|{\cal S}|-|N_{B_\prec(x)}({\cal S})|\bigr).}
 \tag{2.2}
\]

#### Proof

A matching \(M\) in the split graph gives every owner at most one selected
successor and at most one selected predecessor. Because every selected arc
increases \(\prec\), the resulting directed graph has no cycle. It is
therefore a path forest. A path forest on \(|U|\) vertices with
\(|M|\) edges has exactly \(|U|-|M|\) components.

Conversely, the arcs of any increasing path cover form a matching between
the left and right copies. Maximizing their number proves the first
equality. The second is the deficiency form of Hall's theorem:

\[
 |U|-\nu(B)=
 \max_{{\cal S}\subseteq U_L}
       \bigl(|{\cal S}|-|N_B({\cal S})|\bigr).
 \]

\(\square\)

Every directed path forest admits a topological total order. Hence the
unrestricted fixed-state optimum is exactly

\[
 \boxed{
 p^*(x)=\min_\prec
 \max_{{\cal S}\subseteq U}
 \bigl(|{\cal S}|-|N_{B_\prec(x)}({\cal S})|\bigr).}
 \tag{2.3}
\]

If at most \(e\) owners may be discarded, the exact robust form is

\[
 \boxed{
 p_e^*(x)=
 \min_{\substack{D\subseteq{\cal M}\\|D|\le e}}
 \ \min_\prec\
 \max_{{\cal S}\subseteq{\cal M}\setminus D}
 \left(
 |{\cal S}|-
 |N_{B_\prec(x)[({\cal M}\setminus D)_L,
                 ({\cal M}\setminus D)_R]}({\cal S})|
 \right).}
 \tag{2.4}
\]

If every discarded owner is paid as a singleton valid state, deletion
does not improve the combined component count:

\[
 \min_{D,\prec}\bigl(p(x|_{{\cal M}\setminus D},\prec)+|D|\bigr)
 =p^*(x).
 \tag{2.4a}
\]

Indeed, adjoining every discarded owner as an isolated path converts the
left side to a spanning cover, while \(D=\varnothing\) gives the reverse
inequality. Deletion remains relevant only because its target and literal
repair may be charged by a different mechanism.

For fixed \(x,\prec\), the matching LP is integral:

\[
 \begin{aligned}
 \nu(B_\prec(x))=\max\quad&
       \sum_{XY\in E_\prec}y_{XY},\\
 {\rm subject\ to}\quad&
       \sum_Yy_{XY}\le1 &&(X\in U),\\
 &     \sum_Xy_{XY}\le1 &&(Y\in U),\\
 &     y_{XY}\ge0.
 \end{aligned}
 \tag{2.5}
\]

Its exact vertex-cover dual is

\[
 \begin{aligned}
 \nu(B_\prec(x))=\min\quad&
       \sum_Xu_X+\sum_Yv_Y,\\
 {\rm subject\ to}\quad&
       u_X+v_Y\ge1 &&(XY\in E_\prec),\\
 &     u_X,v_Y\ge0.
 \end{aligned}
 \tag{2.6}
\]

Both optima have integral solutions. Equations (2.2) and (2.6) are the
requested exact path-cover/b-matching dual.

## 3. The joint Hoffman/state/bridge formulation

Let

\[
 {\cal T}=\{(q,\sigma,T):1\le q\le H,\ 
        \sigma\in\{-,+\},\ |T|=m+\sigma q\}.
 \tag{3.1}
\]

For a physical state \(\omega\), let \(a_{t\omega}\) be its incidence at
typed target \(t\). Let \(\ell_t,u_t\) be the required integral target
throughputs. For a fixed owner order \(\prec\), introduce

\[
 x_\omega\in\{0,1\},\qquad
 y_{\omega\eta}\in\{0,1\}.
 \tag{3.2}
\]

The exact state-column formulation is

\[
 \sum_{\omega\in\Omega_X}x_\omega=1
 \qquad(X\in{\cal M}),
 \tag{3.3}
\]

\[
 \ell_t\le\sum_\omega a_{t\omega}x_\omega\le u_t
 \qquad(t\in{\cal T}),
 \tag{3.4}
\]

\[
 \sum_{\substack{\eta:\omega\to\eta\\
                   {\rm owner}(\omega)\prec{\rm owner}(\eta)}}
 y_{\omega\eta}\le x_\omega,
 \tag{3.5}
\]

\[
 \sum_{\substack{\eta:\eta\to\omega\\
                   {\rm owner}(\eta)\prec{\rm owner}(\omega)}}
 y_{\eta\omega}\le x_\omega.
 \tag{3.6}
\]

Maximizing \(\sum y_{\omega\eta}\) minimizes the number of paths:

\[
                         p=W-\sum_{\omega\eta}y_{\omega\eta}.
 \tag{3.7}
\]

When the layered Hoffman network is used rather than state columns,
(3.3)--(3.4) must be retained in its extended arc-flow form. The path
constraints (3.5)--(3.6) then link root-flow decompositions at their
ports. This linked matrix is not one directed node--arc incidence matrix.

Let \({\cal H}_{\mathbb Z}\) denote the set of integral common-germ state
selections satisfying the extended Hoffman system. Combining Theorem 2.1
with (3.3)--(3.7) gives the exact min--max identity

\[
 \boxed{
 p_{\rm Hoff}=
 \min_{x\in{\cal H}_{\mathbb Z}}\ 
 \min_\prec\
 \max_{{\cal S}\subseteq{\cal M}}
 \bigl(
 |{\cal S}|-|N_{B_\prec(x)}({\cal S})|
 \bigr).}
 \tag{3.8}
\]

Thus the layered Hoffman theorem proves only
\({\cal H}_{\mathbb Z}\ne\varnothing\) when the target-frame cuts and the
local common-germ lift hold. It supplies no upper bound for (3.8).

## 4. The ordered port-signature obstruction

The full physical ports (1.5)--(1.6) immediately produce dual cuts.
Sometimes a smaller queue signature is more transparent.

Write a bridge-one state at \(X\) as

\[
 \omega=(\beta_1;\alpha_1,\ldots,\alpha_H;\ldots),
 \tag{4.1}
\]

where \(\beta_1\) is its first upper/entrance symbol and
\(\alpha_1,\ldots,\alpha_H\) is its ordered lower/source queue. The exact
FIFO bridge recurrence is

\[
 \alpha(Y)=(\alpha_2(X),\ldots,\alpha_H(X),x),
 \qquad
 \beta_1(Y)=\alpha_1(X)
 \tag{4.2}
\]

for some new residual symbol \(x\). Define

\[
 r_0(\omega)=(\alpha_2,\ldots,\alpha_H;\alpha_1),
 \tag{4.3}
\]

\[
 \ell_0(\omega)=(\alpha_1,\ldots,\alpha_{H-1};\beta_1).
 \tag{4.4}
\]

The shift law for consecutive germs gives the necessary identity

\[
                 \omega\to\eta\quad\Longrightarrow\quad
                 r_0(\omega)=\ell_0(\eta).
 \tag{4.5}
\]

Append the assigned frame label to both signatures when paths are required
to be frame-local.

For a fixed selected state vector \(x\), define

\[
 R_x(\gamma)=
 \#\{\omega:x_\omega=1,\ r_0(\omega)=\gamma\},
 \tag{4.6}
\]

\[
 L_x(\gamma)=
 \#\{\omega:x_\omega=1,\ \ell_0(\omega)=\gamma\}.
 \tag{4.7}
\]

### Theorem 4.1 (port-imbalance cut)

Every path cover of all selected owners satisfies

\[
 \boxed{
 p\ge {1\over2}\sum_\gamma
 |R_x(\gamma)-L_x(\gamma)|.}
 \tag{4.8}
\]

If \(e\) owners are discarded first, then

\[
 \boxed{
 e+p\ge {1\over2}\|R_x-L_x\|_1.}
 \tag{4.9}
\]

#### Proof

By (4.5), every selected bridge consumes one exit and one entrance of the
same signature. Hence the number of bridges is at most

\[
 \sum_\gamma\min\{R_x(\gamma),L_x(\gamma)\}
 =W-\frac12\|R_x-L_x\|_1.
 \tag{4.10}
\]

A path cover with \(p\) components uses \(W-p\) bridges, proving (4.8).
Deleting one owner removes one unit from each histogram, and therefore
can lower their \(L^1\) distance by at most two. Apply (4.8) to the
remaining owners to obtain (4.9). \(\square\)

More generally, every signature family \({\cal C}\) gives the one-sided
Hall cut

\[
 p\ge R_x({\cal C})-L_x({\cal C}),
 \tag{4.11}
\]

and maximizing over \({\cal C}\) gives (4.8). Coordinate projections of
(4.8) give the weaker stationarity constraints equating successive
direction-position histograms. The full ordered-port cut is strictly
stronger.

## 5. Why no Hoffman cut implies the port cut

The distinction is exact inside one physical pair frame.

Fix \(H\ge3\), one owner \(X\), and \(H\) split pair directions

\[
                         D=\{d_1,\ldots,d_H\}.
 \tag{5.1}
\]

Fix all independent upper/past data, including an incoming direction
\(\beta_1\notin D\). For every \(\pi\in S_H\), let
\(\omega_\pi\) be the legal state whose next deletion order is

\[
                         \pi(d_1,\ldots,d_H).
 \tag{5.2}
\]

At lower depth \(q\), the literal target reached by this state depends
only on the unordered set of its first \(q\) directions. For a fixed
\(q\)-set \(Q\subseteq D\),

\[
 \sum_{\substack{\pi\in S_H\\
       \{\pi(d_1),\ldots,\pi(d_q)\}=Q}}
       \operatorname {sgn}\pi=0.
 \tag{5.3}
\]

Indeed, for \(1\le q\le H-1\), that fiber is a coset of
\(S_q\times S_{H-q}\), and one of the two factors contains an odd
permutation because \(H\ge3\). For \(q=0,H\), use the equal numbers of
even and odd elements of \(S_H\).

Therefore the signed vector

\[
 z=\sum_{\pi\in S_H}\operatorname {sgn}\pi\,e_{\omega_\pi}
 \tag{5.4}
\]

has zero incidence in

* the owner row;
* every literal lower target row at every depth;
* every paired upper row determined by the same unordered prefix set, by
  the same calculation; and
* every independent upper/past row, since those data were fixed and
  \(\sum_\pi\operatorname {sgn}\pi=0\).

It is consequently invisible to the full target-throughput data used by
the layered Hoffman circulation.

Equivalently, the two nonnegative probability laws

\[
 \mu_{\rm even}={2\over H!}\sum_{\pi\ {\rm even}}e_{\omega_\pi},
 \qquad
 \mu_{\rm odd}={2\over H!}\sum_{\pi\ {\rm odd}}e_{\omega_\pi}
 \tag{5.4a}
\]

have identical owner mass and identical Hoffman target throughputs at
every depth.

The cyclic shift

\[
 (\pi(d_1),\ldots,\pi(d_H))
 \longmapsto
 (\pi(d_2),\ldots,\pi(d_H),\pi(d_1))
\]

has sign \((-1)^{H-1}\). Let \({\cal C}_D\) be the ordered \(H\)-tuples
with underlying set \(D\) and parity \((-1)^{H-1}\). Then

\[
 r_0(\omega_\pi)\in{\cal C}_D
 \quad\Longleftrightarrow\quad \pi\ {\rm is\ even},
 \tag{5.5}
\]

whereas

\[
 \ell_0(\omega_\pi)\notin{\cal C}_D
 \qquad(\pi\in S_H),
 \tag{5.6}
\]

because its underlying set replaces one member of \(D\) by
\(\beta_1\notin D\). Thus the port functional

\[
 R({\cal C}_D)-L({\cal C}_D)
 \tag{5.7}
\]

has nonzero pairing with \(z\).
Indeed it equals one on \(\mu_{\rm even}\) and zero on
\(\mu_{\rm odd}\), while all Hoffman data of those laws agree.

### Theorem 5.1 (linear independence of the path gate)

For \(H\ge3\), the ordered port-Hall rows are not in the linear span of
the owner rows and all layered literal target-throughput rows. Hence no
argument using only the mixed-frame target marginals and Hoffman's
circulation cuts can imply (4.8).

The construction is physical and lies in every balanced frame with at
least \(H+1\) split directions. In the calibrated band the selected frames
have \(m/2-o(m)\) split directions, so there is ample room.

This is a local signed-multiplicity kernel, not by itself an owner-simple
global counterexample. Its rigorous conclusion is that the port rows are
new dual constraints: any global positive theorem must prove them using
structure beyond the Hoffman target throughputs.

## 6. An integral exact-Hoffman/no-path construction

The preceding kernel is a dual separation. There is also an integral
frame-local counterexample with zero target error.

Fix a symmetric-chain decomposition of \(2^{[2m]}\). For every middle
owner \(X\), extend its lower and upper SCD flags to ordered lists of
\(H\) distinct coordinates. Let \(E_X(P)\) be the event that a pair frame
\(P\)

1. makes every displayed lower and upper step a legal split-pair step;
2. uses disjoint lower and upper direction families; and
3. has balanced pair type at \(X\).

The exact literalization calculation gives, uniformly in \(X\),

\[
 \Pr(E_X(P))\ge p_*,
 \tag{6.1}
\]

where

\[
 p_*\ge
 {1\over2}
 {((m-H)_{\underline H})^2
  \over\prod_{i=0}^{2H-1}(2m-2i-1)}
 \ge
 {1\over2}\,4^{-H}\exp(-CH^2/m).
 \tag{6.2}
\]

Choose

\[
 J=\left\lceil{16m^2\over p_*}\right\rceil
 \tag{6.3}
\]

independent frames. For a fixed owner, the number of successful frames has
mean at least \(16m^2\). Chernoff's inequality gives

\[
 \Pr\bigl(|I(X)|<m^2+1\bigr)\le\exp(-c m^2).
 \tag{6.4}
\]

Since \(W\le4^m\), with probability \(1-o(1)\) every owner has at least
\(m^2+1\) successful frames.

The catalogue may simultaneously be pairwise separated. For two random
frames \(P,P'\), if \(\iota(P,P')\) is their number of common coordinate
pairs, then

\[
                  \Pr(\iota(P,P')\ge r)\le {1\over r!}.
 \tag{6.5}
\]

Because

\[
 \log J=O(H+H^2/m+\log m)=o(m),
 \tag{6.6}
\]

choosing

\[
 r={4\log J\over\log(\log J+2)}+O(1)=o(m)
 \tag{6.7}
\]

makes the union bound over all frame pairs tend to zero. Thus a
deterministic catalogue satisfies both the success-list and separation
properties.

The Johnson graph \(J(2m,m)\) has maximum degree

\[
                              \Delta=m^2.
 \tag{6.8}
\]

Order its vertices arbitrarily. Greedily assign owner \(X\) a frame from
its success list which has not been assigned to any earlier Johnson
neighbor. At most \(m^2\) colors are forbidden, while
\(|I(X)|\ge m^2+1\), so the choice is always possible.

### Theorem 6.1 (exact nested Hoffman does not imply frame-local paths)

The resulting owner-frame assignment has all of the following properties.

1. Every owner receives one balanced frame literalizing its complete
   truncated SCD flags.
2. Every lower and upper physical target through depth \(H\) occurs on its
   unique SCD chain, hence has one literal owner.
3. Sending one unit along every truncated SCD flag is an explicit integral
   feasible flow in both fixed-target-frame Hoffman networks.
4. Johnson-adjacent owners have different assigned frame labels.

Consequently the frame-local middle transition graph has no edge, and
every frame-local path cover has exactly \(W\) components.

The catalogue size obeys

\[
 J=O\!\left(m^2\,4^H\exp(CH^2/m)\right)=W^{o(1)}.
 \tag{6.9}
\]

This theorem refutes the implication

\[
 \text{exact literal Hall}+\text{exact nested Hoffman}
 \Longrightarrow\text{few frame-local paths}.
 \tag{6.10}
\]

It does not refute a new jointly chosen path-correlated assignment, and it
does not rule out frame-changing physical paths.

## 7. The original polynomial Hall assignment is also path-hostile

Return to the polynomial uniform catalogue
\((P_1,\ldots,P_J)\) and choose every owner independently and uniformly
from its good-frame set \(I(X)\). As in the simultaneous literal Hall
theorem,

\[
 |I(X)|\ge(1-\varepsilon)J(1-\tau).
 \tag{7.1}
\]

For one frame, every middle owner has at most \(m\) pair-flip neighbors,
so the total number of frame-labelled undirected pair-flip edges is at
most \(Wm/2\). Across all \(J\) frames it is at most \(JWm/2\).

A fixed frame-labelled edge survives the owner assignment with probability
at most

\[
 {1\over(1-\varepsilon)^2J^2(1-\tau)^2}.
 \tag{7.2}
\]

If \(e(A)\) is the number of surviving same-frame pair-flip edges, then

\[
 \boxed{
 {\bf E}e(A)
 \le {Wm\over
  2(1-\varepsilon)^2(1-\tau)^2J}.}
 \tag{7.3}
\]

The target Hall, quota, collision, and edge-count errors are all
nonnegative. Applying the averaging argument to their normalized sum
shows that one deterministic assignment satisfies the previously proved
summed target bounds and, simultaneously,

\[
                         e(A)=O(Wm/J).
 \tag{7.4}
\]

The catalogue exponent may be chosen so that \(J/(mH)\to\infty\).
Then

\[
                         e(A)=o(W/H).
 \tag{7.5}
\]

Any frame-local path forest covering \(W-e_0\) owners with \(p\)
components uses exactly \(W-e_0-p\) transition edges. Since it can use at
most \(e(A)\) available edges,

\[
 \boxed{
 e_0+p\ge W-e(A)=W-o(W/H).}
 \tag{7.6}
\]

Thus the independent owner assignment used to prove simultaneous
literal-face Hall cannot be postprocessed into the desired paths. Any
later choice or Hoffman decomposition of flags can only delete possible
middle bridges; it cannot create same-frame geometric edges.

This is a no-go for the proof method and for these edge-sparse
realizations, not for every Hall-good assignment. A positive theorem must
correlate frame choices along the prospective paths while re-proving the
mixed-frame target estimates.

## 8. Cross-frame seams

Suppose physical bridge equations permit an arc \(X\to Y\) with different
assigned frames. Let \(s\) be the number of such arcs selected in a path
forest with \(p\) components. Cutting every frame-changing arc gives
\(p+s\) frame-local paths.

If \(e(A)\) is the number of available same-frame transition edges and the
forest covers \(W-e_0\) owners, then

\[
 (W-e_0)-p-s\le e(A),
 \tag{8.1}
\]

or

\[
 \boxed{
 e_0+p+s\ge W-e(A).}
 \tag{8.2}
\]

For the assignment in Section 7, the right side is
\(W-o(W/H)\). Therefore either the component count or the number of frame
changes is linear.

This does not obstruct a genuinely frame-blind compiler which traverses
cross-frame bridges at zero cost. Such a theorem would be new. Every
current frame-specific pair-block or eventual \(C_{2h}\) compiler pays a
full-radius component interface at a frame change, so its coefficient-one
ledger requires

\[
                         (2H+1)(p+s)=o(W).
 \tag{8.3}
\]

In that setting cross-frame paths do not evade the frame-local
obstruction. If a zero-cost frame-changing compiler is supplied, the
relevant remaining obstruction is instead the full port-Hall cut
(3.8)--(4.9), which already allows cross-frame arcs.

## 9. Conditional positive path compiler

The port-Hall condition is not merely necessary. It gives the desired
paths and the correct literal ledger.

### Theorem 9.1 (port-Hall implies long-path fusion)

Suppose there are

1. an owner set \(U\subseteq{\cal M}\), with
   \(|{\cal M}\setminus U|=e_0\);
2. an integral common-germ state selection \(x\) on \(U\) satisfying the
   required target-frame Hoffman throughputs;
3. a total order \(\prec\) for which

   \[
    \max_{{\cal S}\subseteq U}
    \bigl(
      |{\cal S}|-|N_{B_\prec(x)}({\cal S})|
    \bigr)\le p.
    \tag{9.1}
   \]

Then \(U\) has a cover by \(p\) locally geodesic paths realizing every
selected internal flag. The exact full-radius linearization of a path with
\(t\) useful states has length \(t+2H+1\). Hence these paths have total
length at most

\[
                            |U|+(2H+1)p.
 \tag{9.2}
\]

If each omitted owner is paid as a singleton useful block, the complete
middle-row ledger is

\[
                     W+(2H+1)(p+e_0).
 \tag{9.3}
\]

If

\[
                       (2H+1)(p+e_0)=o(W),
 \tag{9.4}
\]

and the starting Hoffman target deficit is \(o(W)\), the path
linearization and the omitted-owner repair have total cost \(o(W)\).

#### Proof

Theorem 2.1 gives a matching of size at least \(|U|-p\), hence a path
forest with at most \(p\) components. Bridge overlap splices its local
states, and every length-\(H\) segment remains locally geodesic.

The standard full-radius collar uses \(2H+1\) additional positions per
component. This exposes every endpoint flag. All internal target traces
are unchanged. Paying an omitted owner as a singleton component gives
(9.3).

Deleting one owner can remove at most one lower and one upper certified
occurrence at each of the \(H\) depths. Thus the summed target repair
increases by at most \(2He_0\). Equations (9.2)--(9.4) prove the ledger.
\(\square\)

The component condition also forces genuinely long paths on almost all
owners. If \(Hp=o(W)\), choose

\[
 g=\sqrt{W/(Hp)}\longrightarrow\infty
 \tag{9.5}
\]

(with the conclusion trivial when \(p=0\)). Paths of fewer than \(gH\)
owners contain altogether at most

\[
                         pgH=\sqrt{WHp}=o(W)
 \tag{9.6}
\]

owners. Hence paths of length at least \(gH=\omega(H)\) cover
\(W-e_0-o(W)\) owners.

The user's stated middle leave \(e_0=o(W)\) suffices for this geometric
near-cover. For the coefficient-one target ledger, however, the present
one-copy repair requires the sharper \(e_0=o(W/H)\), unless a separate
residual compiler is proved.

## 10. Exact proved/conditional boundary

The following are proved.

1. For fixed integral physical states, the minimum path-cover number is
   exactly the ordered split-copy Hall deficiency (2.2)--(2.3).
2. With state choice included, the exact combined problem is the integral
   Hoffman/state/bridge system (3.3)--(3.8).
3. Every solution satisfies the ordered port imbalance cut (4.8)--(4.9).
4. The alternating-permutation kernel proves that this cut is independent
   of every layered Hoffman target-throughput row.
5. Exact literal SCD target coverage and exact integral Hoffman flows can
   coexist with an empty frame-local transition graph.
6. The independent polynomial mixed-frame Hall assignment is
   quantitatively edge-sparse and cannot be postprocessed into long
   frame-local paths.
7. If the port-Hall deficit is \(o(W/H)\), matching produces the desired
   locally geodesic paths with \(o(W)\) collar cost.

The following remain unproved.

1. An assignment-identification theorem combining the polynomial
   Hall/collision owner assignment with an integral nested Hoffman flow.
2. A common-germ lift of the independently rounded lower and upper Hoffman
   flows in the original polynomial catalogue.
3. An integral Hoffman-feasible state choice satisfying every port-Hall
   cut with \(o(W/H)\) deficiency.
4. A correlated frame assignment producing that state choice while
   retaining the simultaneous target and factorial collision estimates.
5. A zero-cost frame-changing seam compiler; without one, the number of
   frame changes must be added to the path-component ledger.

Thus the exact new minimal lemma is:

> **Port-sensitive Hoffman path theorem.** There are an integral
> common-germ Hoffman flow, an owner set of leave \(o(W/H)\), and a total
> order \(\prec\) such that every split-copy bridge Hall cut has deficiency
> \(o(W/H)\).

This is strictly stronger than both simultaneous literal-target Hall and
the layered Hoffman circulation theorem, but strictly weaker than complete
\(C_{2h}\) cycle bundling.

## 11. Independent audit

The decisive steps were audited independently.

1. The split-copy formula is exact with quantifiers

   \[
   \exists\,\prec\quad\forall\,{\cal S}\subseteq U_L,
   \]

   and with neighborhoods taken in the full right copy. Every path forest
   supplies a topological order, and every ordered matching supplies a path
   forest.
2. The audited bridge-one FIFO recurrence is (4.2), giving the port maps
   (4.3)--(4.4). The robust deletion inequality is exactly (4.9).
3. The alternating-order vector (5.4) annihilates every unordered-prefix
   target row. The audit confirms this only as a local signed-multiplicity
   obstruction; no owner-simple global counterexample is claimed from it.
4. The greedy list-coloring construction and its catalogue size are
   correct, including simultaneous pairwise \(o(m)\) frame separation.
   Its obstruction is explicitly frame-local. Differently framed physical
   bridges remain possible and are governed by Sections 4 and 8.
5. The exact full-radius component toll is \(2H+1\), yielding (9.3);
   \(H(p+e_0)=o(W)\) is only the equivalent order-of-magnitude statement.
6. The polynomial Hall/collision assignment and augmented exact-Hoffman
   assignment are not identified. The note treats their combination as
   the new optimization gate (3.8), not as a proved construction.
