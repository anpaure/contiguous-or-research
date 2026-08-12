# Extensive reciprocal-\(C_8\) packets at the one-baseline scale: exact shallow ledger, action budget, and SCD-cycle obstruction

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 B=C_m={W\over m+1},\qquad N_q=\binom{2m}{m-q},
\tag{0.1}
\]

and take the audited one-baseline scales

\[
 r=q_0=\lceil m^{1/4}\rceil,
 \qquad H=\lceil\sqrt{m\log m}\rceil.
\tag{0.2}
\]

Let

\[
 K=\left\lfloor{N_r\over2m}\right\rfloor,
 \qquad M=2mK=N_r-\rho,\qquad 0\le\rho<2m.
\tag{0.3}
\]

The conclusions are as follows.

1.  The packet demand is a near-half selection of Catalan rows:

    \[
    {N_r\over W}
     =1-{r^2\over m}+{r^4\over2m^2}+O(m^{-3/2}),
    \tag{0.4}
    \]

    \[
    \boxed{
    {K\over B}
      ={1\over2}-{r^2-1\over2m}
       +{r^4-2r^2\over4m^2}
       +O(m^{-3/2})+O(B^{-1})
      ={1\over2}-{1\over2\sqrt m}+O(m^{-3/4}).}
    \tag{0.5}
    \]

2.  The exact shallow packet ledger is favourable.  If \(E_q\) is the
    lower repeat excess of the selected packets at depth \(q\), then the
    upper repeat excess is the same and

    \[
      h_q=N_q-N_r+\rho+E_q\qquad(1\le q<r).
    \tag{0.6}
    \]

    The two-sign compulsory part is

    \[
    \boxed{
    2\sum_{q=1}^{r-1}(N_q-N_r+\rho)
     ={W\over3m}(r-1)r(4r+1)
      +O\!\left(W{r^5+r^3\over m^2}\right)
      +2(r-1)\rho
     =\left({4\over3}+o(1)\right){W\over m^{1/4}}.}
    \tag{0.7}
    \]

    Hence the shallow *deficit* does not obstruct coefficient one.  The
    missing condition is exactly

    \[
                     \sum_{q<r}E_q=o(W).
    \tag{0.8}
    \]

3.  Fix \(u=\lfloor\alpha m\rfloor\) disjoint reciprocal-\(C_8\)
    slots, \(0<\alpha<1/2\).  For every distinct-root \(K\)-row
    selection \(S\), the total number of eligible selected slot bits is
    not merely bounded above but is uniformly

    \[
       \boxed{
       \sum_{x\in S}|J(x)|
          ={\alpha\over16}W+O_\alpha(W/\sqrt m).}
    \tag{0.9}
    \]

    If \(I=\sum_{x\in S}|L_x|\) bits are actually used, then the sharp
    middle support action is at most \(2I\), while at every nonmiddle
    depth the lower support action is at most \(4I\).  Thus the complete
    distinct-root bank has the exact leading ceilings

    \[
       \boxed{2I\le\left({\alpha\over8}+o(1)\right)W}
       \quad\hbox{at the middle},
    \tag{0.10}
    \]

    \[
       \boxed{4I\le\left({\alpha\over4}+o(1)\right)W}
       \quad\hbox{at each signed nonmiddle depth}.
    \tag{0.11}
    \]

    Constant \(2\) in (0.10) is the reciprocal-token two-switch
    constant, not the weaker generic adjacent-transposition constant.

4.  Equations (0.10)--(0.11) give capacity, not productive all-depth
    transport.  The shallow occurrence profile has mass
    \((1+o(1))Wr\) per sign, and the bank can alter at most

    \[
             \left({\alpha\over4}+o(1)\right)Wr
             =\left({\alpha\over4}+o(1)\right)Wm^{1/4}
    \tag{0.12}
    \]

    of it.  Yet success requires the *total* shallow collision excess to
    be \(o(W)\), a collision fraction \(o(1/r)\), simultaneously at all
    \(r-1\) ranks.  A precise hereditary positive-part obstruction is
    proved in Theorem 4.1 below.

