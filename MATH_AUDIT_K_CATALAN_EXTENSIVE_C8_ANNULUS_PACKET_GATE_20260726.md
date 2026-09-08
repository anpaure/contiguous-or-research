# Adversarial audit of the extensive reciprocal-\(C_8\) Catalan annulus packet gate

Date: 2026-07-26

Audited file:

\[
 \texttt{MATH\_ATTACK\_K\_CATALAN\_EXTENSIVE\_C8\_ANNULUS\_PACKET\_GATE\_20260726.md}.
\]

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Verdict

The main positive theorem survives. In particular, the passage from a
fixed number of reciprocal-\(C_8\) slots to

\[
 u=\lfloor\alpha m\rfloor,\qquad 0<\alpha<\frac12,
\]

is legitimate; it is not an illicit fixed-\(u\) extrapolation. The
following assertions are correct.

1. Every global mask on the \(u\) disjoint slots is a completed anchored
   exact factor.
2. For every specified set of \(h\) slots, including growing \(h\), the
   common eligible-root count is exactly \(2^hC_{m-2h}\).
3. The first two intersection moments imply
   \(\mathbb E|J|=\alpha m/8+O_\alpha(1)\),
   \(\operatorname {Var}|J|=O_\alpha(m)\), and hence only
   \(O_\alpha(C_m/m)\) roots are inactive.
4. The exact adjacent-order edit mass is
   \(4uC_{m-2}=(\alpha/4+o(1))W\).
5. Infinity cutting gives literal ordinary cyclic packets, the primary
   middle owners partition \(\binom{[2m]}m\), and the cut complement graph
   is loopless and \((m-1)\)-regular.
6. For rows selected from one common factor, \(C_0=2e_G(S)\) exactly.
7. The packet count and compiler collar are correctly normalized:
   \(K_0=(e^{-a^2}/2+o(1))C_m\) and \(2HK_0=o(W)\).
8. Either version of the displayed ECAP conditions is sufficient for a
   literal **fixed-annulus** word of length \(W+o(W)\).

No ECAP selection theorem is proved. The report correctly leaves the
simultaneous middle/trace selection problem open.

There are, however, two corrections which must be made before the stated
boundary is literally sharp.

* The \(\Theta(W)\)-per-depth and
  \(\Theta(W\sqrt m)\)-annulus statements are not proved target action.
  The displayed inequalities prove only \(O(W)\) and
  \(O(W\sqrt m)\) action **capacity**. What is genuinely
  \(\Theta(W)\) is the adjacent-order edit mass.
* The stated rowwise lemma \(\mathrm {ECAP}^{*}\) is sufficient but is not
  the sharp packet-only gate: it permits at most one local variant per
  Dyck root. Literal compilation also permits several different certified
  variants of the same root. This restriction cannot be discarded as
  asymptotically harmless, because the two forced shared ports cost only
  \(O(1)\) collisions per extra variant, and
  \(K_0=\Theta(W/m)=o(W)\).

There are also two scope/wording refinements.

* Root dependence of the displayed formula proves that the construction
  is assembled row-dependently. By itself it does not prove the intrinsic
  nonexistence of some alternative uniform-relabelling representation.
  Unless “row power” has already been defined syntactically, the safe claim
  is “a row-dependent composition of complete sealed layers.”
* ECAP supplies the middle layer plus the fixed Gaussian annulus. It is
  not by itself a complete constant-one theorem for every Boolean rank;
  that further implication requires the separately audited outer-rank
  fusion/reduction.

Finally, the complement-graph action constant in Proposition 3.3 is valid
but eight times weaker than the literal \(C_8\) ledger gives. A single
rectangle is one graph 2-switch and changes \(e_G(S)\) by at most one, so
\(8,8,16\) there may be replaced by \(1,1,2\), respectively.
The scale conclusion is unchanged.

## 1. Normalization and supply against \(N_{q_0}\)

Put

\[
 W=\binom{2m}{m},\qquad B=C_m=\frac{W}{m+1},\qquad
 N_q=\binom{2m}{m-q}.
\]

For fixed \(a>0\) and \(q_0=\lceil a\sqrt m\rceil\),

