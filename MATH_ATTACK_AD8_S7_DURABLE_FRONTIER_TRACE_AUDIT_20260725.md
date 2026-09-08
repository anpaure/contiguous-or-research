# AD8: S7 cross-audit and durable-frontier trace localization

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running local job is used.

## 0. Outcome and exact boundary

Put

\[
n=2m,\qquad W=\binom{2m}{m},\qquad
N_q=\binom{2m}{m-q},\qquad
B=\frac{W}{m+1},
\]

and let \(1\le H<m\).  For the Gaussian application,
\(H=\lceil A\sqrt m\rceil\) with fixed \(A>0\).

This report has two parts.

First, it cross-audits the three S7 reports.  The triangular tube
coefficient is correct:

\[
\boxed{
\Delta_q^\pm\le\sum_{s=0}^{q-1}(q-s)k_s.}
\tag{0.1}
\]

There is no missing factor two.  A cut first made at layer \(s\) can occur
at exactly the \(q-s\) offsets

\[
0,1,\ldots,q-1-s
\]

of a depth-\(q\) tube.  The dual coefficient
\(1/[H(H+1)]\) is also exact.

The printed durable-edge identity, however, has one material definitional
error.  Edges of common lifetime zero are durable vacuously under the
printed predicate, even though they are absent from the baseline
\(E^\circ\).  The required definition is

\[
E^{\rm dur}(\mathbf L,\mathbf R)
\subseteq E^\circ.
\tag{0.2}
\]

With this correction, and only with this correction, the exact identity is

\[
\boxed{
K_H^{\min}
=|E^\circ|-
\max_{\mathbf L,\mathbf R}|E^{\rm dur}(\mathbf L,\mathbf R)|.}
\tag{0.3}
\]

Two further proof corrections are needed in the tube report: the
\(t=0\) case in its crossing-edge injection must be separated, and
distinct departure coordinates alone do not imply that a tube is
rank-good.  The intended odd-cut conclusion is valid because those paths
are complementary Johnson geodesics and hence are fully no-return.

Second, this report uses the corrected durable maximization to attack the
AD useful-prefix trace gate.  Fix a feasible flag pair, let \(D\) be its
nondurable positive-lifetime edges, put

\[
K=|D|,
\qquad G=F_0-D,
\qquad C=B+K.
\tag{0.4}
\]

The \(C\) components of \(G\) have one literal radius-\(H\)
useful-prefix word of exact length

\[
\boxed{W+2HC,}
\tag{0.5}
\]

and every original first-band meet and join remains literal, including at
the \(K\) new seams.

At depth \(q\), all masks not certified by a clean durable cone are
localized to the first or last \(q\) active owners of the components of
\(G\).  If

\[
\ell_{P,q}=|P\cap X_q|,
\qquad
\beta_q^G=\sum_{P\in\operatorname{Comp}(G)}min\{q,\ell_{P,q}\},
\tag{0.6}
\]

then the resulting integral repair envelope \(\mathcal E_D\) has the
exact size

\[
\boxed{
|\mathcal E_D|
=2\sum_{q=2}^H\beta_q^G
\le C\,[H(H+1)-2].}
\tag{0.7}
\]

The true hole family of the word in (0.5) is a subfamily of
\(\mathcal E_D\).  Thus this is a causal localization theorem, not an
assertion that every envelope mask is genuinely absent.

For every marked set \(Z\), the owner flags give the new upper bound

\[
\boxed{
\Phi_Z(\mathcal H)
\le (\nu(n-|Z|)+1)
\sum_v
\min\{r_v,1+|Z\cap Q_v|\},}
\tag{0.8}
\]

for every \(\mathcal H\subseteq\mathcal E_D\), where \(r_v\) is the
number of masks assigned to owner \(v\), and \(Q_v\) is the coordinate
interval crossed by its saturated flag.  This converts trace condensation
into a concrete high-incidence coordinate-selection problem.

There is also a sharp cross-component obstruction.  Put

\[
B_H=H(H+1)-2.
\tag{0.9}
\]

If \(\rho_Z\) is the largest number of distinct durable components
contributing to one \(Z\)-trace, then

\[
\boxed{
\Phi_Z(\mathcal H)
\ge |\mathcal H|
\min\left\{1,
\frac{\nu(n-|Z|)}{B_H\rho_Z}
\right\}.}
\tag{0.10}
\]

Consequently, a linear hole family with \(\Phi_Z=o(W)\) requires one trace
packet meeting

\[
\boxed{
\omega\!\left(\frac{\nu(n-|Z|)}{H^2}\right)}
\tag{0.11}
\]

distinct durable components.  The corresponding cross-component energy
bound is

\[
\boxed{
E_{Z,\mathrm{cross}(G)}^\times
\ge
\nu(n-|Z|)(|\mathcal H|-\Phi_Z(\mathcal H))
-\frac{H(H+1)-3}{2}|\mathcal H|.}
\tag{0.12}
\]

Thus one durable component, one endpoint flag, or one triangular boundary
cone cannot supply the necessary trace condensation when
\(\nu(n-|Z|)\gg H^2\).

