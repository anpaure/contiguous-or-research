# Corrected Gaussian annulus: Catalan trade supply, local-action ceilings, and the root-scale gate

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, web
input, or probabilistic black box is used.

## 0. Outcome

Work on the even ground \([2m]\), and put

\[
 W=\binom{2m}{m},\qquad
 q_0=\lceil a\sqrt m\rceil,\qquad
 H=\lfloor b\sqrt m\rfloor,\qquad 0<a<b<\infty,
 \tag{0.1}
\]

\[
 N_q=\binom{2m}{m-q},\qquad
 K=\left\lfloor\frac{N_{q_0}}{2m}\right\rfloor,\qquad
 M=2mK=N_{q_0}-\rho,\quad0\le\rho<2m.
 \tag{0.2}
\]

The corrected annulus design needs only

\[
 \boxed{
 M=(e^{-a^2}+o(1))W}
 \tag{0.3}
\]

active middle occurrences, grouped into

\[
 \boxed{
 K=\left(\frac{e^{-a^2}}2+o(1)\right)\operatorname {Cat}_m}
 \tag{0.4}
\]

ordinary directed cyclic packets. There is no factor two in (0.3): one
middle start supplies one lower target and, by complementation, its paired
upper target.

This correction removes the old near-spanning row-count objection. It does
**not** make the known Catalan trades into an annulus construction. The
following sharper statements hold.

1. **Exact raw Catalan thresholds.** If a legal component bank contains
   \((\delta+o(1))\operatorname {Cat}_m\) packet rows and its largest
   component is \(o(\operatorname {Cat}_m)\), then it has enough rows for
   (0.4), up to \(o(\operatorname {Cat}_m)\) rounding, exactly when

   \[
                         \delta>\frac12e^{-a^2}.       \tag{0.5}
   \]

   Thus the audited \(3/8\) Catalan component bank passes the scalar test
   for

   \[
                         a^2>\log(4/3),                \tag{0.6}
   \]

   the sealed two-row \(1/8\) bank passes for \(a^2>\log4\), and the
   explicit unrelated pentagon pair, whose genuinely changed row density is
   \(5/256\), passes only for

   \[
                         a^2>\log(128/5).              \tag{0.7}
   \]

   Equality carries no certified slack. These are row-count tests only.

2. **Carrier-local trades are asymptotically powerless at the tight
   entrance.** If two paired ordinary packets differ only by reordering a
   contiguous carrier of \(w\) positions, then at every fixed depth at most
   \(2w\) of their cyclic targets change. For any \(R\le K\) paired packet
   replacements,

   \[
    |h_q-h_q'|\le2wR,\qquad
    |C_{\rm mid}-C_{\rm mid}'|\le2wR.              \tag{0.8}
   \]

   In particular,

   \[
    |h_{q_0}-h_{q_0}'|
       \le\left(e^{-a^2}+o(1)\right)\frac wm\,W.     \tag{0.9}
   \]

   Hence, whenever the reference family has a linear entrance defect,
   every \(w=o(m)\) trade preserves a linear entrance defect. Over
   the full annulus, if \(w=o(\sqrt m)\), it changes the complete
   collision-plus-hole objective by only \(o(W)\). The explicit
   non-row-power pentagon trade has \(w=9\), even when its nominal fringe
   scale grows, and is therefore fully invisible at the required \(o(W)\)
   annulus scale.

3. **The two standard growing mechanisms exhibit a supply--action
   dichotomy.**

   * First-fringe insertion has positive row supply, but every genuinely
     subroot carrier \(w=o(m)\) has \(o(W)\) tight-entrance action.
   * A growing \(t\)-node operadic skeleton has root-scale action potential,
     but the common fixed-coordinate port interface permits at most

     \[
      \left(\frac{16}{3\sqrt\pi}+o(1)\right)
       \frac{\operatorname {Cat}_m}{t^{3/2}}          \tag{0.10}
     \]

     root rows. Relative to (0.4), this is at most

     \[
      \left(\frac{32e^{a^2}}{3\sqrt\pi}+o(1)\right)t^{-3/2}
      =o(1)                                           \tag{0.11}
     \]

     when \(t\to\infty\) and \(t=o(m)\). Thus, in that range, the literal
     common-port skeleton deck is
     occurrence-count insufficient even after the constant-density
     correction.

