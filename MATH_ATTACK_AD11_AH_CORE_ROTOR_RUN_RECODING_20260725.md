# AD11: exact rotor-run recoding of the AH saturating-cycle core

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, solver, finite
search, or long-running local job is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad
 W=\binom{2m+1}{m},\qquad
 N_q=\binom{2m+1}{m-q},\qquad
 d=W-N_1=\frac{2W}{m+2}.
\tag{0.1}
\]

Let

\[
 S_i\subset X_i\supset S_{i+1}
 \qquad(i\in\mathbb Z_{N_1})
\tag{0.2}
\]

be the AH saturating cycle.  The \(S_i\)'s are all the rank-
\((m-1)\) sets and the \(X_i\)'s are distinct rank-\(m\) sets.  Orient its
contracted owner cycle as

\[
 e_i:X_i\longrightarrow X_{i-1}.
\tag{0.3}
\]

Then

\[
 X_i\cap X_{i-1}=S_i.
\tag{0.4}
\]

AH Theorem 1.1 supplies exact core-balanced nested lower flags

\[
 L_q:U:=\{X_i\}\longrightarrow
 V_q:=\binom{[n]}{m-q},
 \qquad L_1(X_i)=S_i,
\tag{0.5}
\]

through every \(H<m\).  This report proves the following exact recoding
and obstruction results.

1. There is an exact labelled quantity \(K_{\rm core}^-(\mathbf L)\): the
   number of owner-cycle edges on which the AH deletion symbols fail the
   one-update lower-prefix recursion.  Cutting precisely those edges (or
   one structural edge if the number is zero) gives

   \[
   P_{\rm core}=\max\{1,K_{\rm core}^-(\mathbf L)\}
   \tag{0.6}
   \]

   literal lower-prefix MTF runs.  A run containing \(t\) owners has exact
   length \(t+H\).  Since the core flags cover every lower target, appending
   the \(d\) omitted middle owners singly gives a literal word covering all
   ranks \(m-H,\ldots,m\) of exact length

   \[
   \boxed{L_{\rm low}=W+H P_{\rm core}.}
   \tag{0.7}
   \]

   Thus the precise core target is

   \[
   \boxed{
   K_{\rm core}^{-,\min}=o_A(W/H),
   \qquad H=\lceil A\sqrt m\rceil.}
   \tag{0.8}
   \]

2. There is a cycle-only multiscale obstruction to (0.8).  Let

   \[
   \Psi_q(i)=S_i\cap S_{i-1}\cap\cdots\cap S_{i-q+1}.
   \tag{0.9}
   \]

   From its legal rank-\((m-q)\) occurrences define the exact marginal
   edit defect \(\Delta_q\) in (5.8).  Every core flag table satisfies

   \[
   \boxed{
   K_{\rm core}^-(\mathbf L)
   \ge
   \left\lceil\frac{\Delta_q}{q-1}\right\rceil
   \qquad(2\le q\le H).}
   \tag{0.10}
   \]

3. For \(m\ge6\) and \(H\ge2\), at depth two, if \(z_2\) is the number of
   rank-\((m-2)\) sets never
   used as an intersection of consecutive \(S\)-vertices, then

   \[
   \boxed{
   K_{\rm core}^-(\mathbf L)\ge z_2.}
   \tag{0.11}
   \]

   More exactly, the least possible number of depth-two recursion failures
   is the integral released-parent Hall optimization in Theorem 6.1.  Its
   capacity part is

   \[
   \boxed{
   \chi_2=z_2+\max\{0,\rho_2-t_2\},
   \qquad
   \rho_2=N_1-N_2=\frac{4N_1}{m+3},}
   \tag{0.12}
   \]

   where \(t_2\) is the number of intersection colours occurring at least
   twice.  Since \(\rho_2=o_A(W/H)\), the capacity part is small if and only
   if

   \[
   z_2=o_A(W/H).
   \tag{0.13}
   \]

4. For \(m\ge6\) and \(2\le H<m\), exact growing-depth core balance and
   AH's weighted spill do not imply (0.8).  For every prescribed
   depth-two selector, there is an exact
   core-balanced AH flow through the entire depth \(H\) which agrees with
   that selector on at most

   \[
   \left\lfloor\frac{N_1}{m-1}\right\rfloor
   \tag{0.14}
   \]

   owners.  Applied to the cycle-forced selector, it gives

   \[
   K_{\rm core}^-(\mathbf L)
   \ge N_1-\left\lfloor\frac{N_1}{m-1}\right\rfloor
   =\Theta(W),
   \tag{0.15}
   \]

   while the omitted-owner augmentation still has weighted spill \(o(W)\).
   This is a rigorous no-go for deriving low \(K\) from marginal balance;
   it is not a lower bound on the best chronology-sensitive AH flow.

5. AH Corollary 1.2 is full-owner only in its domain.  It constructs lower
   flags \(\widetilde L_q\), and the augmented loads have weighted overload
   \(o(W)\); it does not construct upper-complement flags, exact two-sided
   balance, or an MTF chronology.  Hence (0.7) is a literal lower-half
   theorem.  A conditional two-sided version is given in Section 9, but
   its hypotheses are not supplied by AH and no constant-one conclusion is
   claimed.

