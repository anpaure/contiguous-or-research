# Fine strip-cover synthesis: one additive integrality gate for coefficient one

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, search, or web input is
used.

## 0. Verdict

Put

\[
 W_m=\binom{2m}{m}.
\]

There is a strictly sharper synthesis than the previously stated exact-factor
gate. Because each long pair-flip cycle can be converted directly into a
literal contiguous-OR block, selected cycles do **not** have to form one exact
middle factor. Middle-owner disjointness can be replaced by the exact output
length charged to each selected block.

This leads to one finite, labelled, chronology-coherent weighted set-cover
integer program. If its integral optimum differs from its fractional optimum
by \(o(W_m)\), then

\[
 \nu(2m)\le (1+o(1))W_m
\]

and the usual two-copy lift gives the same conclusion for odd ground-set
sizes. The fractional optimum is computed exactly below:

\[
 \tau^*_{m,H,h}
 =W_m+\frac Hh\binom{2m}{m-1}.                  \tag{0.1}
\]

Thus, for \(H/h=o(1)\), the sole residual hypothesis is

\[
 \boxed{\tau_{m,H,h}-\tau^*_{m,H,h}=o(W_m).}      \tag{SCI}
\]

Here every integer column is a whole physical \(C_{2h}\), every row is one
literal target set, both signs and all depths use the same cycle column, and
the objective is the exact length of the literal word produced. Consequently
\((\mathrm{SCI})\) hides no further Hall assignment, owner choice, chronology,
direction-order, seam, or OR-realizability condition.

The exact dual-slack audit below also identifies the limitation of this
reduction.  Asymptotically, (SCI) is equivalent to finding a whole-strip
family whose middle load vector is \(o(W_m)\) in \(\ell^1\) from the all-ones
vector and whose aggregate number of signed band holes is \(o(W_m)\); see
Corollary 4.5.  Thus owner recycling removes exact divisibility and exact
owner-disjointness, but it does **not** turn the remaining synchronization
problem into a generic set-cover rounding problem.  Independent rounding
leaves \((2/e+o(1))N_1\) first-shadow holes and any repair must globally
change \(\Omega(W_m/h)\) cycle decisions.

If one insists on the exact-factor architecture, the stronger remaining
hypothesis is an owner-disjoint version of the same labelled cover. The
explicit fixed-pair Stage A, mixed-frame TU marginals, long-cycle associator,
and tensor coarse-capacity results establish feasibility of necessary marginal
relaxations or exact local moves for that stronger problem, but none proves
either integral hypothesis.

The qualification on “sole” and “smallest” is exact: \((\mathrm{SCI})\) is the
smallest hypothesis inside the literal strip-block plus singleton-repair
compiler defined below. It is not asserted to be necessary for an arbitrary
contiguous-OR word using unrelated blocks.

## 1. Parameters

Take

\[
 H=\left\lceil\sqrt{m\log m}\right\rceil,
 \qquad
 h=2^{\lceil(3/4)\log_2m\rceil}.                    \tag{1.1}
\]

For all sufficiently large \(m\),

\[
 1\le H<h<m,\qquad \frac Hh=o(1),\qquad h=o(m).       \tag{1.2}
\]

The proof below works for every \(1\le H<h<m\). The displayed choice has
three useful features:

1. \(h\) is a power of two, so the explicit fixed-pair Stage-A factor applies;
2. \(H/h=o(1)\), so linearizing every cyclic block costs \(o(W_m)\) in total;
3. the Boolean layers outside distance \(H\) from the middle have total size
   \(o(W_m)\).

The strict inequality \(H<h\) is essential. At depth \(q=h\), all lower
windows of one \(C_{2h}\) collapse to its fixed core and all upper windows
collapse to the complement of its excluded core.

## 2. The physical strip catalogue

Let \(\Omega\) be a \(2m\)-element set. A cyclic \(h\)-strip consists of

* a fixed core \(K\subseteq\Omega\) of size \(m-h\); and
* \(2h\) distinct active coordinates
  \(z_0,z_1,\ldots,z_{2h-1}\in\Omega\setminus K\), in cyclic order.

Indices on the \(z_i\)'s are taken modulo \(2h\). For \(0\le a\le2h\), put

\[
 I_z(t,a)=\{z_t,z_{t+1},\ldots,z_{t+a-1}\}.          \tag{2.1}
\]

The associated middle cycle is

\[
 X_t=K\cup I_z(t,h),\qquad t\in\mathbb Z/(2h).       \tag{2.2}
\]

Consecutive states differ by deleting \(z_t\) and inserting \(z_{t+h}\).
The first \(h\) transitions use \(h\) disjoint replacement pairs and the next
\(h\) transitions reverse them in the same order. Hence (2.2) is precisely
an isometric pair-frame \(C_{2h}\) with direction word

\[
 \pi_1,\ldots,\pi_h,\pi_1,\ldots,\pi_h.             \tag{2.3}
\]

