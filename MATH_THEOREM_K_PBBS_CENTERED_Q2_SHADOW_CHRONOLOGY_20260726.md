# The centered PBBS factor has a complete \(q=2\) shadow

Date: 2026-07-26

Method: pure mathematics only. No web input, computation, finite search, or
solver is used.

## 0. The theorem

Let

\[
 n=2m+1,\qquad m\ge2,\qquad
 \mathcal M=\binom{[n]}m,\qquad
 W=|\mathcal M|,\qquad
 B=\frac{W}{n}=\operatorname {Cat}_m.
\tag{0.1}
\]

Let \(f\) be the canonical forward-parenthesis PBBS permutation of
\(\mathcal M\). The centered Johnson edge at \(X\) is

\[
 e_X=\{f^{-1}X,fX\},
\tag{0.2}
\]

and the directed centered successor is \(g=f^2\).

Every rooted two-edge centered window is indexed uniquely by its middle
owner \(A\):

\[
 f^{-2}A\longrightarrow A\longrightarrow f^2A.
\tag{0.3}
\]

Define its lower \(q=2\) target by

\[
 I_2(A)=f^{-2}A\cap A\cap f^2A
\tag{0.4}
\]

and, for \(S\in\binom{[n]}{m-2}\), define

\[
 \mu_2^-(S)=|\{A\in\mathcal M:I_2(A)=S\}|.
\tag{0.5}
\]

The owner normalization in (0.3)--(0.5) is important: it gives exactly
\(W\) rooted windows. An unrestricted two-parity parametrization
\((\varepsilon,j)\) double-counts a PBBS orbit of odd length, because its
two apparent parity rows are rephasings of the same \(f^2\)-cycle.

### Theorem A (exact parenthesis chronology and complete support)

Normalize \(A\) by cutting at its unique forward-unmatched zero \(r\):

\[
 A=0_rD,
\tag{0.6}
\]

where \(D\) is a Dyck word of semilength \(m\). Let

* \(p_+(D)\) be the first up-step which reaches the global height of \(D\);
* \(p_-(D)\) be the initial up-step of the last primitive factor of \(D\)
  having that global height.

Then

\[
 \boxed{
 I_2(A)=A\setminus\{p_-(D),p_+(D)\}.}
\tag{0.7}
\]

For \(m\ge2\), the two displayed coordinates are distinct. Consequently
every centered turn has the correct lower rank \(m-2\).

Moreover, uniformly for every \(m\ge2\),

\[
 \boxed{
 1\le\mu_2^-(S)\le10
 \qquad\left(S\in\binom{[n]}{m-2}\right).}
\tag{0.8}
\]

In particular,

\[
 \boxed{M_2^-=0.}
\tag{0.9}
\]

Thus the unchanged centered PBBS \(q=1\) core has no lower \(q=2\)
shadow defect. It is not merely \(o(W)\)-complete: it is exactly complete
for every \(m\ge2\).

### Theorem B (exact \(q=1\)-to-\(q=2\) chronology identity)

Orient every centered component by \(g=f^2\), and let

\[
 R(A)=A\cap gA
\tag{0.10}
\]

be its lower \(q=1\) color. For fixed
\(S\in\binom{[n]}{m-2}\), put

\[
 \xi_A(S)=\mathbf1_{\{S\subset R(A)\}}.
\tag{0.11}
\]

On each cyclic centered component, let \(d_C(S)\) be the number of ones in
this binary word and \(r_C(S)\) its number of cyclic one-runs. On an
all-one component set \(r_C(S)=0\). Put

\[
 d_1(S)=\sum_Cd_C(S),\qquad r_S=\sum_Cr_C(S).
\tag{0.12}
\]

Then

\[
 \boxed{
 \mu_2^-(S)
 =\sum_A\xi_{g^{-1}A}(S)\xi_A(S)
 =d_1(S)-r_S,}
\tag{0.13}
\]

and

\[
 \boxed{
 d_1(S)=\sum_{\substack{R\in\binom{[n]}{m-1}\\S\subset R}}
             \mu_1^-(R).}
\tag{0.14}
\]

The PBBS first-shadow theorem gives \(1\le\mu_1^-(R)\le3\), hence

\[
 m+3\le d_1(S)\le3(m+3).
\tag{0.15}
\]

Combining (0.8) and (0.13),

\[
 \boxed{
 d_1(S)-10\le r_S\le d_1(S)-1.}
\tag{0.16}
\]

