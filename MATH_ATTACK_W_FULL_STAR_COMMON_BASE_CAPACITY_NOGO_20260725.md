# Full partner-pair star: an exact common-base owner-capacity obstruction

Date: 2026-07-25

Method: pure mathematics only. No computation, search, solver, or web
search is used.

## 0. Outcome

Put

\[
 n=2m+1,
 \qquad
 W=\binom{n}{m},
 \qquad
 T=\binom{n}{m-1}.
\]

Fix a two-set \(A=\{a,b\}\), let

\[
 R=[n]\setminus A,
 \qquad |R|=2m-1,
\]

and fix one exact local factor \(F_A\) on \(R\).  For every two-set
\(B\subset R\), choose either bijection \(B\to A\), let \(\theta_B\)
exchange the paired coordinates and fix all others, and put

\[
 F_B=\theta_BF_A.
\]

The complete star of these factor conjugacies has a quantitative algebraic
frame, but it cannot be installed over one common first-avoided matching.
For every \(m\ge6\), there is no lower-saturating, middle-simple token
matching which

1. uses the full \(A\)-first phase of \(F_A\) on every rank-\((m-1)\)
   lower root avoiding \(A\); and
2. has one fixed background which remains middle-disjoint from the coherent
   \(B\)-phase endpoint for every \(B\in\binom R2\).

The obstruction occurs before interval side choices, lower-dual flags, or
factorial energy are considered.  Let

\[
 K_m=\binom{2m-1}{m-1}.
\]

The full \(A\)-phase uses all \(K_m\) middle owners avoiding \(A\).  Across
the partner-pair star, its coherent alternatives occupy at least \(K_m\)
distinct middle owners meeting \(A\).  The common background needs
\(T-K_m\) further owners, but after reserving both families at most
\(W-2K_m\) owners remain.  The necessary inequality

\[
 T-K_m\le W-2K_m
\]

is equivalent to \(K_m\le W-T\), whereas

\[
 \boxed{
 \frac{K_m}{W}=\frac{m+1}{2(2m+1)},
 \qquad
 \frac{W-T}{W}=\frac2{m+2}.}
\]

For \(m\ge6\), the first ratio is larger than the second.  Thus the
common-base star lemma proposed in the current partner-pair frame route is
false with its stated full-star quantifier.

A sharp subfamily version is also proved.  If \(\mathcal B\subseteq
\binom R2\) is any partner family, define its exposed-root set by (3.1)
below.  Common-background compatibility forces

\[
 \boxed{|\mathcal S(\mathcal B)|\le W-T=\frac{2W}{m+2}.}
\]

Thus any viable common-base substar may expose only \(O(W/m)\) of the
\(K_m=\Theta(W)\) phase-\(A\) lower roots through owner-changing
alternatives.  This does not rule out upper-flag changes whose alternate
middle owner is unchanged, nor a different base architecture which does
not contain the full \(A\)-first phase.

## 1. The local owner bijection

For an oriented row

\[
 \pi=(x_i)_{i\in\mathbb Z_{2m-1}}
\]

of \(F_A\), use the predecessor convention

\[
 S_i=I_\pi(i,m-1),
 \qquad
 Y_i=I_\pi(i-1,m).
\]

The exact local factor contains every rank-\((m-1)\) interval in \(R\)
exactly once and every rank-\(m\) interval in \(R\) exactly once.  Hence
the predecessor token map is a bijection

\[
 f_A:\binom R{m-1}\longrightarrow\binom Rm,
 \qquad S\longmapsto Y(S).
\tag{1.1}
\]

Moreover \(S\subset Y(S)\), so there is a unique coordinate

\[
 p(S)\in R\setminus S
\]

such that

\[
 \boxed{Y(S)=S\cup\{p(S)\}.}
\tag{1.2}
\]

The number of lower roots and of owners in (1.1) is

\[
 K_m=\binom{2m-1}{m-1}=\binom{2m-1}{m}.
\tag{1.3}
\]

## 2. Every phase-A root creates a distinct star owner meeting A

For \(B\in\binom R2\), the adjacent order exchange between \(A\) and
\(B\) changes precisely the phase-\(A\) lower roots in

\[
 \mathcal D_B=
 \left\{S\in\binom R{m-1}:S\cap B=\varnothing\right\}.
\tag{2.1}
\]

Their coherent alternate owner is

\[
 Y_B(S)=\theta_BY(S).
\tag{2.2}
\]

### Lemma 2.1 (injective owner exposure)

For every \(S\in\binom R{m-1}\), there is a pair
\(B_S\in\binom R2\) such that \(S\in\mathcal D_{B_S}\) and

\[
 \boxed{Y_{B_S}(S)=S\cup\{\alpha_S\}}
 \qquad\text{for some }\alpha_S\in A.
\tag{2.3}
\]

The owners in (2.3) are distinct as \(S\) varies.  Consequently

\[
 \left|
  \bigcup_{B\in\binom R2}
  \{Y_B(S):S\in\mathcal D_B,\ Y_B(S)\cap A\ne\varnothing\}
 \right|
 \ge K_m.
\tag{2.4}
\]

#### Proof

Fix \(S\).  By (1.2), \(Y(S)=S\cup\{p(S)\}\).  Since

\[
 |R\setminus Y(S)|=(2m-1)-m=m-1\ge1,
\]

choose any \(r(S)\in R\setminus Y(S)\), and put

\[
 B_S=\{p(S),r(S)\}.
\]

Both coordinates of \(B_S\) lie outside \(S\), so
\(S\in\mathcal D_{B_S}\).  The set \(Y(S)\) contains \(p(S)\), but it
contains neither \(r(S)\) nor either coordinate of \(A\).  Applying
\(\theta_{B_S}\) therefore replaces \(p(S)\) by whichever coordinate
\(\alpha_S\in A\) is paired with it and changes nothing else.  This proves
(2.3), independently of which of the two bijections \(B_S\to A\) was
chosen.