Finally, if replacement of the frozen radius-\(H\) facet-core word is
allowed, the trace gate disappears exactly.  Cutting \(D\) and the at most
\(H\) genuine lifetime-change edges gives constant-radius rotor paths and
a literal zero-hole word of length

\[
\boxed{
L_{\rm var}
=W+2\sum_S r(S)
\le W+2H(B+K+H).}
\tag{0.13}
\]

This replacement exposes every flag of the exact band SCD at one shared
endpoint.  It need not preserve each original facet-braid colour at its
old edge seam.  Therefore it bypasses, but does not prove, trace
condensation for the frozen fixed-depth word.

No estimate \(K_H^{\min}=o(W/H)\) is proved.  No constant-one conclusion
is claimed.

---

## 1. Corrected audit of the durable-edge identity

Let \(F_0\) be a directed path forest on the middle owners, let
\(\tau(v)\in\{0,\ldots,H\}\) be their prescribed lifetimes, and put

\[
r(e)=\min\{\tau(v),\tau(w)\}
\qquad(e=v\to w).
\tag{1.1}
\]

The edge is ever present in an active induced forest exactly when
\(r(e)\ge1\).  Thus the correct initial baseline is

\[
E^\circ=\{e\in E(F_0):r(e)\ge1\}.
\tag{1.2}
\]

For feasible lower and upper-complement flag systems
\((\mathbf L,\mathbf R)\), define

\[
\boxed{
\begin{aligned}
E^{\rm dur}(\mathbf L,\mathbf R)
=\{e=v\to w\in E^\circ:{}&
L_{h+1}(v)=L_h(v)\cap L_h(w),\\
&R_{h+1}(w)=R_h(v)\cap R_h(w)\\
&\text{for every integer }0\le h<r(e)\}.
\end{aligned}}
\tag{1.3}
\]

The restriction \(e\in E^\circ\) is essential.

### Proposition 1.1 (exact counterexample to the printed definition)

Take \(m=H=1\).  The middle layer of \(B_2\) has two owners.  Orient its
single Johnson edge and assign lifetime zero to one endpoint and lifetime
one to the other.  Then

\[
E^\circ=\varnothing,
\qquad K_1^{\min}=0.
\tag{1.4}
\]

Both flag systems exist uniquely.  Under the printed predicate, the single
initial edge is nevertheless durable because the requirement
\(0\le h<r(e)=0\) is empty.  The printed right side therefore equals

\[
0-1=-1,
\]

contradicting \(K_1^{\min}=0\).

#### Proof

The prescribed multiplicities are

\[
c_0=N_0-N_1=2-1=1,
\qquad N_1=1.
\]

Thus the lifetime assignment is legal.  Since the two endpoints are never
simultaneously active at depth one, there is no active edge to delete.
The unique active owner maps to the empty lower endpoint and to the empty
upper-complement endpoint.  Hence the flags are feasible and (1.4) holds.
The vacuous durability conclusion is immediate. \(\square\)

### Theorem 1.2 (repaired exact first-failure identity)

If both flag families are nonempty, then

\[
\boxed{
K_H^{\min}
=|E^\circ|-
\max_{\mathbf L,\mathbf R}
|E^{\rm dur}(\mathbf L,\mathbf R)|.}
\tag{1.5}
\]

If either flag family is empty, the recursive extension is infeasible and
the right side is left undefined.

#### Proof

Fix feasible flags and impose maximal retention.  For
\(e\in E^\circ\), let \(f(e)\) be the least integer
\(0\le h<r(e)\) at which at least one identity in (1.3) fails, and put
\(f(e)=\infty\) when no such level exists.

The exact one-edge lift rule says inductively that \(e\) remains in the
retained forest through precisely the levels before \(f(e)\).  If
\(f(e)<\infty\), it is charged exactly once, at its first failed level.
If \(f(e)=\infty\), it remains until an endpoint stops and is never
charged.  Hence, for these flags,

\[
K_H(\mathbf L,\mathbf R)
=|\{e\in E^\circ:f(e)<\infty\}|
=|E^\circ|-|E^{\rm dur}(\mathbf L,\mathbf R)|.
\tag{1.6}
\]

Deleting a presently liftable edge cannot improve future flag feasibility:
retain it until its first later failure, if any, and move its unique charge
to that level.  The retained graph remains a subforest of \(F_0\), so no
branch or cycle is created.  Thus maximal retention loses nothing.
Minimizing (1.6) over feasible flag pairs proves (1.5). \(\square\)

For the path-contiguous odd-cut order, \(X_1\) is a global suffix and its
intersection with each initial path is a suffix run.  If \(b_{A,0}\) is
the number of nonempty such runs, then

\[
\boxed{
|E^\circ|=|E(F_0[X_1])|=N_1-b_{A,0},
\qquad 1\le b_{A,0}\le B.}
\tag{1.7}
\]

This floor uses path-contiguous ordering.  It is not valid for an arbitrary
permutation of the owners.

---