5.  At the outer scale,

    \[
           {N_H\over W}=(1+o(1))m^{-1},\qquad
           \sum_{q=r}^{H}N_q
             =\left({\sqrt\pi\over2}+o(1)\right)W\sqrt m.
    \tag{0.13}
    \]

    The target-capped aggregate hole action of the distinct-root bank is
    at most

    \[
       \boxed{
       \left(A_\alpha+o(1)\right)W\sqrt m,\qquad
       A_\alpha={\alpha\over4}\sqrt{\log{4\over\alpha}}
           +\int_{\sqrt{\log(4/\alpha)}}^\infty e^{-x^2}\,dx.}
    \tag{0.14}
    \]

    This is of the required root-profile order, but the same row bits
    determine every depth.  Independent depthwise use of (0.11) is not a
    legal selection theorem.

6.  Exact shallow SCD coherence is substantially stronger than (0.8).
    At depth one, antipodal starts of every ordinary cyclic packet have
    reversed two-letter SCD words.  A common-order monotone SCD, including
    BTK and every coordinate relabelling of BTK, can contain at most one
    start from each antipodal pair.  Therefore:

    \[
       \boxed{\text{No reciprocal-\(C_8\) packet, or any ordinary cyclic
       packet at all, can be exactly shallow-BTK-flag coherent.}}
    \tag{0.15}
    \]

    More strongly, making a \(K\)-packet family monotone-SCD coherent
    requires discarding at least

    \[
                 mK=M/2=(1/2-o(1))W
    \]

    starts.  Thus even the \(o(W/H)\)-exception version needed by the
    one-baseline theorem is impossible for monotone SCDs.  This does not
    rule out the weaker aggregate condition (0.8), nor coherence with a
    genuinely nonmonotone SCD.

7.  The sharp packet catalogue permits several variants of one root.
    Such repetitions evade (0.9): only the crude bound
    \(I\le uK=(\alpha/2+o(1))W\) remains.  Exact SCD coherence forbids
    repetitions.  More quantitatively, if \(R\) selected entries are
    extra variants over already used roots, then at every proper depth

    \[
                E_q\ge (2-4\alpha-o(1))mR.
    \]

    Hence the shallow gate forces \(R=o(B/r)\), while exact shallow
    simplicity forces \(R=0\).  This still does not reduce the entire
    annular problem to a root transversal: replacing those variants can
    alter \(H\) depth profiles, and \(H/r\to\infty\).  Consequently
    Theorem 4.1 closes the distinct-root \(\mathrm{ECAP}^*\) sublane when
    its functional is macroscopic, but it is not a no-go for the broader
    repeated-root catalogue.

The net result is a sharp boundary.  The one-baseline scale repairs the
scalar deficit, and extensive \(C_8\) trades have root-scale action.
What remains is a simultaneous near-perfect packing of the complete
middle-through-\(H\) profile.  Neither edit mass nor separate rankwise
capacity proves that packing.

## 1. Exact census at the moving entrance

The exact product formula is

\[
 {N_q\over W}=\prod_{i=1}^{q}{m-i+1\over m+i}.
\tag{1.1}
\]

For \(q=O(m^{1/4})\), Taylor expansion gives

\[
 \begin{aligned}
 \log{N_q\over W}
 &=\sum_{i=1}^{q}
   \left[\log\left(1-{i-1\over m}\right)
       -\log\left(1+{i\over m}\right)\right]\\
 &=-{q^2\over m}+O\left({q^2\over m^2}+{q^4\over m^3}\right).
 \end{aligned}
\tag{1.2}
\]

At \(q=r\), exponentiating (1.2) gives (0.4).  Since

\[
 {K\over B}
 ={m+1\over2m}{N_r\over W}-{\rho\over2mB},
\tag{1.3}
\]

substitution of (0.4) gives the first expansion in (0.5).  The ceiling
in \(r=\lceil m^{1/4}\rceil\) gives

\[
 {r^2\over m}=m^{-1/2}+O(m^{-3/4}),
\tag{1.4}
\]

which gives the second expansion.  In particular,