4. **The exact SCD scaffold forces root-scale chronology in narrow
   annuli.** The integral SCD scaffold already gives exactly
   \(N_{q_0}\) owner-simple providers and exact support at every depth.
   If it is grouped into \(K\) ordinary \(2m\)-cycles, omitting the
   remainder \(\rho\), then the rotor graph induced by the clipped top
   class \(\mathcal D_{\ge H}\) must contain

   \[
    \lambda_H(\mathcal D,\sigma)\ge
       2N_H-N_{q_0}-\rho-K.                       \tag{0.12}
   \]

   When \(b^2-a^2<\log2\), this is

   \[
    \lambda_H(\mathcal D,\sigma)\ge
     \left(2e^{-b^2}-e^{-a^2}-o(1)\right)W.          \tag{0.13}
   \]

   Equivalently, the average selected packet must devote at least the
   fraction

   \[
       \boxed{\gamma_{a,b}
       =2e^{-(b^2-a^2)}-1-o(1)>0}                    \tag{0.14}
   \]

   of its \(2m\) arcs to top-class-to-top-class rotor transport. Any trade
   which changes only \(o(m)\) relevant chronology arcs per packet cannot
   create this from a fixed port-assigned scaffold with
   \(\lambda_H(\mathcal D,\sigma)=o(W)\).

Therefore the corrected density makes positive Catalan row supply
possible, but none of the audited bounded-fringe, bounded-core, or
shape-respecting growing-skeleton trade families produces the required
ordinary cyclic annulus packets. A viable trade must be genuinely
root-scale: it must change \(\Theta(m)\) entrance/chronology data on a
positive fraction of the selected packets, preserve the complete ordinary
middle-owner ledger after passing from \(2m+1\) to \(2m\), and balance all
hereditary path colours simultaneously. No such trade is constructed
here, and no theorem rules out an unrelated root-scale pair.

## 1. Corrected packet and hole ledgers

Let a packet be a directed cyclic order \(\pi\) on \([2m]\), modulo
rotation. Write

\[
 I_\pi(j,s)=\{\pi_j,\pi_{j+1},\ldots,\pi_{j+s-1}\},
 \qquad j\in\mathbb Z_{2m}.
 \tag{1.1}
\]

Its middle owners and depth-\(q\) lower targets are

\[
 \mathcal O(\pi)=\{I_\pi(j,m):j\in\mathbb Z_{2m}\},
 \tag{1.2}
\]

\[
 \mathcal E_q(\pi)
 =\{I_\pi(j,m-q):j\in\mathbb Z_{2m}\}.             \tag{1.3}
\]

Every displayed family has \(2m\) distinct members. Also

\[
 I_\pi(j+m,m)=I_\pi(j,m)^c,                         \tag{1.4}
\]

and upper targets are complements of the corresponding lower targets.

For a family \(\Pi\) of \(K\) packets, let

\[
 C_{\rm mid}(\Pi)
 =2mK-\left|\bigcup_{\pi\in\Pi}\mathcal O(\pi)\right|
 \tag{1.5}
\]

and

\[
 h_q(\Pi)
 =N_q-\left|\bigcup_{\pi\in\Pi}\mathcal E_q(\pi)\right|.
 \tag{1.6}
\]

The exact literal compiler ledger is

\[
 L\le W+2HK+C_{\rm mid}(\Pi)
             +2\sum_{q=q_0}^{H}h_q(\Pi).             \tag{1.7}
\]

Consequently the exact integral target is

\[
 \boxed{
 C_{\rm mid}(\Pi)=o(W),\qquad
 \sum_{q=q_0}^{H}h_q(\Pi)=o(W).}                     \tag{1.8}
\]

The binomial ratio is

\[
 \frac{N_q}{W}
 =\prod_{i=1}^{q}\frac{m-i+1}{m+i},
 \tag{1.9}
\]

and uniformly for \(q=x\sqrt m+O(1)\), \(a\le x\le b\),

\[
 \frac{N_q}{W}=e^{-x^2+O_{a,b}(m^{-1/2})}.            \tag{1.10}
\]

Equations (0.3)--(0.4) follow, since

\[
 \operatorname {Cat}_m=\frac{W}{m+1}.                \tag{1.11}
\]

At every depth let \(L_q(T)\) be the selected occurrence load and put

\[
 E_q=\sum_T(L_q(T)-1)_+.
 \tag{1.12}
\]

The total occurrence mass is \(M=N_{q_0}-\rho\), so

\[
 E_q=M-\left|\{T:L_q(T)>0\}\right|.
 \]