## 2. Audit of the triangular tube and cone inequalities

Fix a depth \(q\).  A baseline lower tube has edges at offsets
\(t=0,\ldots,q-1\), and the edge at offset \(t\) must survive through
layer \(q-1-t\).  If an edge is first cut at layer \(s\), that cut can
destroy the tube only when

\[
s\le q-1-t,
\]

or equivalently

\[
0\le t\le q-1-s.
\tag{2.1}
\]

There are exactly \(q-s\) possible offsets.

### Theorem 2.1 (audited triangular inequality)

For every actual no-reintroduction recursive lift,

\[
\boxed{
\Delta_q^-
\le\sum_{s=0}^{q-1}(q-s)k_s,
\qquad
\Delta_q^+
\le\sum_{s=0}^{q-1}(q-s)k_s.}
\tag{2.2}
\]

#### Proof

For a fixed edge and fixed offset, a directed path forest has at most one
length-\(q\) tube containing the edge at that offset.  Thus one edge first
cut at level \(s\) destroys at most \(q-s\) tubes of either orientation.

After all destroyed tubes are removed, every surviving tube is transported
to an actual depth-\(q\) endpoint.  Exact rank ownership makes those actual
endpoints pairwise distinct; tube transport makes each one equal to its
canonical tube target.  Thus the survivors are rank-good and simple.
Since \(\Delta_q^\pm\) is the minimum number of tubes that must be removed
to obtain such a family, (2.2) follows. \(\square\)

No factor two belongs in either inequality.  The two signs use the same cut
ledger but are separate assertions.  When they are added with weights, the
coefficient of \(k_s\) is

\[
\sum_{q=s+1}^H(q-s)(\theta_q^-+\theta_q^+).
\tag{2.3}
\]

In particular, taking

\[
\theta_q^-=	heta_q^+=\frac1{H(H+1)}
\]

is feasible because at \(s=0\)

\[
\frac{2}{H(H+1)}\sum_{q=1}^Hq=1,
\tag{2.4}
\]

and every later capacity is smaller.  Therefore

\[
K_H\ge
\frac1{H(H+1)}
\sum_{q=1}^H(\Delta_q^-+\Delta_q^+)
\tag{2.5}
\]

has the correct constant.

### 2.1 Correction to the floor-exact baseline proof

In the proof of the general baseline estimate, let \(t\) be the first
failed offset for a start \(v_0\in\mathcal V_q\).

If \(t=0\), one knows only

\[
v_0\in\mathcal V_q.
\]

Failure of the first edge means \(v_1\notin\mathcal V_q\), so that edge
crosses the stage-\((q-1)\) active cut.

If \(t\ge1\), the preceding successful edge lies in
\(G_{q-t}\), and hence

\[
v_t\in\mathcal V_{q-t+1}\subseteq\mathcal V_{q-t}.
\]

Failure at offset \(t\) then means
\(v_{t+1}\notin\mathcal V_{q-t}\).  This is the required crossing at
stage \(q-t-1\).  Thus the crossing-edge injection and the stated baseline
bound remain correct, but the printed assertion
\(v_t\in\mathcal V_{q-t+1}\) cannot be used at \(t=0\).

For a global suffix intersecting the directed paths in suffix runs of
lengths \(\ell_i\), the exact common lower/upper internal-window count is

\[
\sum_i(\ell_i-q)_+
=N_q-\sum_i\min\{q,\ell_i\}.
\tag{2.6}
\]

Hence the common discarded-window floor is exactly

\[
\boxed{\beta_q=\sum_i\min\{q,\ell_i\}\le qB.}
\tag{2.7}
\]

There is no extra \(+q\), \(+1\), or second boundary term.

### 2.2 Correction to the rank-good scope

Distinct departures do not by themselves make a tube rank-good.  For
example,

\[
\{1,2\}\to\{2,3\}\to\{2,4\}
\tag{2.8}
\]

has distinct departures \(1,3\), but its three-vertex intersection is
\(\{2\}\), whereas \(m-q=0\).

The intended odd-cut conclusion is valid for the stronger reason that an
odd-cut path is a length-\(m\) geodesic from a middle set to its complement.
Every departure is a distinct element of the initial set, every arrival is
a distinct element of its complement, and no arrival is later departed.
Consequently every forward intersection and every backward complementary
union has the required rank.

### 2.3 Cone-report verdict

The clean-cone recursion, duplicate-excess inequality, collision
transversal, and exact cyclic boundary allowance in the cone report are
correct.  In particular, one first-cut event at level \(s\) lies in at
most \(q-s\) depth-\(q\) cones of either orientation, and

\[
(\bar\delta_q^\pm-\beta_q)_+
\le\sum_{s<q}(q-s)k_s
\tag{2.9}
\]

has the stated floor.  Its hypergraph transversal is only a necessary
condition.  It neither produces the two boundary SDRs nor constructs a
band SCD.

All inequalities in this section concern an actual
\(K_H=\sum_s k_s\).  They may be minimized over flag histories only while
the initial forest and active sets, and hence the canonical defect vector,
are fixed.  A fixed defect cannot be carried through a minimization that
also varies the path order or lifetime assignment.

