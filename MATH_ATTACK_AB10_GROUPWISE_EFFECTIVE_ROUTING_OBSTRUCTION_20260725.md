# AB10: groupwise effective-routing obstruction beyond the AB8 cage

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver,
computer algebra, or numerical experiment is used. Every state below is a
literal integral exact middle wreath factor, and every transition is a cut
of a subset of all freshly recomputed ownership components.

## 0. Verdict

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad B=\operatorname{Cat}_m=\frac Wn,
\qquad H=\lceil A\sqrt m\rceil,
\tag{0.1}
\]

where \(A>0\) is fixed. At depth \(q\), put

\[
N_q=\binom n{m-q},\qquad
c_q=\left\lfloor\frac W{N_q}\right\rfloor,
\qquad b_q=\binom{c_q+1}{2}.
\tag{0.2}
\]

Let \(P_q(F)=\sum_X\binom{\mu_q^F(X)}2\), let
\(P_q^{\min}\) be its exact adjacent-integer minimum at total mass \(W\),
and put

\[
\Phi_q(F)=P_q(F)-P_q^{\min},\qquad
\mathfrak F_A(F)=\sum_{q=1}^H\frac{\Phi_q(F)}{b_q}.
\tag{0.3}
\]

Fix an AB8 colour

\[
2\le s\le m-H-2.
\tag{0.4}
\]

Its private family consists of

\[
L=\operatorname{Cat}_{m-s-H-2}
\tag{0.5}
\]

pairwise disjoint target pairs \(\{S_V,T_V\}\), each carrying at least

\[
T=\operatorname{Cat}_H
\tag{0.6}
\]

occurrence tokens at the AB8 cage factor. An arbitrary history in the
protected menu preserves every one of these pair totals. Start a suffix at
any endpoint \(F_-\) of such a protected-menu history and select exactly
\(T\) labelled occurrence tokens from each private pair.

Consider any subsequent realized adaptive history of arbitrary
transposition-component cuts. For a private group \(V\), let \(p_V\) be
the number of suffix stages at which the chosen complete component cut acts
by the identity on at least one current token of group \(V\) and by the
current transposition on at least one other current token of the same group.
Thus a stage is counted for \(V\) only when the freshly recomputed component
signing genuinely branches that group. Empty cuts, full global relabellings,
and proper cuts which act coherently on the whole group do not count.

The main exact inequality is

\[
\boxed{
\Phi_H(F_{\rm end})
\ge
\frac{T^2}{4}\sum_{V=1}^{L}2^{-p_V}
-\frac{LT}{2}-P_H^{\min}.}
\tag{0.7}
\]

Consequently, if \(\mathfrak F_A(F_{\rm end})\le C W\), then

\[
\boxed{
\frac1L\sum_{V=1}^{L}2^{-p_V}
\le
\frac{4K_A(C+1)W}{LT^2}+\frac2T
<
\frac{1024K_A(C+1)nH^4}{4^{H-s}}
+\frac{8H^2}{4^H},}
\tag{0.8}
\]

where

\[
K_A=
\binom{\left\lceil e^{2(A+1)(A+2)}\right\rceil+1}{2}.
\tag{0.9}
\]

For every integer \(r\ge0\), this yields the quantified reduced-routing
no-go

\[
\boxed{
\frac1L\#\{V:p_V\le r\}
\le
2^r\left(
\frac{1024K_A(C+1)nH^4}{4^{H-s}}
+\frac{8H^2}{4^H}
\right).}
\tag{0.10}
\]

In particular, suppose \(H-s=\Theta_A(H)\). For every fixed
\(\delta>0\), every endpoint with \(\mathfrak F_A\le CW\) satisfies

\[
\boxed{
p_V>(2-\delta)(H-s)-1}
\tag{0.11}
\]

for all but \(o_{A,C,\delta}(L)\) private groups. At the balanced cage
\(s=\lfloor H/2\rfloor\), this reads

\[
\boxed{p_V>(1-\delta/2)H-O(1)}
\tag{0.12}
\]

for all but \(o(L)\) groups.

Thus the AB8 cut-depth obstruction is not merely a global support-capacity
statement. Any \(O(H)\)-step outside-menu bypass must make nearly every one
of the Catalan-many protected groups receive both component signs in nearly
every useful stage. A connected overlay branches no group. More generally,
a giant component containing all current tokens of a group makes that stage
useless for the group, even if the cut is proper elsewhere.

This is a strict sharpening of the token-support lower bound and an exact
conflict obstruction to capacity-only binary routing. It does not prove that
the simultaneous branching pattern in (0.11) is impossible for genuine
wreath chronology, and it does not construct a descending endpoint.
Accordingly, no MWB or constant-one claim is made.

