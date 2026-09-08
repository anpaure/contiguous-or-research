# Unbounded primitive CCTPF odd cycles and the exact failure of local-circuit globalization

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or web
input is used.

## 0. Outcome

Use the calibrated CCTPF parameters

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad N=N_H,
\]

\[
 M=m+H,\qquad s=m-H,\qquad L=m-3H+1,
\tag{0.1}
\]

with

\[
 H=(1+o(1))\sqrt{m\log m},\qquad m>4H,
\]

\[
 L+c_0H\le \Lambda:={W\over N_H}\le m+C_0H
\tag{0.2}
\]

for fixed positive constants \(c_0,C_0\), and quotas

\[
 b_0=L,
 \qquad
 b_q=\min\left\{L-1,
 \max\left\{0,\left\lfloor{N_q\over N_H}\right\rfloor-1\right\}
 \right\}
 \quad(1\le q<H).
\tag{0.3}
\]

This note proves the following exact alternative to a bounded odd-port
decomposition theorem.

### Theorem A (unbounded primitive literal odd cycles)

Let \(H\ge5\), and let \(n\ge3\) be odd and satisfy

\[
 n(H-1)\le m-1,
 \qquad
 2n+4H\le m+1.
\tag{0.4}
\]

There are \(n\) distinct rank-\(M\) roots, one fixed \(2H\)-core and one
fixed admissible nested tag family at each root, and two literal CCTPF full
histories \(P_i^0,P_i^1\) at every root, with these properties.

1. Every protected physical target, over the middle and every active signed
   rank, occurs in at most two of the \(2n\) histories. Hence

   \[
   x(P_i^b)=\frac12
   \tag{0.5}
   \]

   is an exact root-saturating fractional solution of all target rows.

2. Histories at distinct roots conflict if and only if their roots are
   adjacent on the cycle \(C_n\) and they have the same bit.

3. No integral choice of one of the two displayed histories per root is
   target-simple, but every proper root subset has such a displayed choice.
   Thus the displayed \(2n\)-column rooted subinstance is
   inclusion-minimal, or primitive.

4. For each bit the designated target--history matrix is the odd-cycle
   matrix \(I+P_n\), of determinant \(2\). The missing inequality is the
   exact odd-cycle inequality

   \[
   \sum_{i\in\mathbb Z_n}x(P_i^b)\le {n-1\over2}.
   \tag{0.6}
   \]

5. Distinct roots in the construction have Johnson distance \(H-1\).
   Consequently none of the audited two-, three-, four-, six-, or eight-top
   moving-hole/common-base exchanges has support entirely inside this root
   set.

At the critical height one may choose

\[
 n=(1+o(1)){m\over H}\longrightarrow\infty.
\tag{0.7}
\]

The prescribed cores can simultaneously be extended to a global core atlas
satisfying every original common-core degree cap.

Four accompanying theorems locate the exact global boundary.

* Every inclusion-minimal obstruction using complete root fibres has
  compatibility-graph minimum degree at least
  \(\lceil1/(kp_*)\rceil\), whose logarithm is at least
  \(((\log 2)/4-o(1))H\).
* The common-core caps nevertheless allow one physical compatibility
  component on \(2^s=\exp(\Theta(m))\) roots, so root locality gives no
  \(\exp(O(H))\) component bound.
* Any same-root replacement against a frozen matching exterior has
  nonnegative exterior derivative; a moving-hole floor descent is not an
  augmenting move without a separately proved free new shore.
* There is an abstract cyclic-Latin primitive of support
  \(\exp(\Theta(H\log(s/H)))\), larger than \(\exp(CH)\) for every fixed
  \(C\), satisfying the coarse root-degree, edge-rank, target-capacity,
  compatible-root-cap, maximum-exposure, and quota-count inequalities. It
  does **not** satisfy the exact typewise exposure identities or physical
  target census of a literal CCTPF fibre. It therefore identifies, but does
  not settle, the missing structural theorem.

The conclusion is deliberately precise. It rules out decomposition of the
displayed literal odd-port subinstance into smaller infeasible induced
rooted subinstances, and none of the presently audited moving-hole exchanges
is supported wholly on its roots. It does **not** rule out a generation
theorem which imports roots or additional columns, and it does **not**
construct a complete-fibre CCTPF counterexample. Indeed, the full root
fibres repair this primitive by the exponential local-repair theorem.
Therefore the following stronger question remains open:

> Does every obstruction which is closed under *all* literal histories in
> each participating root contain, or reduce to, a complete-fibre closed
> obstruction on \(\exp(O(H))\) roots?

The present theorem shows that such a result, if true, must use full-fibre
escape. It is not obtained by decomposing this displayed odd-port minor into
smaller infeasible induced subsystems or by applying one of the listed
moving-hole exchanges wholly inside its root set.

## 1. Full-history notation

Fix a top \(U\), a core \(Q_U\subset U\) of size \(2H\), and put

\[
 S_U=U\setminus Q_U,\qquad |S_U|=s.
\]

For a permutation \(w=(w_1,\ldots,w_s)\) of \(S_U\), phase
\(1\le j\le L\), and deletion length \(0\le\ell\le2H\), set