---

## 3. Durable components and the exact frontier envelope

We now specialize to the exact odd-cut input.  The initial forest \(F_0\)
has

\[
B=\frac{W}{m+1}
\tag{3.1}
\]

complementary no-return Johnson paths.  Its \(N_1=W-B\) lower edge colours
and its \(N_1\) upper edge colours separately exhaust the complete first
band.

Concatenate the paths and prescribe the lifetime blocks in that order, so
that

\[
X_q=\{v:\tau(v)\ge q\}
\tag{3.2}
\]

is one global suffix of size \(N_q\) for every \(q\).

Assume both exact flag families are nonempty, fix a flag pair, and define

\[
D=E^\circ\setminus E^{\rm dur}(\mathbf L,\mathbf R),
\qquad K=|D|.
\tag{3.3}
\]

Cut all edges in \(D\) at depth zero and put

\[
G=F_0-D.
\tag{3.4}
\]

Since \(F_0\) is a forest, every cut adds one component, and hence

\[
\boxed{|\operatorname{Comp}(G)|=C=B+K.}
\tag{3.5}
\]

Every component of \(G\) is an interval in one original path and hence an
interval of the global concatenation.

For \(v\in X_q\), call \(v\) lower clean at depth \(q\) when it has
\(q\) directed successors in the same component of \(G\), all belonging
to \(X_q\).  Call it upper clean when it has \(q\) directed predecessors
with the same property.  Let

\[
\mathcal D_q^-,\qquad \mathcal D_q^+
\tag{3.6}
\]

be the corresponding dirty active owners.

For \(P\in\operatorname{Comp}(G)\), put

\[
\ell_{P,q}=|P\cap X_q|.
\tag{3.7}
\]

Because \(X_q\) is a global suffix, \(P\cap X_q\) is empty, all of
\(P\), or a suffix run of \(P\).

### Lemma 3.1 (exact dirty-frontier count)

For every \(1\le q\le H\),

\[
\boxed{
|\mathcal D_q^-|
=|\mathcal D_q^+|
=\beta_q^G
:=\sum_{P\in\operatorname{Comp}(G)}
\min\{q,\ell_{P,q}\}.}
\tag{3.8}
\]

#### Proof

Inside an active suffix run of length \(\ell\), exactly
\((\ell-q)_+\) owners have \(q\) successors.  Therefore the number
lacking them is

\[
\ell-(\ell-q)_+=\min\{q,\ell\}.
\]

Reading the same run backward gives the identical predecessor count.
Summing over components proves (3.8). \(\square\)

Write

\[
U_q(v)=[n]\setminus R_q(v)
\tag{3.9}
\]

for the actual upper endpoint of the flag chain.

### Lemma 3.2 (clean durable cones equal actual flags)

If \(v\in X_q\) is lower clean, the radius-\(H\) canonical word on its
component exposes

\[
L_q(v).
\tag{3.10}
\]

If \(v\) is upper clean, it exposes

\[
U_q(v).
\tag{3.11}
\]

#### Proof

Take the directed \(q\)-window beginning at a lower-clean owner.  Every
edge of the window has both endpoints in \(X_q\), and hence has common
lifetime at least \(q\).  It does not lie in \(D\), so it satisfies both
durability identities at every level needed by the triangular cone.
Iterating the lower intersection identity gives

\[
L_q(v)=\bigcap_{i=0}^q X_{v_i},
\tag{3.12}
\]

which is precisely the canonical lower useful-prefix mask.

The reflected predecessor argument gives

\[
R_q(v)=\bigcap_{i=0}^q X_{v_{-i}}^c,
\]

and complementation yields the canonical upper union (3.11). \(\square\)

Define the signed-rank repair envelope

\[
\boxed{
\mathcal E_D
=\bigsqcup_{q=2}^H
\left(
\{L_q(v):v\in\mathcal D_q^-\}
\sqcup
\{U_q(v):v\in\mathcal D_q^+\}
\right).}
\tag{3.13}
\]

At a fixed signed rank, the masks in (3.13) are distinct because the
actual endpoint maps are bijections.  Different signed ranks have
different cardinalities.  Thus (3.13) is a family of distinct masks.

### Theorem 3.3 (durable-frontier localization)

There is one literal radius-\(H\) useful-prefix word \(\mathcal W_G\)
of exact length

\[
\boxed{|\mathcal W_G|=W+2H(B+K)}
\tag{3.14}
\]

such that:

1. every middle mask is a principal endpoint;
2. every original first-band meet and join is a literal interval OR;
3. the true family \(\mathcal H_G\) of missing masks in signed depths
   \(2,\ldots,H\) satisfies
   \[
   \boxed{\mathcal H_G\subseteq\mathcal E_D;}
   \tag{3.15}
   \]
4. for every proper \(Z\subset[n]\),
   \[
   \boxed{
   L_{\rm band}
   \le W+2H(B+K)+\Phi_Z(\mathcal E_D).}
   \tag{3.16}
   \]