\[
 \frac{N_{q_0}}W=e^{-a^2}+O_a(m^{-1/2}).
\]

Indeed,

\[
 \log\frac{N_q}{W}
 =\sum_{i=1}^{q}\log\frac{m-i+1}{m+i}
 =-\frac{q^2}{m}+O_a(m^{-1})
\]

uniformly for \(q=O_a(\sqrt m)\); the ceiling contributes the
\(O_a(m^{-1/2})\) final error. Therefore

\[
 K_0=\left\lfloor\frac{N_{q_0}}{2m}\right\rfloor,\qquad
 \frac{K_0}{B}=\frac12e^{-a^2}+o(1).
\]

Since \(a>0\), this density is bounded strictly below \(1/2\).
The extensive all-on factor has

\[
 B-O_\alpha(B/m)
\]

changed rows, so its changed-row supply divided by the demand tends to

\[
 2e^{a^2}>2.
\]

Thus the packet-supply assertion has uniform constant slack.

There are three related but distinct supplies:

\[
\begin{aligned}
 \text{required packet count}&=K_0
       =\left(\frac12e^{-a^2}+o(1)\right)B,\\
 \text{complete local rectangles}&=uC_{m-2}
       =\left(\frac{\alpha}{16}+o(1)\right)W,\\
 \text{active root--slot incidences}&=2uC_{m-2}
       =\left(\frac{\alpha}{8}+o(1)\right)W.
\end{aligned}
\]

The second and third lines are edit resources; they are not counts of
pairwise distinct final packets. The first line is the physical packet
demand.

## 2. Exact legality for \(u=\Theta(m)\)

Choose pairwise disjoint four-bit slots \(I_1,\ldots,I_u\). The
inequality \(\alpha<1/2\) guarantees \(4u\le2m\) for all sufficiently
large \(m\).

At one slot, deletion of either \(1100\) or \(1010\) leaves a Dyck word
of semilength \(m-2\), and insertion at the same gap is inverse.
The positive-height context theorem identifies the two rows as a sealed
affine copy of the reciprocal \(C_8\): the two shores have the same
complete \(X/Y\) ledgers and the same two boundary ports.

For several disjoint slots, delete all marked blocks from right to left.
Their MSW chronology slabs have disjoint interiors and can share only
fixed boundary states. Consequently their local factor replacements
commute. This proof is finite and exact for every
\(u\le\lfloor m/2\rfloor\); it does not invoke an asymptotic whose
constant depends on fixed \(u\). Hence every global mask is a completed
factor even when \(u=\lfloor\alpha m\rfloor\).

For a specified slot set \(T\) of size \(h\), simultaneous deletion and
reinsertion give the bijection

\[
 \{ x\in D_m:T\subseteq J(x)\}
 \longleftrightarrow
 D_{m-2h}\times\{0,1\}^{h}.
\]

Therefore

\[
 \#\{ x:T\subseteq J(x)\}=2^hC_{m-2h}
\]

exactly for every \(0\le h\le u\). This is the required uniform Catalan
intersection statement. In particular, no use of
\(C_{m-2h}/C_m\sim16^{-h}\) for growing \(h\) occurs in the report's
variance proof.

## 3. First two moments and almost-full row support

For \(x\) uniform on \(D_m\), let
\(I_j=\mathbf1_{\{j\in J(x)\}}\). The exact one- and two-slot
probabilities are

\[
 p_m=\frac{2C_{m-2}}{C_m}
 =\frac{m(m+1)}{2(2m-1)(2m-3)}
 =\frac18+O(m^{-1}),
\]

\[
 p_{2,m}=\frac{4C_{m-4}}{C_m}
 =\frac1{64}+O(m^{-1}).
\]

They are independent of the locations or separations of the two disjoint
slots. Thus, uniformly over every allowed deterministic slot atlas,

\[
\begin{aligned}
 \mathbb E|J|&=up_m=\frac{\alpha}{8}m+O_\alpha(1),\\
 \operatorname {Var}|J|
 &=up_m(1-p_m)+u(u-1)(p_{2,m}-p_m^2)
 =O_\alpha(m).
\end{aligned}
\]