\[
 R_{j,\ell}=\{j+2H-\ell,\ldots,j+2H-1\},
\]

\[
 T_{j,\ell}(w)
 =U\setminus\{w_t:t\in R_{j,\ell}\}.
\tag{1.1}
\]

The middle deletion length is \(H\). At signed depth \(q\), the upper and
lower deletion lengths are \(H-q\) and \(H+q\). A nested phase family

\[
 [L]=A_0\supseteq A_1\supseteq\cdots\supseteq A_{H-1},
 \qquad |A_q|=b_q,
\tag{1.2}
\]

activates both signed traces at depth \(q\) precisely on \(A_q\).

The calibration implies

\[
 b_1=L-1
\tag{1.3}
\]

for all sufficiently large \(m\). Indeed,

\[
 {N_1\over N_H}={m\over m+1}\Lambda
 \ge {m\over m+1}(L+c_0H)>L.
\]

## 2. The cyclic root and word construction

Assume (0.4). Choose a set

\[
 K\subset[2m],\qquad |K|=m+1,
\tag{2.1}
\]

and a common core

\[
 Q\in\binom K{2H}.
\tag{2.2}
\]

Choose \(2n\) distinct special labels

\[
 z_{i,b}\in K\setminus Q,
 \qquad i\in\mathbb Z/n\mathbb Z,\quad b\in\{0,1\}.
\tag{2.3}
\]

This is possible because the second inequality in (0.4) gives
\(2n\le m+1-2H\). The complement of \(K\) has size \(m-1\). By the first
inequality in (0.4), choose pairwise disjoint sets

\[
 E_i\subset[2m]\setminus K,
 \qquad |E_i|=H-1
 \quad(i\in\mathbb Z_n).
\tag{2.4}
\]

Define the roots

\[
 U_i=K\cup E_i.
\tag{2.5}
\]

Then \(|U_i|=M\), every \(Q\) is a legal core in \(U_i\), and

\[
 U_i\cap U_j=K,\qquad
 d_J(U_i,U_j)=H-1
 \quad(i\ne j).
\tag{2.6}
\]

Put

\[
 \rho=2n-2,
 \qquad
 p=\rho+2H+1=2n+2H-1,
 \qquad
 a=p-H=2n+H-1.
\tag{2.7}
\]

For each \(i,b\), construct a permutation \(w_i^b\) of
\(S_i=U_i\setminus Q\) as follows.

* Put all \(2n-2\) special labels other than
  \(z_{i-1,b},z_{i,b}\) in positions \(1,\ldots,\rho\).
* Fill positions \(\rho+1,\ldots,p-1\) with arbitrary nonspecial labels.
* In positions \(p,\ldots,p+H\), put the consecutive segment

  \[
  z_{i-1,b},\quad E_i,\quad z_{i,b},
  \tag{2.8}
  \]

  with an arbitrary fixed order on \(E_i\).
* Fill every remaining position arbitrarily.

The number of positions used through the end of (2.8) is

\[
 p+H=2n+3H-1\le m-H=s
\tag{2.9}
\]

by (0.4), so the total position count is feasible. In addition,

\[
 |(K\setminus Q)\setminus\mathcal Z|
 =m+1-2H-2n\ge2H.
\tag{2.9a}
\]

Thus the \(2H\)-position gap before (2.8) can be filled entirely with
nonspecial \(K\setminus Q\) labels, without using the reserved \(E_i\).
After all displayed positions are filled, the number of remaining labels
is

\[
 m+1-2n-4H\ge0.
\tag{2.9b}
\]

This verifies the label types as well as the position count. Moreover,

\[
 a\ge1,\qquad a+1\le L,
\tag{2.10}
\]

again by \(2n+4H\le m+1\). Its two displayed middle windows are

\[
 R_{a,H}=\{p,\ldots,p+H-1\},
 \qquad
 R_{a+1,H}=\{p+1,\ldots,p+H\},
\tag{2.11}
\]

and the intervening upper depth-one window is

\[
 R_{a,H-1}=\{p+1,\ldots,p+H-1\}.
\tag{2.12}
\]

Fix one nested family, the same for every root and both options, with

\[
 A_1\subseteq[L]\setminus\{a\},
 \qquad |A_1|=b_1.
\tag{2.13}
\]

Choose \(A_2,\ldots,A_{H-1}\) nested inside \(A_1\) with the sizes in
(1.2); this is possible because \((b_q)\) is nonincreasing. In the
sufficiently large calibrated regime, (1.3) forces
\(A_1=[L]\setminus\{a\}\). Let \(P_i^b\) be the resulting literal tagged
history.

Finally define the designated middle targets

\[
 T_{i,b}=K\setminus\{z_{i,b}\}.
\tag{2.14}
\]

The two windows in (2.11) show that

\[
 T_{i-1,b},T_{i,b}\in P_i^b.
\tag{2.15}
\]

## 3. Complete signed collision classification

Let

\[
 \mathcal Z=\{z_{i,b}:i\in\mathbb Z_n, b\in\{0,1\}\},
\]

and put