\[
 {M\over W}=1-{r^2\over m}+{r^4\over2m^2}+O(m^{-3/2})+O(m/W)
            =1-m^{-1/2}+O(m^{-3/4}).
\tag{1.5}
\]

Thus the packet starts use \(W-(1+o(1))W/\sqrt m\) of the middle
baseline, not a fixed Gaussian fraction of it.

For \(q\le H\), the same expansion in logarithmic form is uniform:

\[
 {N_q\over W}
 =\exp\left(-{q^2\over m}
       +O\left({q^2\over m^2}+{q^4\over m^3}\right)\right).
\tag{1.6}
\]

At \(H=\lceil\sqrt{m\log m}\rceil\), (1.6) proves the first part of
(0.13).  The change of variables \(x=q/\sqrt m\), together with
\(r/\sqrt m\to0\), \(H/\sqrt m\to\infty\), gives the Riemann sum in
the second part of (0.13).

The number of physical packet components and their two-sided collar are

\[
 {K\over W/H}=\left({1\over2}+o(1)\right){H\over m}
      =\left({1\over2}+o(1)\right)\sqrt{{\log m\over m}}=o(1),
\tag{1.7}
\]

\[
 2HK={H\over m}M
      =(1+o(1))W\sqrt{{\log m\over m}}=o(W).
\tag{1.8}
\]

Every ordinary coordinate cycle is \(H\)-safe because \(H<m\): the two
uses of any coordinate in its middle Johnson cycle are separated by
exactly \(m\) transitions.  Thus no fixed-Gaussian hypothesis is hidden
in (1.7)--(1.8).

## 2. The exact one-baseline packet ledger

Choose \(K\) ordinary cyclic orders on \([2m]\), each of which supplies
\(2m\) starts.  For one sign and depth \(q\), let \(\mu_q(T)\) be the
target load and put

\[
 E_q=\sum_T(\mu_q(T)-1)_+
     =M-|\operatorname{supp}\mu_q|,
\qquad
 h_q=N_q-|\operatorname{supp}\mu_q|.
\tag{2.1}
\]

The complement of a cyclic interval of length \(m-q\) is a cyclic
interval of length \(m+q\), and cyclic starts are carried bijectively to
cyclic starts.  Hence the lower and upper load multisets are related by
target complementation.  They have exactly the same \(E_q\) and \(h_q\).
For every \(q\), without a sign restriction,

\[
 \boxed{h_q=N_q-M+E_q=N_q-N_r+\rho+E_q.}
\tag{2.2}
\]

Let

\[
 C=M-|\operatorname{supp}\mu_0|
\tag{2.3}
\]

be the middle collision excess.  Compile every packet with its
\(2H\)-letter cyclic collar, append every missing middle target once,
and append every missing signed nonmiddle target once.  The resulting
literal word has the exact scheduled length

\[
             L=W+C+2HK+2\sum_{q=1}^{H}h_q.
\tag{2.4}
\]

For \(q<r\), (2.2) gives (0.6).  Uniform central-binomial expansion and

\[
 \sum_{q=1}^{r-1}(r^2-q^2)
 ={(r-1)r(4r+1)\over6}
\tag{2.5}
\]

give (0.7).  Consequently (2.4) becomes

\[
\begin{aligned}
 L-W={}&C+2HK
 +2\sum_{q=1}^{r-1}(N_q-N_r+\rho)\\
 &+2\sum_{q=1}^{r-1}E_q
 +2\sum_{q=r}^{H}h_q.
\end{aligned}
\tag{2.6}
\]

All terms are nonnegative.  Equations (0.7) and (1.8) therefore prove
the exact one-baseline criterion for this scheduled packet compiler:

\[
 \boxed{
 L=W+o(W)
 \quad\Longleftrightarrow\quad
 C+2\sum_{q<r}E_q+2\sum_{q=r}^{H}h_q=o(W).}
\tag{2.7}
\]

Other, unscheduled intervals crossing packet seams can only add coverage;
thus (2.7) is exact for the displayed scheduled construction and is a
sufficient gate for unrestricted literal coverage.  It is not asserted
as a lower bound against every possible use of all seam-crossing
intervals.

