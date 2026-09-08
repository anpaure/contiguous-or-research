# Dense orbit packing and simultaneous signing of the three-top promotion conveyor

Date: 2026-07-27

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad W=\binom{2m}{m},
 \qquad N_q=\binom{2m}{m-q},
\tag{0.1}
\]

and assume

\[
 2\le H,\qquad M\ge 8H,\qquad H=o(m).
\tag{0.2}
\]

Start with the three-top, two-base conveyor of
`MATH_THEOREM_THREE_TOP_TWO_BASE_PROMOTION_CONVEYOR_20260726.md`.
Let

\[
 R_H=\frac{W}{N_H},\qquad
 S_2(H)=\sum_{q=1}^Hq^2
       =\frac{H(H+1)(2H+1)}6,
\tag{0.3}
\]

and define the explicit polynomial-loss parameter

\[
 \boxed{
 P_H=9M^2+\bigl(9+256S_2(H)\bigr)R_H.}
\tag{0.4}
\]

There is a coordinate-conjugate family of at least \(W/P_H\)
three-top packets such that distinct packets have

1. no common rank-\(M\) top;
2. no common middle owner; and
3. no common changed target at any depth \(1\le q\le H\).

The upper root-form changed targets are global complements of the lower
direct changed targets, so item 3 holds simultaneously in both physical
descriptions.  This is an integral packing theorem, not fractional orbit
averaging.

Moreover, whenever the all-zero packet reservoir together with a
nonnegative integral background has total mass at most \(W\) in each protected
ledger, one may freeze some packets and retain

\[
 \boxed{K=\left\lfloor\frac{W}{2P_H}\right\rfloor}
\tag{0.5}
\]

independently switchable packets.  Their shores admit one common signing
for which every one of the at most \(2H\) nonzero direct/root floor-energy
increments has absolute value at most

\[
 \boxed{8H\sqrt{P_HW}.}
\tag{0.6}
\]

After globally reversing the signing if necessary, any prescribed
nonnegative weighted sum of those increments is nonpositive.  Thus the
weighted aggregate is genuinely favorable, while the sum of all positive
depthwise increments is at most

\[
 16H^2\sqrt{P_HW}.
\tag{0.7}
\]

If \(H\le A\sqrt{m\log m}\), with fixed \(A\), then

\[
 R_H\le \exp\!\left(\frac{H^2}{m-H+1}\right)
       \le m^{A^2+o(1)},
\tag{0.8}
\]

and hence

\[
 P_H\le m^{\max\{2,A^2+3/2\}+o(1)},\qquad
 K\ge Wm^{-\max\{2,A^2+3/2\}-o(1)}.
\tag{0.9}
\]

In particular, \(K=\Omega(W/\operatorname{poly}(m))\), (0.7) is
\(o(W)\), and the literal changed-target support over all depths is also
\(o(W)\).  The theorem therefore proves the requested dense
middle-disjoint packing and a simultaneous favorable signing up to
\(o(W)\) floor leakage.  It does not prove a negative increment in every
individual ledger, nor does it complete the unused middle owners to a
global exact factor.

## 1. The packet resources

Fix one labelled copy \(P\) of the three-top conveyor.  It has two shores,
denoted \(P^0,P^1\).  Write

\[
 \mathcal U(P)\subseteq\binom{[n]}M
\tag{1.1}
\]

for its three touched tops and

\[
 \mathcal O(P)\subseteq\binom{[n]}m
\tag{1.2}
\]

for its common middle support.  The exact-middle and squarefreeness theorem
for the conveyor gives

\[
 |\mathcal U(P)|=3,\qquad |\mathcal O(P)|=3M.
\tag{1.3}
\]

At depth \(q\), let

\[
 \Delta_q(P)=\Gamma_q^1(P)-\Gamma_q^0(P)
\tag{1.4}
\]

be the nonzero direct rank-\((m-q)\) derivative, and put