\[
 Z_{i,b}^{\rm adj}=\{z_{i-1,b},z_{i,b}\}.
\tag{3.1}
\]

### Lemma 3.1 (cross-root targets)

For two histories at distinct roots, a common protected target exists if
and only if the roots are adjacent in \(C_n\) and their bits agree.
Every common middle target is one of the targets in (2.14). Every possible
common lower target also joins only such an adjacent same-bit pair. No upper
target is common across roots.

#### Proof

Suppose a target \(T\) occurs in histories at roots \(U_i,U_j\), where
\(i\ne j\). Equation (2.6) gives

\[
 T\subseteq U_i\cap U_j=K.
\tag{3.2}
\]

If \(|T|=m+q\) with \(q\ge2\), (3.2) is impossible because
\(|K|=m+1\). If \(|T|=m+1\), then \(T=K\). In root \(U_i\), this would
require the deletion interval to be exactly \(E_i\). Since the elements of
\(E_i\) occupy the consecutive positions in (2.12), that positional
interval is unique and belongs to phase \(a\). Phase \(a\notin A_1\), so
this upper depth-one target is inactive. Thus no upper target is common.

If \(|T|=m\), then

\[
 U_i\setminus T=E_i\cup\{z\}
\tag{3.3}
\]

for some \(z\in K\). A length-\(H\) interval containing all \(H-1\)
consecutive elements of \(E_i\) must be one of the two windows in (2.11).
Therefore \(z\in Z_{i,b}^{\rm adj}\), and \(T\) is one of the two targets
in (2.15).

It remains to consider \(|T|=m-q\), \(1\le q<H\). Write

\[
 Z=K\setminus T,
 \qquad |Z|=q+1.
\tag{3.4}
\]

The deletion interval in history \(P_i^b\) must be

\[
 E_i\cup Z,
\tag{3.5}
\]

of length \(H+q\le2H-1\). Any interval containing the entire consecutive
\(E_i\)-block contains at least one of its two immediate neighbours in
(2.8). The gap of \(2H\) positions before (2.8) ensures that no other
member of \(\mathcal Z\) lies in such an interval. Hence

\[
 \varnothing\ne Z\cap\mathcal Z
 \subseteq Z_{i,b}^{\rm adj}.
\tag{3.6}
\]

For histories at distinct roots, two sets of the form (3.1) have nonempty
intersection exactly when the bits agree and the two roots are adjacent on
\(C_n\). Thus every possible lower collision has that form.

Conversely, (2.15) shows that \(P_i^b\) and \(P_{i+1}^b\) share the middle
target \(T_{i,b}\). This proves the equivalence. \(\square\)

### Corollary 3.2 (target loads)

Every protected target belongs to at most two histories among the
\(2n\) columns.

#### Proof

A target not contained in \(K\) can occur only at one root, hence in at
most its two options.

Now let \(T\subseteq K\). There is no upper occurrence. For a middle
occurrence, \(K\setminus T=\{z_{j,c}\}\) is one special label. It belongs
to exactly the two endpoint sets
\[
 Z_{j,c}^{\rm adj},\qquad Z_{j+1,c}^{\rm adj},
\]
and to no opposite-bit endpoint set. Hence \(T\) occurs in at most two
histories.

For a lower occurrence put
\[
 Z_*=(K\setminus T)\cap\mathcal Z.
\]
By (3.6), every occurrence in \(P_i^b\) satisfies
\[
 \varnothing\ne Z_*\subseteq Z_{i,b}^{\rm adj}.
\]
If \(T\) occurs at two distinct roots, Lemma 3.1 says they are adjacent
and have the same bit. Their two endpoint sets intersect in exactly their
shared edge label, so the preceding inclusions force \(Z_*\) to equal that
singleton. No third root endpoint set contains this label, including when
\(n=3\), and no opposite-bit endpoint set contains it. Thus there is no
third occurrence. The two bit endpoint sets at one root are disjoint, so a
lower \(K\)-target cannot occur in both options of that root either.
Therefore every protected target occurs in at most two displayed histories.
\(\square\)

## 4. The primitive odd-cycle theorem

### Theorem 4.1 (fractional feasibility and displayed-column failure)

The assignment (0.5) satisfies every root equality and every protected
target-capacity inequality. No integral root-saturating selection exists
among the displayed \(2n\) columns.

#### Proof

Every root has exactly two displayed histories, so (0.5) gives root load
one. Corollary 3.2 gives target load at most one.

An integral selection chooses bits \(b_i\in\{0,1\}\). By Lemma 3.1 it is
target-simple exactly when

\[
 b_i\ne b_{i+1}
 \qquad(i\in\mathbb Z_n).
\tag{4.1}
\]

This would be a proper two-colouring of the odd cycle \(C_n\), which is
impossible. \(\square\)

### Theorem 4.2 (root-minimality)

Every proper subset of the \(n\) roots has a target-simple choice from its
displayed histories. Hence the displayed-column obstruction is
inclusion-minimal in root support and cannot be decomposed into smaller
infeasible induced rooted subinstances.

#### Proof

The subgraph of \(C_n\) induced by a proper vertex subset is a disjoint
union of paths. Two-colour every path and choose the corresponding bit at
each retained root. Lemma 3.1 shows that no two chosen histories share a
target. \(\square\)