All cuts, flows, flags, and literal words below are integral.  Every
surviving transition is an actual edge of the one fixed saturating cycle.

## 1. Exact scope of the AH input

For \(1\le q\le H\), put

\[
 c_q^{\rm core}=\left\lfloor\frac{N_1}{N_q}\right\rfloor,
 \qquad
 r_q=N_1-c_q^{\rm core}N_q.
\tag{1.1}
\]

AH Theorem 1.1 gives nested maps (0.5) such that every \(T\in V_q\)
has load

\[
 c_q^{\rm core}
 \quad\hbox{or}\quad
 c_q^{\rm core}+1,
\tag{1.2}
\]

with exactly \(r_q\) high-load targets.  Since \(N_q\le N_1\) for
\(q\ge1\),

\[
 c_q^{\rm core}\ge1.
\tag{1.3}
\]

Thus the core flags alone cover every target in every lower rank
\(m-H,\ldots,m-1\).

AH Corollary 1.2 augments these flags by arbitrary nested lower flags on
the omitted family

\[
 E=V_0\setminus U,\qquad |E|=d,
\tag{1.4}
\]

and proves

\[
 \sum_{q=1}^H\frac{O_q(\widetilde L)}{c_q}
 \le dH
 =O_A(W/\sqrt m)=o_A(W),
\tag{1.5}
\]

where \(c_q=\lfloor W/N_q\rfloor\).  The symbol \(O_q\) is overload
relative to a balanced \(W\)-mass quota.  Equation (1.5) is not an exact
balance assertion.

More importantly for the present lane, AH constructs no maps

\[
 R_q:X\longmapsto\binom{[n]}{m+1-q}
\tag{1.6}
\]

for the upper-complement side.  Consequently the only unconditional
chronology question furnished by AH is the lower-prefix one treated next.

## 2. The exact one-edge lower-prefix criterion

For a core owner \(X\), put \(L_0(X)=X\), and write

\[
 \{\ell_h(X)\}=L_h(X)\setminus L_{h+1}(X),
 \qquad 0\le h<H.
\tag{2.1}
\]

Every \(\ell_h(X)\) is one coordinate.  The useful lower prefix is the
ordered partition

\[
 \Lambda_H(X)=
 \bigl(
 L_H(X),
 \{\ell_{H-1}(X)\},\ldots,\{\ell_0(X)\}
 \bigr).
\tag{2.2}
\]

Its successive prefix unions are exactly

\[
 L_H(X),L_{H-1}(X),\ldots,L_0(X)=X.
\tag{2.3}
\]

### Theorem 2.1 (exact tail-insensitive lower-prefix update)

Let \(v\to w\) be a Johnson edge such that

\[
 L_1(v)=v\cap w.
\tag{2.4}
\]

Appending the single mask \(L_H(w)\) to a literal history whose useful
prefix is \(\Lambda_H(v)\) changes its useful prefix exactly to
\(\Lambda_H(w)\), independently of the unresolved tail, if and only if

\[
 \ell_h(v)=\ell_{h-1}(w)
 \qquad(1\le h<H)
\tag{2.5}
\]

and

\[
 L_H(v)\setminus L_H(w)=\{\ell_{H-1}(w)\}.
\tag{2.6}
\]

Equivalently, the exact conditions are

\[
 L_{h+1}(v)=L_h(v)\cap L_h(w)
 \qquad(0\le h<H)
\tag{2.7}
\]

together with

\[
 L_H(v)\ne L_H(w).
\tag{2.8}
\]

#### Proof

Write the source blocks as

\[
 A_0=L_H(v),\qquad
 A_j=\{\ell_{H-j}(v)\}\quad(1\le j\le H),
\]

and the target blocks similarly as \(B_0,\ldots,B_H\).  On appending
\(B_0=L_H(w)\), the augmented last-occurrence update puts \(B_0\) first
and then lists the nonempty differences

\[
 A_0\setminus B_0,
 A_1\setminus B_0,\ldots,A_H\setminus B_0
\tag{2.9}
\]

in their old order.

By (2.4),

\[
 A_H=\{\ell_0(v)\}=v\setminus w.
\]

Since \(B_0\subseteq w\), the block \(A_H\) survives (2.9).  Moreover it
cannot occur among the target's first \(H\) singleton blocks, whose union
with \(B_0\) is \(w\); it must be the first unresolved tail block after
the target useful prefix.

Before \(A_H\), the update has only the \(H\) possible blocks
\[
 A_0\setminus B_0,\ A_1\setminus B_0,\ldots,A_{H-1}\setminus B_0.
\]
The target requires exactly \(H\) nonempty singleton blocks there.
Consequently \(A_0\setminus B_0\) is one singleton and none of
\(A_1,\ldots,A_{H-1}\) disappears into \(B_0\).  Order now forces
\[
 B_1=A_0\setminus B_0,\qquad
 B_j=A_{j-1}\quad(2\le j\le H),
\]
which is precisely (2.5)--(2.6).  Conversely those identities make (2.9)
begin with \(B_1,\ldots,B_H\), followed by the surviving block \(A_H\);
the update is therefore exact and tail-insensitive.