Conversely, every isometric \(C_{2h}\) arising from a pair-flip \(Q_h\) cycle
has representation (2.2): call the coordinate removed at transition \(t\)
\(z_t\); the coordinate inserted there is \(z_{t+h}\), and induction gives
\(X_t=K\cup I_z(t,h)\).

Let \(\mathscr C_{m,h}\) be the set of these cycles, where cyclic rotation and
reversal of \(z\) describe the same unoriented cycle. It is closed under all
coordinate permutations and has exact size

\[
 |\mathscr C_{m,h}|
 =\frac{(2m)!}{4h(m-h)!^2}.                           \tag{2.4}
\]

For \(0\le q<h\), define its lower and upper physical targets by

\[
 L^q_t(C)=\bigcap_{j=0}^qX_{t+j}
          =K\cup I_z(t+q,h-q),                        \tag{2.5}
\]

\[
 U^q_t(C)=\bigcup_{j=0}^qX_{t+j}
          =K\cup I_z(t,h+q).                          \tag{2.6}
\]

For \(q=0\), both are \(X_t\), and this target is counted once. For every
\(0\le q<h\), the \(2h\) targets in (2.5) are distinct, as are the \(2h\)
targets in (2.6). This fails at \(q=h\), which is why the strict range
\(H<h\) is retained everywhere.

Write

\[
 \mathcal T_H(C)
 =\{X_t:t\in\mathbb Z_{2h}\}
  \cup\bigcup_{q=1}^H
     \{L^q_t(C),U^q_t(C):t\in\mathbb Z_{2h}\}.       \tag{2.7}
\]

This is one whole labelled, simultaneous, two-sided chronology column. No
target at one depth may be chosen independently of the other targets in the
same column.

## 3. Exact literalization of one cycle

### Lemma 3.1 (strip factor identity)

For \(C\in\mathscr C_{m,h}\), define

\[
 A_t=\bigcap_{j=0}^H X_{t+j}
    =K\cup I_z(t+H,h-H).                              \tag{3.1}
\]

Then, for \(0\le r\le2H\),

\[
 \bigcup_{s=0}^rA_{t+s}
 =K\cup I_z(t+H,h-H+r).                               \tag{3.2}
\]

In particular, for \(0\le q\le H\),

\[
 L^q_u(C)=\bigcup_{v=u+q-H}^{u}A_v,                   \tag{3.3}
\]

\[
 U^q_u(C)=\bigcup_{v=u-H}^{u+q}A_v.                   \tag{3.4}
\]

All index intervals in (3.3)--(3.4) are cyclic and consecutive.

#### Proof

The intersection of the cyclic intervals
\(I_z(t,h),I_z(t+1,h),\ldots,I_z(t+H,h)\) is
\(I_z(t+H,h-H)\), proving (3.1). Consecutive intervals in (3.1) have
consecutive starting points, so their union has the same first point and its
length increases by one at each step. The maximum length is

\[
 h-H+2H=h+H<2h,
\]

so the union never becomes the full active cycle. This proves (3.2).

For (3.3), the first \(A\)-interval starts at \(u+q\), there are
\(H-q+1\) consecutive intervals, and their union has length \(h-q\); this is
(2.5). For (3.4), the first \(A\)-interval starts at \(u\), there are
\(H+q+1\) consecutive intervals, and their union has length \(h+q\); this is
(2.6). \(\square\)

### Corollary 3.2 (literal cycle block)

The linear word

\[
 \mathcal W_H(C)=
 A_0,A_1,\ldots,A_{2h-1},A_0,A_1,\ldots,A_{2H-1}     \tag{3.5}
\]

has length exactly

\[
 c_{H,h}=2h+2H                                      \tag{3.6}
\]

and literally covers every target in \(\mathcal T_H(C)\) by a contiguous OR.

#### Proof

Every required interval in (3.3)--(3.4) has at most \(2H+1\) letters. An
interval starting at the last position \(A_{2h-1}\) therefore ends at the last
repeated position \(A_{2H-1}\). Thus the repeated prefix has exactly \(2H\)
letters. Lemma 3.1 proves the OR identity. \(\square\)

There is no inter-block seam condition: every advertised witness is contained
inside one block (3.5). Concatenating blocks cannot destroy those witnesses.

## 4. The weighted labelled strip-cover program

Let

\[
 \mathcal B_{m,H}
 =\bigcup_{q=-H}^{H}\binom{\Omega}{m+q}.              \tag{4.1}
\]

For \(C\in\mathscr C_{m,h}\), let \(x_C\in\{0,1\}\). For every physical
target \(S\in\mathcal B_{m,H}\), let \(z_S\in\{0,1\}\). Define

\[
 \begin{split}
 \tau_{m,H,h}=\min\quad &
 (2h+2H)\sum_{C\in\mathscr C_{m,h}}x_C
       +\sum_{S\in\mathcal B_{m,H}}z_S,\\
 \text{subject to}\quad &
 z_S+\sum_{C:S\in\mathcal T_H(C)}x_C\ge1
 \quad(S\in\mathcal B_{m,H}).                       \tag{4.2}
 \end{split}
\]