### Theorem 4.3 (exact odd-port matrix)

Fix \(b\in\{0,1\}\). Index rows by \(T_{i,b}\) and columns by \(P_i^b\).
The resulting designated target--history incidence matrix is

\[
 B_n=I+P_n,
\tag{4.2}
\]

where \(P_n\) is the permutation matrix of a cyclic shift. Since \(n\) is
odd,

\[
 \det B_n=2.
\tag{4.3}
\]

Every integral target-simple subfamily of these \(n\) columns satisfies

\[
 \sum_i x(P_i^b)\le {n-1\over2},
\tag{4.4}
\]

whereas the target rows alone permit \(x(P_i^b)=1/2\) and total \(n/2\).

#### Proof

By (2.15) and Lemma 3.1, row \(T_{i,b}\) has ones exactly in columns
\(P_i^b,P_{i+1}^b\), proving (4.2). If \(\zeta\) ranges over the \(n\)-th
roots of unity, then

\[
 \det(I+P_n)=\prod_{\zeta^n=1}(1+\zeta)
 =1-(-1)^n=2.
\]

The conflict graph is \(C_n\), whose maximum stable-set size is
\((n-1)/2\). This proves (4.4). \(\square\)

Summing (4.4) over the two bits gives an integral upper bound \(n-1\),
while the \(n\) root equalities require total selected mass \(n\). This is
the exact odd-set certificate.

## 5. Asymptotic size and compatibility with the common-core caps

### Corollary 5.1 (unbounded support)

At the calibrated height, there is a choice of odd \(n\) satisfying (0.4)
and

\[
 n=(1+o(1)){m\over H}.
\tag{5.1}
\]

#### Proof

Let \(u=\lfloor(m-1)/(H-1)\rfloor\), and take the largest odd integer
\(n\le u\). Since \(H\to\infty\) and \(H=o(m)\),

\[
 2u+4H=o(m)+o(m)<m+1
\]

for all sufficiently large \(m\). Thus (0.4) holds, and
\(n=(1+o(1))m/H\to\infty\). \(\square\)

### Theorem 5.2 (the growing prescribed core family extends)

For the choice in Corollary 5.1, the prescribed pairs \((U_i,Q)\) extend
to a core assignment on every rank-\(M\) top satisfying all CCTPF middle
and signed maximum-degree caps.

#### Proof

Choose every unprescribed top core independently and uniformly, as in the
audited common-core theorem. A fixed target receives at most \(n=O(m/H)\)
deterministic compatible tops from the prescribed family.

At the middle, with \(d_0=\binom{s}{H}\), the cap-minus-mean margin is

\[
 d_0\left({1\over L}-{1\over\Lambda}\right)
 \ge c\,d_0{H\over m^2}.
\tag{5.2}
\]

This is superpolynomial and hence is \(\gg n\).

At signed rank \(m+r\), put

\[
 d_r=\binom{s}{H-r},
 \qquad
 \Lambda_r={N_{|r|}\over N_H}.
\]

Whenever \(b_{|r|}>0\), one has \(\Lambda_r-b_{|r|}\ge1\), so the
cap-minus-mean margin is at least

\[
 {d_r\over b_{|r|}}-{d_r\over\Lambda_r}
 \ge {d_r\over\Lambda_r^2}.
\tag{5.3}
\]

Positivity of \(b_q\) implies

\[
 H-q\ge
 t_*:=\left\lceil{(m-H+1)\log 2\over2H-1}\right\rceil.
\tag{5.4}
\]

For large \(m\), one has \(2H-1<s/2\), so binomial monotonicity on
\([0,s/2]\) gives

\[
 d_r=\binom{s}{H-r}\ge\binom{s}{t_*}
\]

at every active signed rank, including lower ranks for which \(H-r>H\).
Also \(\Lambda_r\le\Lambda=O(m)\). At the critical height,

\[
 \log\binom{s}{t_*}
 \ge\left({\log 2\over4}-o(1)\right)H.
\tag{5.5}
\]

Consequently the margin in (5.3) is \(\exp(\Omega(H))\), up to a
polynomial factor, and is again \(\gg n\).

After subtracting the deterministic contribution \(n\), at least half of
each cap-minus-mean margin remains for large \(m\). The original Chernoff
exponents, namely

\[
 \Omega\left({d_0H^2\over m^3}\right)
 \quad\hbox{and}\quad
 \Omega\left({d_r\over\Lambda_r^3}\right),
\]

remain \(\gg m\). A union bound over fewer than \(2H4^m\) target rows has
positive success probability. Hence a completion satisfying every cap
exists. \(\square\)

## 6. What a complete-fibre obstruction would have to satisfy

The primitive above uses only two columns per root. We now record the exact
stronger condition forced by a genuinely complete-fibre obstruction.