\[
 \mathcal D_q(P)=\operatorname{supp}\Delta_q(P).
\tag{1.5}
\]

The local theorem gives, exactly,

\[
 |\mathcal D_q(P)|=16q,\qquad
 \Delta_q(P)(T)\in\{+1,-1\}\quad(T\in\mathcal D_q(P)).
\tag{1.6}
\]

It has \(8q\) coefficients of either sign and

\[
 \|\Delta_q(P)\|_2^2=16q.
\tag{1.7}
\]

Global complementation maps this support bijectively to the nonzero
root-form rank-\((m+q)\) support.  The opposite direct/root derivatives
are zero.  Therefore disjointness of the sets in (1.5) implies
disjointness in every nonzero physical protected ledger.

For \(g\in\mathfrak S_n\), let \(gP\) be the literal packet obtained by
applying \(g\) to every label, frame and target.  We use the indexed orbit

\[
 \mathscr E=(gP:g\in\mathfrak S_n).
\tag{1.8}
\]

Keeping stabilizer repetitions in this indexed family is convenient and
does not weaken an integral matching: two repetitions have all resources
in common and hence cannot both be selected.

## 2. A transitive-orbit matching lemma

We record the elementary form needed here.

### Lemma 2.1 (multi-layer orbit packing)

Let a finite group \(G\) act transitively on each of the finite sets
\(V_1,\ldots,V_s\).  Suppose an indexed object \(gE\), \(g\in G\), uses
exactly \(r_j\) distinct vertices in \(V_j\).  Then there is a family of
objects, pairwise disjoint in every layer, of cardinality at least

\[
 \left(\sum_{j=1}^s\frac{r_j^2}{|V_j|}\right)^{-1}.
\tag{2.1}
\]

#### Proof

For a fixed \(v\in V_j\), transitivity and double counting show that the
number of indexed objects using (v) is

\[
 d_j=\frac{|G|r_j}{|V_j|}.
\tag{2.2}
\]

A fixed object therefore meets at most

\[
 r_jd_j=|G|\frac{r_j^2}{|V_j|}
\tag{2.3}
\]

indexed objects in layer (j).  Greedily select one object and delete all
objects meeting it in any layer.  Each selection deletes at most

\[
 |G|\sum_j\frac{r_j^2}{|V_j|}
\tag{2.4}
\]

indexed objects.  Exhausting all \(|G|\) objects proves (2.1).  Every pair
of selected indexed objects is resource-disjoint, so stabilizer
repetitions cause no ambiguity. \(\square\)

### Theorem 2.2 (dense conveyor packing)

The orbit (1.8) contains a family \(\mathscr M\) with

\[
 |\mathscr M|\ge \frac{W}{P_H}
\tag{2.5}
\]

whose packets are pairwise top-disjoint, middle-owner-disjoint and
changed-target-disjoint at every \(1\le q\le H\).

#### Proof

Apply Lemma 2.1 to the following transitive layers:

\[
\begin{array}{c|c|c}
\text{layer}&\text{universe size}&\text{packet size}\\ \hline
\text{rank-}M\text{ tops}&N_H&3\\
\text{middle owners}&W&3M\\
\text{changed targets at depth }q&N_q&16q.
\end{array}
\tag{2.6}
\]

The resulting conflict density is

\[
 D=\frac9{N_H}+\frac{9M^2}{W}
       +256\sum_{q=1}^H\frac{q^2}{N_q}.
\tag{2.7}
\]

Since \(N_q\ge N_H\) for \(q\le H\),

\[
 D\le \frac{9M^2}{W}
       +\frac{9+256S_2(H)}{N_H}
   =\frac{P_H}{W}.
\tag{2.8}
\]

Lemma 2.1 now gives (2.5).  Complementation carries disjoint lower
supports to disjoint upper supports, so all nonzero direct/root ledgers
are covered. \(\square\)

### Corollary 2.3 (exact resource ledger)

Any \(K\)-packet subfamily of \(\mathscr M\) has:

\[
 \begin{array}{rcl}
 \text{distinct touched tops}&=&3K,\\[2mm]
 \text{common middle owners on either shore}&=&3MK,\\[2mm]
 |\operatorname{supp}\sum_P\epsilon_P\Delta_q(P)|&=&16qK,\\[2mm]
 \|\sum_P\epsilon_P\Delta_q(P)\|_2^2&=&16qK
 \end{array}
\tag{2.9}
\]

for every signing \(\epsilon_P\in\{\pm1\}\) and every \(q\).  Consequently
one nonzero physical side has total changed support

\[
 16K\sum_{q=1}^Hq=8H(H+1)K.
\tag{2.10}
\]

Counting both complementary direct/root realizations doubles (2.10).
There is no hidden target collision in these equalities.

## 3. Why disjoint derivatives make the floor energy affine

Fix one protected ledger \(\alpha\).  It may be the direct lower ledger or
the complementary root upper ledger at some depth \(q\).  Let

\[
 \Gamma_{i,\alpha}^0,\quad \Gamma_{i,\alpha}^1,
 \quad \Delta_{i,\alpha}=\Gamma_{i,\alpha}^1-\Gamma_{i,\alpha}^0
\tag{3.1}
\]

be the two packet loads and their derivative.  The supports of the
derivatives are pairwise disjoint.  Let \(R_\alpha\ge0\) be an arbitrary
integral fixed background and take the all-zero endpoint

\[
 L_\alpha^0=R_\alpha+\sum_i\Gamma_{i,\alpha}^0.
\tag{3.2}
\]

We require only the physical mass bound

\[
 \|L_\alpha^0\|_1\le W.
\tag{3.3}
\]

For a literal partial owner resolution, the background is additionally
required to avoid the \(3M|\mathscr M|\) middle owners and the
\(3|\mathscr M|\) top variables used by the reservoir.  This is exactly
the ordinary legality condition for adjoining the packets; it is not
needed for the numerical floor identity below.

The mass hypothesis is the physical one: three complete cyclic frames
contribute \(3M\) targets in every rank ledger.  Since the reservoir is
middle-owner-disjoint, \(3M|\mathscr M|\le W\).  Thus the reservoir by
itself satisfies (3.3), and a complete ambient resolution would satisfy
(3.3) with equality.

For an integer floor \(c_\alpha\), set

\[
 \Phi_{c_\alpha}(L)
 =\frac12\sum_T(L_T-c_\alpha)(L_T-c_\alpha-1).
\tag{3.4}
\]

For \(x\in\{0,1\}^{\mathscr M}\), put

\[
 L_\alpha(x)=L_\alpha^0+\sum_ix_i\Delta_{i,\alpha}.
\tag{3.5}
\]

Because every derivative has coordinate sum zero and distinct packet
derivatives have disjoint supports, direct expansion gives the exact
affine identity

\[
 \boxed{
 \Phi_{c_\alpha}(L_\alpha(x))
 -\Phi_{c_\alpha}(L_\alpha^0)
 =\sum_ix_i A_{i,\alpha},}
\tag{3.6}
\]

where

\[
 A_{i,\alpha}
 =\langle L_\alpha^0,\Delta_{i,\alpha}\rangle
   +\frac12\|\Delta_{i,\alpha}\|_2^2.
\tag{3.7}
\]

Thus no cross-packet restitution survives.  Notice that full shallow
carriers may overlap; disjointness of the derivatives, rather than
disjointness of both endpoint loads, is exactly what (3.6) needs.

For a depth-\(q\) nonzero ledger, (1.6), (3.3), and disjoint derivative
supports imply

\[
\begin{aligned}
 \sum_i|A_{i,\alpha}|
 &\le
 \sum_i|\langle L_\alpha^0,\Delta_{i,\alpha}\rangle|
 +\frac12\sum_i\|\Delta_{i,\alpha}\|_2^2\\
 &\le W+8q|\mathscr M|.
\end{aligned}
\tag{3.8}
\]