Starting from (2.4), elementary set subtraction shows inductively that
(2.5)--(2.6) are equivalent to (2.7)--(2.8).  In one direction,
intersecting the two rank-\((m-h)\) endpoints removes from the source the
coordinate \(\ell_h(v)=\ell_{h-1}(w)\).  In the other direction, the
rank drop in (2.7) identifies those two deleted coordinates, and the final
non-equality gives (2.6).  \(\square\)

For the oriented AH edge \(e_i:X_i\to X_{i-1}\), (0.4)--(0.5) give

\[
 L_1(X_i)=X_i\cap X_{i-1}.
\tag{2.10}
\]

Thus the depth-zero identity in (2.7) is automatic on every cycle edge.
All remaining chronology is contained in the labelled shifts
(2.5)--(2.6).

## 3. Exact cycle run count and literal length

Call \(e_i\) **lower-prefix good** when it satisfies Theorem 2.1, and put

\[
 K_{\rm core}^-(\mathbf L)
 =|\{i:e_i\text{ is not lower-prefix good}\}|.
\tag{3.1}
\]

### Lemma 3.1 (one good path costs \(t+H\))

Let

\[
 v_1\to v_2\to\cdots\to v_t
\tag{3.2}
\]

be a directed path of lower-prefix good edges.  There is a literal word of
exact length

\[
 \boxed{t+H}
\tag{3.3}
\]

which exposes every lower flag \(L_q(v_j)\), \(0\le q\le H\), as a
contiguous OR interval ending at one shared principal position for \(v_j\).

#### Proof

Initialize with the \(H+1\) masks

\[
 \{\ell_0(v_1)\},
 \{\ell_1(v_1)\},\ldots,
 \{\ell_{H-1}(v_1)\},
 L_H(v_1).
\tag{3.4}
\]

The suffix ORs ending at the last position are exactly

\[
 L_H(v_1),L_{H-1}(v_1),\ldots,L_0(v_1).
\]

For \(j=2,\ldots,t\), append only \(L_H(v_j)\).  Theorem 2.1 says that
the augmented last-occurrence prefix is then exactly \(\Lambda_H(v_j)\),
so the corresponding suffix ORs expose its whole lower flag.  The first
owner costs \(H+1\) positions and every later owner costs one.  \(\square\)

### Theorem 3.2 (exact AH-core lower literalization)

For fixed AH core flags \(\mathbf L\), put

\[
 P_{\rm core}=\max\{1,K_{\rm core}^-(\mathbf L)\}.
\tag{3.5}
\]

There is one literal word covering every mask in ranks

\[
 m-H,m-H+1,\ldots,m
\tag{3.6}
\]

of exact length

\[
 \boxed{L_{\rm low}=W+H P_{\rm core}.}
\tag{3.7}
\]

It consists of \(P_{\rm core}\) positive-radius core runs and \(d\)
radius-zero omitted-owner singleton runs.

#### Proof

If \(K_{\rm core}^->0\), cut every bad edge of the directed cycle.
Removing \(K_{\rm core}^-\) edges from a cycle gives exactly that many
directed paths.  If \(K_{\rm core}^-=0\), cut one arbitrary structural
edge and obtain one path.  Lemma 3.1 gives total core length

\[
 N_1+H P_{\rm core}.
\tag{3.8}
\]

By (1.3), the core flags cover every lower target in (3.6), except that
the middle rank currently contains only the used owners \(U\).  Append
each omitted middle owner in \(E\) as one literal mask.  This adds
\(d=W-N_1\) positions and completes the middle rank, proving (3.7).
All intended flag intervals lie within their own core-run words, so the
concatenation and singleton appendices destroy none of them.  \(\square\)

If one insists on physically realizing the arbitrary omitted lower flags
from AH Corollary 1.2, apply Lemma 3.1 separately to every omitted owner.
The exact length becomes

\[
 L_{\rm low}^{\rm all\ flags}
 =W+H(P_{\rm core}+d).
\tag{3.9}
\]

For \(H=\lceil A\sqrt m\rceil\),

\[
 \frac{d}{W/H}
 =\frac{dH}{W}
 =\frac{2H}{m+2}
 =\frac{2A+o_A(1)}{\sqrt m}
 \longrightarrow0.
\tag{3.10}
\]

Consequently

\[
 K_{\rm core}^-=o_A(W/H)
\tag{3.11}
\]

implies both

\[
 d+P_{\rm core}=o_A(W/H)
\tag{3.12}
\]

and

\[
 L_{\rm low}=W+o_A(W),
 \qquad
 L_{\rm low}^{\rm all\ flags}=W+o_A(W).
\tag{3.13}
\]

The weighted-spill bound (1.5) needs no literal repair for lower-rank
coverage: the core loads already have the pointwise lower bound (1.3).
Its only relevance to (3.9) is that separately initializing all omitted
flags costs \(Hd=o(W)\).

## 4. The exact labelled \(K\) formula

For \(e_i:X_i\to X_{i-1}\), define

\[
 \eta_h(e_i)=
 \mathbf1\bigl[\ell_h(X_i)\ne\ell_{h-1}(X_{i-1})\bigr],
 \qquad 1\le h<H,
\tag{4.1}
\]

and

\[
 \eta_H(e_i)=
 \mathbf1\bigl[
 L_H(X_i)\setminus L_H(X_{i-1})
 \ne\{\ell_{H-1}(X_{i-1})\}
 \bigr].
\tag{4.2}
\]