For fixed cores, let \(\Omega_U\) be either the \(s!\)-element tail-order
fibre for one fixed nested tag family, or the unrestricted fibre of all
pairs \((w,A)\) with an admissible nested family \(A\). In the unrestricted
case, permutation of the \(L\) phase labels acts transitively on tag
families, so a fixed phase is active at depth \(q\) in fraction \(b_q/L\)
of them. Consequently the exact single-port exposures are still bounded by
(6.0b). Join two roots in the
**compatibility graph** \(G\) when some protected target is compatible with
both complete fibres.

Put

\[
 k=L+2\sum_{q=1}^{H-1}b_q
\tag{6.0a}
\]

and

\[
 p_*=\max\left\{
 {L\over\binom{s}{H}},
 \max_{\substack{1\le q<H\\b_q>0}}
 \left\{
 {b_q\over\binom{s}{H-q}},
 {b_q\over\binom{s}{H+q}}
 \right\}
 \right\}.
\tag{6.0b}
\]

### Theorem 6.1 (full-fibre wall and minimum degree)

Let \(\mathcal R\) be an inclusion-minimal root set whose complete fibres
have no target-simple transversal. Then, for every \(U\in\mathcal R\) and
every transversal \(\mathcal M\) of \(\mathcal R\setminus\{U\}\), the
targets used by \(\mathcal M\) block every order in \(\Omega_U\). Moreover,

\[
 \delta(G[\mathcal R])
 \ge \left\lceil{1\over kp_*}\right\rceil,
\tag{6.1}
\]

Here \(p_*\) is the exact largest normalized single-port exposure in one
fixed-tag root fibre. The same values hold after averaging over the
unrestricted tag fibre.

#### Proof

Minimality supplies \(\mathcal M\). Let \(\mathcal B\) be the union of its
protected targets. If one order in \(\Omega_U\) avoided \(\mathcal B\), it
could be adjoined to \(\mathcal M\), contradicting infeasibility. Hence the
union of the port cylinders indexed by \(\mathcal B\) covers all members of
\(\Omega_U\). With \(p_U(T)\) denoting the exact fraction of the fibre using
\(T\), the union bound gives

\[
 1\le\sum_{T\in\mathcal B}p_U(T).
\tag{6.2}
\]

One history of \(\mathcal M\) contributes at most \(kp_*\) to this sum.
Therefore at least \(\lceil1/(kp_*)\rceil\) histories of \(\mathcal M\)
have positive blocking contribution. Their roots are distinct neighbours
of \(U\) in \(G\). Since \(U\) was arbitrary, (6.1) follows. \(\square\)

This is a sharp peeling condition, but it points in the wrong direction
for the proposed decomposition: it gives a lower degree and lower support,
not an upper bound on a primitive component.

### Corollary 6.2 (local edges do not imply local components)

Every edge \(UV\) of \(G\) satisfies

\[
 d_J(U,V)\le2H-t_*.
\tag{6.3}
\]

#### Proof

A shared protected target \(T\) lies in \(U\cap V\). If its deletion
length is \(\ell\), then

\[
 d_J(U,V)=M-|U\cap V|\le M-|T|=\ell.
\]

The middle length is \(H\). At an active upper or lower depth \(q\),
Inequality (5.4) gives \(q\le H-t_*\), so every active deletion length is at
most \(H+q\le2H-t_*\). \(\square\)

### Theorem 6.3 (the caps permit a giant physical compatibility component)

There is a prescribed family of

\[
 2^s=\exp(\Theta(m))
\tag{6.4}
\]

top--core pairs which extends to a globally capped common-core atlas and
which lies in one connected component of \(G\).

#### Proof

Fix \(Q\subset[2m]\), \(|Q|=2H\), and partition the remaining \(2s\)
coordinates into pairs

\[
 \{a_{j,0},a_{j,1}\},\qquad 1\le j\le s.
\]

For \(\varepsilon\in\{0,1\}^s\), put

\[
 U_\varepsilon
 =Q\cup\{a_{j,\varepsilon_j}:1\le j\le s\},
 \qquad Q_{U_\varepsilon}=Q.
\tag{6.5}
\]

These are \(2^s\) distinct rank-\(M\) tops. Adjacent cube corners have
intersection of size \(M-1\) and share a compatible middle target: take
\(Q\) together with any \(m-2H\) of their \(s-1\) common selected
coordinates. More generally, two cell roots at Hamming distance
\(d\le H\) share such a middle target. Thus the whole cube is connected in
\(G\), and every cell root has at least

\[
 \sum_{d=1}^{H}\binom{s}{d}
 =\exp\left(\Theta\left(H\log{s\over H}\right)\right)
\tag{6.5a}
\]

neighbours inside the cell.

It remains to retain the caps. Let \(T\) have rank \(m+r\), and put
\(\ell=H-r\). If \(Q\nsubseteq T\), no cell top--core pair is compatible
with \(T\). If \(Q\subseteq T\) but \(T\setminus Q\) contains both members
of one coordinate pair, no cell top contains \(T\). Otherwise
\(T\setminus Q\) fixes exactly \(s-\ell\) pair choices, and precisely

\[
 2^\ell
\tag{6.6}
\]

cell tops contain \(T\).

At the middle, \(2^H=o(\binom{s}{H}H/m^2)\), so (6.6) is negligible
relative to the cap-minus-mean margin (5.2). At an active signed rank,
\(t_*\le\ell\le2H-1\). Since

