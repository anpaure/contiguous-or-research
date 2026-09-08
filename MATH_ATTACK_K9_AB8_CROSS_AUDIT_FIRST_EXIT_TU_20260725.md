# Lane K9: AB8 cross-audit, a linear Dyck cage, and the first-exit TU obstruction

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver, computer
experiment, or long local job is used.

## 0. Verdict

Put

\[
 n=2m+1,\qquad W=\binom nm,\qquad B=\frac Wn=\operatorname{Cat}_m,
 \qquad H=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed. At depth \(q\), put

\[
 N_q=\binom n{m-q},\qquad
 c_q=\left\lfloor\frac W{N_q}\right\rfloor,\qquad
 b_q=\binom{c_q+1}{2},
\]

and let \(\Phi_q\) and

\[
 \mathfrak F_A=\sum_{q\le H}\frac{\Phi_q}{b_q}
\]

have the exact adjacent-integer normalization used in AB8.

The principal AB8 theorem is mathematically sound. Its menu cardinality,
private-pile floor, token exponent, and
\(\Omega_A(\sqrt m)\) cut conclusion all pass audit. Four qualifications are
essential.

1. The forest edges are coordinate-subgroup fresh only in a forest-only
   ordering; arbitrary interposed menu chords can destroy freshness of a
   prescribed later tree edge.
2. Only \(\tau_s\) is a native MSW packet colour. The clique labels in the
   always-in and always-out atoms are protected full cells obtained by
   invariant-fibre minimization, not native packet components.
3. The proof of the raw full-cell transport statement needs one short
   wreath-specific fixed-window lemma. With that lemma inserted, the
   component-cut quantifiers are correct.
4. The escape theorem is a factorial-collision obstruction. It does not make
   the displayed depth necessary for \(J_A=o(W)\), MWB, or constant one.

The audit yields four stronger theorems.

### A. The protected menu admits a linear, not merely Gaussian, forest

Let

\[
 2\le s\le m-H-4,\qquad
 d=m-s-H-2,\qquad L=\operatorname{Cat}_d,\qquad
 T=\operatorname{Cat}_H.
\]

There is a protected menu \(\mathcal M^\dagger_s\), a literal exact factor
\(\widehat G_{m,s}\), and a coordinate forest inside that menu with exactly

\[
 \boxed{m+s+H+1}                                      \tag{0.1}
\]

edges such that every adaptive menu-only endpoint has objective at least
\(\mathfrak F_A(\widehat G_{m,s})\). For
\(s=\lfloor H/2\rfloor\), the forest size is

\[
 m+\frac32H+O(1),
\]

whereas AB8's original displayed forest has only \(3H+O(1)\) edges.
The same private Catalan floor survives:

\[
 \boxed{
 \mathfrak F_A(\widehat G_{m,s})
 >
 W\left(
 \frac{4^{H-s}}{2048K_A\,nH^4}-1
 \right).
 }                                                     \tag{0.2}
\]

### B. Renewal depth is controlled by graphic rank, not merely cut count

For a realized suffix, let \(\Gamma\) be the simple graph of its distinct
transposition labels and put

\[
 r(\Gamma)=\sum_{Q\in\operatorname{cc}(\Gamma)}(|Q|-1).
 \tag{0.3}
\]

Starting from any state reached by an arbitrary
\(\mathcal M^\dagger_s\)-history, every subsequent endpoint satisfies

\[
 \boxed{
 \frac{\mathfrak F_A(F_{\rm end})}{W}
 >
 \frac{2^{\,2(H-s)-r(\Gamma)-10}}
 {K_A\,nH^4}
 -1-\frac1{2n}.
 }                                                     \tag{0.4}
\]

Consequently, if \(C_0\ge0\) and
\(\mathfrak F_A(F_{\rm end})\le C_0W\), then, with

\[
 R_0=
 2(H-s)-10-
 \log_2\!\left[
 K_A nH^4\left(C_0+1+\frac1{2n}\right)
 \right],
\]

one has the sharp integral conclusion

\[
 \boxed{
 r(\Gamma)\ge\max\{0,\lfloor R_0\rfloor+1\}.
 }                                                     \tag{0.5}
\]

At \(s=\lfloor H/2\rfloor\), this is

\[
 r(\Gamma)\ge H-3\log_2m-O_{A,C_0}(1)
 =\Omega_A(\sqrt m).
 \tag{0.6}
\]

Thus the suffix beginning with the first outside-menu cut contains
\(\Omega_A(\sqrt m)\) rank-increasing first-occurrence labels, i.e. genuinely
coordinate-fresh bridges relative to that suffix. They need not all be
outside-menu labels.

### C. All one-outside-colour palettes except one block type remain caged

The coordinate components of the sharpened menu have sizes

\[
 a=s+2,\qquad z=s+2H+3,\qquad
 2,2,\ldots,2.
 \tag{0.7}
\]

Every first outside transposition joins two distinct blocks. If it does not
join the large always-in block to the large always-out block, then for
\(s=\lfloor H/2\rfloor\) the fixed palette consisting of the sharpened menu
and that one outside colour still satisfies

\[
 \frac{\mathfrak F_A(F)}W\longrightarrow\infty
 \tag{0.8}
\]

for every adaptive history of arbitrary length. The unique one-outside-colour
class not excluded by this invariant-orbit argument is an
always-in--to--always-out bridge. A later second outside colour remains open.

### D. Even the surviving bridge fails the exact profile gate before TU

Let \(\sigma\) be an always-in--to--always-out bridge, and let
\(\mathcal P_s\) be the \(2L\) private targets. Immediately before the first
\(\sigma\)-cut, after any protected-menu history,

\[
 \mathcal P_s\cap\sigma\mathcal P_s=\varnothing.
\]

The relevant \(\sigma\)-orbits are

\[
 p_X=\{X,\sigma X\},\qquad X\in\mathcal P_s.
\]

Writing \(\ell_X\) for their invariant pair totals, one has

\[
 \boxed{
 \sum_{X\in\mathcal P_s}
 [\ell_X-2(c_H+1)]_+
 \ge L[T-4(c_H+1)].
 }                                                     \tag{0.9}
\]

Hence every component signing in the first fresh \(\sigma\)-overlay obeys

\[
 \boxed{
 O_H\ge L[T-4(c_H+1)]_+,
 \qquad
 \Phi_H\ge\Psi(LT,4L)-P_H^{\min},
 }                                                     \tag{0.10}
\]

where \(\Psi(M,Q)\) is the exact minimum of
\(\sum_{i=1}^Q\binom{x_i}{2}\) over integral nonnegative
\((x_i)\) of total \(M\).

Thus the floor-compatible-pair-total hypothesis of the exact K8 TU theorem
fails quantitatively before unit leakage, total unimodularity, or signed-cycle
holonomy is considered. TU cannot give exact profile-compatible balance or
remove this factorial pile on the first cut. Because the displayed profile
excess is \(o(W)\), this does not exclude a first-cut TU theorem aimed only at
\(J_A=o(W)\) after charging these rows as residue.

If the history uses no second outside colour, the sole possible first colour
must be always-in--to--always-out and must itself occur more than

\[
 \boxed{H/16}                                         \tag{0.11}
\]

times before an \(O(W)\)-factorial-energy endpoint is possible.

These statements are fully integral and literal. Their linear-overflow mass
is \(o(W)\), so none proves or obstructs constant one.

## 1. Cross-audit of the original AB8 cage

### 1.1 Exact menu size and graphic rank

AB8 has disjoint coordinate atoms

\[
 |\mathcal I_s|=s+1,\qquad
 |\mathcal Z_s|=s+2H+2,\qquad
 E_s=\{\beta_s,\gamma_s\},
\]

and menu

\[
 \mathcal M_s=
 \binom{\mathcal I_s}{2}\cup
 \binom{\mathcal Z_s}{2}\cup
 \{(\beta_s\ \gamma_s)\}.
\]

Therefore

\[
 \boxed{
 |\mathcal M_s|
 =
 \binom{s+1}{2}+\binom{s+2H+2}{2}+1
 }                                                     \tag{1.1}
\]

and its graphic-matroid rank is exactly

\[
 \boxed{2s+2H+2.}                                     \tag{1.2}
\]

Indeed, its nontrivial coordinate components are the two cliques and the
single \(E_s\)-edge. A spanning tree in each clique plus that edge attains
(1.2), and no forest can contain more.

For \(s=\lfloor H/2\rfloor\),

\[
 |\mathcal M_s|=\frac{13}{4}H^2+O(H)=\Theta_A(m),
 \qquad
 \operatorname{rank}(\mathcal M_s)=3H+O(1).
 \tag{1.3}
\]

The menu is quadratic in \(H\), not in \(m\). Its displayed forest is fresh
in the following exact sense: if its edges alone are placed in any order,
each new edge joins two components of the graph of earlier forest edges.
Interposing arbitrary menu chords can make a later prescribed tree edge
nonfresh. This is coordinate-subgroup freshness; it implies no
ownership-overlay fragmentation.

Only \((\beta_s\ \gamma_s)=\tau_s\) is supplied as a native contextual packet
colour. The clique labels are protected because they fix the private targets
and preserve the minimizing fibre.

### 1.2 The missing full-cell transport lemma

The component-cut claim in AB8 is true, but its proof should insert the
following wreath-specific fact.

### Lemma 1.1 (a row and its transposition lie in one overlay component)

Let \(C\) be an odd wreath row and let \(\sigma=(x\ y)\). Among the \(n\)
cyclic middle windows of \(C\), each coordinate occurs in exactly \(m\).
Their total \(x,y\)-incidence is therefore

\[
 2m=n-1.
\]

If every middle window contained exactly one of \(x,y\), this incidence would
be \(n\), a contradiction. Hence some middle window contains both or neither
and is fixed by \(\sigma\). It is owned by both \(C\) and \(\sigma C\), so
those two rows lie in one component of the \(F\)-versus-\(\sigma F\) overlay.

Coordinate relabelling by \(\sigma\) swaps the two shores of the overlay.
Since every row is connected to its own translate, every connected component
is \(\sigma\)-invariant and its new shore is exactly the translate of its old
shore. Thus switching a complete component changes its load by

\[
 (\sigma-I)a_K,
\]

and the rowwise map is \(C\mapsto C\) or \(C\mapsto\sigma C\), as AB8 uses.

For \(m\ge2\), a coordinate transposition does not stabilize an unoriented
\((2m+1)\)-cycle: the stabilizer is dihedral, and an odd-cycle reflection has
cycle type \(1\,2^m\), not \(1^{n-2}2\). Thus the two shores are disjoint and
every child is squarefree. This completes the raw full-cell justification.

### 1.3 Floors, constants, and scope

The private-pair total theorem gives \(L=\operatorname{Cat}_{m-s-H-2}\)
disjoint pairs, each with total at least \(T=\operatorname{Cat}_H\). The exact
pair collision floor is

\[
 \psi(T)=\left\lfloor\frac{(T-1)^2}{4}\right\rfloor.
\]

The constant in AB8 is correct:

\[
 2048=8\cdot16\cdot16.
\]

The factors are, respectively, the safe bound
\(\psi(T)\ge T^2/8\), the estimate
\(T^2\ge16^H/(16H^4)\), and the two extra Catalan-ratio steps.

The unrestricted token argument starts on two targets and after \(D\) cuts
has at most \(2^{D+1}\) target values. This gives

\[
 \frac{T^2}{2^{D+2}}-\frac T2
\]

per private pair and hence the exponent
\(2(H-s)-D-10\). The negative terms in AB8 are exactly

\[
 -1-\frac1{2n}.
\]

At \(s=\lfloor H/2\rfloor\),

\[
 \log_2(K_AnH^4)=3\log_2m+O_A(1),
\]

so the displayed \(\Omega_A(\sqrt m)\) cut conclusion is correct.
It counts all actual cuts, including repeats and empty cuts. It does not by
itself count distinct labels, useful renewals, or outside-menu labels.

The objective \(\mathfrak F_A\) is a factorial collision criterion. The
protected mass satisfies \(LT\le B=W/n\), and for
\(s=\lfloor H/2\rfloor\) is much smaller still. Therefore a divergent
factorial pile can coexist with \(o(W)\) linear overload. Every implication
toward MWB or constant one remains conditional on adopting a factorial or
max-load control theorem.

## 2. Saturating the Dyck symmetries gives a linear protected forest

Assume \(d=m-s-H-2\ge2\). Write the shifted Dyck coordinates as

\[
 r_j=2s+4+2H+j,\qquad 1\le j\le2d.
 \tag{2.1}
\]

The \(2L\) private targets form

\[
 \mathcal P_s=
 \left\{
 \mathcal I_s\cup
 \{r_j:j\in\operatorname{Down}(V)\}\cup\{\epsilon\}:
 V\in\mathcal D_d,\ 
 \epsilon\in\{\beta_s,\gamma_s\}
 \right\}.
 \tag{2.2}
\]

They are distinct. Let

\[
 M_*=\sum_{X\in\mathcal P_s}\mu_H^{F_m^{\rm MSW}}(X).
 \tag{2.3}
\]

The shifted private-pile theorem gives

\[
 M_*\ge LT.                                            \tag{2.4}
\]

### Lemma 2.1 (endpoint atoms and even-adjacent Dyck involutions)

Every Dyck word begins with an up-step and ends with a down-step. Hence \(r_1\)
is absent and \(r_{2d}\) is present in every target in \(\mathcal P_s\). Put

\[
 \mathcal I_s^+=\mathcal I_s\cup\{r_{2d}\},\qquad
 \mathcal Z_s^+=\mathcal Z_s\cup\{r_1\},
 \tag{2.5}
\]

so

\[
 a:=|\mathcal I_s^+|=s+2,\qquad
 z:=|\mathcal Z_s^+|=s+2H+3.
 \tag{2.6}
\]

For \(1\le t\le d-1\), put

\[
 \eta_t=(r_{2t}\ \ r_{2t+1}).                         \tag{2.7}
\]

Every \(\eta_t\) permutes the Dyck family. Equal adjacent steps are unchanged.
Changing down--up to up--down only raises the intermediate height. Changing
up--down to down--up lowers the intermediate height by two; immediately
before position \(2t\), the path has taken \(2t-1\) steps, so its positive
height is odd and at least one. The lowered intermediate height is therefore
nonnegative, and all later heights are unchanged. Thus the swapped word is
again Dyck.

In the native contextual notation these are exactly the tail colours

\[
 \eta_t=\tau_{s+H+t+1},
 \qquad
 \tau_{s+H+2},\ldots,\tau_{m-2}.
 \tag{2.7a}
\]

### Theorem 2.2 (linear protected cage)

Define

\[
 \mathcal M_s^\dagger=
 \binom{\mathcal I_s^+}{2}
 \cup\binom{\mathcal Z_s^+}{2}
 \cup\{(\beta_s\ \gamma_s)\}
 \cup\{\eta_t:1\le t\le d-1\}.
 \tag{2.8}
\]

Let \(\mathscr J_{m,s}\) be the set of literal exact factors satisfying

\[
 \sum_{X\in\mathcal P_s}\mu_H^F(X)=M_*,
 \tag{2.9}
\]

and choose

\[
 \widehat G_{m,s}\in
 \operatorname*{argmin}_{F\in\mathscr J_{m,s}}\mathfrak F_A(F).
 \tag{2.10}
\]

Every finite adaptive history from \(\widehat G_{m,s}\), using arbitrary cuts
of all freshly recomputed components with colours in
\(\mathcal M_s^\dagger\), remains in \(\mathscr J_{m,s}\). Consequently its
endpoint has objective at least \(\mathfrak F_A(\widehat G_{m,s})\).

#### Proof

Transpositions internal to \(\mathcal I_s^+\) or \(\mathcal Z_s^+\) fix every
private target. The \(E_s\)-edge interchanges the two \(\epsilon\)-choices.
Lemma 2.1 shows that each \(\eta_t\) permutes the target family. Thus every
menu colour preserves \(\mathcal P_s\) setwise. Lemma 1.1 and target-union
invariance preserve (2.9) after each full component cut. Minimality proves the
claim. \(\square\)

The coordinate components of the menu are

\[
 \mathcal I_s^+,\quad
 \mathcal Z_s^+,\quad
 E_s,\quad
 \{r_2,r_3\},\ldots,\{r_{2d-2},r_{2d-1}\}.
 \tag{2.11}
\]

They partition all \(n\) coordinates. Hence the exact menu size is

\[
 |\mathcal M_s^\dagger|
 =
 \binom{s+2}{2}
 +\binom{s+2H+3}{2}
 +1+(d-1),
 \tag{2.12}
\]

and its graphic rank, equivalently its maximum forest size, is

\[
\begin{aligned}
 &(a-1)+(z-1)+1+(d-1)\\
 &\qquad=2s+2H+d+3
 =\boxed{m+s+H+1}.
\end{aligned}                                         \tag{2.13}
\]

For the exact collision floor, if

\[
 M=qQ+r,\qquad0\le r<Q,
\]

write

\[
 \Psi(M,Q)=Q\binom q2+rq.                              \tag{2.14}
\]

This is the integral minimum of
\(\sum_{i=1}^Q\binom{x_i}{2}\) at total mass \(M\). Since

\[
 \Psi(LT,2L)=L\psi(T),                                \tag{2.15}
\]

every factor in the fibre obeys

\[
 \Phi_H\ge L\psi(T)-P_H^{\min}.                       \tag{2.16}
\]

Indeed, \(M_*\ge LT\) and \(\Psi(M,2L)\) is nondecreasing in \(M\).
Consequently the proof of AB8's floor gives (0.2), with the same constant
\(2048\) and the same two divergent ratios in its two parameter regimes.

## 3. Graphic-rank renewal after the first exit

### Lemma 3.1 (orbit support is exponential only in graph rank)

Let \(\Gamma\) be the simple coordinate graph of all distinct transposition
labels in a realized suffix. The labels generate

\[
 \prod_{Q\in\operatorname{cc}(\Gamma)}
 \operatorname{Sym}(Q).
\]

For a rank target \(S\), its orbit has size

\[
 \prod_Q\binom{|Q|}{|S\cap Q|}
 \le2^{r(\Gamma)}.                                    \tag{3.1}
\]

For \(|Q|\ge2\), the binomial coefficient is at most
\(2^{|Q|-1}\); singleton components contribute one. Multiplication proves
(3.1).

Every occurrence token in a realized component-cut history is acted on by a
word in these labels, because each cut transports its row by either the
identity or that cut's transposition. Therefore a group of tokens initially
supported on \(u\) targets is finally supported on at most

\[
 u\,2^{r(\Gamma)}                                     \tag{3.2}
\]

targets.

### Theorem 3.2 (rank-renewal inequality)

Start from any \(F_-\in\mathscr J_{m,s}\), including the state immediately
before the first cut outside \(\mathcal M_s^\dagger\). Select \(LT\) occurrence
tokens on \(\mathcal P_s\). They form one labelled group initially supported
on \(2L\) targets. After any realized suffix with label graph \(\Gamma\),

\[
 \boxed{
 \mathfrak F_A(F_{\rm end})
 \ge
 \frac1{b_H}
 \left(
 \frac{LT^2}{2^{r(\Gamma)+2}}
 -\frac{LT}{2}
 -P_H^{\min}
 \right).
 }                                                     \tag{3.3}
\]

Consequently (0.4)--(0.6) hold.

#### Proof

By (3.2), the selected tokens end on at most
\(2L\,2^{r(\Gamma)}\) targets. Cauchy--Schwarz gives selected-token collision
at least

\[
 \frac{(LT)^2}{2(2L\,2^{r(\Gamma)})}-\frac{LT}{2}
 =
 \frac{LT^2}{2^{r(\Gamma)+2}}-\frac{LT}{2}.
\]

Unselected occurrences only increase collision. Subtract the exact floor and
divide by \(b_H\), proving (3.3).

The Catalan estimates give

\[
 \frac{LT^2}{2^{r+2}}
 >
 \frac{W\,2^{\,2(H-s)-r-10}}{nH^4}.
\]

Also \(LT\le\operatorname{Cat}_{m-s-2}<B=W/n\),
\(b_H\le K_A\), and \(P_H^{\min}/b_H\le W\). These give (0.4).
Rearrangement yields the strict inequality \(r(\Gamma)>R_0\), hence the
integer conclusion (0.5).
\(\square\)

Chronologically exposing distinct suffix labels, the graph rank increases by
one exactly when the new label joins two previous coordinate components.
Therefore a final rank \(r(\Gamma)\) certifies that many rank-increasing
first-occurrence labels. All menu cuts before \(F_-\) are absent from this
suffix count. Protected labels used after the first exit may contribute, so
the theorem does not certify \(r(\Gamma)\) distinct outside-menu colours.

## 4. Exact classification of the first outside bridge

Let

\[
 G_s^\dagger=\langle\mathcal M_s^\dagger\rangle
 =
 \operatorname{Sym}(\mathcal I_s^+)
 \times\operatorname{Sym}(\mathcal Z_s^+)
 \times\operatorname{Sym}(E_s)
 \times\prod_{t=1}^{d-1}\operatorname{Sym}(\{r_{2t},r_{2t+1}\}).
 \tag{4.1}
\]

The menu contains every transposition internal to each displayed block.
Consequently every \(\sigma\notin\mathcal M_s^\dagger\) joins two distinct
blocks and is genuinely coordinate-fresh after every possible menu history.

For one native block profile, joining blocks \(B_1,B_2\) expands its orbit by

\[
 R(B_1,B_2;t_1,t_2)=
 \frac{\binom{|B_1|+|B_2|}{t_1+t_2}}
 {\binom{|B_1|}{t_1}\binom{|B_2|}{t_2}}.
 \tag{4.2}
\]

Indeed, connected transposition graphs generate the full symmetric group.
The private profiles have occupancy \(a\) on \(\mathcal I_s^+\), zero on
\(\mathcal Z_s^+\), one on \(E_s\), and an element of \(\{0,1,2\}\) on each
remaining two-block.

Let

\[
 \mathcal Q_\sigma=
 \langle G_s^\dagger,\sigma\rangle\mathcal P_s,
 \qquad
 \lambda_\sigma=\frac{|\mathcal Q_\sigma|}{2L}.
 \tag{4.3}
\]

Then

\[
\begin{array}{c|c}
\text{blocks joined by }\sigma&\lambda_\sigma\\ \hline
\mathcal I_s^+,\mathcal Z_s^+&
\binom{a+z}{a}\quad\text{exactly}\\[1mm]
\mathcal I_s^+,E_s&(a+2)/2\\
\mathcal Z_s^+,E_s&(z+2)/2\\
\mathcal I_s^+,\text{a two-block}&
\le\binom{a+2}{2}\\
\mathcal Z_s^+,\text{a two-block}&
\le\binom{z+2}{2}\\
E_s,\text{a two-block}&\le2\\
\text{two distinct two-blocks}&\le6 .
\end{array}                                           \tag{4.4}
\]

The first three values follow by substituting occupancies
\((a,0),(a,1),(0,1)\) in (4.2). For a two-block occupancy
\(t\in\{0,1,2\}\), maximizing (4.2) gives the displayed bounds.

Every history whose labels lie in
\(\mathcal M_s^\dagger\cup\{\sigma\}\) preserves at least \(LT\) load on
\(\mathcal Q_\sigma\). Therefore

\[
\begin{aligned}
 \sum_X\binom{\mu_H(X)}2
 &\ge
 \frac{(LT)^2}{2|\mathcal Q_\sigma|}-\frac{LT}{2}\\
 &\ge
 \frac{LT^2}{4\lambda_\sigma}-\frac{LT}{2}.
\end{aligned}                                         \tag{4.5}
\]

After subtracting the exact floor and normalizing,

\[
 \boxed{
 \frac{\mathfrak F_A(F)}W
 >
 \frac{4^{H-s}}
 {1024K_A\lambda_\sigma nH^4}
 -1-\frac1{2n}.
 }                                                     \tag{4.6}
\]

For \(s=\lfloor H/2\rfloor\), every row of (4.4) except the first has
\(\lambda_\sigma\le\binom{z+2}{2}=O_A(m)\). Equation (4.6) then diverges for
arbitrarily long histories. Thus an always-in--to--always-out bridge is the
only one-outside-colour palette not permanently excluded by this orbit floor.
An unrestricted schedule may use a non-cross first exit and then a second
outside colour; that two-colour continuation is not excluded here.

## 5. The first surviving bridge fails at the profile level

Fix

\[
 \sigma=(i\ z_0),\qquad
 i\in\mathcal I_s^+,\quad z_0\in\mathcal Z_s^+.
\]

Every private target contains \(i\) and omits \(z_0\), so

\[
 \mathcal P_s\cap\sigma\mathcal P_s=\varnothing.
 \tag{5.1}
\]

Immediately before the first \(\sigma\)-cut, let \(F_-\in\mathscr J_{m,s}\).
The \(2L\) moved \(\sigma\)-orbits meeting \(\mathcal P_s\) are

\[
 p_X=\{X,\sigma X\},\qquad X\in\mathcal P_s.
 \tag{5.2}
\]

Let \(\ell_X\) be their pair totals. Then

\[
 \sum_{X\in\mathcal P_s}\ell_X
 =
 \mu_H^{F_-}(\mathcal P_s)
 +\mu_H^{F_-}(\sigma\mathcal P_s)
 \ge M_*\ge LT.
 \tag{5.3}
\]

Since \([x-u]_+\ge x-u\),

\[
\begin{aligned}
 \sum_{X\in\mathcal P_s}
 [\ell_X-2(c_H+1)]_+
 &\ge
 \sum_X\ell_X-4L(c_H+1)\\
 &\ge L[T-4(c_H+1)].
\end{aligned}                                         \tag{5.4}
\]

Every whole-component signing in the fresh \(\sigma\)-overlay preserves each
\(\ell_X\). A quota pair has total at most \(2(c_H+1)\), so its positive
quota excess is at least the summand in (5.4). This proves the overload bound
in (0.10).

The invariant union

\[
 \Omega_\sigma=\mathcal P_s\cup\sigma\mathcal P_s
\]

has \(4L\) targets and mass at least \(LT\). Integral convexity gives

\[
 \Phi_H\ge\Psi(LT,4L)-P_H^{\min},                     \tag{5.5}
\]

for every first-cut component signing. Equivalently,

\[
 \frac{\mathfrak F_A(F_+)}W
 >
 \frac{4^{H-s}}{2048K_A nH^4}
 -1-\frac1{2n}.                                       \tag{5.6}
\]

For the K8 leakage matrix, write

\[
 z_{XK}=a_K(X)-a_K(\sigma X),\qquad
 D_X(\varepsilon)=\sum_K\varepsilon_Kz_{XK}.
\]

The signed pair loads are

\[
 \frac{\ell_X+D_X(\varepsilon)}2,\qquad
 \frac{\ell_X-D_X(\varepsilon)}2.
\]

The exact TU theorem can optimize the discrepancies \(D_X\) only after the
invariant totals \(\ell_X\) are floor-compatible. Equation (5.4) shows a total
profile violation of at least \(L[T-4(c_H+1)]\). Therefore even a unit,
totally unimodular leakage matrix cannot make these rows exactly
floor/ceiling-balanced or remove their factorial pile in this first bridge.
Conversely, coordinate freshness gives no reason for \(|z_{XK}|\le1\), many
component columns, or TU support; the fresh ownership overlay could be
connected.

Since \(LT<B=W/n\), the profile violation in (5.4) is \(o(W)\). A generalized
near-TU theorem could delete or charge these \(2L\) rows and still conceivably
prove \(J_A=o(W)\) on the first cut. The theorem here rules out exact profile
balance and factorial descent, not such a linear-overload capture.

## 6. One outside colour must be reused linearly many times

Continue with one fixed always-in--to--always-out colour
\(\sigma=(i\ z_0)\), allow arbitrary protected-menu cuts, and suppose no
second outside colour is used. Let \(k\) be the number of occurrences of
\(\sigma\).

Protected permutations do not alter the number \(j\) of holes in the
always-in block or the equal number of extras in the always-out block. One
\(\sigma\)-occurrence changes \(j\) by at most one. Starting at \(j=0\), after
\(k\) occurrences every selected token therefore lies in one of at most

\[
 Q_k=
 \sum_{j=0}^{\min(k,a,z)}
 \binom aj\binom zj                                  \tag{6.1}
\]

profiles relative to its protected starting orbit. The selected \(LT\) tokens
are supported on at most \(2LQ_k\) targets. Hence

\[
 \boxed{
 \frac{\mathfrak F_A(F)}W
 >
 \frac{4^{H-s}}
 {1024K_AQ_k nH^4}
 -1-\frac1{2n}.
 }                                                     \tag{6.2}
\]

Take \(s=\lfloor H/2\rfloor\). For all sufficiently large \(H\),

\[
 a\le H,\qquad z\le3H.
\]

If \(1\le j\le H/16\), then

\[
 \binom aj\binom zj
 \le
 \left(\frac{e^2az}{j^2}\right)^j.                   \tag{6.3}
\]

The logarithm of the right side is increasing for
\(j\le H/16\), because its derivative is
\(\log(az/j^2)>0\). At \(j=H/16\),

\[
 \frac{e^2az}{j^2}
 \le 768e^2<6912<2^{13}.
\]

Thus, if \(k\le H/16\),

\[
 Q_k\le(H+1)2^{13H/16}.                               \tag{6.4}
\]

On the other hand, an endpoint with
\(\mathfrak F_A(F)\le C_0W\), \(C_0\ge0\), would require from (6.2)

\[
 Q_k>
 \frac{4^{H-s}}
 {1024K_AnH^4(C_0+1+1/(2n))}
 =2^{H-O_{A,C_0}(\log m)}.                            \tag{6.5}
\]

The gap between \(H\) and \(13H/16\) dominates the logarithmic factors.
Therefore, for all sufficiently large \(m\),

\[
 \boxed{k>H/16.}                                      \tag{6.6}
\]

If the sole outside colour is not always-in--to--always-out, Section 4 gives
the stronger permanent obstruction (0.8). Thus one outside cut followed only
by protected renewal cannot work. A one-colour escape must use the unique
cross-atom type and reuse it \(\Omega(H)\) times.

## 7. Precise proved/conditional boundary

The following statements are proved.

* AB8's original menu, floor, and cut-depth constants are correct after
  inserting Lemma 1.1.
* The original \(3H+O(1)\) protected forest enlarges to a
  \(m+s+H+1\)-edge protected forest by using exact Dyck automorphisms.
* The escape exponent is controlled by suffix graphic rank. Hence an
  \(O(W)\)-factorial endpoint needs \(\Omega_A(\sqrt m)\) rank-increasing
  first-occurrence labels after the first exit.
* If no second outside colour is introduced, every first outside block type
  except always-in--to--always-out remains permanently collision-caged under
  unlimited protected alternation.
* The surviving one-colour bridge has a large relative profile violation and
  cannot make the private rows exactly balanced or remove their factorial pile
  in its first overlay.
* With no second outside colour, that bridge must be used more than \(H/16\)
  times.

The exact remaining bridge theorem is therefore:

> For the factorial route, disperse the protected pair totals using repeated
> cross-atom cuts or further outside colours, and then prove unit or otherwise
> controlled leakage with a joint all-depth matrix made TU after deleting
> \(o(W)\) rows (or prove an equally strong dependent signing theorem).

An unrestricted schedule may take a non-cross first exit and introduce a
second outside colour immediately; that multicolour route remains open. For
the weaker linear-overload target, it also remains possible that the first
cross-atom overlay charges the \(o(W)\) bad profile rows as residue and uses TU
on the rest.

Forest freshness alone gives none of the required ownership statements.
The first fresh ownership overlay may be connected, and even a fragmented
overlay may have nonunit leakage or signed-cycle frustration.

All lower bounds in this report concern the factorial objective
\(\mathfrak F_A\). The overload lower bound in (0.10) is of order \(LT=o(W)\).
Therefore no result here proves a lower bound for MWB, literal contiguous-OR
width, or the constant-one theorem.

## 8. Independent audit

The package was checked independently along three proof lines.

1. **Original AB8 normalization.** The audit rederived the menu cardinality,
   its exact graphic rank, both parity cases at
   \(s=\lfloor H/2\rfloor\), the factor
   \(2048=8\cdot16\cdot16\), the token denominator \(2^{D+2}\), the
   \(-1-1/(2n)\) residue, and
   \(\log_2(nH^4)=3\log_2m+O_A(1)\). It identified Lemma 1.1 as the only
   missing self-contained overlay justification.
2. **Dyck-menu and first-exit geometry.** A separate audit verified the forced
   endpoint steps, every even-adjacent Dyck involution, their identification
   with the native tail colours
   \(\tau_{s+H+2},\ldots,\tau_{m-2}\), the partition of all \(n\)
   coordinates into the displayed blocks, the exact forest rank
   \(m+s+H+1\), the equality
   \(\Psi(LT,2L)=L\psi(T)\), and every entry of table (4.4).
3. **Renewal and TU floors.** The renewal audit replaced cut count by suffix
   graphic rank, checked the strict-to-integral conversion in (0.5), and
   independently recovered the profile excess (5.4), the overload
   normalization with no missing factor \(1/2\), the
   \(\Psi(LT,4L)\) floor, and the denominator \(2048\) in (5.6). It also
   checked the \(Q_k\) chronology and the constant \(H/16\).

The audits imposed the two scope qualifications now stated in Sections 5 and
7: a second outside colour is not covered by the one-colour orbit table, and
the \(o(W)\) profile residue does not obstruct a linear-overload TU theorem.