Middle-owner disjointness gives

\[
 3M|\mathscr M|\le W.
\tag{3.9}
\]

Since \(M\ge8H\), equations (3.8)--(3.9) yield the convenient uniform
bound

\[
 \boxed{\sum_i|A_{i,\alpha}|\le2W.}
\tag{3.10}
\]

The zero direct/root ledgers have \(A_{i,\alpha}=0\) and require no
separate treatment.

## 4. Simultaneous truncation and signing

There are at most \(L=2H\) nonzero physical floor functionals: direct
lower and root upper for \(q=1,\ldots,H\).  They may have unrelated
ambient loads, so both are retained in the argument.

Start with the family \(\mathscr M\) from Theorem 2.2.  In every ledger
discard from the switchable set every packet satisfying

\[
 |A_{i,\alpha}|>T,\qquad T=16HP_H.
\tag{4.1}
\]

The discarded packets may be kept frozen on shore zero; their loads are
then simply part of the fixed background in (3.2).  By (3.10), at most

\[
 \frac{2W}{T}=\frac{W}{8HP_H}
\tag{4.2}
\]

packets are discarded by one ledger.  Across at most \(2H\) ledgers, at
most \(W/(4P_H)\) packets are discarded.  Since

\[
 |\mathscr M|\ge W/P_H,
\tag{4.3}
\]

there remain at least \(3W/(4P_H)\) packets.  For all sufficiently large
\(m\), choose a retained set \(\mathscr K\) of the cardinality \(K\) in
(0.5).

Choose independent fair signs \(\epsilon_i\in\{\pm1\}\), \(i\in\mathscr K\),
and put

\[
 Z_\alpha=\sum_{i\in\mathscr K}\epsilon_iA_{i,\alpha}.
\tag{4.4}
\]

Using (3.10) and (4.1),

\[
\begin{aligned}
 \mathbb E\sum_\alpha Z_\alpha^2
 &=\sum_\alpha\sum_{i\in\mathscr K}A_{i,\alpha}^2\\
 &\le\sum_\alpha T\sum_{i\in\mathscr K}|A_{i,\alpha}|\\
 &\le (2H)T(2W)=64H^2P_HW.
\end{aligned}
\tag{4.5}
\]

Therefore one deterministic signing satisfies

\[
 \sum_\alpha Z_\alpha^2\le64H^2P_HW,
 \qquad
 |Z_\alpha|\le8H\sqrt{P_HW}\quad\text{for every }\alpha.
\tag{4.6}
\]

Let \(x_i=(1+\epsilon_i)/2\) for \(i\in\mathscr K\).  Define two state
vectors \(x^{(0)},x^{(1)}\in\{0,1\}^{\mathscr M}\) by

\[
 x_i^{(0)}=x_i,\qquad x_i^{(1)}=1-x_i
       \quad(i\in\mathscr K),\qquad
 x_i^{(0)}=x_i^{(1)}=0
       \quad(i\notin\mathscr K).
\tag{4.7}
\]

Thus every discarded packet stays frozen on shore zero in both endpoints.
Equation (3.6) gives

\[
 \Phi_{c_\alpha}(L_\alpha(x^{(1)}))
 -\Phi_{c_\alpha}(L_\alpha(x^{(0)}))=-Z_\alpha.
\tag{4.8}
\]

Both endpoints in (4.8) are literal integral frame systems.  Indeed,
every coordinate \(x_i^{(s)}\) chooses one entire three-frame shore, the
packets use distinct top variables, and every shore has the same
squarefree \(3M\)-element middle support.  Those middle supports are
disjoint between packets.  If the background obeys the avoidance
condition after (3.3), adjoining it preserves both top legality and
middle ownership.  No convex combination or fractional packet is used.