Let \(\tau^*_{m,H,h}\) be the relaxation with \(x_C,z_S\ge0\).

The \(z_S\)-column is literal singleton repair: if \(z_S=1\), append \(S\)
itself as one letter. There are no owner variables, hidden target quotas, or
profile equalities. The coefficient \(2h+2H\) is not a surrogate cost; it is
the exact length of (3.5).

### Theorem 4.1 (exact fractional optimum)

For every \(1\le H<h<m\), writing

\[
 N_1=\binom{2m}{m-1},
\]

one has the exact identity

\[
 \boxed{
 \tau^*_{m,H,h}=W_m+\frac HhN_1.}                    \tag{4.3}
\]

#### Proof: lower bound

Put \(X=\sum_Cx_C\).  Summing the constraints over the middle layer and
over each of the two signed depth-one layers gives respectively

\[
 Z_0+2hX\ge W_m,
 \qquad Z_1^-+2hX\ge N_1,
 \qquad Z_1^++2hX\ge N_1,                            \tag{4.4}
\]

where the \(Z\)'s are the corresponding total singleton weights.  Hence
the objective is at least

\[
 f(X)=(2h+2H)X+(W_m-2hX)_+
                 +2(N_1-2hX)_+.                     \tag{4.5}
\]

On \(0\le X\le N_1/(2h)\), its slope is \(2H-4h<0\); on
\(N_1/(2h)\le X\le W_m/(2h)\), its slope is \(2H>0\); and after
\(W_m/(2h)\) it is increasing as well.  Therefore its unique breakpoint
minimum is

\[
 f\!\left(\frac{N_1}{2h}\right)
 =W_m+\frac HhN_1.                                   \tag{4.6}
\]

#### Proof: upper bound

The action of \(\operatorname{Sym}(\Omega)\) is transitive on
\(\mathscr C_{m,h}\), on the middle layer, and on each signed target layer.
The exact number of catalogue cycles through a fixed middle target is

\[
 D_0=\frac{m!^2}{2(m-h)!^2}.                          \tag{4.5}
\]

For \(0<q<h\), the exact number through a fixed signed depth-\(q\) target is

\[
 D_q=\frac{(m+q)!(m-q)!}{2(m-h)!^2}.                  \tag{4.6}
\]

Indeed, double-counting middle incidences gives
\(|\mathscr C_{m,h}|2h=W_mD_0\), and double-counting signed depth-\(q\)
incidences gives
\(|\mathscr C_{m,h}|2h=\binom{2m}{m-q}D_q\), proving
(4.5)--(4.6) from (2.4).

Set

\[
 x_C=D_1^{-1}\quad(C\in\mathscr C_{m,h}).             \tag{4.7}
\]

Every signed depth-one target has load one.  Every signed target at depth
\(q\ge1\) has load

\[
 \frac{D_q}{D_1}
 =\frac{N_1}{\binom{2m}{m-q}}\ge1.                   \tag{4.8}
\]

Its middle load is \(D_0/D_1=N_1/W_m\).  Give every middle target the
singleton weight \(1-N_1/W_m\), and give every nonmiddle target singleton
weight zero.  This is feasible simultaneously for every \(q\le H\).  Its
total cycle weight is

\[
 \frac{|\mathscr C_{m,h}|}{D_1}=\frac{N_1}{2h}.       \tag{4.9}
\]

Its objective is therefore

\[
 (2h+2H)\frac{N_1}{2h}+W_m-N_1
 =W_m+\frac HhN_1,                                   \tag{4.10}
\]

which proves the upper bound. \(\square\)

This orbit proof is stronger than averaging the explicit Stage-A partial
factors. The unscaled average of those factors has an exponentially small
middle leave \(L_{m,h}\), but rescaling its cycle vector to middle load one
is not optimal for the weighted programme: the exact optimum deliberately
leaves the fraction \(1-N_1/W_m=1/(m+1)\) of the middle layer to singleton
repair, while its cycle mass saturates the two first-shadow layers and
automatically overcovers every deeper layer.  Thus the natural cover LP has
the explicit objective (4.3); the Stage-A leave is not its fractional
optimum.

### Proposition 4.2 (dual certificate and exact gap ledger)

Put

\[
 a=\frac{H}{2h}.
\]

The dual of the relaxation in (4.2) is

\[
 \begin{split}
 \max\quad &\sum_{S\in\mathcal B_{m,H}}y_S,\\
 \text{subject to}\quad
 &0\le y_S\le1,\\
 &\sum_{S\in\mathcal T_H(C)}y_S\le2h+2H
       \qquad(C\in\mathscr C_{m,h}).
 \end{split}                                                   \tag{4.11}
\]

The rank-constant vector

\[
 y_S=
 \begin{cases}
 1,&|S|=m,\\
 a,&|S|=m-1\text{ or }m+1,\\
 0,&\bigl||S|-m\bigr|\ge2
 \end{cases}                                                   \tag{4.12}
\]