The audited product-SCD exterior applies because
\(H/\sqrt m\to\infty\) and \(H=o(m)\).  Hence (2.7), if proved for one
packet selection, composes into coefficient one.

## 3. Selected reciprocal-\(C_8\) supply and exact action constants

Use \(u=\lfloor\alpha m\rfloor\) pairwise disjoint four-coordinate
slots.  For a Dyck root \(x\), let \(J(x)\) be the eligible reciprocal
slots.  The Catalan deletion bijections give

\[
 \overline z:={1\over B}\sum_x|J(x)|
 =u{2C_{m-2}\over C_m}
 ={\alpha m\over8}+O_\alpha(1),
\tag{3.1}
\]

\[
 {1\over B}\sum_x(|J(x)|-\overline z)^2=O_\alpha(m).
\tag{3.2}
\]

Indeed

\[
 {2C_{m-2}\over C_m}
 ={m(m+1)\over2(2m-1)(2m-3)}={1\over8}+O(m^{-1}),
\tag{3.3}
\]

and the two-slot census \(4C_{m-4}/C_m=1/64+O(m^{-1})\)
gives (3.2).

For every \(K\)-set \(S\), Cauchy--Schwarz gives

\[
 \left|\sum_{x\in S}|J(x)|-K\overline z\right|
 \le\sqrt{K\sum_x(|J(x)|-\overline z)^2}
 =O_\alpha(B\sqrt m).
\tag{3.4}
\]

Now (0.5), (3.1), and \(mB=(1+o(1))W\) prove (0.9).  Notice the
strengthening over the fixed-Gaussian census: because the selected row
density approaches \(1/2\), *every* \(K\)-set sees the same leading
eligible-bit mass.  Choosing unusually active roots changes only the
\(O(W/\sqrt m)\) term.

For a selected root \(x\), choose a local mask \(L_x\subseteq J(x)\),
and put

\[
                         I=\sum_{x\in S}|L_x|.
\tag{3.5}
\]

Each chosen packet is literal: it occurs as row \(x\) in the completed
global factor whose mask is \(L_x\).  Different selected rows need not
belong to one common factor.

### Lemma 3.1 (sharp middle and nonmiddle action)

Let \(\mathcal Q^0(S)\) be the canonical packet family on the same roots,
and \(\mathcal Q^L(S)\) the chosen local variants.  Then

\[
       \boxed{|C(\mathcal Q^L)-C(\mathcal Q^0)|\le2I,}
\tag{3.6}
\]

and for every \(1\le q<m\),

\[
 {1\over2}\|\mu_q^L-\mu_q^0\|_1\le4I,
 \qquad
 \boxed{|E_q^L-E_q^0|=|h_q^L-h_q^0|\le4I.}
\tag{3.7}
\]

The same nonmiddle statement holds for the upper histogram.

#### Proof

In one reciprocal rectangle the two primary nonport tokens \(Q,R\) are
swapped between two fixed-port rows, and every other primary token is
fixed.  For one chosen row, the full middle interval multiset therefore
replaces at most the complementary pair \(\{Q,Q^c\}\) by
\(\{R,R^c\}\).  Its half-\(\ell^1\) action is at most two.  The
support-defect functional is one-Lipschitz in half-\(\ell^1\), proving
(3.6) after telescoping.

At a nonmiddle rank, one active slot performs one adjacent transposition
in each of the two order halves.  One adjacent transposition changes at
most two indexed windows of any proper length.  Thus one bit has
half-\(\ell^1\) action at most four.  Telescope and use the same
one-Lipschitz property to obtain (3.7). \(\square\)

For a common global factor mask there is a sharper structural reading of
(3.6).  Each reciprocal rectangle performs one complement-graph
two-switch, changes its selected induced-edge count by at most one, and
middle collision is twice that induced-edge count.  Hence the factor two
in (3.6) is attained by the elementary switch ledger and is sharp.

Taking \(I\le\sum_{x\in S}|J(x)|\) in Lemma 3.1 proves
(0.10)--(0.12).  It also proves the target-capped annular estimate