Thus the \(q=1\) incidences above any \(S\) are mostly isolated, but the
PBBS parenthesis coupling forces at least one consecutive collision for
every \(S\). This is the exact chronological information absent from a
bare \(q=1\) rainbow ledger.

### Quantitative consequence

Since the total number of rooted turns is \(W\),

\[
\begin{aligned}
 \sum_S(\mu_2^-(S)-1)
 &=W-\binom{2m+1}{m-2}\\
 &=\frac{6(m+1)}{(m+2)(m+3)}W
 <12\operatorname {Cat}_m.
\end{aligned}
\tag{0.17}
\]

Therefore all but fewer than \(12\operatorname {Cat}_m\) lower
\(q=2\) targets occur exactly once. The excess repeated mass is
\(O(W/m)=o(W)\), not linear. The balanced floor becomes one at
\(m=8\) and remains one for every \(m\ge8\); the support theorem (0.8)
itself holds from \(m=2\).

The upper \(q=2\) shadow is also complete:

\[
 \boxed{
 1\le\mu_2^+(U)\le3
 \qquad\left(U\in\binom{[n]}{m+2}\right),}
\tag{0.18}
\]

so \(M_2^+=0\).

## 1. PBBS edges, omitted labels, and centered chronology

Write a subset as a cyclic binary word, with \(1\) an opening step and
\(0\) a closing step. Forward cyclic parenthesis matching repeatedly
removes \(10\) pairs; reverse matching removes \(01\) pairs. A middle word
has one unmatched zero in each matching. Write these coordinates as

\[
 r_+(A),\qquad r_-(A).
\tag{1.1}
\]

The PBBS permutation and its inverse are

\[
 f(A)=A^c\setminus\{r_+(A)\},
\qquad
 f^{-1}(A)=A^c\setminus\{r_-(A)\}.
\tag{1.2}
\]

On an oriented \(f\)-orbit, write

\[
 A_t=f^t(A_0),
\qquad
 \lambda_t=[n]\setminus(A_t\cup A_{t+1}).
\tag{1.3}
\]

The omitted coordinate is \(\lambda_t=r_+(A_t)\). Since
\(A_t\) and \(A_{t+1}\) are disjoint \(m\)-sets, the complement of
\(A_{t+1}\) is \(A_t\cup\{\lambda_t\}\). Therefore

\[
 \boxed{
 A_{t+2}
 =A_t\setminus\{\lambda_{t+1}\}\cup\{\lambda_t\}.}
\tag{1.4}
\]

We will also use the elementary odd-gap rule. Fix a coordinate \(x\) and
write \(b_t=\mathbf1_{\{x\in A_t\}}\). If \(\lambda_t\ne x\), then
disjointness and the one-point complement relation give

\[
 b_{t+1}=1-b_t.
\]

If \(\lambda_t=x\), then \(b_t=b_{t+1}=0\). Between two consecutive
occurrences \(\lambda_t=\lambda_{t+g}=x\), the bit therefore makes
\(g-1\) ordinary flips and must return to zero. Hence \(g-1\) is even:

\[
 \boxed{\text{every consecutive same-label gap is odd}.}
\tag{1.4a}
\]

Gap one is impossible. Indeed, \(\lambda_t=\lambda_{t+1}\) would make
\(A_{t+2}=A_t\) in (1.4), whereas the parenthesis formula (2.2) below
replaces the occupied coordinate \(p_+(D)\) by the unoccupied root \(r\).
Thus \(f^2A_t\ne A_t\). It follows in particular that

\[
 \boxed{\lambda_i\ne\lambda_{i+2}.}
\tag{1.4b}
\]

For if equality held and there were no intermediate occurrence of that
label, it would contradict oddness; if the intermediate label were the
same, it would create a forbidden gap one. Combined with the no-gap-three
theorem proved in Section 2, every consecutive same-label gap is at least
five.

The centered edge at \(A_{t+1}\) is

\[
 e_{A_{t+1}}=\{A_t,A_{t+2}\}.
\tag{1.5}
\]

Its lower color is

\[
 C_t=A_t\cap A_{t+2}
     =A_t\setminus\{\lambda_{t+1}\}.
\tag{1.6}
\]

The next centered edge has lower color \(C_{t+2}\), and their common
\(q=2\) target is

\[
 T_t=C_t\cap C_{t+2}
    =A_t\cap A_{t+2}\cap A_{t+4}.
\tag{1.7}
\]