is feasible and saturates every cycle constraint.  Its value is

\[
 W_m+2aN_1=W_m+\frac HhN_1.                           \tag{4.13}
\]

Consequently (4.12), together with the primal point in the proof of
Theorem 4.1, is a direct primal--dual proof of (4.3).

More precisely, let \((x,z)\) be any feasible fractional solution and write

\[
 \ell_S=z_S+\sum_{C:S\in\mathcal T_H(C)}x_C.          \tag{4.14}
\]

Then its objective excess above \(\tau^*_{m,H,h}\) is exactly

\[
\begin{split}
 \Delta(x,z)
 ={}&\sum_{|S|=m}(\ell_S-1)\\
 &+a\sum_{|S|=m-1,m+1}(\ell_S-1)\\
 &+(1-a)\sum_{|S|=m-1,m+1}z_S\\
 &+\sum_{2\le\lvert |S|-m\rvert\le H}z_S .
                                                               \tag{4.15}
\end{split}
\]

Every term in (4.15) is nonnegative.  In particular, an integral solution
has objective \(\tau^*+o(W_m)\) if and only if the sum on the right of
(4.15) is \(o(W_m)\).  Thus the precise integral gate is:

1. total middle-layer overcoverage is \(o(W_m)\);
2. the number of singleton repairs outside the middle layer is \(o(W_m)\);
3. depth-one overcoverage is charged only at the collar price
   \(a=H/(2h)=o(1)\).

There is deliberately no penalty for a middle target covered only by its
singleton column, and no direct penalty for overcovering depths at least two.
Accordingly, (SCI) is weaker than asking the selected cycles to form an
approximate factor or to be nearly disjoint at every shadow depth.

#### Proof

Duality gives (4.11).  Every strip cycle contains \(2h\) middle targets and
\(2h\) targets in each of the two signed depth-one layers.  Therefore the
left side of its dual constraint under (4.12) is

\[
 2h+4ha=2h+2H,
\]

and \(a<1/2\) because \(H<h\).  This proves feasibility and (4.13).

For the gap identity, subtract the dual objective from the primal objective
and insert the dual constraints:

\[
 c^Tx+\mathbf1^Tz-\mathbf1^Ty
 =\sum_Cx_C(c_C-A_C^Ty)
  +\sum_Sz_S(1-y_S)
  +\sum_Sy_S(\ell_S-1).                              \tag{4.16}
\]

All cycle reduced costs in (4.16) vanish by saturation.  Substitution of
(4.12) yields (4.15). \(\square\)

### Corollary 4.3 (cycle-family form of the remaining theorem)

For a set \(\mathcal F\subseteq\mathscr C_{m,h}\), let
\(\mu_{0}(S)\) be its middle multiplicity, let
\(\mu_{1}^{\pm}(S)\) be its two signed depth-one multiplicities, and let
\(M_q^{\pm}(\mathcal F)\) be the number of uncovered signed depth-\(q\)
targets.  Define

\[
\begin{split}
 \mathfrak L_{H,h}(\mathcal F)={}&
 \sum_{|S|=m}(\mu_0(S)-1)_+\\
 &+\frac{H}{2h}
   \left[
    \sum_{|S|=m-1}(\mu_1^-(S)-1)_+
    +\sum_{|S|=m+1}(\mu_1^+(S)-1)_+
   \right]\\
 &+\left(1-\frac{H}{2h}\right)
       \bigl(M_1^-(\mathcal F)+M_1^+(\mathcal F)\bigr)\\
 &+\sum_{q=2}^{H}
       \bigl(M_q^-(\mathcal F)+M_q^+(\mathcal F)\bigr).       \tag{4.17}
\end{split}
\]

Then

\[
 \tau_{m,H,h}-\tau^*_{m,H,h}
   =\min_{\mathcal F\subseteq\mathscr C_{m,h}}
        \mathfrak L_{H,h}(\mathcal F).               \tag{4.18}
\]

Consequently (SCI) is equivalent to the existence of one whole-cycle family
\(\mathcal F\) satisfying

\[
 \mathfrak L_{H,h}(\mathcal F)=o(W_m).               \tag{4.19}
\]

#### Proof

For fixed integral cycle variables, the unique cost-minimizing singleton
choice is \(z_S=1\) exactly at uncovered targets.  Thus
\(\ell_S-1=(\mu(S)-1)_+\) at every rank.  Insert these values into
(4.15).  At depths at least two the dual weight is zero, so only uncovered
targets remain.  Minimizing over the selected cycle family proves
(4.18). \(\square\)

### Proposition 4.4 (mass-conservation normal form)

Let

\[
 P=2h|\mathcal F|,
\]

the total number of cycle occurrences in any one signed layer, and let
\(M_0(\mathcal F)\) be the number of uncovered middle targets.  Then

\[
\begin{split}
 \mathfrak L_{H,h}(\mathcal F)={}&
 \bigl(M_0+P-W_m\bigr)\\
 &+M_1^-+M_1^+
   +\frac Hh(P-N_1)\\
 &+\sum_{q=2}^{H}(M_q^-+M_q^+).                    \tag{4.20}
\end{split}
\]