#### Proof

Every component of \(G\) is a no-return geodesic piece.  Independently
reverse-write its \(2H+1\) useful blocks and then use one MTF update per
remaining owner.  A component with \(t\) owners has exact word length
\(t+2H\).  Summing over the \(C=B+K\) components proves (3.14).

An uncut original edge exposes its ordinary canonical meet and join.  At a
cut edge

\[
v\to w=v-\{p\}+\{a\},
\]

choose \(p\) as the left piece's first terminal dummy departure and as the
right piece's first initial upper singleton.  The left terminal lower flag
is

\[
v-\{p\}=v\cap w,
\]

and the right initial upper flag is

\[
w\cup\{p\}=v\cup w.
\]

Both are literal suffix intervals and use no extra position.  The incoming
and outgoing prescriptions on a piece are independent.  Since the original
edge colours exhaust both first-band ranks, item 2 follows.

Let \(S\) be a lower rank-\((m-q)\) target absent from
\(\mathcal W_G\).  Exact endpoint ownership gives a unique
\(v\in X_q\) with \(L_q(v)=S\).  If \(v\) were lower clean, Lemma 3.2
would put \(S\) in the word.  Thus \(v\in\mathcal D_q^-\).  The upper
argument is identical.  This proves (3.15).

The fixed-trace cylinder word for \(\mathcal E_D\) covers every member of
the envelope and hence every true hole.  Appending it to
\(\mathcal W_G\) proves (3.16).  Every step is integral and every
certificate is a literal interval. \(\square\)

The theorem does not assert equality in (3.15): a dirty actual endpoint can
already occur incidentally as another canonical interval.

### Corollary 3.4 (exact envelope size and its unavoidable boundary scale)

Put

\[
B_H=2\sum_{q=2}^Hq=H(H+1)-2.
\tag{3.17}
\]

Then

\[
\boxed{
|\mathcal E_D|
=2\sum_{q=2}^H\beta_q^G
\le (B+K)B_H.}
\tag{3.18}
\]

Moreover,

\[
\boxed{
|\mathcal E_D|
\ge
\left\lfloor\frac{N_H}{m+1}\right\rfloor B_H.}
\tag{3.19}
\]

For fixed \(A>0\) and \(H=\lceil A\sqrt m\rceil\),

\[
\left\lfloor\frac{N_H}{m+1}\right\rfloor B_H
=\bigl(A^2e^{-A^2}+o_A(1)\bigr)W.
\tag{3.20}
\]

#### Proof

Equation (3.8) gives the equality in (3.18), and
\(\min\{q,\ell_{P,q}\}\le q\) gives its upper bound.

The global suffix \(X_H\), of size \(N_H\), contains at least

\[
\left\lfloor\frac{N_H}{m+1}\right\rfloor
\]

whole original odd-cut paths.  Fix one.  It lies in every \(X_q\) for
\(q\le H\).  If cuts in \(D\) divide its \(m+1\) vertices into lengths
\(a_1,\ldots,a_j\), then

\[
\sum_i\min\{q,a_i\}
\ge\min\left\{q,\sum_i a_i\right\}=q.
\]

Thus each whole path contributes at least \(2q\) to the two frontiers at
depth \(q\), proving (3.19).

Finally,

\[
\frac{N_H}{W}
=\prod_{i=0}^{H-1}\frac{m-i}{m+i+1}
=e^{-A^2+o_A(1)},
\qquad
\frac{B_H}{m+1}=A^2+o_A(1).
\]

The floor error contributes only \(O_A(m)=o(W)\), proving (3.20).
\(\square\)

Equation (3.20) is a lower bound for the certified repair envelope, not for
the true hole family.  It proves that small \(K\), even formally \(K=0\),
does not make the durable-frontier envelope sublinear by cardinality alone.
Trace sharing or variable-radius replacement is indispensable.

---

## 4. An exact coordinate-incidence sufficient condition

Let \(\mathcal H\subseteq\mathcal E_D\) be any subfamily; this may be the
true hole family or the full envelope.  Assign each mask to its owner in
(3.13), and write

\[
\mathcal H(v)=\{S\in\mathcal H:S\text{ is assigned to }v\},
\qquad r_v=|\mathcal H(v)|.
\tag{4.1}
\]

For \(h\le\tau(v)\), the actual owner flag is the saturated chain

\[
L_h(v)\subset\cdots\subset L_1(v)\subset v
\subset U_1(v)\subset\cdots\subset U_h(v).
\tag{4.2}
\]

Put

\[
Q_v=U_{\tau(v)}(v)\setminus L_{\tau(v)}(v).
\tag{4.3}
\]

Every mask in \(\mathcal H(v)\) lies on this one chain, and
\(|Q_v|=2\tau(v)\le2H\).

### Lemma 4.1 (trace changes along one owner flag)

For \(Z\subset[n]\), the masks in \(\mathcal H(v)\) occupy at most

\[
\boxed{
c_v(Z)=\min\{r_v,1+|Z\cap Q_v|\}}
\tag{4.4}
\]