Subtracting this from (1.6) gives the exact \(L^1\) conservation law

\[
 \boxed{
 h_q
 =E_q-\bigl(N_{q_0}-N_q-\rho\bigr).}             \tag{1.13}
\]

Thus later depths are allowed, and indeed forced, to contain
\(\Theta(W)\) repeat mass. The target is not to make raw repetition small;
it is to track the forced term in (1.13) with aggregate additive error
\(o(W)\).

The tight entrance is different:

\[
                         h_{q_0}=E_{q_0}+\rho.        \tag{1.14}
\]

It must therefore be a near-factor. In particular, any construction has
at least \(N_{q_0}-o(W)\) distinct active middle starts. This proves that
(0.3) is the exact demand.

For scale comparison, the signed annular target mass is

\[
 2\sum_{q=q_0}^{H}N_q
 =\left(2\int_a^b e^{-x^2}\,dx+o(1)\right)W\sqrt m,
 \tag{1.15}
\]

whereas the selected packets supply

\[
 2M(H-q_0+1)
 =\left(2e^{-a^2}(b-a)+o(1)\right)W\sqrt m.
 \tag{1.16}
\]

There is no scalar shortage: \(M\ge N_q-o(W)\) for every \(q\ge q_0\).
The remaining condition is dispersion of the hereditary directed path
colours.

## 2. Raw Catalan row supply

Put

\[
                         B=\operatorname {Cat}_m.
 \tag{2.1}
\]

Suppose a literal component deck has disjoint components whose root-row
blocks contain in total

\[
                         V_m=(\delta+o(1))B          \tag{2.2}
\]

rows, and whose largest component has \(p_m=o(B)\) rows on one shore.
If only these active rows may be used as packet rows, then the necessary
row-count condition is

\[
                         V_m\ge K-o(B).              \tag{2.3}
\]

Using (0.4), this is exactly

\[
                         \delta\ge\frac12e^{-a^2}.   \tag{2.4}
\]

With strict inequality, the condition is also sufficient as a scalar
component count up to \(o(B)\): add whole components until their row mass
first reaches \(K\). The overshoot is at most \(p_m=o(B)\), which
corresponds to \(o(W)\) owner occurrences. This argument asserts neither
ordinary-packet owner disjointness nor target dispersion.

### Corollary 2.1 (audited bank thresholds)

The bounded-component truncation of the \(s_1=(2,3)\) MSW component
hierarchy contains

\[
                       \left(\frac38+o(1)\right)B      \tag{2.5}
\]

root rows in components of any prescribed growing polynomial maximum
size. Its raw threshold is therefore (0.6).

The sealed size-two layer contains

\[
                       \left(\frac18+o(1)\right)B,     \tag{2.6}
\]

giving the threshold \(a^2>\log4\).

The explicit unrelated pentagon pair has
\(\operatorname {Cat}_{r-4}\) five-row components in a size-\(r\) local
factor. Hence its genuinely changed row fraction is

\[
 \frac{5\operatorname {Cat}_{r-4}}{\operatorname {Cat}_r}
 =\frac5{256}+o(1),                                  \tag{2.7}
\]

which gives (0.7) after an asymptotically complete first-fringe lift.

These thresholds are deliberately stated in projected ordinary-packet row
units. On the odd PBBS/MSW ground,

\[
 W_{\rm odd}=(2m+1)B
             =\left(2+o(1)\right)W.                  \tag{2.8}
\]

A \(\delta B\)-row odd bank owns \(\delta W_{\rm odd}\) odd middle
occurrences but supplies at most \(2m\delta B=(2\delta+o(1))W\)
ordinary projected starts. Therefore:

* the same-ground odd occurrence test is \(\delta>e^{-a^2}\);
* the even projected row-count test is \(\delta>\tfrac12e^{-a^2}\).

They must not be conflated. Infinity cutting does transport a canonical
primary-owner partition, but neither count proves that a prescribed-density
selection has \(o(W)\) collisions among all \(2m\) starts; Section 7 gives
the exact complement-graph formula for that issue.

### 2.2 A conditional orbit gate for a transposition bank

The \(3/8\) bank is not carrier-local in the sense of Section 3. A
coordinate transposition can exchange labels whose positions in a packet
are macroscopically separated, and can therefore change \(\Theta(m)\)
intervals in one row. It must be treated separately.