Here the first parenthesis is nonnegative: it is exactly the total middle
multiplicity excess.  In particular, (4.19) forces

\[
 P\ge N_1-o(W_m),\qquad P\le W_m+o(W_m),             \tag{4.21}
\]

and hence

\[
 M_0=o(W_m),\qquad
 \sum_{|S|=m}(\mu_0(S)-1)_+=o(W_m).                 \tag{4.22}
\]

Thus owner recycling removes exact owner-disjointness and its divisibility
constraints, but it does not evade the asymptotic middle-factor requirement:
every successful family is an \(L^1\)-approximate middle factor.

#### Proof

At any rank with \(N\) targets, total occurrence mass \(P\), hole count
\(M\), and excess \(E=\sum_S(\mu(S)-1)_+\), mass conservation gives

\[
 E-M=P-N.                                            \tag{4.23}
\]

Apply (4.23) at the middle rank and at each signed depth-one rank, then
substitute into (4.17).  The two depth-one terms combine as

\[
 \frac H{2h}(E_1^-+E_1^+)
 +\left(1-\frac H{2h}\right)(M_1^-+M_1^+)
 =M_1^-+M_1^++\frac Hh(P-N_1),                      \tag{4.24}
\]

which proves (4.20).

If \(P<N_1\), each signed depth-one hole count is at least \(N_1-P\);
therefore the second line of (4.20) is at least
\(2(1-H/(2h))(N_1-P)\).  This proves the first inequality in
(4.21).  The middle excess is at least \((P-W_m)_+\), proving the second.
Finally

\[
 M_0=\sum_{|S|=m}(\mu_0(S)-1)_++W_m-P,
\]

and \(W_m-N_1=W_m/(m+1)=o(W_m)\); (4.19) and (4.21)
now imply (4.22). \(\square\)

### Corollary 4.5 (unweighted asymptotic core)

For the parameter regime \(H<h\) with \(H/h=o(1)\), (SCI) is equivalent to
the existence of a whole-cycle family \(\mathcal F\) such that

\[
 \boxed{
 \sum_{|S|=m}|\mu_0(S)-1|
 +\sum_{q=1}^{H}
    \bigl(M_q^-(\mathcal F)+M_q^+(\mathcal F)\bigr)
 =o(W_m).}                                           \tag{4.25}
\]

Moreover every family satisfying (4.25) also has

\[
 M_0=o(W_m),\qquad
 \sum_{|S|=m-1}(\mu_1^-(S)-1)_+
 +\sum_{|S|=m+1}(\mu_1^+(S)-1)_+=o(W_m).             \tag{4.26}
\]

It also forces the coefficient-safe cycle count

\[
 |\mathcal F|=\frac{W_m}{2h}+o(W_m/h).               \tag{4.27}
\]

Thus the exact strip-cover LP gives a useful chronology-complete compiler and
removes exact ownership congruences, but its \(o(W_m)\) integrality gap is
asymptotically equivalent to the original missing-shadow synchronization
problem for an approximate middle factor.  It is not an independent generic
set-cover-rounding shortcut.

#### Proof

If (SCI) holds, (4.17) directly gives middle excess \(o(W_m)\), all holes at
depth at least two \(o(W_m)\), and, because
\(1-H/(2h)>1/2\), depth-one holes \(o(W_m)\).  Proposition 4.4 then gives
middle holes \(o(W_m)\), hence (4.25).

Conversely suppose (4.25).  Middle mass conservation gives
\(P\le W_m+o(W_m)\).  At depth one, (4.23) gives

\[
 E_1^-+E_1^+
 =M_1^-+M_1^++2(P-N_1)
 \le o(W_m)+2(W_m-N_1)+o(W_m)=o(W_m),                \tag{4.27}
\]

because \(W_m-N_1=W_m/(m+1)\).  Substitution in (4.17) proves
\(\mathfrak L_{H,h}(\mathcal F)=o(W_m)\), hence (SCI).  The same equations,
together with Proposition 4.4, prove (4.26).  Finally
\(2h|\mathcal F|=W_m-M_0+E_0=W_m+o(W_m)\), proving
(4.27). \(\square\)

## 5. Exact finite compiler and the coefficient-one theorem

Let

\[
 R_{m,H}=2\sum_{q=H+1}^{m}\binom{2m}{m-q}             \tag{5.1}
\]

be the number of masks outside the central band.

### Theorem 5.1 (finite strip-cover compiler)

For every \(1\le H<h<m\),

\[
 \boxed{\nu(2m)\le\tau_{m,H,h}+R_{m,H}.}             \tag{5.2}
\]

#### Proof

Take an optimal integral solution of (4.2). For each selected cycle, append
the literal block (3.5). For each \(S\in\mathcal B_{m,H}\) with \(z_S=1\),
append the one-letter block \(S\). By (4.2), every central-band target is
covered either inside a selected strip block or by its singleton repair. The
length used is exactly the objective in (4.2).