The last estimate uses only
\(p_{2,m}-p_m^2=O(m^{-1})\). Chebyshev now gives

\[
 \Pr(J=\varnothing)
 \le\frac{\operatorname {Var}|J|}{(\mathbb E|J|)^2}
 =O_\alpha(m^{-1}).
\]

It also gives

\[
 \Pr\left(|J|<\frac{\alpha m}{17}\right)
 =O_\alpha(m^{-1}),
\]

which justifies the exponential local-variant count on all but
\(O_\alpha(B/m)\) roots.

Every active slot reverses one adjacent pair in each of the two rooted
coordinate-order halves. The pairs belonging to disjoint slots are
disjoint, so they cannot cancel. Hence

\[
 d(x)=2|J(x)|,\qquad
 \sum_{x\in D_m}d(x)
 =2\sum_{j=1}^{u}\#\{x:j\in J(x)\}
 =4uC_{m-2}.
\]

Using

\[
 \frac{C_{m-2}}{C_m}
 =\frac{m(m+1)}{4(2m-1)(2m-3)}
 =\frac1{16}+O(m^{-1}),\qquad
 B=\frac{W}{m+1},
\]

gives

\[
 4uC_{m-2}=\left(\frac\alpha4+o(1)\right)W.
\]

All constants in this part pass.

## 4. Infinity cutting and the primary partition

Let a row coordinate order, rotated at infinity, be

\[
 r_x=(\infty,a_1,\ldots,a_{2m}),\qquad
 \pi_x=(a_1,\ldots,a_{2m}).
\]

The \(m+1\) length-\(m\) intervals of \(r_x\) avoiding
\(\infty\) are

\[
 P_{x,j}=\{a_j,\ldots,a_{j+m-1}\},\qquad1\le j\le m+1.
\]

Exactness of the anchored odd factor and
\((m+1)C_m=W\) prove that these primary owners partition
\(\binom{[2m]}m\).

The \(m-1\) cyclic windows crossing the new cut are exactly
\(P_{x,j}^{c}\), \(2\le j\le m\). The only complementary pair among
one row's primary windows is

\[
 P_{x,1}^{c}=P_{x,m+1}.
\]

It follows that the nonport primary set is complement-closed and that no
complementary nonport pair is owned by one row. Pairing complementary
nonports therefore gives a loopless multigraph \(G_F\) in which every
row has degree \(m-1\).

For selected rows \(S\), primary occurrences are mutually distinct and
extra occurrences are mutually distinct. A collision occurs precisely
when both endpoints of a complement-graph edge lie in \(S\), and then
both members of the complementary target pair are duplicated. Hence

\[
 \left|\bigcup_{x\in S}E_m(\pi_x)\right|
 =2m|S|-2e_{G_F}(S),\qquad
 C_0(S)=2e_{G_F}(S).
\]

The cut form

\[
 C_0(S)=(m-1)|S|-|\delta_{G_F}(S)|
\]

also follows from the degree sum. All normalizations and the factor of
two pass.

The report's statement that the uniform value
\(x_v=K_0/B<1/2\) passes every edge inequality
\(x_u+x_v\le1\) is correct as a basic fractional relaxation. It is
not a fractional stable-set theorem: clique, odd-cycle, or expansion
inequalities may still obstruct a large integral shore. The report does
not claim otherwise.

## 5. Sharpened complement-graph action

The report obtains an eight-edge bound from generic adjacent-window
locality. The literal reciprocal \(C_8\) ledger gives a sharper bound.

### Proposition 5.1 (exact 2-switch bound)