\[
 {\binom{s}{\ell}\over 2^\ell}
 \ge\left({s\over2\ell}\right)^\ell
 \ge\left({s\over4H}\right)^{t_*}
 =\exp(\Omega(H)),
\tag{6.7}
\]

one has

\[
 2^\ell=o\left({\binom{s}{\ell}\over m^2}\right).
\tag{6.8}
\]

Thus the deterministic cell contribution is negligible relative to every
signed cap-minus-mean margin (5.3). Choose all remaining cores independently
at random. The same Chernoff exponents as in Theorem 5.2 survive, and the
union bound completes the cell to a globally capped atlas. \(\square\)

Since \(H=o(m)\), the component in (6.4) is much larger than
\(\exp(CH)\) for every fixed \(C\). It is not asserted infeasible. Its role
is exact: connected-component or root-locality closure cannot prove the
desired \(\exp(O(H))\) decomposition.

## 7. Moving-hole and six-frame exchange audit

### Theorem 7.1 (internal exchange inertness)

No nontrivial instance of any of the following audited exchanges is
supported entirely on the root set \(\{U_i:i\in\mathbb Z_n\}\):

1. the two-top moving-hole transfer;
2. the three-top or symmetric six-top two-base conveyor;
3. the four-top squarefree moving-hole cube;
4. the six-frame mixed-placeholder rectangle; or
5. the eight-top squarefree moving-hole cube.

#### Proof

By (2.6), every pair of distinct gadget roots has Johnson distance
\(H-1\ge4\).

The two-top transfer uses adjacent tops and hence distance one. The
two-base conveyors and the four-top cube use a common base of size
\(M-2\), so every two touched tops have distance at most two. The
mixed-placeholder six-frame rectangle and the eight-top cube use a common
base of size \(M-3\), so every two touched tops have distance at most
three. Therefore no listed exchange can contain two distinct roots from
the gadget, while every nontrivial listed exchange changes at least two
roots. \(\square\)

This is an internal statement. An exchange may import exterior roots, but
then it is not a decomposition of the given rooted subsystem. Moreover,
the complete-frame moving-hole theorems do not by themselves prove the
fixed-core, \(L\)-phase CCTPF interface for such an imported exchange.

### Theorem 7.2 (frozen-exterior orthogonality)

Let \(\mathcal Q\) be a target-simple matching. Remove a block
\(\mathcal O\subseteq\mathcal Q\), and let \(\mathcal B_{\rm ext}\) be
the typed target set used by the unchanged exterior
\(\mathcal Q\setminus\mathcal O\). Let \(\mathcal N\) be any internally
target-simple same-root replacement. If \(\Gamma^0,\Gamma^1\) are the
aggregate \(0\)-\(1\) target indicators of \(\mathcal O,\mathcal N\), and
\(\Delta=\Gamma^1-\Gamma^0\), then

\[
 \left\langle1_{\mathcal B_{\rm ext}},\Delta\right\rangle
 =\left\langle1_{\mathcal B_{\rm ext}},\Gamma^1\right\rangle
 =\left|\Gamma(\mathcal N)\cap\mathcal B_{\rm ext}\right|\ge0.
\tag{7.1}
\]

Equality holds if and only if the new shore is completely disjoint from the
exterior.

#### Proof

The old shore belongs to the matching \(\mathcal Q\), so

\[
 \left\langle1_{\mathcal B_{\rm ext}},\Gamma^0\right\rangle=0.
\]

Subtracting this identity gives (7.1). The last inner product counts new
exterior collisions and is zero exactly when none exists. \(\square\)

The identity remains true with arbitrary positive weights on ranks. If, in
addition, the two shores are internally target-simple at every typed rank,
have equal port counts rank by rank, and the objective baseline is constant
within each rank, then a floor-energy derivative cannot cancel a frozen
CCTPF port wall: every negative coordinate belongs to the removed old shore
and has exterior load zero. The conclusion does not apply to an
algebraically signed objective or to an augmentation which also removes
exterior blockers. Under the stated hypotheses, the state-adaptive descent
in a moving-hole or conveyor theorem reduces inside a matching to the
free-new-shore test in (7.1).

There are two further interface gaps. The two-top moving-hole packet has
repeated middle owners. The three-/six-top squarefree conveyor is certified
squarefree at the middle, but its reports do not prove that either shore is
target-simple at every active signed rank, and arbitrary fixed-tag schedules
are not covered. Thus none of these packets is presently a universal CCTPF
Markov move.

### Corollary 7.3 (binary-subinstance monodromy)

On a proper arc of \(\ell\) edges in the primitive of Section 4, target
simplicity imposes the two-terminal relation

\[
 b_v=b_u\mathbin\oplus(\ell\bmod2).
\tag{7.2}
\]

Any replacement already certified to preserve this binary two-terminal
relation preserves it. Composing around odd \(C_n\) gives

\[
 b_0=b_0\mathbin\oplus1,
\]

so no sequence of such relation-preserving moves repairs or decomposes the
displayed primitive. The full exterior target ledger alone has not been
proved to force (7.2) for arbitrary additional histories. A successful
step may therefore import exterior roots/ports or change the boundary
relation by using additional columns.