The recurrence gives the exact return formula

\[
 \boxed{
 |T_t|
 =m-2+\mathbf1_{\{\lambda_t=\lambda_{t+3}\}}.}
\tag{1.8}
\]

Indeed, the first centered transition inserts \(\lambda_t\). The only way
the second transition can fail to delete a second original coordinate is
to delete that newly inserted coordinate, which is exactly
\(\lambda_{t+3}=\lambda_t\). Omitted-label recurrences have odd gap, so
the two ordinary deletion labels \(\lambda_{t+1}\) and
\(\lambda_{t+3}\) are distinct.

Section 2 proves directly from parenthesis blocks that PBBS has no gap
three:

\[
 \lambda_t\ne\lambda_{t+3}\qquad(m\ge2).
\tag{1.9}
\]

Consequently

\[
 \boxed{
 T_t
 =A_t\setminus\{\lambda_{t+1},\lambda_{t+3}\},
 \qquad |T_t|=m-2.}
\tag{1.10}
\]

Equivalently, the two consecutive lower colors are the distinct
one-point extensions

\[
 C_t=T_t\cup\{\lambda_{t+3}\},
\qquad
 C_{t+2}=T_t\cup\{\lambda_t\}.
\tag{1.11}
\]

The upper rank is exact as well. The recurrence gives

\[
 A_t\cup A_{t+2}\cup A_{t+4}
 =A_t\cup\{\lambda_t,\lambda_{t+2}\}.
\tag{1.12}
\]

The two inserted labels are distinct because an omitted-label recurrence
has odd gap. Also \(\lambda_{t+2}\notin A_t\): it is outside
\(A_{t+2}\), and the only member of \(A_t\) absent from \(A_{t+2}\) is
\(\lambda_{t+1}\), which differs from the consecutive label
\(\lambda_{t+2}\). Therefore

\[
 \boxed{
 |A_t\cup A_{t+2}\cup A_{t+4}|=m+2.}
\tag{1.13}
\]

This is literal owner chronology in the centered factor, not an incidence
or matching relaxation.

## 2. Exact two-sided parenthesis formula

For a binary word \(Q\), let \(\overline Q\) denote its bitwise
complement. Normalize a middle owner \(A\) at its unique
forward-unmatched zero:

\[
 A=0_rD,
\tag{2.1}
\]

where \(D\) is Dyck. Let \(H\) be the maximum height of \(D\). Define:

* \(p_+(D)\): the first up-step ending at height \(H\);
* \(v(D)\): the down-step immediately after the rightmost visit to height
  \(H\);
* \(p_-(D)\): the initial up-step of the last primitive factor of \(D\)
  whose height is \(H\).

### Lemma 2.1 (distinguished forward and backward deletions)

\[
 \boxed{
 f^2A=(A\cup\{r\})\setminus\{p_+(D)\},}
\tag{2.2}
\]

\[
 \boxed{
 f^{-2}A=(A\cup\{v(D)\})\setminus\{p_-(D)\}.}
\tag{2.3}
\]

#### Proof

Write

\[
 D=P1_{p_+}Q.
\tag{2.4}
\]

After one PBBS step, root the word at \(p_+\). It is

\[
 0_{p_+}\,\overline Q\,0_r\,\overline P.
\tag{2.5}
\]

The suffix is Dyck. The path \(\overline Q\) rises from zero to \(H\)
and stays nonnegative because the old suffix \(Q\), which started at the
first global maximum, never rises above \(H\). The displayed \(0_r\)
lowers to \(H-1\). During \(\overline P\), the height is
\(H-1-h_P\), which is nonnegative and ends at zero. Hence \(p_+\) is the
forward-unmatched root of \(fA\). Since

\[
 (fA)^c=A\cup\{r\},
\]

a second forward PBBS step proves (2.2).

For the inverse formula, write

\[
 D=P'0_vQ'.
\tag{2.6}
\]

We first verify the reverse root rather than merely invoking it. Rotate
\(A\) to begin at \(v\). With \(0\) treated as a reverse opening and
\(1\) as a reverse closing, its suffix is

\[
 Q'\,0_r\,P'.
\]

Because \(v\) follows the rightmost height-\(H\) visit, the old path
\(Q'\) stays at absolute height at most \(H-1\). During \(Q'\), the
reverse height is \(H-1\) minus that absolute height and is nonnegative.
It equals \(H-1\) at the end of \(Q'\); the root bit \(0_r\) raises it
to \(H\); during \(P'\) it is \(H-h_{P'}\), again nonnegative and
ending at zero. The ordinary stack criterion for reverse matching
therefore makes \(v\) the unique reverse-unmatched zero of \(A\).