\[
 \sum_{q=r}^{H}|h_q^L-h_q^0|
 \le\sum_{q=r}^{H}\min(4I,N_q).
\tag{3.8}
\]

By (0.9), \(4I/W\le\alpha/4+o(1)\).  Apply (1.6) and the same Riemann
sum as in Section 1.  The two curves \(\alpha/4\) and \(e^{-x^2}\)
cross at

\[
 x_\alpha=\sqrt{\log(4/\alpha)}.
\tag{3.9}
\]

This proves (0.14).

## 4. A rigorous all-profile obstruction functional

For a distinct-root \(K\)-set \(S\), let \(C^0(S)\), \(E_q^0(S)\), and
\(h_q^0(S)\) be its canonical middle collision, shallow repeat excess,
and annular holes.  Put

\[
 Z_K=\max_{|S|=K}\sum_{x\in S}|J(x)|
     ={\alpha\over16}W+O_\alpha(W/\sqrt m),
\tag{4.1}
\]

and define

\[
\begin{aligned}
 \mathcal R^{\rm 1B}_{m,\alpha}
 =\min_{|S|=K}\bigg\{&
       (C^0(S)-2Z_K)_+\\
 &+2\sum_{q=1}^{r-1}(E_q^0(S)-4Z_K)_+\\
 &+2\sum_{q=r}^{H}(h_q^0(S)-4Z_K)_+\bigg\}.
\end{aligned}
\tag{4.2}
\]

### Theorem 4.1 (one-baseline hereditary robustness)

If the distinct-root reciprocal-\(C_8\) catalogue contains a packet
family satisfying the one-baseline gate (2.7), then

\[
                    \boxed{\mathcal R^{\rm 1B}_{m,\alpha}=o(W).}
\tag{4.3}
\]

Consequently, \(\mathcal R^{\rm 1B}_{m,\alpha}\not=o(W)\) is a rigorous
statewise no-go for this entire distinct-root catalogue.

#### Proof

For the actual selection, Lemma 3.1 and nonnegativity give

\[
 C^L\ge(C^0-2I)_+,
 \quad E_q^L\ge(E_q^0-4I)_+,
 \quad h_q^L\ge(h_q^0-4I)_+.
\tag{4.4}
\]

Replace \(I\) by the larger \(Z_K\), sum with the coefficients in
(2.7), and minimize over \(S\).  The left side is \(o(W)\) under
(2.7), proving (4.3). \(\square\)

Several explicit necessary margins follow.  Any witness must use one
row set \(S=S_m\) satisfying

\[
 C^0(S)\le\left({\alpha\over8}+o(1)\right)W+o(W),
\tag{4.5}
\]

\[
 \sum_{q<r}
   \left(E_q^0(S)-\left({\alpha\over4}+o(1)\right)W\right)_+
 =o(W),
\tag{4.6}
\]

\[
 \sum_{q=r}^{H}
   \left(h_q^0(S)-\left({\alpha\over4}+o(1)\right)W\right)_+
 =o(W).
\tag{4.7}
\]

Separate row sets minimizing separate depths do not establish these
conditions.  The same \(S\) and the same local packet masks must satisfy
all depths.

The scale contrast is worth recording.  The total shallow target-cell
slack per sign is

\[
 D_{<r}=\sum_{q=1}^{r-1}(N_q-M)
 =\left({2\over3}+o(1)\right){Wr^3\over m}
 =\left({2\over3}+o(1)\right){W\over m^{1/4}},
\tag{4.8}
\]

whereas the full shallow profile has \((1+o(1))Wr\) cells.  Thus an
exact collision-free selection is a packing of density

\[
 1-O(m^{-1/2})
\tag{4.9}
\]

simultaneously in every shallow rank, and the allowed aggregate collision
fraction under (0.8) is \(o(1/r)\).  Root-scale edit mass supplies enough
raw motion to alter a constant fraction of the profile, but says nothing
about the multirank injectivity of the destinations.

## 5. What “shallow SCD-flag coherent” entails

Write a cyclic order as

\[
                    \pi=(a_0,a_1,\ldots,a_{2m-1}),
\]

with subscripts modulo \(2m\), and let