If

\[
 S\cup\{\alpha_S\}=S'\cup\{\alpha_{S'}\},
\]

then intersection with \(A\) first gives
\(\alpha_S=\alpha_{S'}\), and deleting this common coordinate gives
\(S=S'\).  Thus the owners are distinct, proving (2.4). \(\square\)

## 3. The general exposed-root capacity inequality

Let \(\mathcal B\subseteq\binom R2\).  Define

\[
 \boxed{
 \mathcal S(\mathcal B)=
 \left\{S\in\binom R{m-1}:
 \text{there is }B\in\mathcal B\text{ with }
 p(S)\in B\text{ and }B\cap S=\varnothing
 \right\}.}
\tag{3.1}
\]

For every \(S\in\mathcal S(\mathcal B)\), choose one witnessing pair
\(B(S)\).  Exactly as in Lemma 2.1,

\[
 Y_{B(S)}(S)=S\cup\{\alpha_S\},
\]

and these alternate owners are distinct over \(S\).  Hence the union of
owner-changing coherent alternatives for the substar \(\mathcal B\) has
size at least \(|\mathcal S(\mathcal B)|\), all of them meeting \(A\).

### Theorem 3.1 (common-background capacity)

Suppose a common matching \(M\) has all of the following properties.

1. For every \(S\in\binom R{m-1}\), it contains the \(F_A\)-token
   \((S,Y(S))\).
2. It saturates all remaining rank-\((m-1)\) lower roots and is
   middle-simple.
3. For every \(B\in\mathcal B\), replacing all \(F_A\)-tokens over
   \(\mathcal D_B\) by their coherent \(F_B\)-alternatives, while leaving
   the common background fixed, is middle-simple.

Then

\[
 \boxed{|\mathcal S(\mathcal B)|\le W-T.}
\tag{3.2}
\]

#### Proof

The phase-\(A\) tokens in item 1 use every owner in \(\binom Rm\), by
(1.1).  Therefore the common background in item 2 consists of

\[
 T-K_m
\tag{3.3}
\]

tokens whose distinct middle owners all meet \(A\).  There are exactly

\[
 W-K_m
\tag{3.4}
\]

rank-\(m\) sets meeting \(A\).

For every \(S\in\mathcal S(\mathcal B)\), the coherent endpoint belonging
to its witness \(B(S)\) contains the alternate owner
\(S\cup\{\alpha_S\}\).  Item 3 forces this owner to be absent from the
common background.  These forbidden owners are distinct, so the background
has at most

\[
 W-K_m-|\mathcal S(\mathcal B)|
\tag{3.5}
\]

available owners.  Comparing (3.3) and (3.5) gives

\[
 T-K_m\le W-K_m-|\mathcal S(\mathcal B)|,
\]

which is (3.2). \(\square\)

The proof used only each coherent all-new endpoint.  Therefore the same
necessary inequality holds a fortiori if every maximal physical interval
is required to be an independent legal bit over the common background.

## 4. Full-star impossibility and exact threshold

For the full star \(\mathcal B=\binom R2\), Lemma 2.1 gives

\[
 \mathcal S(\mathcal B)=\binom R{m-1},
 \qquad
 |\mathcal S(\mathcal B)|=K_m.
\]

Theorem 3.1 would therefore require

\[
 K_m\le W-T.
\tag{4.1}
\]

Direct division gives

\[
 \frac{K_m}{W}
 =\frac{m+1}{2(2m+1)},
 \qquad
 \frac{T}{W}=\frac m{m+2},
 \qquad
 \frac{W-T}{W}=\frac2{m+2}.
\tag{4.2}
\]

Now

\[
 \frac{m+1}{2(2m+1)}>\frac2{m+2}
\]

is equivalent to

\[
 (m+1)(m+2)>4(2m+1),
\]

or

\[
 m^2-5m-2>0.
\tag{4.3}
\]

For integral \(m\), (4.3) holds exactly when \(m\ge6\).  Thus (4.1) is
false for every \(m\ge6\), proving the announced full-star obstruction.

The threshold has been independently checked at its two neighboring
integers:

\[
 m=5:\quad m^2-5m-2=-2,
 \qquad
 m=6:\quad m^2-5m-2=4.
\]

## 5. Exact implication boundary

The theorem refutes the following literal statement:

> one common \(A\)-first pair-omission matching supports the coherent
> endpoint, and hence the interval cube, for every member of the complete
> partner-pair star \(\binom R2\).

It is stronger than a boundary-count objection: even allowing an unlimited
number of runs and ignoring every flag energy, the middle-owner capacity is
insufficient.

It does not refute any of the following possible escapes.

1. A substar \(\mathcal B\) satisfying the necessary exposure bound
   \(|\mathcal S(\mathcal B)|\le W-T\).
2. A menu whose different partner charts use genuinely different old
   backgrounds rather than one common matching.  Such a menu does not yet
   support endpoint-stable iteration.
3. A new base which does not contain all \(F_A\)-tokens on lower roots
   avoiding \(A\).
4. Owner-preserving partner alternatives, for which \(p(S)\notin B\).
   These can still change upper collars while leaving the middle owner
   fixed, and are not counted by \(\mathcal S(\mathcal B)\).
5. A nonbinary multiway chart with a separately proved exact ownership
   rule.

Accordingly, the positive algebraic \(A_n\) star frame does not compose
with the current first-avoided interval theorem.  Any replacement must
either find a quantitatively spanning substar below the exposure cap
\(2W/(m+2)\), or change the common-base architecture itself.