Finally append every nonempty mask outside \(\mathcal B_{m,H}\) once. (The
empty target requires no position under the convention defining \(\nu\).)
There are at most \(R_{m,H}\) such one-letter blocks, and they cover all
remaining required masks. All advertised witness intervals lie within an
individual block, so arbitrary concatenation is safe. This proves (5.2).
\(\square\)

### Lemma 5.2 (outer-tail estimate)

For \(H=\lceil\sqrt{m\log m}\rceil\),

\[
 R_{m,H}\le 2\,4^m e^{-H^2/m}
 \le \frac{2\,4^m}{m}=o(W_m).                        \tag{5.3}
\]

#### Proof

After division by \(4^m\), (5.1) is the two-sided tail probability of a
\(\operatorname{Bin}(2m,1/2)\) variable outside distance \(H\) from its mean.
Hoeffding's inequality gives the first bound. The second follows from the
choice of \(H\), and \(W_m=\Theta(4^m/\sqrt m)\) gives the last assertion.

Equivalently, (5.3) follows elementarily from

\[
 \frac{\binom{2m}{m-q}}{W_m}
 =\prod_{j=1}^{q}\frac{m-j+1}{m+j}
 \le \exp\!\left(-\frac{q^2}{m+q}\right)
\]

and a geometric summation of the remaining ratios. \(\square\)

### Theorem 5.3 (single sufficient hypothesis for coefficient one)

Use the parameters (1.1). If

\[
 \tau_{m,H,h}-\tau^*_{m,H,h}=o(W_m),                 \tag{5.4}
\]

then

\[
 \nu(2m)=(1+o(1))W_m.                                \tag{5.5}
\]

Consequently

\[
 \nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}        \tag{5.6}
\]

for all \(k\).

#### Proof

By Theorem 4.1, (1.2), and (5.4),

\[
 \tau_{m,H,h}
 \le W_m+\frac Hh\binom{2m}{m-1}+o(W_m)
 =W_m+o(W_m).                                         \tag{5.7}
\]

Theorem 5.1 and Lemma 5.2 give
\(\nu(2m)\le W_m+o(W_m)\). The middle-layer antichain gives the reverse
bound: witnesses for two distinct middle masks cannot have the same right
endpoint, because intervals with a common right endpoint are nested and their
ORs are comparable. Hence \(\nu(2m)\ge W_m\), proving (5.5).

For a new coordinate \(z\), concatenate an even-ground word, the singleton
\(\{z\}\), and a second copy in which \(z\) is adjoined to every letter. Thus

\[
 \nu(2m+1)\le2\nu(2m)+1.                             \tag{5.8}
\]

Since

\[
 \binom{2m+1}{m}=\frac{2m+1}{m+1}W_m,
\]

(5.5) implies (5.6). \(\square\)

## 6. The stronger exact-factor/owner-packed corollary

To compare directly with the existing Stage-A/Stage-B program, impose the
additional owner-packing constraints

\[
 \sum_{C:X\in\{X_t(C):t\in\mathbb Z_{2h}\}}x_C\le1
 \qquad\left(X\in\binom\Omega m\right).              \tag{6.1}
\]

For an integral owner-packed family \(\mathcal F\), let

\[
 B_H(\mathcal F)
 =\left|\mathcal B_{m,H}\setminus
       \bigcup_{C\in\mathcal F}\mathcal T_H(C)\right|. \tag{6.2}
\]

Because every selected cycle contains \(2h\) distinct middle owners,

\[
 2h|\mathcal F|\le W_m.                              \tag{6.3}
\]

Therefore the direct compiler gives the exact finite inequality

\[
 \nu(2m)
 \le W_m+\frac HhW_m+B_H(\mathcal F)+R_{m,H}.        \tag{6.4}
\]

In particular, the following stronger condition implies \((\mathrm{SCI})\)
and coefficient one:

\[
 \boxed{\text{there is an owner-packed }\mathcal F
        \text{ with }B_H(\mathcal F)=o(W_m).}         \tag{OP-FCR}
\]

The \(q=0\) summand in (6.2) already charges every uncovered middle owner.
Thus exact ownership equality, divisibility \(2h\mid W_m\), and coordinate-star
congruences are unnecessary; an \(o(W_m)\) residual is repaired literally.

Within the owner-disjoint whole-cycle architecture, \((\mathrm{OP\text{-}FCR})\)
is exactly the physical union-coverage gate. It is stronger than
\((\mathrm{SCI})\), because literal contiguous-OR realizability permits
recycling a middle mask in two different selected cycles as long as the total
output-length budget remains sharp.

## 7. Audit of the five proved ingredients

This section distinguishes strict implications from useful but noncomposing
evidence.

### 7.1 Explicit fixed-pair Stage A

For dyadic \(h=o(m)\), the fixed-pair theorem partitions every occupancy cube
of split dimension \(d\ge h\) into physical isometric \(C_{2h}\)'s. Its
middle leave obeys