Theorem 2.1 gives the exact identity

\[
 \boxed{
 K_{\rm core}^-(\mathbf L)
 =\sum_i
 \min\left\{1,\sum_{h=1}^H\eta_h(e_i)\right\}.}
\tag{4.3}
\]

It also gives the persistent-shield form

\[
 \boxed{
 K_{\rm core}^-(\mathbf L)
 =\min_{Z\subseteq E(\mathcal C)}
 \left(
 |Z|+
 \sum_{e\notin Z}\sum_{h=1}^H\eta_h(e)
 \right).}
\tag{4.4}
\]

Indeed, edge by edge, a good edge costs zero outside \(Z\), while a bad
edge costs at least one outside \(Z\) and exactly one when placed in
\(Z\).

Let \(\mathfrak F_H^{\rm core}(\mathcal C)\) be the nonempty set of all
AH core-balanced nested lower flag tables preserving \(L_1(X_i)=S_i\).
The chronology-sensitive optimum supplied by the current input is

\[
 \boxed{
 K_{\rm core}^{-,\min}(\mathcal C,H)
 =\min_{\mathbf L\in\mathfrak F_H^{\rm core}(\mathcal C)}
 K_{\rm core}^-(\mathbf L).}
\tag{4.5}
\]

Equations (3.7) and (4.5) formulate the requested rotor-run count directly
for the AH core.  AH proves only that the feasible set in (4.5) is
nonempty.  Its flow objective is zero and therefore gives no estimate on
(4.3) or (4.4).

## 5. A cycle-only multiscale obstruction

For \(2\le q\le H\), define the natural backward window

\[
 \Psi_q(i)=\bigcap_{j=0}^{q-1}S_{i-j}.
\tag{5.1}
\]

Adjacent \(S\)-vertices differ in one coordinate, so

\[
 |\Psi_q(i)|\ge m-q.
\tag{5.2}
\]

Call the occurrence legal when equality holds.  For \(T\in V_q\), put

\[
 h_q(T)=
 |\{i:\Psi_q(i)=T,\ |\Psi_q(i)|=m-q\}|.
\tag{5.3}
\]

### Lemma 5.1 (forced natural windows)

If the \(q-1\) edges

\[
 e_i,e_{i-1},\ldots,e_{i-q+2}
\tag{5.4}
\]

are lower-prefix good, then

\[
 \boxed{L_q(X_i)=\Psi_q(i).}
\tag{5.5}
\]

In particular the occurrence in (5.1) is legal.

#### Proof

For \(q=2\), (2.7) gives

\[
 L_2(X_i)=L_1(X_i)\cap L_1(X_{i-1})=S_i\cap S_{i-1}.
\]

Inductively, apply (2.7) on \(e_i\) at level \(q-1\) and use the
induction hypothesis at \(i\) and \(i-1\).  The two consecutive windows
have union of index sets \(\{i,i-1,\ldots,i-q+1\}\), giving (5.5).
The left side has rank \(m-q\), proving legality.  \(\square\)

Every bad edge belongs to at most \(q-1\) windows of the form (5.4).
Hence the actual balanced map \(L_q\) differs from the legal natural
partial map at no more than

\[
 (q-1)K_{\rm core}^-(\mathbf L)
\tag{5.6}
\]

owner positions.

For a high-target set \(Y\subseteq V_q\), \(|Y|=r_q\), the balanced
capacity is

\[
 b_Y(T)=c_q^{\rm core}+\mathbf1_Y(T).
\tag{5.7}
\]

Let

\[
 t_q=|\{T\in V_q:h_q(T)\ge c_q^{\rm core}+1\}|.
\]

The maximum number of natural positions which can be retained by the
unconstrained balanced-marginal relaxation at depth \(q\) is

\[
 \sum_T\min\{h_q(T),c_q^{\rm core}\}
 +\min\{r_q,t_q\}.
\]

Therefore define the exact marginal Hamming-relaxation defect

\[
 \boxed{
 \Delta_q=
 N_1-
 \sum_T\min\{h_q(T),c_q^{\rm core}\}
 -\min\{r_q,t_q\}.}
\tag{5.8}
\]

Illegal positions are included automatically in \(\Delta_q\), because
they contribute to the initial \(N_1\) but to none of the \(h_q(T)\).

### Theorem 5.2 (multiscale histogram lower bound)

For every \(\mathbf L\in\mathfrak F_H^{\rm core}(\mathcal C)\) and every
\(2\le q\le H\),

\[
 \boxed{
 K_{\rm core}^-(\mathbf L)
 \ge
 \left\lceil\frac{\Delta_q}{q-1}\right\rceil.}
\tag{5.9}
\]

#### Proof

For a chosen balanced high set \(Y\), a target \(T\) retains at most
\(\min\{h_q(T),b_Y(T)\}\) natural occurrences.  A high slot adds one
retained occurrence exactly when \(h_q(T)\ge c_q^{\rm core}+1\), so the
optimal \(r_q\) high slots add \(\min\{r_q,t_q\}\).  Thus \(\Delta_q\)
is the minimum number of owner assignments which the unconstrained
balanced-marginal relaxation must change.  It does not impose nesting or
parent--facet containment on the edited assignments.  Lemma 5.1 and (5.6)
show that the actual map
changes at most \((q-1)K_{\rm core}^-\) positions.  \(\square\)