Let \(\tau\) be the defining coordinate transposition. For a selected
ownership component \(J\), let \(u_{J,q}\) be the complete old-shore
depth-\(q\) occurrence histogram. Assume the **full-profile equivariance**

\[
                         v_{J,q}=\tau u_{J,q}         \tag{2.9}
\]

for every selected component and every protected depth. This hypothesis is
stronger than root-block closure: equality of the root block and transport
of the owned \(X/Y\) tokens do not by themselves identify every exported
Gaussian-depth occurrence. Under this explicit hypothesis, choose a family
\(\mathcal J\) of whole components and one shore
\(\varepsilon_J\in\{0,1\}\) from each. Its histogram is

\[
 \mu_q^\varepsilon
 =\sum_{J\in\mathcal J}
    \tau^{\varepsilon_J}u_{J,q}.                     \tag{2.10}
\]

For a target orbit \(O\) under \(\langle\tau\rangle\), put

\[
 s_{q,O}(\mathcal J)
 =\sum_{J\in\mathcal J}\sum_{T\in O}u_{J,q}(T).      \tag{2.11}
\]

Then every component signing has the exact invariant

\[
 \boxed{
 \sum_{T\in O}\mu_q^\varepsilon(T)
 =s_{q,O}(\mathcal J).}                              \tag{2.12}
\]

Consequently

\[
 \boxed{
 h_q(\mu^\varepsilon)
 \ge D_q^\tau(\mathcal J)
 :=\sum_{O\in\mathcal T_q/\langle\tau\rangle}
       \bigl(|O|-s_{q,O}(\mathcal J)\bigr)_+.}        \tag{2.13}
\]

#### Proof

Under the stated full-profile hypothesis, summing either \(u_{J,q}\) or
its \(\tau\)-image
over a complete \(\tau\)-orbit gives the same value, which proves
(2.12). A target orbit of size \(|O|\) receiving total integral mass
\(s\) can support at most \(\min\{|O|,s\}\) of its members. Summing the
resulting orbitwise holes proves (2.13). \(\square\)

At the tight entrance, total mass is \(N_{q_0}-\rho\), so a successful
tail-cube packet family must first select whole components satisfying

\[
 D_{q_0}^\tau(\mathcal J)=o(W),\qquad
 \sum_{q=q_0}^{H}D_q^\tau(\mathcal J)=o(W),           \tag{2.14}
\]

as well as the projected middle-owner analogue. Only after these quotient
near-factor conditions hold can the component signs decide which member
of each two-point orbit is hit. The same signs occur at every depth, so
that second step is a hereditary two-colour/NAE problem, not independent
depthwise rounding.

No audited theorem proves even the full-profile premise (2.9), let alone
(2.14), for the complete Gaussian profiles of the \(3/8\) Catalan tail
bank. Thus this nonlocal bank is not ruled out by the carrier ceiling
below, but its positive row density is not yet a packet theorem. If (2.9)
is established, the quotient deficit (2.13), followed by simultaneous
all-depth orientation of the two-point orbits, is the exact next gate.

### 2.3 Catalogue-union cuts

There is a factor-independent supply test stronger than row count. For any
catalogue \(\mathscr C\) of legal ordinary packets, define

\[
 \mathcal U_{\rm mid}(\mathscr C)
 =\bigcup_{\pi\in\mathscr C}\mathcal O(\pi),\qquad
 \mathcal U_q(\mathscr C)
 =\bigcup_{\pi\in\mathscr C}\mathcal E_q(\pi).        \tag{2.15}
\]

Every \(K\)-packet subfamily \(\Pi\subseteq\mathscr C\) obeys

\[
 \boxed{
 C_{\rm mid}(\Pi)
 \ge\bigl(M-|\mathcal U_{\rm mid}(\mathscr C)|\bigr)_+,}
                                                               \tag{2.16}
\]

\[
 \boxed{
 h_q(\Pi)\ge N_q-|\mathcal U_q(\mathscr C)|.}          \tag{2.17}
\]

Indeed, the selected distinct owner and target supports are contained in
the corresponding catalogue unions. Therefore every viable Catalan/Dyck
trade catalogue must satisfy

\[
 \bigl(M-|\mathcal U_{\rm mid}|\bigr)_+
 +2\sum_{q=q_0}^{H}
     \bigl(N_q-|\mathcal U_q|\bigr)=o(W).              \tag{2.18}
\]