distinct \(Z\)-traces.

#### Proof

Order the selected masks along the saturated chain (4.2).  Consecutive
chain masks differ by one coordinate.  Their traces change only when that
coordinate belongs to \(Z\).  All coordinates crossed between selected
masks lie in \(Q_v\), and each is crossed once.  Hence there are at most
\(1+|Z\cap Q_v|\) trace states and at most \(r_v\) selected masks.
\(\square\)

### Theorem 4.2 (durable-frontier trace-incidence bound)

Let \(d=n-|Z|\ge1\).  Then

\[
\boxed{
\Phi_Z(\mathcal H)
\le(\nu(d)+1)\sum_v c_v(Z).}
\tag{4.5}
\]

Consequently, for each fixed \(1\le d\le n\),

\[
\boxed{
\min_{|Z|=n-d}\Phi_Z(\mathcal H)
\le
(\nu(d)+1)
\min_{|Y|=d}
\sum_v
\min\{r_v,1+|Q_v\setminus Y|\}.}
\tag{4.6}
\]

#### Proof

Let \(\mathcal T_Z\) be the set of occupied traces.  Since

\[
\min\{h_R,\nu(d)+\mathbf1_{R\ne\varnothing}\}
\le\nu(d)+1,
\]

one has

\[
\Phi_Z(\mathcal H)\le(\nu(d)+1)|\mathcal T_Z|.
\]

The number of global occupied traces is at most the sum of the numbers
occupied by the individual owners.  Lemma 4.1 gives (4.5).  Put
\(Y=[n]\setminus Z\) to obtain (4.6). \(\square\)

There is a simpler incidence relaxation.  Put

\[
\mathcal U=\{v:r_v>0\},
\qquad
a_x=|\{v\in\mathcal U:x\in Q_v\}|.
\tag{4.7}
\]

Then

\[
\sum_v\min\{r_v,1+|Q_v\setminus Y|\}
\le
|\mathcal U|+\sum_{x\notin Y}a_x.
\tag{4.8}
\]

Therefore

\[
\boxed{
\begin{aligned}
\min_{|Z|=n-d}\Phi_Z(\mathcal H)
\le(\nu(d)+1)\Bigg(
|\mathcal U|+\sum_xa_x
-\max_{|Y|=d}\sum_{x\in Y}a_x
\Bigg).
\end{aligned}}
\tag{4.9}
\]

The expression in parentheses is the exact optimum of the coarse bound
in (4.8): choose the \(d\) coordinates of largest total flag-interval
incidence for the unmarked complement \(Y\).

### Lemma 4.3 (exceptional-owner union)

For the full envelope,

\[
\boxed{
|\mathcal U|
\le2HC+\sum_{q=2}^Hq
=2H(B+K)+\frac{H(H+1)}2-1.}
\tag{4.10}
\]

#### Proof

For a fixed component, every lower-dirty owner at every depth lies among
its last \(H\) vertices.  This contributes at most \(HC\) owners.

For upper-dirty owners, if a component is fully active at depth \(q\),
its dirty owners lie among its first \(q\le H\) vertices.  Their union over
all such depths contributes at most another \(HC\).  At each depth \(q\),
at most one component is cut internally by the single global suffix
boundary.  Its moving initial active frontier contributes at most \(q\)
additional owners.  Summing over \(q=2,\ldots,H\) proves (4.10).
\(\square\)

Equations (3.16), (4.6), and (4.10) give a proved sufficient gate:
if, for the maximizing durable flags, some sequence \(d=d(m)\) satisfies

\[
H(B+K)
+(\nu(d)+1)
\min_{|Y|=d}
\sum_v\min\{r_v,1+|Q_v\setminus Y|\}
=o(W),
\tag{4.11}
\]

then the fixed-depth facet-core word covers the whole Gaussian band with
length \(W+o(W)\).  This is a literal integral theorem.  Condition (4.11)
is unproved.

---

## 5. Minimum cross-component portal degree

This section applies to the true hole family
\(\mathcal H\subseteq\mathcal E_D\).  Partition it according to the
component of \(G\) containing its assigned owner.

### Lemma 5.1 (sharp component packet size)

Every component contributes at most

\[
\boxed{B_H=H(H+1)-2}
\tag{5.1}
\]

masks to \(\mathcal E_D\), and hence at most that many true holes.

#### Proof

At depth \(q\), a component has at most \(q\) lower-dirty and at most
\(q\) upper-dirty active owners.  Summing over \(2\le q\le H\) gives

\[
2\sum_{q=2}^Hq=B_H.
\]

This bound is attained at the level of the frontier ledger whenever the
component is active and has at least \(q\) vertices at every relevant
depth. \(\square\)

For a marked set \(Z\), define the durable-component portal degree

\[
\rho_Z
=\max_{R\subseteq Z}
|\{P\in\operatorname{Comp}(G):
P\text{ contributes a member of }\mathcal H
\text{ with trace }R\}|.
\tag{5.2}
\]