\[
 \frac{L_{m,h}}{W_m}
 \le (2m+1)h\,2^{-m}
       \left(\frac{em}{h-1}\right)^{h-1}
 =\exp[-(\log2-o(1))m].                              \tag{7.1}
\]

For (1.1), it therefore supplies an explicit owner-disjoint integral family
with \(q=0\) leave \(o(W_m)\), cycle length \(2h\), and negligible
linearization toll \(HW_m/h=o(W_m)\).

What it does not supply is lower- or upper-target union coverage. Hence Stage
A proves the exact physical column supply and the middle ledger, but not
\((\mathrm{OP\text{-}FCR})\) or \((\mathrm{SCI})\).

The fractional cover in Theorem 4.1 does not require the full Stage-A factor:
one conjugacy orbit of physical strips already gives (4.7). Stage A remains
the strongest proved integral middle-only starting point.

### 7.2 Fixed-frame Stage B no-go

For one fixed unordered pairing and
\(q=\lfloor c\sqrt m\rfloor\), \(c>0\) fixed, the exact type-Hall deficit is

\[
 D_{m,q}
 =\sum_f(T_{f,q}-V_f)_+
 =(\delta(c)+o(1))W_m,                                \tag{7.2}
\]

where

\[
 \delta(c)=e^{-c^2}\Phi(c/2)-\Phi(-3c/2)>0.          \tag{7.3}
\]

Changing orders, tilings, or resolution classes inside that same pairing does
not remove the deficit. Therefore every owner-packed construction in which all
but \(o(W_m)\) middle starts (equivalently, owner occurrences) lie on cycles
of one fixed frame fails \((\mathrm{OP\text{-}FCR})\). Indeed, deleting
\(o(W_m)\) fixed-frame owners changes every type-supply ledger by at most
\(o(W_m)\), while \(o(W_m)\) outside-frame starts expose at most \(o(W_m)\)
targets at a fixed depth. Hence the \(\Theta(W_m)\) deficit in (7.2)
persists.

This no-go must not be applied to the weaker weighted cover (4.2). Program
(4.2) allows two selected cycles to reuse a middle owner and charges their
literal lengths instead. The capacity \(V_f\) responsible for (7.2) is then
no longer an owner capacity. No current fixed-frame report proves a positive
deficit for (4.2).

Thus the exact implication is

\[
 \text{fixed frame}\not\Rightarrow\mathrm{OP\text{-}FCR},          \tag{7.4}
\]

not

\[
 \text{fixed frame}\not\Rightarrow\mathrm{SCI}.                    \tag{7.5}
\]

The latter statement is presently unsupported.

### 7.3 Mixed-frame TU marginals

The mixed-frame theorem constructs a polynomial frame catalogue and an
integral assignment of every middle owner to a frame. Independently for every
depth and sign, it assigns every target to a frame/type bin whose demand is at
most its assigned owner supply. The critical slack is exact:

\[
 1-\rho_1=\frac1{m+1}.                               \tag{7.6}
\]

This removes the Gaussian pair-type capacity obstruction integrally and
simultaneously at the level of occurrence marginals.

It does **not** prove any of the following:

1. induced labelled face Hall inside a chosen bin;
2. a common nested prefix for choices made at different depths;
3. a common lower/upper cycle choice;
4. grouping all assigned occurrences into owner-disjoint \(C_{2h}\)'s; or
5. membership of the rounded marginal flow in the whole-cycle semigroup.

Consequently it proves integral feasibility of the pair-type marginal
relaxation of the stronger owner-packed problem, not that its chosen marginal
point is the image of a whole-cycle solution, and not
\((\mathrm{OP\text{-}FCR})\) itself. It is not needed for the validity of the
literal weighted cover theorem, whose orbit solution is already a whole-cycle
fractional solution.

### 7.4 Long-cycle associator

The local associator gives two six-cycle partitions of the same 24-set middle
support, with connected ownership overlap. Its depth-one action relative to
one frame is

\[
 16f_0+8f_1\longleftrightarrow24f_0
 \quad\text{on the lower side},                       \tag{7.7}
\]

\[
 16f_1+8f_2\longleftrightarrow24f_1
 \quad\text{on the upper side}.                       \tag{7.8}
\]

For every \(h\ge2\), the phase-compatible suspension replaces the six \(C_4\)'s
on each side by six vertex-disjoint physical \(C_{2h}\)'s on the same \(12h\)
middle vertices. Hence it supplies an exact integral kernel move of the
middle-incidence matrix and valid long columns of \(\mathscr C_{m,h}\).

It does not prove that these local moves pack globally, connect all required
factors, or control their labelled shadows simultaneously at every depth.
In (4.2), no reachability from a canonical factor is required; the associator
therefore enriches the explicit integral catalogue but does not round it.

### 7.5 Tensor packets and coarse capacity

Tensoring disjoint associator supports produces genuine chronology-coherent
packet columns. The audited coarse necessary condition for a lower
depth-\(q\) target is