Let \(F'\) be obtained from \(F\) by one sealed reciprocal-\(C_8\)
rectangle, with row vertices identified by their fixed ports. Then only
two nonport primary targets change row owner, and they form one graph
2-switch. Consequently

\[
 \bigl|e_{G_{F'}}(S)-e_{G_F}(S)\bigr|\le1
\]

for every row set \(S\).

#### Proof

In the base rectangle the two old paths and two new paths are

\[
\begin{array}{c|ccc}
1100&12&14&34\\
1010&13&23&24
\end{array}
\qquad\longleftrightarrow\qquad
\begin{array}{c|ccc}
1100&12&23&34\\
1010&13&14&24.
\end{array}
\]

The ports are fixed, and the two internal primary targets \(14\) and
\(23\) exchange row owners. An affine/spectator lift preserves this
description: exactly two internal primary target labels exchange owners.
Call the two rows \(x,y\), the exchanged targets \(Q,R\), and let the
owners of \(Q^c,R^c\) be \(z,w\). If \(Q^c\ne R\), the two graph edges
change as

\[
                         xz,\ yw\longmapsto yz,\ xw.
\]

Writing \(s_v=\mathbf1_{\{v\in S\}}\), the change in the number of
internal edges is

\[
 (s_ys_z+s_xs_w)-(s_xs_z+s_ys_w)
 =(s_y-s_x)(s_z-s_w),
\]

whose absolute value is at most one. If \(Q^c=R\), the unique edge
\(xy\) is unchanged, so the same bound holds. \(\square\)

Therefore a mask containing \(t\) complete layers satisfies

\[
 \bigl|e_{G_{F^A}}(S)-e_{G_F}(S)\bigr|
 \le tC_{m-2},
\]

and the same bound holds after minimizing over \(|S|=K\). Since
\(C_0=2e_G\), the best collision minimum changes by at most

\[
 2tC_{m-2}.
\]

The report's bounds \(8tC_{m-2}\) for \(e_G\) and
\(16tC_{m-2}\) for \(C_0\) are safe, but they are not sharp.
Either set of constants yields the same dichotomy:

\[
 t=o(m)\implies o(W)\text{ possible change},\qquad
 t=\Theta(m)\text{ is the first scale allowing }\Theta(W).
\]

The last statement is a capacity statement conditional on a macroscopic
canonical minimum; it is not an expansion theorem for the canonical cut
graph.

There is a useful selected-shore sharpening. A rectangle contributes
zero to the displayed 2-switch formula unless exactly one of its two row
vertices lies in \(S\). Hence, for a mask \(A\),

\[
 |e_{G_{F^A}}(S)-e_{G_F}(S)|
 \le I_A(S)
 :=\sum_{x\in S}|A\cap J(x)|.
\]

For the all-slot bank and a \(K_0\)-set, \(I_A(S)\le Z_{K_0}\), where
the report's first-two-moment calculation gives

\[
 Z_{K_0}\le
 \left(\frac{\alpha e^{-a^2}}{16}+o(1)\right)W
 =\left(\frac{\alpha}{16}+o(1)\right)N_{q_0}.
\]

Thus middle collision \(C_0=2e_G\) can improve, relative to the
same-root canonical selection, by at most

\[
 2Z_{K_0}
 \le\left(\frac{\alpha}{8}+o(1)\right)N_{q_0}
 <\left(\frac1{16}+o(1)\right)N_{q_0}.
\]

This is sharper than the generic \(4Z_{K_0}\) target-action ceiling at
nonmiddle ranks.

## 6. Edit mass is not target action

An adjacent transposition changes at most two indexed length-\(r\)
windows and hence has histogram transportation action at most two. Thus
the displayed estimates

\[
 \mathsf A(\mu_r^0,\mu_r^1)\le2D_{\rm edit},
\]

\[
 \sum_{q=q_0}^{H}
 \bigl(\mathsf A_{m-q}+\mathsf A_{m+q}\bigr)
 \le4(H-q_0+1)D_{\rm edit}
\]

are correct. With \(u=\lfloor\alpha m\rfloor\), their right
sides are respectively \(O_\alpha(W)\) and
\(O_{\alpha,a,b}(W\sqrt m)\).

No matching lower bound is proved. In fact, at ranks \(1\) and
\(2m-1\) the full catalogue histogram is unchanged by every order
edit. At rank \(m\) there is also a useful exact check: the full cut
catalogue has load one on every port target and load two on every nonport
target. The anchored port set is fixed across the sealed trades, so its
complete rank-\(m\) histogram is invariant even though the ownership
graph changes.

Accordingly the phrases “root-scale action” and “\(\Theta(W)\) raw
action per depth” must mean **edit/action budget**. If they are intended
as statements about \(\mathsf A\), replace them by

\[
 O(W)\text{ per depth},\qquad O(W\sqrt m)\text{ in aggregate}.
\]

The bounded-fringe converse remains correct: if a construction is already
known to reduce one rank's hole count by \(\eta W\), the
one-Lipschitz property forces histogram action at least \(\eta W\),
and hence \(\Lambda\ge\eta W/2\). This is a necessary repair
condition, not evidence that the extensive bank actually realizes the
needed action.

The later selected-row ceiling is also correctly normalized on its stated
domain. For a family

\[
 \{\pi_x^{L_x}:x\in S\},\qquad |S|=K,
\]

with distinct roots, the same-root canonical comparison changes at most
\(4|L_x|\) occurrences at any proper rank. Therefore both the middle
collision defect and a fixed lower-rank hole defect can decrease by at
most \(4Z_K\) under this generic argument. Moreover,

\[
 Z_{K_0}
 \le K_0\frac{\alpha m}{8}
   +\sqrt{K_0\sum_{x\in D_m}(|J(x)|-\overline{|J|})^2}
 =\left(\frac{\alpha e^{-a^2}}{16}+o(1)\right)W.
\]

Thus the reported \(4Z_{K_0}\le(\alpha/4+o(1))N_{q_0}\) and the
\((1/8+o(1))N_{q_0}\) consequence pass for nonmiddle target support.
For middle collision, the local ledger improves \(4Z_{K_0}\) to
\(2Z_{K_0}\): one row-slot change replaces the primary/extra pair
\(\{Q,Q^c\}\) by \(\{R,R^c\}\), so its middle occurrence action is at
most two. This gives the \(<N_{q_0}/16\) ceiling above even for
independently chosen row variants. Proposition 5.1 is the sharper
common-factor graph form of the same cancellation.

This selected-row theorem compares one variant with the canonical packet
of the **same distinct root**. It therefore does not apply unchanged to
the broader sharp catalogue gate in Section 8, where several variants of
one root may be selected. Its phrase “the entire rowwise cube” must be
read as the report's one-variant-per-root rowwise cube.

There is one typographical correction in its Cauchy--Schwarz display:
\(\sqrt{K\sum_x(z_x-\bar z)^2}\) is intended; the source currently omits
the backslash on the square-root command.

## 7. Physical compiler and ECAP sufficiency

Let \(\mathcal Q\) be any \(K_0\) ordinary cyclic packets, and put

\[
 M=2mK_0=N_{q_0}-\rho,\qquad0\le\rho<2m.
\]

Every packet is strongly \(H\)-safe when \(H<m\): the insertion and
deletion uses of a coordinate in the cyclic middle walk are separated
by exactly \(m\) transitions. Its erosion word has length
\(2m+2H\). Hence all packet blocks cost

\[
 M+2HK_0.
\]

If \(C_0\) is their repeated-middle occurrence mass, their middle union
has size \(M-C_0\). Appending all absent middle masks costs

\[
 W-M+C_0.
\]

At depth \(q\), let \(h_q\) be the lower hole count. Packetwise
complementation bijects lower and upper support, so signed repair costs
\(2h_q\). The explicit word therefore has length

\[
 W+C_0+2HK_0+2\sum_{q=q_0}^{H}h_q. \tag{7.1}
\]

For a common factor, \(C_0=2e_{G_F}(S)\), which gives the report's
formula (5.7). Thus common-factor ECAP really is sufficient. There is no
hidden requirement that the chosen rows form overlay components: after a
factor has certified each row, the final compiler uses the rows as
separate ordinary cycles.

Likewise, rows drawn from different completed global masks may be mixed.
Each is already an ordinary cyclic packet, and formula (7.1) depends only
on the final packet multiset. No common exact-factor completion of that
multiset is needed. Thus the report's rowwise relaxation is legitimate.

The most precise wording is that (7.1) is the length of the displayed
packet-plus-repair construction, and hence an upper bound on the optimum.
Accidental witnesses across concatenation seams can only shorten what is
needed.

Finally,

\[
 K_0=\Theta_a(W/m)=o(W/H),\qquad
 2HK_0\le\frac{H}{m}N_{q_0}=O_{a,b}(W/\sqrt m)=o(W).
\]

These constants and the factor of two for the signed annulus pass.

## 8. The sharp rowwise quantifier

For each root \(x\), every local mask \(L\subseteq J(x)\) occurs
as row \(x\) of the completed global factor \(F^L\). Hence define
the row-labelled certified packet catalogue

\[
 \mathscr C_u
 =\{(x,L;\pi_x^L):x\in D_m,\ L\subseteq J(x)\}.
\]

The actual sharp packet-only existence gate for this catalogue is:
choose any \(K_0\)-element packet family \(\mathcal Q_m\) from
\(\mathscr C_u\), allowing two different local masks attached to the
same root, and require

\[
 2mK_0-\left|\bigcup_{\pi\in\mathcal Q_m}E_m(\pi)\right|
 =o(W), \tag{8.1}
\]

\[
 \sum_{q=q_0}^{H}
 \left[
 N_q-\left|\bigcup_{\pi\in\mathcal Q_m}E_{m-q}(\pi)\right|
 \right]=o(W). \tag{8.2}
\]

Repeated copies of the identical cyclic order never improve a union and
are dominated by an unused certified packet; different variants of one
root may not be discarded by that argument.
All variants of one root share its two fixed port owners, but selecting
\(r_x\) variants forces only the elementary lower bound

\[
 C_0\ge2(r_x-1).
\]

Even if a positive fraction of the \(K_0\) packets are extra variants
of previously used roots, this compulsory port collision is only

\[
 O(K_0)=O(W/m)=o(W).
\]

Therefore the one-variant-per-root restriction in the report's stated
\(\mathrm {ECAP}^{*}\) may exclude a valid asymptotic design. The
displayed \(\mathrm {ECAP}^{*}\) remains a clean sufficient lemma,
but “the sharp literal packet gate” should refer to (8.1)--(8.2), not to
the restricted transversal \(\{(x,L_x):x\in S_m\}\).

The provider cut survives this correction. From

\[
 \pi_x^L=h\pi_y^0,\qquad h\in\Gamma_u,\qquad y=hx,
\]

every certified target lies in
\(\Gamma_u\mathcal V_r^0\). Hence every packet family from the
broader catalogue still obeys

\[
 h_q\ge N_q-|\Gamma_u\mathcal V_{m-q}^0|.
\]

The summed provider-union condition remains necessary, but no theorem in
the report evaluates it at Gaussian ranks.

## 9. Exact proved/conditional boundary after audit

The following is proved without a fixed-\(u\) loophole.

* There is a \(2^{\Theta(m)}\)-state family of completed anchored exact
  factors generated by \(\Theta(m)\) disjoint reciprocal-\(C_8\)
  layers.
* Its all-on state has positive-density edit mass and changes all but
  \(O(C_m/m)\) rows.
* It supplies more than the corrected number of ordinary annulus packets.
* Infinity cutting yields the exact regular complement graph and collision
  identity.
* The physical packet/collar overhead is \(o(W)\).
* Common-factor ECAP, the report's restricted rowwise ECAP\(^*\), and
  the broader catalogue gate (8.1)--(8.2) are all literal sufficient
  conditions for a fixed-annulus \(W+o(W)\) word.

The following is not proved.

* No global mask is shown to possess a prescribed-density
  \(o(W)\)-edge shore in its complement graph.
* No common-factor or rowwise packet choice is shown to have
  \(o(W)\) aggregate Gaussian-annulus holes.
* The provider union \(\Gamma_u\mathcal V_{m-q}^0\) is not evaluated at
  \(q=\Theta(\sqrt m)\).
* Root-scale edit mass is not shown to become root-scale productive target
  transport.
* The fixed-annulus implication is not, without the separate outer-scale
  fusion theorem, a complete proof of the global constant-one conjecture.

Subject to the two corrections in Section 0, the report is theorem-level
and its central extensive-\(C_8\) construction is valid.