### Theorem 5.2 (exact portal-degree lower bound)

Let \(M=|\mathcal H|\) and \(d=n-|Z|\ge1\).  Then

\[
\boxed{
\Phi_Z(\mathcal H)
\ge
M\min\left\{1,
\frac{\nu(d)}{B_H\rho_Z}
\right\}.}
\tag{5.3}
\]

When \(M>0\), one has \(\rho_Z\ge1\), so the quotient is defined.

#### Proof

For every trace \(R\), Lemma 5.1 gives

\[
h_R\le B_H\rho_Z.
\tag{5.4}
\]

Also its repair cap satisfies

\[
\ell_R=\nu(d)+\mathbf1_{R\ne\varnothing}\ge\nu(d).
\]

Thus

\[
\min\{h_R,\ell_R\}
\ge h_R
\min\left\{1,
\frac{\nu(d)}{B_H\rho_Z}
\right\}.
\]

Sum over \(R\) to prove (5.3). \(\square\)

### Corollary 5.3 (minimum unbounded portal degree)

Suppose, along a sequence of instances,

\[
M\ge cW
\]

for a fixed \(c>0\), while \(\Phi_Z(\mathcal H)=o(W)\).  Then

\[
\boxed{
\frac{B_H\rho_Z}{\nu(d)}\longrightarrow\infty.}
\tag{5.5}
\]

In particular,

\[
\boxed{
\rho_Z
=\omega\!\left(\frac{\nu(d)}{H^2}\right).}
\tag{5.6}
\]

#### Proof

Divide (5.3) by \(M\).  The left side tends to zero because
\(M\ge cW\), so the second argument of the minimum must tend to zero.
This is (5.5), and \(B_H=\Theta(H^2)\) gives (5.6). \(\square\)

The \(H^2\) local scale cannot be improved from durable-frontier
information alone: Lemma 5.1 gives exactly \(B_H\) possible demands in
one component, and a saturated flag may change its marked trace at every
selected depth.

---

## 6. Cross-component trace energy

Let

\[
E_Z^\times(\mathcal H)
=\sum_{R\subseteq Z}
\sum_{\alpha<\beta}h_{\alpha,R}h_{\beta,R}
\tag{6.1}
\]

be the same-trace energy between distinct signed-rank layers.  Split it as

\[
E_Z^\times
=E_{Z,\mathrm{int}(G)}^\times
+E_{Z,\mathrm{cross}(G)}^\times,
\tag{6.2}
\]

according to whether the two masks are assigned to the same or to distinct
components of \(G\).

The exact trace-energy theorem gives

\[
E_Z^\times
\ge\nu(d)(M-\Phi_Z(\mathcal H)).
\tag{6.3}
\]

### Theorem 6.1 (durable cross-component energy obstruction)

For every true hole family \(\mathcal H\subseteq\mathcal E_D\),

\[
\boxed{
E_{Z,\mathrm{cross}(G)}^\times
\ge
\nu(d)(M-\Phi_Z(\mathcal H))
-\frac{B_H-1}{2}M.}
\tag{6.4}
\]

Equivalently, since \(B_H-1=H(H+1)-3\), this is (0.12).

#### Proof

If component \(P\) contributes \(M_P\) holes, then
\(M_P\le B_H\) by Lemma 5.1.  Its internal cross-rank energy is at most
the total number of unordered pairs of its masks:

\[
E_{Z,P}^\times
\le\binom{M_P}{2}
\le\frac{B_H-1}{2}M_P.
\]

Summing over components gives

\[
E_{Z,\mathrm{int}(G)}^\times
\le\frac{B_H-1}{2}M.
\]

Subtract this from (6.3) and use (6.2). \(\square\)

### Corollary 6.2 (local cones cannot supply supercritical energy)

If

\[
M\ge cW,
\qquad
\Phi_Z(\mathcal H)=o(W),
\qquad
\frac{\nu(d)}{H^2}\longrightarrow\infty,
\tag{6.5}
\]

then

\[
\boxed{
E_{Z,\mathrm{cross}(G)}^\times
\ge(1-o(1))\nu(d)M.}
\tag{6.6}
\]

Thus essentially all of the trace energy demanded by condensation must
pair different durable components.  Owner-vertical nesting and
single-component frontier triangles are asymptotically negligible on this
scale.

For completeness, owner-vertical energy has an exact local floor as well.
If one owner contributes \(r\) masks occupying at most \(c\) traces, write

\[
r=ac+b,
\qquad0\le b<c.
\]

The minimum number of its same-trace pairs is

\[
\boxed{
\operatorname{Bal}(r,c)
=b\binom{a+1}{2}+(c-b)\binom a2.}
\tag{6.7}
\]

Indeed the occupancy numbers minimize their sum of binomial pairs when
they differ by at most one.  Lemma 4.1 permits
\(c=c_v(Z)\).  This vertical floor is real, but Theorem 6.1 proves that it
cannot replace cross-component alignment when \(\nu(d)\gg H^2\).

---

## 7. Exact zero-hole variable-radius replacement