\[
                    M_t=\{a_t,\ldots,a_{t+m-1}\}.
\]

For a cyclic start \(t\), its centered traces form the symmetric chain
segment

\[
 L_{r,t}\subset\cdots\subset L_{1,t}\subset M_t
 \subset U_{1,t}\subset\cdots\subset U_{r,t},
\tag{5.1}
\]

where

\[
 L_{q,t}=\{a_{t+q},\ldots,a_{t+m-1}\},\qquad
 U_{q,t}=\{a_t,\ldots,a_{t+m+q-1}\}.
\tag{5.2}
\]

At a fixed depth these are exactly the cyclic intervals of lengths
\(m-q\) and \(m+q\).  The ordered labels added from \(L_{d,t}\) to
\(U_{d,t}\) are

\[
 w_{d,t}=(a_{t+d-1},a_{t+d-2},\ldots,a_t,
          a_{t+m},a_{t+m+1},\ldots,a_{t+m+d-1}).
\tag{5.3}
\]

There are two different coherence notions.

* **Collision-free shallow flag packing:** \(C=0\) and
  \(E_q=0\) for \(1\le q<r\).  Then the \(M\) segments in (5.1),
  truncated before depth \(r\), are vertex-disjoint at every displayed
  rank.  This need not extend to a prescribed full SCD.
* **SCD-flag coherence:** the segments, through some protected depth
  \(d\ge1\), are the original centered flags of distinct chains of one
  fixed SCD \(\mathcal D\).

The first condition makes the shallow collision term in (2.7) exactly
zero.  Its scalar capacity is compatible with (4.8).  The second has an
additional chronology restriction, but consecutive packet starts are
not rotor neighbours: (5.3) shows directly that shifting \(t\) changes
both ends of the word.  Thus no rotor-cycle or prefix/suffix conclusion
may be inferred merely from cyclicity.

Call an SCD **common-order monotone at depth one** if there is one total
order \(\ell\) of the coordinates such that the two labels added across
the middle of every radius-at-least-one chain occur in increasing
\(\ell\)-order.  The Greene--Kleitman/BTK SCD has this property, and a
coordinate relabelling merely transports \(\ell\).

### Theorem 5.1 (antipodal reversal obstruction)

For every ordinary cyclic packet, at most \(m\) of its \(2m\) centered
start flags can be original flags of one common-order monotone SCD.
Consequently, if a \(K\)-packet family becomes coherent with such an SCD
after discarding \(s\) starts, then

\[
                  \boxed{s\ge mK=M/2.}
\tag{5.4}
\]

In particular neither exact coherence nor coherence outside
\(o(W/H)\) exceptional starts is possible at the scale (0.2).

#### Proof

At depth one, (5.3) becomes

\[
                  w_{1,t}=(a_t,a_{t+m}).
\tag{5.5}
\]

The antipodal start has the reversed word

\[
                  w_{1,t+m}=(a_{t+m},a_t).
\tag{5.6}
\]

Both cannot be increasing in the same total order \(\ell\).  The
\(2m\) starts split into \(m\) disjoint antipodal pairs, so at most one
start per pair can be coherent.  Summing over the \(K\) packets proves
(5.4).  Finally \(M=N_r-\rho=(1-o(1))W\), whereas
\(W/H=o(W)\). \(\square\)

This theorem is independent of the reciprocal-\(C_8\) choices: it is an
invariant of complete ordinary cyclic packets.  It closes the BTK and
all common-order monotone SCD sublanes, but says nothing about a genuinely
nonmonotone SCD.  Collision-free shallow flag packing also remains
strictly weaker than extendability to any full SCD.

## 6. Repeated roots and the sharp scope of the action theorem

The literal packet catalogue is

\[
 \mathscr C_u={(x,L;\pi_x^L):x\in D_m,\ L\subseteq J(x)\}.
\tag{6.1}
\]

A general packet choice may use two distinct variants of the same root.
The estimates (0.9), (4.1), and Theorem 4.1 assume a root transversal:
at most one chosen catalogue entry lies over each \(x\).

For an unrestricted \(K\)-packet catalogue selection, only