Put \(C=f^{-1}A\). Rooted at \(v\), its word is

\[
 0_v\,\overline{Q'}\,1_r\,\overline{P'}.
\tag{2.7}
\]

The suffix is Dyck. The block \(\overline{Q'}\) has height at most
\(H-1\); the bit \(1_r\) first raises the path to \(H\); and during
\(\overline{P'}\) its height is \(H-h_{P'}\).

Let \(F\) be the last primitive factor of \(D\) having height \(H\).
The last zero-height prefix of \(P'\) ends immediately before \(F\).
Consequently the rightmost height-\(H\) visit in (2.7) occurs immediately
before the complement of the initial up-step of \(F\). That complemented
step is a down-step at the coordinate \(p_-(D)\). The reverse cycle
lemma—whose stack proof is exactly the preceding rightmost-maximum
calculation—therefore gives

\[
 r_-(C)=p_-(D).
\]

Since \(C^c=A\cup\{v(D)\}\), applying \(f^{-1}\) once more proves
(2.3). \(\square\)

### Lemma 2.2 (the two distinguished steps are distinct)

For \(m\ge2\),

\[
 p_-(D)\ne p_+(D).
\tag{2.8}
\]

#### Proof

If the first and last primitive factors attaining height \(H\) are
different, the two steps lie in different factors. If they are the same
and \(H\ge2\), then \(p_-\) is the initial up-step of that factor and
ends at height one, while \(p_+\) first ends at height \(H\). If \(H=1\),
then every primitive factor is \(10\). Since \(m\ge2\), the first and last
factors differ. \(\square\)

Intersecting (2.2)--(2.3) with \(A\) now proves

\[
 \boxed{
 f^{-2}A\cap A\cap f^2A
 =A\setminus\{p_-(D),p_+(D)\},}
\tag{2.9}
\]

which is (0.7).

This also gives a parenthesis proof of (1.9). Apply (2.9) to
\(A=A_{t+2}\). If \(\lambda_t=\lambda_{t+3}\), recurrence (1.4) would
make the triple intersection have rank \(m-1\), contradicting
Lemma 2.2.

## 3. A literal preimage for every \((m-2)\)-set

Fix

\[
 S\in\binom{[n]}{m-2}.
\tag{3.1}
\]

Its forward parenthesis reduction has five unmatched zeros. In cyclic
order, after choosing the name \(z_0\), there is the cyclic decomposition

\[
 0_{z_0}D_0\,
 0_{z_1}D_1\,
 0_{z_2}D_2\,
 0_{z_3}D_3\,
 0_{z_4}D_4,
\tag{3.2}
\]

where every \(D_j\) is a possibly empty Dyck word and indices are modulo
five.

Suppose first that \(m\ge3\). Then \(S\) contains at least one \(1\), so
some \(D_i\) is nonempty. Choose \(D_i\) of maximum height \(H\). Let
\(u\) be the down-step immediately following the rightmost visit of
\(D_i\) to height \(H\), and let \(D_i^\uparrow\) be obtained by changing
that step \(0_u\) to \(1_u\). Put

\[
 A=S\cup\{z_i,u\}.
\tag{3.3}
\]

Root \(A\) at \(z_{i+4}\). Its Dyck suffix is

\[
\begin{aligned}
 E={}&D_{i+4}\,
 1_{z_i}D_i^\uparrow\,
 0_{z_{i+1}}D_{i+1}\,
 0_{z_{i+2}}D_{i+2}\,
 0_{z_{i+3}}D_{i+3}.
\end{aligned}
\tag{3.4}
\]

To see that \(E\) is Dyck, note that after \(D_{i+4}\) returns to zero,
the successive displayed baselines are

\[
 1,\quad 3,\quad 2,\quad 1,\quad 0.
\tag{3.5}
\]

The factor

\[
 1_{z_i}D_i^\uparrow\,
 0_{z_{i+1}}D_{i+1}\,
 0_{z_{i+2}}D_{i+2}\,
 0_{z_{i+3}}
\tag{3.6}
\]

is primitive and has height \(H+2\). It is the unique primitive factor
of \(E\) of that height: every outside primitive factor lies in
\(D_{i+4}\) or \(D_{i+3}\) and has height at most \(H\).

The initial up-step of (3.6) is \(z_i\). The first attainment of height
\(H+2\) is the flipped step \(u\). Before \(u\), the old path has height
at most \(H\); at \(u\), flipping the down-step after the rightmost
height-\(H\) visit raises the new relative height to \(H+1\), hence the
height inside the primitive factor to \(H+2\). Any later tie occurs
strictly later.

Thus, for the rooted Dyck word \(E\),

\[
 p_-(E)=z_i,\qquad p_+(E)=u.
\tag{3.7}
\]

Equation (2.9) gives

\[
 I_2(A)=A\setminus\{z_i,u\}=S.
\tag{3.8}
\]

For \(m=2\), \(S=\varnothing\). Take a middle owner whose rooted word is

\[
 0\,1100.
\tag{3.9}
\]

Its sole primitive factor has \(p_-\) equal to its first up-step and
\(p_+\) equal to its second. Equation (2.9) again gives
\(I_2(A)=\varnothing\).

This proves

\[
 \mu_2^-(S)\ge1
\tag{3.10}
\]

for every \(m\ge2\) and every target \(S\).

## 4. Exact targetwise chronology and the load cap

The direct witness above proves support. The full deficit-five
parenthesis fiber gives an exact multiplicity formula and the uniform cap.

Let

\[
 Z=[n]\setminus S.
\tag{4.1}
\]

The word of \(S\) has five forward-unmatched and five reverse-unmatched
zeros. Denote these sets by

\[
 U_+(S),\qquad U_-(S).
\tag{4.2}
\]

For \(u\in Z\), put

\[
 C_u=S\cup\{u\},\qquad
 P_u=U_+(C_u),\qquad
 Q_u=U_-(C_u).
\tag{4.3}
\]

Both \(P_u\) and \(Q_u\) have size three.

### Lemma 4.1 (one-flip survivor triples)

In the physical cyclic order:

* \(P_u\) consists of the three members of \(U_+(S)\) immediately
  preceding \(u\);
* \(Q_u\) consists of the three members of \(U_-(S)\) immediately
  following \(u\).

Here predecessor and successor are strict. The statement also applies
when \(u\) itself is an old unmatched zero.

#### Proof

For the forward statement, cut at the five forward-unmatched zeros and
use decomposition (3.2). If \(u=z_i\), flipping it to one consumes
\(z_i\) and matches \(z_{i+1}\), leaving the other three zeros
\(z_{i+2},z_{i+3},z_{i+4}\). These are precisely the three strict
predecessors of \(u\) in the cyclic survivor order. If \(u\) lies inside
a Dyck block \(D_i\), leave its old matched pair uncontracted and contract
all other pairs. The two resulting excess openings consume
\(z_{i+1},z_{i+2}\), leaving \(z_i,z_{i+4},z_{i+3}\), again the three
strict predecessors. Reverse the physical circle for the reverse
statement. \(\square\)

For a three-set \(P\) of marked points, write
\(\operatorname{pv}_P(x)\) for the strict predecessor of the physical
point \(x\) in \(P\). Define \(\operatorname{nx}_Q(x)\) dually.

### Lemma 4.2 (exact internal centered-edge rule)

For distinct \(a,u,c\in Z\),

\[
 \boxed{
 f^2(S\cup\{a,u\})=S\cup\{u,c\}}
\tag{4.4}
\]

if and only if

\[
 \boxed{
 c=\operatorname{pv}_{P_u}(a),
 \qquad
 a=\operatorname{nx}_{Q_u}(c).}
\tag{4.5}
\]

#### Proof

We use the one-flip rule once more. In any deficit-three word \(C\), cut
at its three forward-unmatched zeros. If the flipped zero \(a\) is one of
them, it consumes itself and the next survivor; if it lies inside a Dyck
block, contract every old matched pair except the pair containing \(a\).
In both cases the unique forward survivor of \(C\cup\{a\}\) is the strict
predecessor of \(a\) in \(U_+(C)\). Reversing the circle gives the strict
successor rule for reverse matching.

Applied to the deficit-three core \(C_u\), this gives

\[
 r_+(C_u\cup\{a\})=\operatorname{pv}_{P_u}(a),
\qquad
 r_-(C_u\cup\{c\})=\operatorname{nx}_{Q_u}(c).
\tag{4.6}
\]

Put \(X=C_u^c\setminus\{a,c\}\). By (1.2),

\[
 f(C_u\cup\{a\})=X=f^{-1}(C_u\cup\{c\})
\]

holds exactly when (4.5) holds. This is equivalent to (4.4).
\(\square\)

Form the directed graph \(H_S\) on the pair states \(\binom Z2\) by
placing the arc

\[
 \{a,u\}\longrightarrow\{u,c\}
\tag{4.7}
\]

whenever (4.5) holds. It is exactly the subgraph of the deterministic
permutation \(g=f^2\) induced by the owner fiber

\[
 \{S\cup P:P\in\textstyle\binom Z2\}.
\tag{4.8}
\]

For ordered distinct \(b,c\in Z\), define

\[
\begin{aligned}
 \operatorname {In}_S(b,c)
 &=\mathbf1_{\{\exists a:(a,b,c)\text{ satisfies }(4.5)\}},\\
 \operatorname {Out}_S(b,c)
 &=\mathbf1_{\{\exists d:(b,c,d)\text{ satisfies }(4.5)\}}.
\end{aligned}
\tag{4.9}
\]

Because \(g\) is a permutation, each possible predecessor and successor is
unique.

### Theorem 4.3 (exact deficit-five multiplicity formula)

\[
 \boxed{
 \mu_2^-(S)
 =\sum_{\substack{b,c\in Z\\b\ne c}}
   \operatorname {In}_S(b,c)\operatorname {Out}_S(b,c).}
\tag{4.10}
\]

Equivalently, \(S\) is missing if and only if \(H_S\) has no directed
two-edge path.

#### Proof

Every directed two-edge path in \(H_S\) has the literal owner form

\[
 S\cup\{a,b\}
 \longrightarrow
 S\cup\{b,c\}
 \longrightarrow
 S\cup\{c,d\}.
\tag{4.11}
\]

Indeed the incoming edge retains \(b\). A priori the outgoing edge from
\(S\cup\{b,c\}\) could also retain \(b\), but then all three owners would
contain the \((m-1)\)-set \(S\cup\{b\}\), contradicting the pointwise
rank-\((m-2)\) identity (2.9). Hence the outgoing edge retains \(c\), and
the ordered form (4.11) is forced.

All three owners contain \(S\). By (2.9), every centered two-edge window
has intersection rank exactly \(m-2\), so the intersection in (4.11) is
exactly \(S\). Conversely, a centered window with target \(S\) stays in
the fiber (4.8) and gives exactly one term of (4.10). \(\square\)

### Corollary 4.4 (uniform load cap)

\[
 \mu_2^-(S)\le\binom52=10.
\tag{4.12}
\]

#### Proof

In (4.11), the two elements of the initial owner outside \(S\) are
\(a,b\), and they are deleted successively. From Lemma 4.2,

\[
 a=\operatorname{nx}_{Q_b}(c)\in Q_b\subseteq U_-(S),
\]

and, on the second edge,

\[
 b=\operatorname{nx}_{Q_c}(d)\in Q_c\subseteq U_-(S).
\]

They are distinct. Thus the initial extra pair \(\{a,b\}\) is a
two-subset of the five-set \(U_-(S)\). That unordered pair determines the
initial owner \(S\cup\{a,b\}\), and the deterministic map \(g=f^2\)
determines the entire oriented window. There are at most
\(\binom52=10\) possibilities. \(\square\)

Together with Section 3, this proves (0.8)--(0.9).

## 5. The exact \(q=1\) collision/run formula

Let \(C\) be one directed \(g\)-component. For
\(S\in\binom{[n]}{m-2}\), read the cyclic binary word

\[
 \xi_A(S)=\mathbf1_{\{S\subset R(A)\}}
\qquad(A\in C).
\tag{5.1}
\]

A rooted centered turn at \(A\) has lower target

\[
 R(g^{-1}A)\cap R(A).
\tag{5.2}
\]

By (2.9), this intersection always has rank \(m-2\). It equals \(S\)
exactly when the two corresponding entries of (5.1) are both one.
Therefore the component contribution is the number of adjacent \(11\)
pairs.

If the cyclic word is not all one, a one-run of length \(\ell\) contributes
\(\ell-1\) adjacent \(11\) pairs. Summing over its runs gives

\[
 \mu_{2,C}^-(S)=d_C(S)-r_C(S).
\tag{5.3}
\]

If the word is all one, it contributes its full component length; the
convention \(r_C(S)=0\) makes (5.3) valid there as well. Summing over
components proves (0.13).

Every occurrence \(R(A)\supset S\) is counted once in
\(d_1(S)\), so grouping by its rank-\((m-1)\) color gives (0.14).
The first-shadow bounds then give (0.15), and (0.8) gives (0.16).

The missing criterion is especially transparent:

\[
 \boxed{
 S\text{ is missing at }q=2
 \Longleftrightarrow r_S=d_1(S),}
\tag{5.4}
\]

that is, every eligible \(q=1\) occurrence is isolated in its centered
component. The parenthesis construction of Section 3 proves that this
never happens in PBBS.

## 6. Aggregate excess and the upper shadow

There are \(W\) rooted centered turns and

\[
 N_2=\binom{2m+1}{m-2}
\tag{6.1}
\]

lower targets. Since every target occurs,

\[
 \sum_S(\mu_2^-(S)-1)=W-N_2.
\tag{6.2}
\]

The exact ratio is

\[
 \frac{N_2}{W}
 =\frac{m(m-1)}{(m+2)(m+3)}.
\tag{6.3}
\]

Thus

\[
 \boxed{
 W-N_2
 =\frac{6(m+1)}{(m+2)(m+3)}W
 <12B.}
\tag{6.4}
\]

In particular,

\[
 |\{S:\mu_2^-(S)>1\}|
 \le W-N_2<12B.
\tag{6.5}
\]

The pointwise cap also gives the baseline-one collision estimate

\[
 \sum_S\binom{\mu_2^-(S)-1}{2}
 \le4(W-N_2)<48B.
\tag{6.6}
\]

For \(m\ge8\), when the balanced floor is one, this is exactly the
floor-corrected collision estimate. The inequality itself remains true
for \(2\le m<8\).

For the upper shadow, every element of
\(f^{-1}A\cap fA\) is outside all three sets
\(f^{-2}A,A,f^2A\): use disjointness on the two adjacent odd-graph edges.
Both

\[
 \left(f^{-2}A\cup A\cup f^2A\right)^c
\quad\text{and}\quad
 f^{-1}A\cap fA
\]

have rank \(m-1\), the first by the upper half of depth-two geodesicity
and the second because it is a centered lower color. Hence

\[
 \boxed{
 \left(f^{-2}A\cup A\cup f^2A\right)^c
 =f^{-1}A\cap fA.}
\tag{6.7}
\]

As \(A\) ranges over all middle owners, the right side is exactly the
PBBS centered \(q=1\) lower ledger. Complementation therefore gives

\[
 1\le\mu_2^+(U)\le3,
\qquad M_2^+=0,
\tag{6.8}
\]

which proves (0.18).

## 7. Literal five-rank consequence

The shadow theorem has a literal contiguous-OR consequence, but one must
use the correct parity/complement interface.

Every PBBS orbit has length \(\ell n\); this uses the audited PBBS
site-homomesy theorem. Its step-two centered projection has
\(\gcd(2,\ell)\) components. Since the sum of all orbit levels is

\[
 \sum\ell=\frac Wn=B,
\]

the total number \(K\) of centered components satisfies

\[
 K\le B.
\tag{7.1}
\]

Let \(B_j\) be a directed centered rank-\(m\) row and put

\[
 X_j=[n]\setminus B_j.
\tag{7.2}
\]

Consecutive same-label gaps are odd. Gap one would make
\(f^2A=A\) in (1.4), which is excluded by the nontrivial exchange
(2.2); hence every such gap is at least three. The no-gap-three theorem
then makes it at least five.

More exactly, write a consecutive gap as \(g=2s+1\), lift the cyclic
\(f\)-indices over this return interval to integers, and take the
step-two subsequence on which the first occurrence inserts the coordinate
into the \(X\)-row and the second occurrence deletes it. Recurrence (1.4),
after complementation, shows that the coordinate is present in exactly

\[
 s+1=\frac{g+1}{2}
\]

consecutive \(X\)-states. Thus every nonconstant positive coordinate run
in the \(X\)-row has length at least three.
Together with depth-two geodesicity, this is the \(G_2+P_2\) interface.
Define

\[
 D_j=X_j\cap X_{j+1}\cap X_{j+2}.
\tag{7.3}
\]

Then the exact erosion/dilation identities are

\[
\begin{aligned}
 D_i&=X_i\cap X_{i+1}\cap X_{i+2},\\
 D_i\cup D_{i+1}&=X_{i+1}\cap X_{i+2},\\
 D_i\cup D_{i+1}\cup D_{i+2}&=X_{i+2},\\
 D_i\cup\cdots\cup D_{i+3}&=X_{i+2}\cup X_{i+3},\\
 D_i\cup\cdots\cup D_{i+4}
 &=X_{i+2}\cup X_{i+3}\cup X_{i+4}.
\end{aligned}
\tag{7.4}
\]

For completeness, these identities are coordinatewise. If
\(x_i=\mathbf1_{\{x\in X_i\}}\), then

\[
 \mathbf1_{\{x\in D_i\}}=x_ix_{i+1}x_{i+2}.
\]

Every cyclic one-run of \(x_i\) is either constant or has length at least
three. Hence two consecutive ones \(x_{i+1}=x_{i+2}=1\) extend on at
least one side to a triple, proving the second line of (7.4). Any one at
\(i+2\) lies in a triple whose start is one of \(i,i+1,i+2\), proving
the third line. The same interval argument with the central position set
\(\{i+2,i+3\}\), respectively
\(\{i+2,i+3,i+4\}\), proves the fourth and fifth lines. Constant runs are
immediate.

The five right-hand sides range over every target in ranks

\[
 m-1,m,m+1,m+2,m+3,
\tag{7.5}
\]

using the two \(q=2\) support theorems, the centered \(q=1\) theorem,
middle ownership, and complementation.

For each component, emit its cyclic \(D\)-word once and copy its first four
letters. All certified windows then remain inside that unrolled component.
The resulting literal word has length at most

\[
 \boxed{W+4K\le W+4\operatorname {Cat}_m.}
\tag{7.6}
\]

Thus the centered PBBS core extends through \(q=2\) not only as an
abstract shadow ledger, but as a literal coefficient-one five-rank band.

There is a necessary caveat. The original rank-\(m\) centered rows need
not themselves satisfy the positive-dwell condition \(P_2\): a gap-five
omitted-label return can create a positive run of two states. The
complementary \(X\)-rows in (7.2) have the required \(P_2\) interface.
Nothing here asserts growing-window safety.

## 8. Exact implication boundary

The result is stronger than a \(q=1\) marginal theorem and weaker than a
growing-depth PBBS compiler.

1. **What is proved.** For every \(m\ge2\), every centered turn has the
   correct lower and upper depth-two ranks; every lower and upper
   \(q=2\) target occurs; lower loads lie in \([1,10]\), upper loads in
   \([1,3]\); and all but \(O(\operatorname {Cat}_m)\) lower targets have
   load one.

2. **Why \(q=1\) rainbowness alone is insufficient.** For fixed \(S\), the
   \(q=1\) theorem only forces internal arcs in the pair-state fiber
   \(H_S\). Abstractly, on a cyclic label set one may take

   \[
    \{u,u+1\}\longrightarrow\{u,u+2\}
   \]

   for every \(u\). The tails and heads form disjoint families, so all
   arcs are isolated and there is no two-edge path. The positive theorem
   uses the joint forward/reverse parenthesis coupling, encoded either by
   the distinguished-block formula (2.9) or by the exact edge rule (4.5).

3. **First remaining chronology issue.** Gap-five returns can obstruct
   pointwise depth-three geodesicity and the original-row \(P_2\)
   interface. The separate audited gap-five classification gives exactly
   \(n(m-1)=o(W)\) such rooted starts, but no Gaussian-window
   return-packing theorem follows from the present result.

The precise decision is therefore:

\[
 \boxed{
 \text{the canonical centered PBBS \(q=1\) core extends completely
 through \(q=2\), with no linear defect.}}
\]

The next unresolved gate begins beyond depth two.

## 9. Independent audit

Three independent proof reconstructions checked:

* the owner-start normalization and omitted-label recurrence;
* the two-sided distinguished-block identities (2.2)--(2.3);
* the all-target witness (3.2)--(3.8);
* the deficit-five edge rule, multiplicity formula, and cap ten;
* the run identity (0.13);
* the Catalan constants and the upper-shadow duality.

Two corrections from the audits are incorporated explicitly:

1. starts are counted once by their middle owner, not by an unrestricted
   parity pair \((\varepsilon,j)\);
2. an arbitrary \(A\)-to-\(C\) mark boundary is not a valid support proof.
   Section 3 uses the maximal-height parenthesis-block witness, while the
   exact fiber statement in Section 4 uses only the audited one-flip rule.