The fixed-depth theorem above preserves the original facet braid but leaves
the trace gate (4.11).  If one permits a global replacement by the actual
flag states, durability gives a different exact conclusion.

Let

\[
J=\{e=v\to w\in E(F_0):\tau(v)\ne\tau(w)\}.
\tag{7.1}
\]

Because the lifetime classes \(0,1,\ldots,H\) are globally contiguous in
the concatenated order, each of their \(H\) interfaces crosses at most one
genuine path edge.  Hence

\[
\boxed{|J|\le H.}
\tag{7.2}
\]

Cut all edges in \(D\cup J\).  Every resulting segment \(S\) has one
constant lifetime, denoted \(r(S)\).  There are at most

\[
B+K+H
\tag{7.3}
\]

segments.

### Theorem 7.1 (literal variable-radius durable replacement)

The segments above have one literal word of exact length

\[
\boxed{
L_{\rm var}
=W+2\sum_Sr(S)}
\tag{7.4}
\]

and therefore

\[
\boxed{
L_{\rm var}
\le W+2H(B+K+H).}
\tag{7.5}
\]

At the principal endpoint of every owner \(v\), the word exposes the
entire exact flag chain of radius \(\tau(v)\).  Consequently every mask in
the depth-\(H\) central band is represented and the resulting hole family
is empty.

#### Proof

Consider an edge \(e=v\to w\) remaining inside a segment of constant
radius \(r\).

If \(r=0\), it is the original radius-zero Johnson rotor edge.  If
\(r\ge1\), then \(r(e)=r\), so \(e\in E^\circ\).  Since it was not cut
in \(D\), it is durable through every level \(0\le h<r\).  Repeated use
of the exact one-edge lift criterion shows that the full radius-\(r\) flag
states at \(v\) and \(w\) are genuine directed rotor neighbours.

Thus the owners in each segment form one radius-\(r(S)\) rotor path.
Reverse-write the \(2r(S)+1\) useful blocks of its first state and append
one principal core for every later state.  A segment with \(t\) owners has
exact length

\[
t+2r(S).
\]

Summing the owner counts gives \(W\), proving (7.4).  Equations
(7.2)--(7.3) and \(r(S)\le H\) give (7.5).

Every member of an owner's saturated flag chain is a suffix OR ending at
that owner's principal position.  The flag systems are bijective on each
active rank, so these chains form one exact integral band SCD and cover
every band target. \(\square\)

If \((\mathbf L,\mathbf R)\) maximizes corrected durability, then
\(K=K_H^{\min}\).  Under the still-unproved estimate

\[
K_H^{\min}=o(W/H),
\tag{7.6}
\]

the three excess terms satisfy

\[
2HB=O_A(W/\sqrt m)=o(W),
\qquad
2HK=o(W),
\qquad
2H^2=O_A(m)=o(W).
\tag{7.7}
\]

Hence (7.5) would be a \(W+o(W)\) literal band word.  This is only a
conditional implication.

Theorem 7.1 is a replacement theorem.  It covers the complete first band
literally because the flag SCD covers it, but it does not assert that an
old meet or join remains attached to the same original forest edge.  When
that occurrence-level facet-braid requirement is frozen, Theorem 3.3 and
the trace gate (4.11) are the relevant conclusions.

---

## 8. Proved and unproved boundary

### Proved

1. The printed durable definition must be restricted to \(E^\circ\).
   The two-owner example proves necessity, and Theorem 1.2 proves the
   corrected identity with exact quantifiers.
2. The tube coefficient is exactly \(q-s\), with no factor-two loss.
   The dual constant and the cyclic boundary floor are exact.
3. The tube report needs the \(t=0\) proof split and the stronger
   no-return premise for rank-goodness.  These repairs do not change its
   stated inequalities.
4. Maximal durability localizes every true fixed-depth hole to the exact
   frontier envelope (3.13), while preserving the original literal
   first-band braid in a word of length \(W+2H(B+K)\).
5. The trace-incidence criterion (4.6), portal-degree theorem (5.3), and
   cross-component energy theorem (6.4) are integral exact consequences.
6. Allowing variable-radius replacement yields the zero-hole literal word
   (7.4), with shared endpoints through the entire growing band.

### Unproved

1. Nonemptiness of both exact flag families for the prescribed globally
   contiguous odd-cut lifetime assignment.
2. The decisive estimate
   \[
   K_H^{\min}=o(W/H).
   \]
3. The high-incidence selection condition (4.11) for the frozen
   radius-\(H\) facet-core word.
4. The required unbounded cross-component trace packet when the true hole
   mass is linear.

Small durable defect therefore has two sharply different consequences.
It gives a conditional zero-hole solution after variable-radius global
replacement.  For the frozen fixed-depth facet braid, it only localizes
the remaining holes; coefficient-one trace repair still requires either
the exceptional coordinate incidence in (4.11) or the unbounded portal
degree forced by (5.6).  Static owner marginals supply neither datum.

No fractional owner, cross-factor operation, or nonliteral witness is used
anywhere in the proved statements.