\[
                    I\le uK=\left({\alpha\over2}+o(1)\right)W
\tag{6.2}
\]

follows without further multiplicity information.  Thus the near-half
Catalan moment calculation cannot be used as a no-go for the unrestricted
catalogue.

All variants over one root share its two fixed middle port owners.  If
\(r_x\) variants of root \(x\) are selected, then

\[
                         C\ge2(r_x-1).
\tag{6.3}
\]

Consequently exact middle simplicity, and hence exact SCD-flag coherence,
forces \(r_x\le1\) for every root.  In that exact lane Theorem 4.1 loses
no catalogue choices.  On the other hand,

\[
 2\sum_x(r_x-1)_+\le2K=O(W/m)=o(W),
\tag{6.4}
\]

so (6.3) does not exclude repeated roots from the asymptotic
coefficient-one gate (2.7).  A complete no-go for general
\(\mathrm{ECAP}^*\) would have to use the provider union or a
multiplicity-sensitive full-profile Hall cut, not (0.9) alone.

There is, however, a stronger shallow overlap estimate.  Let two variants
over the same root have masks \(L,L'\), and put

\[
                         d=|L\mathbin\triangle L'|\le u.
\tag{6.5}
\]

Their cyclic orders differ by two adjacent transpositions for every bit
in \(L\mathbin\triangle L'\).  At any proper interval length, one
adjacent transposition changes at most two cyclic windows.  Since each
packet support has size \(2m\),

\[
 \boxed{
 |E_{m-q}(\pi_x^L)\cap E_{m-q}(\pi_x^{L'})|
       \ge 2m-4d
       \ge(2-4\alpha)m-O(1)}
 \qquad(0\le q<m).
\tag{6.6}
\]

Let

\[
 R=K-|\{x:r_x>0\}|=\sum_x(r_x-1)_+
\tag{6.7}
\]

be the number of extra variants.  Within each root fibre, expose one
reference variant first.  Every further variant overlaps the already
exposed union in at least the amount in (6.6).  Therefore, uniformly for
every proper depth,

\[
 \boxed{E_q\ge\bigl((2-4\alpha)m-O(1)\bigr)R.}
\tag{6.8}
\]

For fixed \(\alpha<1/2\), exact shallow simplicity gives \(R=0\), while
the aggregate shallow condition in (2.7) gives

\[
 \boxed{R=o\!\left({W\over mr}\right)=o(B/r).}
\tag{6.9}
\]

This closes the repeated-root loophole for *exact* SCD coherence and
shows that it is sparse under approximate shallow coherence.  It does
not justify replacing the exceptional variants while preserving the
annular sum: a replacement can change \(O(m)\) targets at each of
\(H-r+1\) depths, and (6.9) alone does not make that aggregate \(o(W)\).

## 7. Certified boundary

Proved here:

1. the exact moving-entrance expansions (0.4)--(0.5), including the
   floor remainder;
2. the exact one-baseline ledger (2.6) and the harmless
   \((4/3+o(1))Wm^{-1/4}\) compulsory shallow bill;
3. the uniform near-half selected-row incidence census (0.9);
4. the sharp middle \(2I\) and nonmiddle \(4I\) action constants;
5. the all-depth robustness obstruction (4.2)--(4.3);
6. the target-capped annular action constant (0.14);
7. the antipodal-reversal theorem, which linearly obstructs monotone/BTK
   SCD coherence; and
8. the exact distinction between transversal and repeated-root packet
   catalogues.

Not proved here:

1. a distinct-root or repeated-root packet choice satisfying (2.7);
2. a nonmonotone SCD containing the required compatible packet cycles;
3. productive alignment of reciprocal two-switch signs at the middle and
   all shallow/annular ranks; or
4. the constant-one theorem.

The exact remaining positive statement is therefore a full-profile
selection theorem, not another supply estimate: choose literal packet
variants so that their middle collision, total shallow repeat excess, and
total annular holes satisfy (2.7).  Extensive reciprocal-\(C_8\) action
is of the necessary root scale, but only a correlated multirank packing
can turn it into coefficient one.