Consequently the target (0.8) forces the simultaneous, completely
cycle-intrinsic estimates

\[
 \boxed{
 \Delta_q=o_A(qW/H)
 \qquad(2\le q\le H).}
\tag{5.10}
\]

For fixed \(A\), the uniform meaning of (5.10) is

\[
 \sup_{2\le q\le H}
 \frac{\Delta_q}{qW/H}\longrightarrow0.
\tag{5.11}
\]

These conditions are necessary, not sufficient.  They contain neither the
nested residual Hall cuts nor the requirement that one persistent edge
shield work at every depth.

## 6. The exact depth-two optimization

At depth two,

\[
 \psi_i:=\Psi_2(i)=S_i\cap S_{i-1}
 \in V_2.
\tag{6.1}
\]

This always has rank \(m-2\), because \(S_i,S_{i-1}\) are distinct
facets of \(X_{i-1}\).  Put

\[
 h(T)=|\{i:\psi_i=T\}|,
 \qquad
 z_2=|\{T:h(T)=0\}|,
 \qquad
 t_2=|\{T:h(T)\ge2\}|.
\tag{6.2}
\]

For \(m\ge6\),

\[
 \frac{N_1}{N_2}=\frac{m+3}{m-1}\in(1,2),
\]

so every balanced core depth-two quota is

\[
 b_J(T)=1+\mathbf1_J(T),
 \qquad
 |J|=\rho_2:=N_1-N_2=\frac{4N_1}{m+3}.
\tag{6.3}
\]

For a released index set \(Q\subseteq\mathbb Z_{N_1}\), let

\[
 h_{\bar Q}(T)=|\{i\notin Q:\psi_i=T\}|.
\tag{6.4}
\]

Identify the released parent \(i\) with \(S_i=L_1(X_i)\), and for a
released family \(A\subseteq Q\) write

\[
 \partial A=
 \{T\in V_2:T\subset S_i\text{ for some }i\in A\}.
\tag{6.5}
\]

### Theorem 6.1 (exact core depth-two release/Hall formula)

There is a balanced map \(L_2:U\to V_2\) agreeing with
\(L_2(X_i)=\psi_i\) for every \(i\notin Q\) if and only if there is a
set \(J\subseteq V_2\), \(|J|=\rho_2\), such that

\[
 h_{\bar Q}(T)\le b_J(T)
 \qquad(T\in V_2)
\tag{6.6}
\]

and

\[
 |A|
 \le
 \sum_{T\in\partial A}
 \bigl(b_J(T)-h_{\bar Q}(T)\bigr)
 \qquad(A\subseteq Q).
\tag{6.7}
\]

Consequently the minimum number of depth-two lower recursion failures is
exactly

\[
 \boxed{
 \zeta_2=
 \min_{J,Q}
 \{|Q|:(J,Q)\text{ satisfy }(6.6)\text{--}(6.7)\}.}
\tag{6.8}
\]

Every growing-depth table satisfies

\[
 K_{\rm core}^-(\mathbf L)\ge\zeta_2.
\tag{6.9}
\]

#### Proof

After freezing the natural assignments outside \(Q\), target \(T\) has
residual demand

\[
 r(T)=b_J(T)-h_{\bar Q}(T).
\tag{6.10}
\]

Nonnegativity is (6.6), and total residual demand is

\[
 \sum_T r(T)=N_1-(N_1-|Q|)=|Q|.
\]

Clone \(T\) exactly \(r(T)\) times and join a released parent \(S_i\)
to every clone of each facet \(T\subset S_i\).  Hall's theorem is exactly
(6.7), and a perfect matching gives the desired assignments.  Every
balanced completion supplies such a matching, while every such matching
produces a balanced map whose mismatch set is contained in \(Q\).  Taking
\(Q\) to be the actual mismatch set in one direction, and deleting any
redundant released indices in the other, proves that the minimum in (6.8)
is exact.  A genuine mismatch at index \(i\) is exactly a failure of the
level-one identity

\[
 L_2(X_i)=L_1(X_i)\cap L_1(X_{i-1}).
\]

This proves (6.8)--(6.9).  Notice that later levels and the final
deepest-core non-equality may force additional bad edges.  \(\square\)

The capacity-only part of (6.8) is explicit.  For fixed \(J\), at least

\[
 \sum_T(h(T)-b_J(T))_+
\]

natural owners must be released.  Moreover

\[
 \sum_T(h(T)-1)_+
 =N_1-|\operatorname{supp}h|
 =\rho_2+z_2.
\tag{6.11}
\]

Placing a high slot on a repeated target reduces this excess by one.  The
best \(\rho_2\) high slots therefore give

\[
 \boxed{
 \chi_2
 :=\min_{|J|=\rho_2}\sum_T(h(T)-b_J(T))_+
 =\rho_2+z_2-\min\{\rho_2,t_2\}
 =z_2+\max\{0,\rho_2-t_2\}.}
\tag{6.12}
\]

Thus

\[
 z_2\le\chi_2\le z_2+\rho_2,
 \qquad
 \zeta_2\ge\chi_2.
\tag{6.13}
\]