## 1. Literal token transport

Let

\[
F_-=F_0\longrightarrow F_1\longrightarrow\cdots
\longrightarrow F_D=F_{\rm end}
\tag{1.1}
\]

be the realized suffix. At stage \(j\), let \(\sigma_j\) be the chosen
transposition and let \(\mathcal I_j\) be the chosen subset of all
freshly recomputed \(\sigma_j\)-components.

Every old row belongs to one ownership component. On an unswitched
component it is carried by the identity, and on a switched component it is
carried by \(\sigma_j\). These row maps form a bijection from \(F_{j-1}\)
to \(F_j\). Hence every labelled cyclic-interval occurrence token \(\omega\)
has a well-defined action bit

\[
a_j(\omega)=
\begin{cases}
0,&\text{its current owner component is not in }\mathcal I_j,\\
1,&\text{its current owner component is in }\mathcal I_j,
\end{cases}
\tag{1.2}
\]

and its target changes by

\[
X_j(\omega)=\sigma_j^{a_j(\omega)}X_{j-1}(\omega).
\tag{1.3}
\]

Occurrence tokens remain distinct throughout the history because every
stage is a row bijection and coordinate relabelling preserves the marked
cyclic position.

For a private group \(\Omega_V\) of \(T\) selected tokens, define

\[
b_{j,V}=
\begin{cases}
1,&\{a_j(\omega):\omega\in\Omega_V\}=\{0,1\},\\
0,&\text{otherwise},
\end{cases}
\qquad
p_V=\sum_{j=1}^D b_{j,V}.
\tag{1.4}
\]

The definition uses the actual current components and the actual selected
component subset. It is therefore pathwise and remains valid for adaptive,
randomized, or history-dependent schedules after conditioning on the
realized path.

### Lemma 1.1 (groupwise support grows only at genuine branch stages)

At the endpoint, group \(V\) is supported on at most

\[
\boxed{2^{p_V+1}}
\tag{1.5}
\]

depth-\(H\) targets.

#### Proof

At \(F_-\), every selected token of group \(V\) lies on one of the two
private targets \(S_V,T_V\), so the initial support has size at most two.

If \(b_{j,V}=0\), then \(a_j\) is constant on the group. Equation (1.3)
applies either the identity to every current group target or \(\sigma_j\)
to every current group target. Since either map is a bijection, the group
support cardinality does not change.

If \(b_{j,V}=1\), every new group target lies in

\[
\operatorname{supp}_{j-1}(V)
\cup\sigma_j\operatorname{supp}_{j-1}(V),
\]

whose cardinality is at most twice the old cardinality. Induction proves
(1.5). \(\square\)

The lemma makes the distinction missed by a total cut count. A proper cut
can branch none, some, or all of the private groups. Conversely, a full cut
is a global coordinate relabelling and has \(b_{j,V}=0\) for every \(V\).

## 2. Exact factorial collision inequality

For a fixed private group \(V\), let \(u_{V,X}\) be the number of its
selected tokens ending at target \(X\). Then

\[
\sum_Xu_{V,X}=T,
\qquad
\#\{X:u_{V,X}>0\}\le2^{p_V+1}.
\tag{2.1}
\]

By Cauchy--Schwarz,

\[
\sum_Xu_{V,X}^2
\ge\frac{T^2}{2^{p_V+1}}.
\tag{2.2}
\]

Therefore the number of colliding unordered selected-token pairs internal
to group \(V\) is at least

\[
\sum_X\binom{u_{V,X}}2
\ge
\frac{T^2}{2^{p_V+2}}-\frac T2.
\tag{2.3}
\]

The labelled token groups are disjoint. Hence the unordered token pairs
counted for two different groups are disjoint, even if the groups land on
the same endpoint target. Unselected occurrences and collisions between
different groups only add nonnegative terms. Thus

\[
P_H(F_{\rm end})
\ge
\sum_{V=1}^{L}
\left(\frac{T^2}{2^{p_V+2}}-\frac T2\right).
\tag{2.4}
\]

Subtracting the exact adjacent-integer floor \(P_H^{\min}\) gives (0.7).
No fractional variance baseline has been substituted.

## 3. Quantified low-energy consequence

Assume

\[
\mathfrak F_A(F_{\rm end})\le CW.
\tag{3.1}
\]

Every \(\Phi_q\) is nonnegative, so its depth-\(H\) summand gives

\[
\Phi_H(F_{\rm end})\le b_HCW.
\tag{3.2}
\]

Combining (0.7) and (3.2) yields

\[
\sum_V2^{-p_V}
\le
\frac4{T^2}
\left(b_HCW+\frac{LT}{2}+P_H^{\min}\right).
\tag{3.3}
\]