## 8. An exponential abstract primitive satisfying coarse marginal bounds

The next theorem is a no-go for proofs using only capacities, exposures,
root degrees, and quota counts. It is explicitly **not** a literal interval
construction.

### Theorem 8.1 (cyclic Latin monodromy countermodel)

Let \(D=s!\), and let

\[
 h=\left\lfloor{H\over4}\log_2{s\over H}\right\rfloor,
 \qquad n=2^h.
\tag{8.1}
\]

For all sufficiently large \(m\), there is a rooted typed-port system on
\(n\) roots with exactly \(D\) configurations per root and exactly \(k\)
ports per configuration such that:

1. the uniform weight \(1/D\) is root-saturating and loads every port by at
   most one;
2. every shared port occurs in exactly a \(1/n\) fraction of each incident
   root fibre, and \(1/n=o(p_*)\);
3. shared middle ports are compatible with \(n\le\binom{s}{H}/L\) roots,
   while every private signed port is compatible with only one root; hence
   all numerical common-core caps are respected;
4. the complete root fibres have no integral target-simple transversal;
5. deleting any root leaves a transversal; and
6. \(\log n=\Theta(H\log(s/H))\), so \(n\) is larger than
   \(\exp(CH)\) for every fixed \(C\).

#### Construction

Index roots and two shared port families by \(\mathbb Z/n\mathbb Z\):

\[
 U_i,\qquad C_j,\qquad S_j.
\]

Since \(h=o(s)\), the power \(n=2^h\) divides \(s!\). At root \(U_i\),
take configurations

\[
 F_{i,j,a},
 \qquad j\in\mathbb Z/n\mathbb Z,
 \quad 1\le a\le D/n.
\tag{8.2}
\]

Configuration \(F_{i,j,a}\) contains the two shared ports

\[
 C_j,\qquad S_{i+j},
\tag{8.3}
\]

and \(k-2\) ports \(P_{i,j,t}\), \(1\le t\le k-2\), private to the
root--state pair \((i,j)\) and repeated over the parallel index \(a\). Ports
with different triples \((i,j,t)\) are distinct. The two shared ports may
be assigned to two middle slots and all private ports assigned types so that
each configuration has exactly \(L\) middle, \(b_q\) lower, and \(b_q\)
upper ports at every depth. This matches the CCTPF typed cardinalities, but
no interval-word realization is asserted.

In particular, every positive-depth signed port can be private. Separate
signed coordinate-injectivity and cemetery-nesting requirements are then
tautological; the obstruction lives entirely in coupling two middle slots
to one root choice. What is absent is precisely the literal tight-path
interval relation between those slots.

#### Fractional and numerical audit

At one root, a fixed \(C_j\), a fixed \(S_j\), or a fixed private port in
that root occurs in exactly \(D/n\) configurations. Across all roots,
uniform weight \(1/D\) therefore
gives each shared port total load

\[
 n{D/n\over D}=1.
\tag{8.4}
\]

A private port has load \(1/n\). Thus all rows pass. The total number of
formal ports of any one prescribed type is at most \(n^2k=\exp(o(m))\),
whereas every active Boolean target layer has \(\exp(\Theta(m))\) members.
Thus the ports can be injected into labels of the correct ranks. This does
not reproduce the physical target census: most compatible Boolean targets
never occur, and the occurrences of those which do occur need not have the
literal typewise exposure.

The elementary valuation bound

\[
 v_2(s!)\ge\left\lfloor{s\over2}\right\rfloor>h
\]

proves \(n\mid D\). Stirling's lower bound gives

\[
 \log\binom{s}{H}\ge H\log{s\over H},
\]

so (8.1) gives \(n\le\binom{s}{H}/L\) for large \(m\).

For completeness, take

\[
 \ell_0=\left\lceil {4(\log 2)m\over H}\right\rceil,
 \qquad q_0=H-\ell_0.
\]

For all \(q_0<i\le H\),

\[
 \log{m+i\over m-i+1}
 \ge {2i-1\over m+i}\ge {H\over2m}
\]

for large \(m\). Hence \(N_{q_0}/N_H\ge4\), so \(b_{q_0}>0\). The
corresponding upper-port exposure is at least
\(1/\binom{s}{\ell_0}=\exp(-O(H))\), because
\(\ell_0=O(m/H)\) and
\((m/H)\log(e sH/m)=O(H)\) at the calibrated height. Therefore

\[
 {1\over n}
 =\exp\left(-\Theta(H\log(s/H))\right),
\]

and hence \(1/n=o(p_*)\). Finally \(\log(s/H)\to\infty\), proving Item 6.

#### Integral obstruction

An integral transversal chooses one \(j_i\) at every root. Avoiding the
\(C\)-ports requires \(i\mapsto j_i\) to be a permutation of
\(\mathbb Z/n\mathbb Z\); avoiding the \(S\)-ports requires
\(i\mapsto i+j_i\) to be another permutation. Write \(n=2t\). The sum of
all residues modulo \(n\) is \(t\), so the first permutation would give