For \(H=\lceil A\sqrt m\rceil\),

\[
 \frac{\rho_2H}{W}
 =\frac{4mH}{(m+2)(m+3)}
 \le\frac{4A}{\sqrt m}+\frac4m
 \longrightarrow0.
\tag{6.14}
\]

Hence the capacity obstruction is \(o_A(W/H)\) if and only if

\[
 \boxed{z_2=o_A(W/H).}
\tag{6.15}
\]

The Hall inequalities (6.7) are an additional condition; no scalar
histogram estimate implies them.

### 6.2 Exact all-owner recourse at depth two

The corrected omitted-owner theorem gives an SDR at depth one.  Let its
image be

\[
 H_1\subseteq V_1,\qquad |H_1|=d.
\tag{6.16}
\]

Thus the full depth-one load is one everywhere and two on \(H_1\).  For
\(m\ge8\), a balanced full \(W\)-mass depth-two quota is

\[
 b_J^{\rm full}(T)=1+\mathbf1_J(T),
 \qquad
 |J|=W-N_2=d+\rho_2.
\tag{6.17}
\]

All core edges retain their natural depth-two child, while the omitted
tokens complete an exactly balanced load, if and only if

\[
 h(T)\le1+\mathbf1_J(T)
 \qquad(T\in V_2)
\tag{6.18}
\]

and

\[
 \boxed{
 |H_1\cap N(\mathcal A)|
 \ge
 |\mathcal A|+|J\cap\mathcal A|-h(\mathcal A)
 \qquad(\mathcal A\subseteq V_2),}
\tag{6.19}
\]

where \(N(\mathcal A)\) is the family of rank-\((m-1)\) parents of
\(\mathcal A\) and \(h(\mathcal A)=\sum_{T\in\mathcal A}h(T)\).

Indeed, the omitted tokens have parent set \(H_1\), while child \(T\) has
residual demand \(1+\mathbf1_J(T)-h(T)\).  Equations (6.18)--(6.19) are
respectively nonnegativity and Hall after cloning residual children.

More generally, if a core position set \(Q\) is released, put

\[
 w_Q(S)=\mathbf1_{H_1}(S)+
 |\{i\in Q:S_i=S\}|
\tag{6.20}
\]

and

\[
 r_{J,Q}(T)=1+\mathbf1_J(T)-h_{\bar Q}(T).
\tag{6.21}
\]

The exact full-owner residual criterion is

\[
 r_{J,Q}(T)\ge0\quad(T\in V_2)
\tag{6.22}
\]

and

\[
 \boxed{
 \sum_{S\in A}w_Q(S)
 \le
 \sum_{T\in\partial A}r_{J,Q}(T)
 \qquad(A\subseteq V_1).}
\tag{6.23}
\]

For this fixed admissible SDR image \(H_1\), the minimum \(|Q|\) over
(6.22)--(6.23), also minimizing over
\(J\subseteq V_2\) with \(|J|=d+\rho_2\), is therefore the exact number
of core depth-two recurrences which must be sacrificed when omitted tokens
are allowed as recourse.  The global optimum must additionally minimize
over all admissible omitted-owner SDR images \(H_1\).

Its capacity-only lower bound is

\[
 \chi_2^{\rm full}
 =\rho_2+z_2-\min\{d+\rho_2,t_2\},
\tag{6.24}
\]

so

\[
 \max\{0,z_2-d\}\le\chi_2^{\rm full}\le z_2+\rho_2.
\tag{6.25}
\]

If one permits depth-two overload \(O_2\) instead of exact full balance,
then every release set still obeys

\[
 |Q|\ge\chi_2^{\rm full}-O_2.
\tag{6.26}
\]

To see this, compare the full natural load \(h\) with the load \(\mu\)
after releasing \(Q\).  Fibrewise, the positive excess of \(h\) above a
balanced quota is at most the number of released occurrences in that
fibre plus the positive excess of \(\mu\).  Summing gives
\(\chi_2^{\rm full}\le |Q|+O_2\).

Combining (6.25)--(6.26) makes the restitution explicit:

\[
 |Q|+O_2\ge\chi_2^{\rm full}\ge z_2-d.
\tag{6.27}
\]

Since AH gives \(O_2\le d\),

\[
 |Q|\ge z_2-2d.
\tag{6.28}
\]

Moreover,

\[
 \frac{(d+\rho_2)H}{W}=o_A(1).
\tag{6.29}
\]

Therefore even the allowed weighted spill cannot hide a depth-two deficit
\(z_2\) larger than \(o_A(W/H)\).

## 7. Exact balanced marginals can have nearly maximal \(K\)

The preceding section isolates the special min-cost flow one would need.
The next theorem proves that the uncosted AH flow conclusion, even through
the entire growing depth, has no implication toward it.

### Theorem 7.1 (full-depth anti-chronological AH flow)

Assume \(m\ge6\) and \(2\le H<m\).  Let

\[
 \psi:V_1\longrightarrow V_2,
 \qquad \psi(S)\subset S,
\tag{7.1}
\]

be any prescribed facet selector.  There is an exact core-balanced common-
owner lower flag family through every depth \(1,\ldots,H\) such that