The fixed-window floor estimates are

\[
b_H\le K_A,
\qquad
P_H^{\min}\le N_Hb_H\le Wb_H.
\tag{3.4}
\]

Divide (3.3) by \(L\) and use (3.4). This gives the first inequality in
(0.8):

\[
\frac1L\sum_V2^{-p_V}
\le
\frac{4K_A(C+1)W}{LT^2}+\frac2T.
\tag{3.5}
\]

For \(H\ge2\),

\[
T=\operatorname{Cat}_H
\ge\frac{4^H}{4H^2}.
\tag{3.6}
\]

Every successive Catalan ratio is less than four, so

\[
L=\operatorname{Cat}_{m-s-H-2}
>\frac{\operatorname{Cat}_m}{4^{s+H+2}}
=\frac W{n4^{s+H+2}}.
\tag{3.7}
\]

Consequently

\[
LT^2>
\frac{W4^{H-s}}{256nH^4}.
\tag{3.8}
\]

Substitution of (3.6)--(3.8) into (3.5) proves the second inequality in
(0.8).

If \(p_V\le r\), then \(2^{-p_V}\ge2^{-r}\). Therefore

\[
2^{-r}\#\{V:p_V\le r\}
\le\sum_V2^{-p_V}.
\tag{3.9}
\]

Equations (0.8) and (3.9) prove (0.10).

Now put \(d=H-s\), assume \(d=\Theta_A(H)\), and take

\[
r=\left\lceil(2-\delta)d\right\rceil-1.
\tag{3.10}
\]

Then \(r<(2-\delta)d\), and the right side of (0.10) is at most

\[
1024K_A(C+1)nH^4\,2^{-\delta d}
+8H^2\,2^{-2s-\delta d+1}.
\tag{3.11}
\]

Because \(H=\Theta_A(\sqrt m)\), the exponential factor
\(2^{-\delta d}\) dominates the polynomial \(nH^4\). Thus (3.11) tends
to zero. This proves (0.11), and \(s=\lfloor H/2\rfloor\) gives (0.12).

## 4. Relation to the floor-corrected energy

The usual floor-corrected quadratic energy is

\[
\mathcal Q_H(F)=\sum_{q=1}^H\frac{Q_q(F)}{c_q},
\qquad Q_q(F)=2\Phi_q(F).
\tag{4.1}
\]

Since

\[
b_q=\frac{c_q(c_q+1)}2,
\]

one has termwise

\[
\frac{\Phi_q(F)}{b_q}
=\frac{Q_q(F)}{c_q(c_q+1)}
\le\frac{Q_q(F)}{c_q}.
\tag{4.2}
\]

Hence

\[
\mathfrak F_A(F)\le\mathcal Q_H(F).
\tag{4.3}
\]

In particular, an endpoint at the desired fixed-window scale

\[
\mathcal Q_H(F_{\rm end})\le C_AH\operatorname{Cat}_m
=C_A\frac HnW
\tag{4.4}
\]

satisfies \(\mathfrak F_A(F_{\rm end})\le W\) for all sufficiently large
\(m\). Thus (0.10)--(0.12) apply with \(C=1\) to every prospective
constant-one bypass endpoint.

## 5. The exact surviving chronology statement

For the balanced AB8 cage, a successful \(D=O_A(H)\) suffix must satisfy

\[
\sum_{V=1}^{L}p_V\ge(1-o_A(1))LH.
\tag{5.1}
\]

Equivalently, if

\[
\mathcal B_j
=\{V:\text{stage }j\text{ gives both component signs to group }V\},
\tag{5.2}
\]

then

\[
\boxed{
\sum_{j=1}^{D}|\mathcal B_j|
\ge(1-o_A(1))LH.}
\tag{5.3}
\]

This is the exact simultaneous-routing burden. For example, if
\(D\le(1+o(1))H\), then the average useful stage must branch
\((1-o(1))L\) private groups.

The giant-shield obstruction is relevant precisely here: whenever all
current tokens of \(V\) are contained in one ownership component, no
signing of that overlay can put \(V\) in \(\mathcal B_j\). However, the
present theorem does not identify the private AB8 token groups with the
high-harmonic component mass in the giant-shield theorem. Establishing that
no-recycling incidence estimate, or constructing a literal history meeting
(5.3), remains the genuine chronology fork.

Therefore the proved boundary is:

\[
\boxed{
\begin{gathered}
\text{support capacity and }O(H)\text{ distinct labels are insufficient;}\\
\text{near-total groupwise component fragmentation in near-every round is
necessary;}\\
\text{its impossibility or realization in exact wreath chronology remains open.}
\end{gathered}}
\tag{5.4}
\]

No constant-one conclusion follows from this report alone.