\[
 Z(S)\ge r-q,                                         \tag{7.9}
\]

where \(Z(S)\) counts untouched selected 8-blocks. In the stated regimes,
the fraction failing this coarse condition is exponentially small. Exact
macroprofile flow has row sums \(V_k\), target column sums
\((W_m/N_q)T_\ell\), and its network matrix permits integral floor/ceiling
macroprofile quotas. Thus neither the 8-block eligibility statistic nor the
macroprofile marginal ledger gives an \(\Omega(W_m)\) obstruction.
This does not show that the rounded quota vector lies in the image of the
physical whole-cycle cone.

The consequences stop there. These results do not control

* overlaps between different packets or frames;
* collisions of the same physical labelled target across packets;
* the global selection of packet direction orders whose labelled targets
  cover across packets at every depth (the consecutive-window theorem supplies
  a valid common order inside each individual packet, but the coarse-capacity
  and macroprofile-flow results do not select those orders globally); or
* lifting a rounded macroprofile flow into the whole-cycle semigroup.

There are also two quantitative cautions.

First, the estimate deleting flags that use at least three coordinates of one
8-block is

\[
 O(W_mq^3/m^2)                                        \tag{7.10}
\]

at one depth. Its crude sum through
\(H=\sqrt{m\log m}\) is not \(o(W_m)\); therefore (7.10) alone cannot be cited
as an aggregate growing-window theorem.

Second, the least-power packet construction with active half-length
\(h=\Theta(H)\) incurs prefix toll

\[
 \frac HhW_m=\Theta(W_m).                             \tag{7.11}
\]

It proves local all-depth injectivity, not coefficient-one linearization.
The final theorem requires \(h/H\to\infty\), supplied at the column level by
the arbitrary-\(h\) associator suspension and, integrally in one frame, by the
dyadic Stage-A theorem.

## 8. Exact implication diagram

The rigorous chain is

\[
 \begin{array}{c}
 \text{owner-packed labelled fine cover with }o(W_m)\text{ holes}
 \\
 \Downarrow
 \\
 \tau_{m,H,h}\le W_m+(H/h)\binom{2m}{m-1}+o(W_m)
 \\
 \Downarrow
 \\
 \text{literal central-band OR word of length }W_m+o(W_m)
 \\
 \Downarrow
 \\
 \nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}.
 \end{array}                                           \tag{8.1}
\]

The first line can be weakened to the single additive integrality statement
\((\mathrm{SCI})\). The five named reports prove, respectively:

\[
 \begin{array}{c|c}
 \text{proved ingredient}&\text{exact force}\\ \hline
 \text{fixed-pair Stage A}&
 \text{integral middle-only near-factor and valid long columns}\\
 \text{fixed-frame Stage B}&
 \text{negative Hall cut for the fixed-frame owner-packed face}\\
 \text{mixed-frame TU}&
 \text{integral feasibility of the pair-type marginal relaxation}\\
 \text{long associator}&
 \text{bounded exact support-kernel move and arbitrary-length columns}\\
 \text{tensor coarse capacity}&
 \text{necessary coarse eligibility and macroprofile relaxations only}.
 \end{array}                                           \tag{8.2}
\]

There is no proved arrow from the positive relaxation/local-move statements
in (8.2), separately or together, to an integral labelled fine cover. In
particular, separate TU roundings at each depth cannot be composed after the
fact into one cycle choice.

## 9. Smallest remaining hypothesis

For the literal strip-block architecture, define the **strip-cover
integrality assertion** by (5.4). It is the smallest remaining hypothesis in
the following precise sense.

1. Every variable is already a complete physical chronology object.
2. Every constraint is a labelled target that must literally appear.
3. Every cost is the exact number of output letters used.
4. Uncovered middle owners, divisibility errors, congruence errors, and target
   holes are all represented by the same literal singleton repair columns.
5. An integral solution is converted to the final word without a further
   matching, scheduling, factorization, or synchronization lemma.
6. Conversely, every certified concatenation in which each band target is
   assigned to an advertised within-block witness or to an equal singleton is
   represented by a feasible integral solution of (4.2) with no larger
   objective. Accidental cross-seam witnesses are deliberately not credited
   in this restricted compiler; repeated identical strip or singleton blocks
   may first be deleted.

Thus the exact unresolved assertion for this compiler is

\[
 \boxed{
 \text{prove an additive }o(W_m)\text{ integrality gap for the labelled
 whole-strip cover (4.2).}}                           \tag{9.1}
\]

If future work remains inside one exact middle factor, replace (9.1) by the
stronger \((\mathrm{OP\text{-}FCR})\). The current TU, associator, and tensor
results remove important marginal and local obstructions to that stronger
statement, but the unresolved object is still the fine physical target
incidence matrix, not a type histogram or coarse packet ledger.

No coefficient-one conclusion is claimed here unconditionally. The proved
advance is the reduction of all remaining requirements in this route to the
single explicit additive integrality gap (5.4), together with the exact
fractional value (4.3) and a literal finite compiler.