\[
 \boxed{
 |\{S\in V_1:L_2(\phi^{-1}(S))=\psi(S)\}|
 \le
 \left\lfloor\frac{N_1}{m-1}\right\rfloor.}
\tag{7.2}
\]

For the natural cycle selector

\[
 \psi(S_i)=S_i\cap S_{i-1},
\tag{7.3}
\]

the resulting exact balanced flag family satisfies

\[
 \boxed{
 K_{\rm core}^-(\mathbf L)
 \ge
 N_1-\left\lfloor\frac{N_1}{m-1}\right\rfloor
 =(1-O(1/m))N_1=\Theta(W).}
\tag{7.4}
\]

#### Proof

Use the full layered inclusion-flow polytope from AH Theorem 1.1.  Every
node of \(V_1\) has supply one; every \(T\in V_q\) has a split arc with
the integral bounds

\[
 \left\lfloor\frac{N_1}{N_q}\right\rfloor
 \le f(T)\le
 \left\lceil\frac{N_1}{N_q}\right\rceil;
\tag{7.5}
\]

and all downward facet arcs are present.  Total source mass bounds every
arc, so this is a bounded integral network-flow polytope.

Its symmetric fractional point sends the unit at every \(S\in V_1\)
equally over the \(m-1\) facets of \(S\), and thereafter splits every
node equally among its facets.  The throughput at every \(V_q\)-node is
\(N_1/N_q\), so this point satisfies (7.5).

Put cost one on the prescribed first-transition arc

\[
 S\longrightarrow\psi(S)
\]

and cost zero on every other first-transition arc and on all deeper arcs.
The symmetric fractional point has total cost exactly

\[
 \frac{N_1}{m-1}.
\tag{7.6}
\]

Network integrality gives an integral vertex of cost at most (7.6).
Decompose that integral flow into its \(N_1\) unit owner paths.  These are
the required exact balanced common-owner flags, and their integral cost is
the agreement count in (7.2).  For (7.3), every disagreement makes the
level-one intersection identity fail on the corresponding cycle edge, so
(7.4) follows.  \(\square\)

Now augment the flags in Theorem 7.1 by arbitrary nested flags for the
\(d\) omitted owners.  The proof of AH Corollary 1.2 applies to every
balanced core load, hence still gives

\[
 \sum_{q=1}^H\frac{O_q}{c_q}\le dH=o_A(W)
 \qquad(H\le A\sqrt m).
\tag{7.7}
\]

Equations (7.4) and (7.7) coexist.  Therefore neither exact core balance,
common ownership, full-depth nesting, nor weighted spill \(o(W)\) implies
even \(K=o(W)\), let alone \(K=o(W/H)\).

The theorem does **not** prove that
\(K_{\rm core}^{-,\min}=\Theta(W)\).  It proves the sharp logical
boundary of the AH input: a special chronology-sensitive minimum-cost flow
must be selected and analysed.

## 8. The directly testable edge-distribution estimate

The depth-two statistic has a simple graph interpretation.  The
\(S_i\)'s form a Hamilton cycle \(\mathcal C_S\) in
\(J(2m+1,m-1)\).  For \(T\in V_2\), put

\[
 \mathcal K_T=\{S\in V_1:T\subset S\}.
\tag{8.1}
\]

This is a clique on exactly \(m+3\) vertices, and

\[
 \boxed{h(T)=e(\mathcal C_S[\mathcal K_T]).}
\tag{8.2}
\]

Thus (6.15) is the explicit edge-distribution estimate

\[
 \boxed{
 |\{T\in V_2:e(\mathcal C_S[\mathcal K_T])=0\}|
 =o_A(W/H).}
\tag{8.3}
\]

Equivalently, the Hamilton cycle must meet all but \(o_A(W/H)\) of the
rank-\((m-2)\) Johnson cliques by an internal edge.

For \(m\ge6\), the displayed elementary scalar/per-clique ledger yields
only the following.  Since
\(\mathcal K_T\) is a proper vertex subset of one Hamilton cycle, its
induced subgraph is a union of paths, so

\[
 0\le h(T)\le m+2.
\tag{8.4}
\]

Also

\[
 \sum_{T\in V_2}h(T)=N_1.
\tag{8.5}
\]

These facts alone imply only

\[
 |\operatorname{supp}h|
 \ge\left\lceil\frac{N_1}{m+2}\right\rceil,
\tag{8.6}
\]

which is smaller than \(N_2\) by a linear-in-\(W\) amount.  The defining
saturating property says that the union colours of the cycle edges are
distinct.  It does not improve (8.4) locally: two distinct edges inside
\(\mathcal K_T\), say between \(T+a,T+b\), already have the distinct
union labels \(T+a+b\).  Therefore maximum-multiplicity, degree, and the
raw union-rainbow condition do not prove (8.3).

This is not a constructed counterexample saturating cycle.  It proves only
that the displayed scalar and per-clique ledgers (8.4)--(8.5), even with
the local union-label observation, are insufficient.  For example those
scalar constraints admit an abstract histogram placing multiplicity
\(m+2\) on \(\lfloor N_1/(m+2)\rfloor\) colours and the remainder on one
more colour; this histogram need not be realizable by a Hamilton cycle.
A positive proof of (8.3)
must use a new global property of the particular saturating-cycle
construction, or construct a new saturating cycle with this clique-hitting
property deliberately.