\[
 \sum_i(i+j_i)\equiv t+t\equiv0\pmod n.
\]

The second permutation would require the same sum to be \(t\not\equiv0\),
a contradiction.

To prove root-minimality, use the sequence

\[
 a_0,a_1,\ldots,a_{n-1}
 =(0,1,n-1,2,n-2,\ldots,t).
\tag{8.5}
\]

Its consecutive differences are all the nonzero residues: the odd-indexed
differences are \(1,3,\ldots,n-1\), and the even-indexed differences are
\(n-2,n-4,\ldots,2\). If root \(r\) is omitted, for
\(0\le q\le n-2\) assign

\[
 i_q=r+(a_{q+1}-a_q),
 \qquad
 j_{i_q}=a_q-r.
\tag{8.6}
\]

The rows \(i_q\) are all residues except \(r\), the columns \(j_{i_q}\)
are distinct, and the symbols satisfy

\[
 i_q+j_{i_q}=a_{q+1},
\]

so they too are distinct. This is a transversal after deleting \(r\).
Restricting it proves feasibility of every proper root subset. \(\square\)

The wall has an exact central-involution form. In any transversal after
deleting root \(r\), let \(c\) and \(s_0\) be the unused \(C\)- and
\(S\)-port indices. Summing the selected cells gives

\[
 t-s_0\equiv(t-r)+(t-c)\pmod n,
\]

and hence

\[
 s_0\equiv t+r+c\pmod n.
\tag{8.7}
\]

The missing root would have to use \(C_c\) and \(S_{r+c}\), but
\(r+c\not\equiv s_0\) because \(t=n/2\ne0\). Thus every configuration of
the missing root is blocked although one port of each shared family remains
free. This is monodromy, not scalar target shortage.

Theorem 8.1 proves that the requested \(\exp(O(H))\) primitive-support
bound is false for the abstraction retaining root degree, edge rank,
target load at most one, numerical compatible-root caps, quota counts, and
only the coarse ceiling \(p_U(T)\le p_*\). It does **not** satisfy the exact
CCTPF exposure identities. For example, a shared middle port has root-fibre
exposure \(1/n\), whereas a literal compatible middle target has exposure

\[
 p_0={L\over\binom{s}{H}},
\]

and \(1/n\gg p_0\). Private positive-depth ports likewise have exposure
\(1/n\), rather than their prescribed typewise values. Thus the Latin
model is not a counterexample to literal complete-fibre localization.
Excluding its central-involution monodromy requires a theorem using exact
interval cylinders, their codegrees, or the full target census. Coarse
marginal flow and bounded exchange support cannot do it.

## 9. Why the literal primitive does not contradict local repair

Let

\[
 k=L+2\sum_{q=1}^{H-1}b_q
\]

be the number of protected targets in one history, and let \(p_*\) be the
maximum normalized single-target exposure in one fixed root fibre. The
previous full-history repair theorem proves

\[
 \log{1\over kp_*}
 \ge\left({\log 2\over4}-o(1)\right)H.
\tag{9.1}
\]

Since \(\log n=O(\log m)=o(H)\), (9.1) gives

\[
 (n-1)kp_*<1
\tag{9.2}
\]

for the primitive in Corollary 5.1. Therefore, after restoring every tail
order in each of the same roots while keeping the same cores and nested tag
families, the greedy repair theorem finds another target-simple integral
selection.

Thus three different statements must not be conflated.

1. **Proved negative:** the natural full-history incidence matrix has
   primitive literal odd-port minors of unbounded root support, compatible
   with every common-core cap and internally inert under the current
   moving-hole library.
2. **Proved positive:** every one of these particular primitives is repaired
   by unused columns in its complete root fibres.
3. **Open:** whether every complete-fibre, blocker-closed global obstruction
   admits such a repair or contains a complete-fibre closed subsystem of
   size \(\exp(O(H))\).

Accordingly, exponential local repair does not globalize by a formal
decomposition of incidence circuits. A successful globalization theorem
must prove a new full-fibre closure or augmentation statement; the known
odd-set inequalities and moving-hole exchanges do not supply it.

## 10. Independent audit record

The decisive claims were audited independently in two parts.

1. The literal construction, complete signed collision classification,
   odd-cycle determinant, root-minimality, and common-core cap completion
   were rederived. The audit found and repaired the former \(n=3\) gap in
   Corollary 3.2 by using the fixed special set
   \(Z_*=(K\setminus T)\cap\mathcal Z\). It also required the typed gap
   count (2.9a)--(2.9b) and the displayed-column qualifications in
   Theorems 4.1--4.2. After those repairs, Sections 2--5 pass.
2. The full-fibre wall, giant compatibility component, frozen-exterior
   identity, and cyclic-Latin algebra were rederived. The wall and giant
   component pass. The audit required the hypotheses now stated after
   (7.1) and the restriction in Corollary 7.3. It also identified that the
   Latin system has only coarse exposure control, not the exact CCTPF
   typewise exposures or target census; Section 8 now states that boundary
   explicitly.

No audited step proves or disproves \(\exp(O(H))\) localization for literal
complete root fibres. That is the exact unresolved boundary.