Thus (4.6) is the claimed simultaneous floor bound.  Given arbitrary
nonnegative weights \(w_\alpha\), globally interchange the two endpoints
if necessary.  This replaces every \(Z_\alpha\) by \(-Z_\alpha\), so one
orientation satisfies

\[
 \sum_\alpha w_\alpha
 \bigl(\Phi_{c_\alpha}(L_\alpha(x^{(1)}))
      -\Phi_{c_\alpha}(L_\alpha(x^{(0)}))\bigr)\le0.
\tag{4.9}
\]

At the same time, the sum of the positive unweighted increments is at
most

\[
 (2H)\,8H\sqrt{P_HW}=16H^2\sqrt{P_HW},
\tag{4.10}
\]

which proves (0.7).

## 5. Exact asymptotic accounting

The central-to-height ratio has the exact product form

\[
 R_H=\prod_{i=1}^H\frac{m+i}{m-i+1}.
\tag{5.1}
\]

Since

\[
 \log\frac{m+i}{m-i+1}
 =\log\left(1+\frac{2i-1}{m-i+1}\right)
 \le\frac{2i-1}{m-H+1},
\tag{5.2}
\]

summing (5.2) proves

\[
 R_H\le\exp\left(\frac{H^2}{m-H+1}\right).
\tag{5.3}
\]

For \(H\le A\sqrt{m\log m}\), this is at most \(m^{A^2+o(1)}\).
Since \(S_2(H)=O(H^3)\) and \(M=\Theta(m)\), (0.4) gives the upper
bound for \(P_H\) in (0.9), and (0.5) gives the stated lower bound for
\(K\).

If more precisely
\[
 H=(A+o(1))\sqrt{m\log m},
\tag{5.4}
\]
then expansion of (5.1) gives
\[
 \log R_H=\frac{H^2}{m}+O\!\left(\frac{H^3}{m^2}
                                 +\frac{H}{m}\right)
          =(A^2+o(1))\log m.
\tag{5.5}
\]
Consequently the exact calibrated asymptotics are
\[
 P_H=m^{\max\{2,A^2+3/2\}+o(1)},\qquad
 K=Wm^{-\max\{2,A^2+3/2\}+o(1)}.
\tag{5.6}
\]

The active family has exactly \(3K\) distinct tops and exactly \(3MK\)
distinct middle owners.  Its changed support in one physical description
is, by (2.10),

\[
 8H(H+1)K
 \le \frac{4H(H+1)}{P_H}W
 \le \frac{4H(H+1)}{9M^2}W=o(W).
\tag{5.7}
\]

Counting both complementary descriptions merely doubles this bound.  The
floor leakage (4.10) obeys

\[
 \frac{16H^2\sqrt{P_HW}}W
 =16\sqrt{\frac{H^4P_H}{W}}=o(1),
\tag{5.8}
\]

because \(H^4P_H\) is polynomial in \(m\), whereas \(W\) is
exponential.  This proves all asserted \(o(W)\) statements with no
omitted factor of \(H\), \(M\), or \(R_H\).

## 6. Precise boundary

Proved:

1. an integral orbit packing of \(W/P_H\) actual three-top packets;
2. pairwise disjoint tops, middle owners and changed targets at every
   protected depth;
3. exact packet, owner, top, action-support and squared-norm counts;
4. exact affine decoupling of their floor energies;
5. one common all-depth signing with \(o(W)\) positive floor leakage; and
6. a favorable orientation for every prescribed nonnegative aggregate
   of the protected floor energies.

Not proved:

1. strict descent separately in every protected ledger;
2. extension of the packed partial owner resolution to all \(W\) middle
   owners;
3. the presence of this reservoir inside an arbitrary preassigned exact
   factor; or
4. coefficient one.

The remaining gate is no longer local packet availability or common
signing on a polynomially dense reservoir.  It is completion/absorption:
embed such a reservoir into a global exact owner resolution while
retaining enough external gradient to turn the \(o(W)\) one-ledger
leakage into strict simultaneous descent or an \(o(W)\) final defect.