Even (8.3) is only the capacity part of depth two.  The complete positive
depth-two theorem is (6.6)--(6.7), or (6.18)--(6.19) when omitted tokens
are used.  Across a growing depth, one must prove the multiscale estimates
(5.10) and choose one persistent released edge set whose residual tokens
pass all nested Hall systems simultaneously.

## 9. Conditional two-sided composition and the exact boundary

For clarity, suppose as an additional hypothesis that there are
upper-complement flags on all \(W\) owners, with

\[
 R_0(X)=[n]\setminus X,
 \qquad |R_q(X)|=m+1-q,
\tag{9.1}
\]

which cover every upper target and which are nested by one deletion at
each depth.  Write

\[
 \{u_h(X)\}=R_h(X)\setminus R_{h+1}(X)
 \qquad(0\le h<H),
\tag{9.2}
\]

and let

\[
 \{x_i\}=X_i\setminus X_{i-1}
\tag{9.3}
\]

be the coordinate removed on \(e_i\).  Conditional on the preceding
levels, the exact upper-complement recursion on \(e_i\) is

\[
 u_0(X_{i-1})=x_i,
 \qquad
 u_h(X_{i-1})=u_{h-1}(X_i)\quad(1\le h<H).
\tag{9.4}
\]

At the deepest residual interface one must also have

\[
 R_H(X_{i-1})\setminus R_H(X_i)
 =\{u_{H-1}(X_i)\}.
\tag{9.5}
\]

Equivalently, (9.4)--(9.5) say

\[
 R_{h+1}(X_{i-1})
 =R_h(X_i)\cap R_h(X_{i-1})
 \qquad(0\le h<H),
\tag{9.6}
\]

and \(R_H(X_i)\ne R_H(X_{i-1})\).

Let \(K_{\rm core}^{\pm}\) count the core-cycle edges which fail either
the lower criterion of Theorem 2.1 or (9.4)--(9.5).  Thus, after adjoining the
upper mismatch indicators to (4.1)--(4.2), the same edgewise proof gives

\[
 K_{\rm core}^{\pm}
 =\sum_i\mathbf1[\text{at least one lower or upper mismatch on }e_i]
\tag{9.7}
\]

and the same persistent-shield identity as (4.4).  Initialize every
omitted owner separately to full radius \(H\).

The full useful state has block-size ledger

\[
 |L_H|+2H+|R_H|
 =(m-H)+2H+(m+1-H)
 =2m+1.
\tag{9.8}
\]

The ordinary two-sided rotor-path word then gives the exact conditional
length

\[
 \boxed{
 L_{\rm band}
 =W+2H\bigl(d+\max\{1,K_{\rm core}^{\pm}\}\bigr).}
\tag{9.9}
\]

Indeed, a two-sided radius-\(H\) run with \(t\) owners costs \(t+2H\),
and every omitted owner is one isolated run.  Therefore, for each fixed
\(A>0\),

\[
 K_{\rm core}^{\pm}=o_A(W/H)
\tag{9.10}
\]

would imply a literal symmetric-band word of length \(W+o_A(W)\) with
\(o_A(W/H)\) runs.  This is exactly the quantitative form needed by the
constant-one outer-tail composition.

Neither premise in the preceding paragraph is currently proved:

* AH Corollary 1.2 supplies no upper-complement family at all;
* even on the lower side it supplies no estimate on
  \(K_{\rm core}^{-,\min}\).

### Proved

1. The exact lower deletion-symbol criterion (2.5)--(2.8).
2. The exact core run count \(\max\{1,K_{\rm core}^-\}\).
3. The exact literal lower-half length \(W+H P_{\rm core}\), and the
   all-flag variant \(W+H(P_{\rm core}+d)\).
4. The exact labelled shield identity (4.4).
5. The multiscale cycle-only lower bound (5.9).
6. The exact depth-two release/Hall formula (6.6)--(6.9), its capacity
   identity (6.12), and the all-owner recourse cuts (6.18)--(6.23).
7. The rigorous marginal no-go Theorem 7.1: exact full-depth balance and
   weighted spill \(o(W)\) can coexist with \(K=\Theta(W)\).
8. The directly testable first estimate (8.3), and the insufficiency of
   the displayed scalar/per-clique counting ledger.

### Unproved

1. The clique-hitting estimate (8.3) for a suitable saturating cycle.
2. The depth-two residual Hall cuts with \(o_A(W/H)\) released core
   positions.
3. The simultaneous multiscale estimates (5.10) with one persistent
   release set through \(H=\lceil A\sqrt m\rceil\).
4. The central target

   \[
   K_{\rm core}^{-,\min}=o_A(W/H).
   \]

5. Any upper-complement flag system and the joint estimate (9.10).

The precise boundary is therefore: the AH core can be recoded into
\(o(W/H)\) literal lower-prefix rotor runs **if and only if** its specially
selected balanced flag flow has the labelled defect (4.3) of that order.
The first unavoidable cycle statistic is (8.3), followed by the exact Hall
system (6.7).  Weighted spill is already small but is orthogonal to this
chronology gate.  No constant-one theorem follows from the current input.