This condition is necessary, not sufficient: it allows a different packet
subfamily for every provider. The remaining theorem must choose one common
grouped subfamily of \(K\) cyclic orders.

## 3. A partial-packet carrier-locality theorem

### Definition 3.1

Two directed cyclic orders \(\pi,\pi'\) are \(w\)-carrier-local if, after
a common rotation, they agree outside one contiguous block of \(w\)
positions and the two versions of that block contain the same coordinate
set, possibly in different orders.

### Lemma 3.2 (two-boundary interval bound)

For every \(1\le s\le2m-1\), at most \(2w\) starts \(j\) satisfy

\[
                         I_\pi(j,s)\ne I_{\pi'}(j,s). \tag{3.1}
\]

#### Proof

If neither boundary cut of a cyclic interval lies strictly inside the
carrier block, the interval contains either all carrier coordinates or
none of them. Its target set is unchanged. There are fewer than \(w\)
internal cuts at which the left boundary can lie and fewer than \(w\) at
which the right boundary can lie. The union bound gives \(2w\). \(\square\)

### Theorem 3.3 (partial-family \(L^1\) ceiling)

Let

\[
 \Pi=(\pi_1,\ldots,\pi_R),\qquad
 \Pi'=(\pi_1',\ldots,\pi_R')
 \tag{3.2}
\]

be paired packet families, with every pair \(w\)-carrier-local. Then for
every depth \(q\),

\[
 \boxed{
 \frac12\|\mu_q(\Pi)-\mu_q(\Pi')\|_1\le2wR,}          \tag{3.3}
\]

\[
 \boxed{
 |h_q(\Pi)-h_q(\Pi')|\le2wR,}                        \tag{3.4}
\]

and

\[
 \boxed{
 |C_{\rm mid}(\Pi)-C_{\rm mid}(\Pi')|\le2wR.}        \tag{3.5}
\]

Consequently, with

\[
 D=H-q_0+1,
 \tag{3.6}
\]

\[
\begin{aligned}
 &\left|
 C_{\rm mid}(\Pi)+2\sum_{q=q_0}^{H}h_q(\Pi)
 -C_{\rm mid}(\Pi')-2\sum_{q=q_0}^{H}h_q(\Pi')
 \right|\\
 &\hspace{45mm}\le(4D+2)wR.                         \tag{3.7}
\end{aligned}
\]

#### Proof

Lemma 3.2 changes at most \(2w\) target occurrences per packet. Replacing
one occurrence changes its histogram by one positive and one negative
unit, so summing over \(R\) packets proves (3.3).

For two nonnegative integer histograms of equal total mass,

\[
 \left||\operatorname {supp}x|-|\operatorname {supp}y|\right|
 \le\frac12\|x-y\|_1.                                \tag{3.8}
\]

Apply this first to the depth-\(q\) histograms and then to the middle-owner
histograms. Equations (3.4)--(3.5) follow. Summing gives (3.7).
\(\square\)

### Corollary 3.4 (the exact locality scales)

For \(R\le K\), (3.4) at \(q=q_0\) becomes

\[
 |h_{q_0}(\Pi)-h_{q_0}(\Pi')|
 \le
 \left(e^{-a^2}+o(1)\right)\frac wm\,W.              \tag{3.9}
\]

Thus:

* \(w=o(m)\) cannot repair a positive-density entrance defect;
* \(w=o(\sqrt m)\) changes the complete objective (1.8) by only \(o(W)\);
* \(w=\Theta(\sqrt m)\) may have \(\Theta(W)\) aggregate annulus action,
  but still has only \(o(W)\) action at the tight entrance;
* creating an entrance near-factor from a reference family with
  \(h_{q_0}\ge cW\) requires \(w=\Omega_{a,c}(m)\).

The conclusion is statewise. It allows arbitrary correlated component
signs; independence is not used.

## 4. Consequences for the known non-row-power fringe pair

On its native odd factor ground, the explicit unrelated pair at local
scale \(r\) consists of
\(\operatorname {Cat}_{r-4}\) independently switchable five-row
components. Nominally \(r\) grows, but the two packet shores differ only
inside the once-suspended size-three core. Its active carrier width is

\[
                              w=9.                  \tag{4.1}
\]

Any ordinary even-ground deployment obtained by deleting infinity in a
way which preserves the common cyclic alignment and this carrier block is
therefore \(9\)-carrier-local. For every such deployment, after
first-fringe lifting and arbitrary port-closed component signs, Theorem
3.3 gives

\[
 |h_{q_0}-h_{q_0}'|=O(W/m),                          \tag{4.2}
\]

\[
 \left|
 C_{\rm mid}+2\sum_{q=q_0}^{H}h_q
 -C_{\rm mid}'-2\sum_{q=q_0}^{H}h_q'
 \right|
 =O(W/\sqrt m)=o(W).                                 \tag{4.3}
\]

Thus even in the range (0.7), where its raw active-row count is large
enough, a carrier-preserving projection of the pentagon bank cannot turn a
failing reference packet family into a successful annulus family. No
arbitrary parity projection is asserted: Section 7 records that the
complete even owner ledger itself is still missing.

More generally, a one-hole size-\(r\) pair is
\((2r+1)\)-carrier-local. If \(r=o(\sqrt m)\), it is invisible to the full
objective; if \(r=o(m)\), it cannot repair the entrance. The minimal scale
for a genuinely new entrance construction is therefore not
\(\Theta(\sqrt m)\) but

\[
                              \boxed{r=\Omega(m)}.   \tag{4.4}
\]

This is specific to constructing the tight constant-density entrance.
The older \(\Theta(\sqrt m)\) scale was the threshold for accumulating
\(\Theta(W)\) action over \(\Theta(\sqrt m)\) depths after the entrance
had already been controlled.

## 5. Growing operadic skeletons have the opposite failure

Let \(\mathcal T_m\) be the \(B=\operatorname {Cat}_m\) ordered binary
trees with \(m\) internal nodes. For a \(t\)-node skeleton \(S\) and an
ordered spectator tuple

\[
 \mathbf A=(A_0,\ldots,A_t),\qquad
 \sum_i|A_i|=m-t,
 \tag{5.1}
\]

the full skeleton packet is

\[
 E_{\mathbf A}
 =\{S(A_0,\ldots,A_t):S\in\mathcal T_t\}.             \tag{5.2}
\]

It has \(\operatorname {Cat}_t\) root rows. To transport one common local
factor by literal shape-respecting substitution, the root ports must have
the form

\[
 \operatorname {port}(S(\mathbf A))
 =U\mathbin{\dot\cup}\iota(\operatorname {port}(S)),  \tag{5.3}
\]

where \(U\) and the coordinate injection \(\iota\) are independent of
\(S\).

The elementary rotation test forces

\[
 A_0\text{ to be a mountain},\qquad
 A_1=\cdots=A_{t-2}=\varnothing.                    \tag{5.4}
\]

Therefore the number of spectator tuples which can pass even this
necessary port test is at most

\[
 B_{m-t}
 =[z^{m-t}]\frac{C(z)^2}{1-z}
 =\sum_{j=0}^{m-t}\operatorname {Cat}_{j+1}
 =\left(\frac{16}{3}+o(1)\right)\operatorname {Cat}_{m-t}.
 \tag{5.5}
\]

Even if all eligible packets were disjoint, they could contain at most

\[
 \operatorname {Cat}_t B_{m-t}
 =\left(\frac{16}{3\sqrt\pi}+o(1)\right)
   \frac{\operatorname {Cat}_m}{t^{3/2}}             \tag{5.6}
\]

root rows, for \(t\to\infty\), \(t=o(m)\). Dividing by (0.4) gives
(0.11).

More generally, when both \(t\to\infty\) and \(m-t\to\infty\), the same
calculation gives

\[
 \operatorname {Cat}_t B_{m-t}
 =\left(\frac{16}{3\sqrt\pi}+o(1)\right)
   \frac{m^{3/2}}{t^{3/2}(m-t)^{3/2}}
   \operatorname {Cat}_m.                           \tag{5.6a}
\]

Thus the supply is \(o(\operatorname {Cat}_m)\) whenever both sides of
the skeleton grow. Formula (5.6) is its \(t=o(m)\) specialization. Neither
formula excludes the root-near regime \(m-t=O(1)\).

### Theorem 5.1 (corrected-density skeleton no-go)

For every fixed \(a>0\), and every \(t\to\infty\) with \(t=o(m)\), no
packing of full growing-skeleton packets using the common interface
(5.3) can supply the
\(K=(e^{-a^2}/2+o(1))\operatorname {Cat}_m\) ordinary packet rows required
by the corrected annulus design.

#### Proof

Equation (5.6) divided by \(K\) tends to zero by (0.11). Hence the union
of every physically eligible growing-skeleton packet contains only
\(o(K)\) roots. \(\square\)

This is an actual supply obstruction, not a matching or pseudorandomness
failure. Arbitrary row-dependent reindexing or a newly constructed
root-scale \(D_m\)-port factor is outside (5.3).

## 6. The exact SCD scaffold and the top-tag transport cut

The corrected density admits an integral incidence scaffold. Fix any
symmetric chain decomposition \(\mathcal D\) of \(B_{2m}\), and retain
the chains of tag at least \(q_0\). Their number is exactly \(N_{q_0}\);
their middle members are distinct. At every depth \(q_0\le q\le H\),
the tag-\(\ge q\) chains contain every lower and upper rank-\(q\) target
exactly once. Thus owner and all-depth target incidence are solved before
chronology is imposed.

Fix an annular port/extension assignment \(\sigma\) on \(\mathcal D\).
Let \(\mathcal D_{\ge H}\) be the chains whose tag is at least \(H\), and
let \(\lambda_H(\mathcal D,\sigma)\) be the maximum number of genuine
rotor arcs in a vertex-disjoint directed linear forest induced by this
clipped top class. The dependence on \(\sigma\) is essential: an SCD by
itself does not specify the rotor graph.

### Theorem 6.1 (cycle-form clipped-top cut)

Suppose \(2mK=N_{q_0}-\rho\) retained states are partitioned into
\(K\) radius-\(H\) rotor cycles of length \(2m\). Let
\(e_{HH}^{\circ}\) be the number of actually used cycle arcs whose two
endpoints both lie in \(\mathcal D_{\ge H}\). Then

\[
 \boxed{
 e_{HH}^{\circ}\ge2N_H-N_{q_0}-\rho.}              \tag{6.1a}
\]

Moreover,

\[
 \boxed{
 \lambda_H(\mathcal D,\sigma)
 \ge2N_H-N_{q_0}-\rho-K.}                         \tag{6.1}
\]

#### Proof

Omit the \(\rho\) unused states. Mark a selected state by \(\mathsf H\)
when its SCD tag is at least \(H\), and by \(\mathsf O\) otherwise. Let
their used counts be \(M_H,M_O\). Then

\[
 M_H\ge N_H-\rho,\qquad M_O\le N_{q_0}-N_H.          \tag{6.2a}
\]

In a directed cyclic \(\mathsf H/\mathsf O\)-word, the number of
\(\mathsf H\to\mathsf O\) transitions is at most its number of
\(\mathsf O\)-vertices; on an all-\(\mathsf H\) cycle it is zero.
Therefore

\[
 e_{HH}^{\circ}\ge M_H-M_O
 \ge2N_H-N_{q_0}-\rho,                               \tag{6.2b}
\]

which proves (6.1a).

Delete at most one top--top arc from each of the \(K\) cycles so that the
remaining top--top arcs form a directed linear forest. Clipped-top
rigidity
makes all of them genuine rotor arcs. Hence

\[
 \lambda_H(\mathcal D,\sigma)
 \ge e_{HH}^{\circ}-K
 \ge2N_H-N_{q_0}-\rho-K,
\]
proving (6.1). \(\square\)

Using (1.10),

\[
 \lambda_H(\mathcal D,\sigma)
 \ge
 \left(2e^{-b^2}-e^{-a^2}-o(1)\right)W.             \tag{6.3}
\]

When \(b^2-a^2<\log2\), divide the sharper used-arc bound (6.1a) by

\[
 2mK=(e^{-a^2}+o(1))W
 \tag{6.4}
\]

to obtain the required arc fraction (0.14). Equivalently,

\[
 \frac{\lambda_H(\mathcal D,\sigma)}K
 \ge
 2m\left(2e^{-(b^2-a^2)}-1-o(1)\right).              \tag{6.5}
\]

### Corollary 6.2 (root-scale chronology is necessary)

Assume a fixed port-assigned reference scaffold has
\(\lambda_H(\mathcal D,\sigma)=o(W)\), and a packet trade can
change at most \(c w\) top-class adjacency incidences per selected packet,
where \(c\) is fixed. In the narrow-annulus range
\(b^2-a^2<\log2\), no \(w=o(m)\) trade can produce the required cycle
factor.

#### Proof

At most \(K\) packets are changed, so the trade creates at most
\(cwK=o(mK)=o(W)\) new eligible arcs. This contradicts the positive
linear used-arc requirement (6.1a).
\(\square\)

Thus bounded-fringe and bounded-core rethreadings cannot turn any
verified low-\(\lambda_H\) reference into the corrected annulus compiler.
No low-\(\lambda_H\) assertion is made here for the clipped BTK scaffold.
For a wider annulus, (6.3) may be nonpositive at the top class;
the lower-tag protected-promotion hierarchy remains a necessary condition,
but it permits late-promotion escape and does not give the same unconditional
root-scale conclusion.

## 7. What infinity cutting gives, and what it does not

The Catalan/MSW component theorems live on
\(\Omega=[2m]\cup\{\infty\}\). Rotate an anchored exact-factor row to
\((\infty,a_1,\ldots,a_{2m})\), delete infinity, and call the resulting
ordinary cyclic order \(\pi\). The \(m+1\) nonwrapping middle windows in
all rows partition \(\binom{[2m]}m\), because they are exactly the
infinity-avoiding odd-factor owners and
\((m+1)\operatorname {Cat}_m=W\).

The remaining \(m-1\) middle windows in a row are complements of its
nonport nonwrapping windows. Hence every common exact factor defines a
loopless \((m-1)\)-regular complement multigraph \(G_F\) on its Catalan
rows, and every selected row set \(S\) satisfies the exact identity

\[
  2m|S|-\left|\bigcup_{x\in S}E_m(\pi_x)\right|
  =2e_{G_F}(S).                                      \tag{7.1}
\]

Thus infinity cutting does give literal ordinary packets and an exact
middle-collision ledger. It does not automatically give a sparse
prescribed-density shore of \(G_F\), nor does it control the rank-\(q_0\)
and hereditary deeper interval unions. Also, rows used merely as ordinary
packets need not come from one common factor state: it suffices that each
row variant occur in some certified exact state. A common state is a
useful structured sublane, not a completion requirement of the final
packet concatenation.

## 8. Exact proved and open boundary

The following is proved.

1. The corrected active mass and packet count are (0.3)--(0.4).
2. The exact hole/repeat identity is (1.13), so the target is the
   floor-correct \(L^1\) profile, not raw low collision.
3. The \(3/8\), \(1/8\), and \(5/256\) banks pass the raw projected row
   count exactly in the ranges (0.6), \(a^2>\log4\), and (0.7).
4. Every \(w\)-carrier-local partial packet trade obeys (3.3)--(3.7).
5. The unrelated pentagon bank is \(o(W)\)-invisible to the complete
   corrected annulus objective.
6. Full growing-skeleton substitution with the literal common port
   interface supplies only \(o(K)\) packet roots when
   \(t,m-t\to\infty\); the root-near regime remains outside the theorem.
7. In the narrow-annulus range, every SCD-scaffold cycle realization
   needs the positive clipped-top arc fraction (0.14), forcing root-scale
   chronology changes from every low-\(\lambda_H\) reference.
8. Under full-profile equivariance, a nonlocal coordinate-transposition
   bank obeys the quotient deficit (2.13)--(2.14); that premise is not yet
   proved for the full \(3/8\) Gaussian tail bank.
9. Infinity cutting gives the exact complement-graph identity (7.1), so
   the even middle-owner issue is a prescribed-density induced-edge
   problem, not an undefined parity transfer.

The following is not proved.

1. A prescribed-density projected ordinary-packet family with
   \(o(W)\) middle collisions.
2. A rank-\(q_0\) cyclic interval near-factor inside any Catalan trade
   cube.
3. Aggregate \(o(W)\) hereditary path-colour holes through \(H\).
4. A new root-scale unrelated exact pair with fragmented port-closed
   components and \(\Theta(m)\) active chronology per selected row.
5. The quotient near-factor and hereditary orientation conditions
   (2.14) for the \(3/8\) transposition tail cube.

Accordingly the known positive-density Catalan/Dyck trades do not produce
the corrected annulus design. The exact surviving positive theorem is:

> Construct directly, on the ordinary \(2m\)-ground, a root-scale
> port-closed trade deck with at least
> \((e^{-a^2}/2+o(1))\operatorname {Cat}_m\) usable packet rows, projected
> middle collision \(o(W)\), a rank-\(q_0\) interval near-factor, and
> aggregate hereditary path-colour holes \(o(W)\). In every narrow annulus,
> its selected packets must carry the clipped-top arc fraction (0.14).

This object is genuinely new. It is neither a bounded-core suspension nor
a shape-respecting operadic lift of one.
