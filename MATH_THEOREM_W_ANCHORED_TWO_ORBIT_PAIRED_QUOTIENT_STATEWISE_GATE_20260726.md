# Anchored promotion rings: paired quotient histories, exact collar flux, and the statewise two-orbit obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},
 \qquad \lambda_q={W\over N_q},
\]

and choose the covering-side radius

\[
 H=\max\{0\le h<m:\lambda_h\le m+h\},\qquad
 M=m+H,\qquad N=N_H.
\tag{0.1}
\]

Then

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 T:=MN=W+E,\qquad
 0\le E=O(WH/m)=o(W),
\tag{0.2}
\]

\[
 N=(1+o(1)){W\over m}=o(W/H).
\tag{0.3}
\]

The error estimate in (0.2) follows directly from the maximal choice of
\(H\). Indeed

\[
 {\lambda_{h+1}\over\lambda_h}={m+h+1\over m-h},
\]

so \(\lambda_{H+1}>m+H+1\) implies
\(\lambda_H>m-H\), whereas \(\lambda_H\le m+H\). Consequently

\[
 0\le E=N(M-\lambda_H)<2HN=O(WH/m).
\tag{0.3a}
\]

Finally, the uniform expansion
\(\log\lambda_h=h^2/m+o(1)\) for
\(h=O(\sqrt{m\log m})\) gives the asserted value of \(H\).

Fix one coordinate \(x\), put \(k=m-H\), and split the roots into

\[
 {\cal A}_1=\{A\in\tbinom{[2m]}k:x\in A\},\qquad
 {\cal A}_0=\{A\in\tbinom{[2m]}k:x\notin A\}.
\tag{0.4}
\]

Their exact sizes are

\[
 R_1=|{\cal A}_1|={k\over2m}N,\qquad
 R_0=|{\cal A}_0|={M\over2m}N,
\tag{0.5}
\]

and

\[
 R_0-R_1={H\over m}N=o(W/H).
\tag{0.6}
\]

This note attacks the proposed global two-orbit resolution after common
vacancies and common nested tags are imposed. The conclusions are:

1. The paired quotient-chain theorem is a genuine integral completion
   theorem, but only after global trace compatibility has been built.
   If active lower and upper traces are injective at every depth, common
   stopping tags make the quotient condition automatic.

2. Common tags refine the two raw \(G_x=S_{[2m]\setminus\{x\}}\)
   catalogue orbits into \(M+1\) state orbits. The class
   \({\cal A}_1\) remains one orbit. The class \({\cal A}_0\) splits
   into \(M\) orbits indexed by the cyclic offset of \(x\) from phase
   zero. Their exact sizes are

   \[
   R_1M!,\qquad
   R_0(M-1)!\quad\hbox{for each of the \(M\) offsets}.
   \tag{0.7}
   \]

3. There is an exact all-coordinate collar equation. At depth \(q\), an
   exact paired resolution must use

   \[
                         b_q={q\over m}N_q
   \tag{0.8}
   \]

   occurrences whose lower trace avoids \(x\) and whose upper trace
   contains \(x\). Among all \(T\) raw phase slots there are
   \((q/m)T\) such slots. Hence the vacancy set \(V_q\) must satisfy

   \[
   \boxed{
   |V_q\cap{\cal B}_{q,x}|={q\over m}(T-N_q).}
   \tag{0.9}
   \]

   This holds for every coordinate \(x\). It is the exact entry-neutral
   vacancy condition hidden by scalar tag counts.

4. The single-coordinate anchored collar equations are arithmetically
   feasible. Assigning the \(M\) phase offsets nearly uniformly across
   the \({\cal A}_0\) roots meets all moments for the fixed anchor
   coordinate simultaneously, with only polynomial aggregate rounding
   error \(o(W)\). Thus there is no one-coordinate marginal or tag-birth
   obstruction. Simultaneous feasibility for all coordinates is not
   proved by this batching. It is, however, feasible in the global-slot
   nested first-moment LP: the constant survival point
   \(z_{e,q}=N_q/T\) satisfies
   every coordinate equation exactly, and repeated common profiles admit
   an integral all-coordinate realization with \(o(W)\) error per
   coordinate across all depths. Summing all coordinate spill cuts gives
   only \(q(T-n_q)\ge0\). Hence there is no stronger first-moment/Farkas
   obstruction from this global-slot vacancy/nesting system.

5. There is nevertheless an exact quantified statewise no-go for the
   tempting sector-separated construction. Let \(G_q\) count active
   \({\cal A}_0\)-histories whose middle owner avoids \(x\) but whose
   upper depth-\(q\) trace contains \(x\). If \(D_{\rm deep}\) is the
   total two-sign paired deficiency, then

   \[
   \boxed{
   {D_{\rm deep}\over2}
   +\sum_{q=q_0}^{\lfloor\sqrt m/2\rfloor}G_q
   \ge
   \left(
     {1-e^{-1/4}\over2}-{1\over16}+o(1)
   \right)W,}
   \tag{0.10}
   \]

   where \(q_0=\lceil m^{1/4}\rceil\). In particular, suppressing all
   such cross-sector histories forces

   \[
   \boxed{
   D_{\rm deep}\ge
   \left(1-e^{-1/4}-{1\over8}+o(1)\right)W.}
   \tag{0.11}
   \]

   The constant is approximately \(0.0962\). This is statewise and
   permits arbitrary global dependence.

6. Independent motion of the two anchored catalogue classes also fails.
   For common-floor, internally simple class seeds satisfying the
   necessary low-defect capacity conditions (7.0a), it creates at least

   \[
   \left({1-e^{-1}\over2}+o(1)\right)W
   \tag{0.12}
   \]

   expected cross-class upper collisions already through
   \(q\le\sqrt m\).

7. A positive skeleton does exist. Every full Boolean SCD supplies one
   literal tag-\(H\) promotion phase at every root, with both signed
   traces globally injective. Also, the inclusion graph pairs every
   \({\cal A}_1\) root with a distinct \({\cal A}_0\) root; only the
   \(o(W/H)\) roots in (0.6) remain. A paired root frame has exactly
   \(H\) raw common-owner phase pairs and \(m\) exchanged owner pairs.
   This is a literal source of cross-class two-history shores.

8. These facts do not produce the full resolution. A successful
   construction must retain \(\Omega(W)\) cross-sector bridge-depth
   incidences, hence \(\Omega(W/H)\) distinct such histories, and align
   their entire all-depth target profile with the holes of the dominant
   class. Layerwise marginals, independent orbit averaging, and separate
   classwise quotient chains are insufficient.

Thus the two-orbit route is neither closed universally nor solved. What
is closed is the status-separated and independent-relative-motion
versions. The exact surviving object is an exceptional correlated
all-depth alignment, for which the anchored near-matching stated in
Section 9 is a sufficient formulation.

## 1. Physical traces and the paired quotient interface

Use the complemented promotion-ring convention. For a root
\(A\in\binom{[2m]}k\), choose a directed cyclic order \(\pi\) on
\(A^c\), and let

\[
 X_{A,i}=A\cup I_\pi(i,H)
\tag{1.1}
\]

be its middle phase. Its signed depth-\(q\) traces are

\[
 L_q(A,i)=A\cup I_\pi(i+q,H-q),
\tag{1.2}
\]

\[
 U_q(A,i)=A\cup I_\pi(i,H+q).
\tag{1.3}
\]

Thus \(L_q\subseteq X_{A,i}\subseteq U_q\), with ranks
\(m-q,m,m+q\).

Let \(E\) be a set of physical phase occurrences with stopping depths
\(d(e)\), and put

\[
 E_q=\{e\in E:d(e)\ge q\}.
\tag{1.4a}
\]

For \(e\in E_q\), put

\[
 \Theta_q(e)=(L_q(e),U_q(e)),
\tag{1.4}
\]

and let

\[
 I_q^{\rm act}=\Theta_q(E_q)
\tag{1.4b}
\]

be the physical active image. Define \(\widehat\Theta_q\) on all of
\(E\) by sending every member of \(E\setminus E_q\) to one cemetery
symbol \(\bot\).

The stopped form of the paired quotient-chain theorem says the
following. Suppose every depth-\(q\) fibre of
\(\widehat\Theta_q\) lies in one depth-\((q+1)\) fibre and both
coordinate projections of \(I_q^{\rm act}\) are injective. Then there
are nested integral representative sets

\[
 A_H\subseteq A_{H-1}\subseteq\cdots\subseteq A_{q_0},
 \qquad A_q\subseteq E_q,
\tag{1.5}
\]

such that \(\Theta_q:A_q\to I_q^{\rm act}\) is bijective at every
depth. The cemetery symbol is bookkeeping only and is not represented
by a physical selected occurrence. The signed defect is therefore
exactly

\[
 2\sum_{q=q_0}^H(N_q-|I_q^{\rm act}|).
\tag{1.6}
\]

For completeness, choose one representative from every deepest active
fibre. Descending in \(q\), the already chosen representatives lie in
\(E_{q+1}\). Two of them cannot merge in one active depth-\(q\) fibre,
because fibre coarsening would then put them in one depth-\((q+1)\)
fibre. Add one representative from each still-unrepresented active
depth-\(q\) fibre. This proves (1.5) without ever selecting a cemetery
representative.

For common stopping tags, if the active lower and upper maps are already
injective, every active fibre is a singleton and all stopped
occurrences form the cemetery fibre. Fibre coarsening is then automatic.
In that special case one may simply take \(A_q=E_q\). Accordingly the
global mathematical task is not another rounding of (1.5); it is the
construction of one physical active family whose two signed maps are
simultaneously injective.

The theorem does not choose the cyclic frames, choose vacancies, control
middle owners, or splice physical paths. These remain additional
hypotheses in every use below.

## 2. Exact anchored signature and bridge flux

For a root in \({\cal A}_1\), both traces (1.2)--(1.3) contain \(x\) at
every depth. For a root in \({\cal A}_0\), a fixed coordinate \(x\) lies
in exactly \(H-q\) lower intervals and \(H+q\) upper intervals. The
lower event is contained in the upper event. Hence the \(M\) phases
split exactly as

\[
\begin{array}{c|c}
(x\in L_q,\ x\in U_q)&H-q\\
(x\notin L_q,\ x\in U_q)&2q\\
(x\notin L_q,\ x\notin U_q)&m-q.
\end{array}
\tag{2.1}
\]

The middle row consists of the depth-\(q\) bridge phases.

The numbers of signed rank targets containing \(x\) are

\[
 u_q^-={m-q\over2m}N_q,\qquad
 u_q^+={m+q\over2m}N_q.
\tag{2.2}
\]

### Lemma 2.1 (exact bridge equation)

Suppose a paired image at depth \(q\) has injective coordinate
projections. Let \(h_q^\pm(x)\) be the number of missing
\(x\)-containing targets of the two signs, and let \(B_q(x)\) be the
number of selected bridge occurrences. Then

\[
 \boxed{
 B_q(x)={q\over m}N_q-h_q^+(x)+h_q^-(x).}
\tag{2.3}
\]

If the two paired images have common size \(N_q-h_q\), then

\[
 \boxed{
 \left|B_q(x)-{q\over m}N_q\right|\le h_q.}
\tag{2.4}
\]

#### Proof

Every selected occurrence has signature \(11,01\), or \(00\); signature
\(10\) is impossible because \(L_q\subseteq U_q\). Therefore the number
of selected upper targets containing \(x\) minus the corresponding lower
number is exactly \(B_q(x)\). By (2.2), those two selected counts are
\(u_q^+-h_q^+(x)\) and \(u_q^--h_q^-(x)\). Their difference proves
(2.3). If each sign has \(h_q\) total holes, then
\(0\le h_q^\pm(x)\le h_q\), proving (2.4). \(\square\)

The aggregate required bridge incidence is macroscopic:

\[
 \sum_{q=q_0}^H{q\over m}N_q
 =\left({1\over2}+o(1)\right)W.
\tag{2.5}
\]

Indeed \(N_q/W=\exp(-q^2/m+o(1))\) uniformly in the present range, and
the Riemann sum of \(t e^{-t^2}\) from \(0\) to
\(\sqrt{\log m}\) tends to \(1/2\). Thus any \(o(W)\)-defect
construction contains \((1/2+o(1))W\) bridge depth-incidences and at
least \((1/2+o(1))W/H\) distinct bridge-tagged occurrences.

## 3. Exact all-coordinate vacancy identity

Let \({\cal B}_{q,x}\) be the set of all raw phase slots
\((A,i)\) satisfying

\[
 x\notin L_q(A,i),\qquad x\in U_q(A,i).
\]

There are \(R_0\) roots whose top contains \(x\), and each has exactly
\(2q\) such slots. By (0.5),

\[
 |{\cal B}_{q,x}|=2qR_0={q\over m}MN={q\over m}T.
\tag{3.1}
\]

### Theorem 3.1 (entry-neutral vacancy equation)

Suppose an active phase family is bijective onto both complete signed
rank-\(q\) layers, and let \(V_q\) be the inactive raw phase slots. Then,
for every coordinate \(x\),

\[
 \boxed{
 |V_q\cap{\cal B}_{q,x}|
 ={q\over m}(T-N_q).}
\tag{3.2}
\]

If the two signed load vectors have total \(\ell^1\) defects
\(\varepsilon_q^-,\varepsilon_q^+\), the absolute error in (3.2) is at
most \(\varepsilon_q^-+\varepsilon_q^+\).

#### Proof

In an exact resolution, Lemma 2.1 with no holes gives
\((q/m)N_q\) active bridge slots. Subtract this from (3.1).

For the defective statement, let \(a_q^\pm(x)\) count active signed
occurrences containing \(x\), with multiplicity. The active bridge count
is \(a_q^+(x)-a_q^-(x)\). Its deviation from
\((q/m)N_q\) is bounded by the two \(\ell^1\) load errors, since summing
a load error over targets containing \(x\) cannot increase its absolute
value beyond the full \(\ell^1\) norm. Subtraction from (3.1) completes
the proof. \(\square\)

Equation (3.2) is statewise. It forces the correct total vacancy mass on
every physical boundary family \({\cal B}_{q,x}\). It does not by
itself split that mass between the internal and exterior subcollars;
indeed \({\cal B}_{q,x}\) lies wholly over roots in \({\cal A}_0\).
Nor does the family of equations by itself imply target injectivity.

At the middle rank there is a matching exact sector equation. Across all
full rings, the number of owner occurrences containing \(x\) is

\[
 MR_1+HR_0={T\over2},
\tag{3.3}
\]

and the number avoiding \(x\) is \(mR_0=T/2\). An exact one-copy
middle resolution contains \(W/2\) owners of either status. Therefore
its calibrated middle vacancies split exactly as

\[
 \boxed{
 V_{\rm mid}(x\in X)=V_{\rm mid}(x\notin X)={E\over2}.}
\tag{3.4}
\]

With middle holes or repetitions, the error is bounded by the
corresponding sector load defect. Thus even the middle dump cannot be
placed wholly in the nominal spill class.

## 4. Common tags refine the raw two-orbit picture

An aligned frame has a distinguished phase zero. There are \(M!\)
aligned directed frames at one root. Fix one common nested phase profile
\(P_q\subseteq{\mathbb Z}_M\), with

\[
 |P_q|=k_q,\qquad
 P_H\subseteq\cdots\subseteq P_1.
\tag{4.1}
\]

The phase tag is the last \(q\) for which it lies in \(P_q\).

For the common-floor choice

\[
 N_q=Nk_q+r_q,\qquad 0\le r_q<N,
\tag{4.1a}
\]

the middle positive-radius dump has exact total size

\[
 T-Nk_1
 =E+{W\over m+1}+r_1
 =O(WH/m).
\tag{4.1b}
\]

Thus its average length per root is \(O(H)\); for the standard
\(H=\lfloor\sqrt{m\log m}\rfloor\) calibration it is
\(\Theta(H)\). At depth \(q\), the exact common-floor vacancy count is
\(T-Nk_q\), while the unavoidable target shortfall is \(r_q\).

### Theorem 4.1 (exact tagged \(G_x\)-orbits)

Under \(G_x=S_{[2m]\setminus\{x\}}\), the aligned configuration
catalogue has:

1. one orbit over \({\cal A}_1\), of size
   \[
   R_1M!;
   \tag{4.2}
   \]
2. \(M\) orbits over \({\cal A}_0\), indexed by the cyclic offset
   \(t\in{\mathbb Z}_M\) of \(x\) from phase zero, each of size
   \[
   R_0(M-1)!.
   \tag{4.3}
   \]

#### Proof

If \(x\in A\), the group fixes \(x\) inside the unordered root and can
map every other root label and every ordered top position arbitrarily.
The rooted aligned-state stabilizer has size \((k-1)!\), so its orbit
has size

\[
 {(2m-1)!\over(k-1)!}=R_1M!.
\]

If \(x\notin A\), its top position relative to the distinguished phase
is invariant. At one fixed offset the group is transitive, and the
stabilizer consists of arbitrary permutations of the \(k\) root labels.
The orbit size is

\[
 {(2m-1)!\over k!}=R_0(M-1)!.
\]

The \(M\) offsets exhaust all aligned frames. \(\square\)

Thus the raw two catalogue orbits from the unpointed frame problem do
not remain two state orbits after common tags are fixed.

For offset \(t\), let

\[
 b_q(t)=|\{i\in P_q:
   x\notin L_q(A,i),\ x\in U_q(A,i)\}|.
\tag{4.4}
\]

Also put

\[
 \ell_q(t)=|\{i\in P_q:x\in L_q(A,i)\}|,
 \qquad
 u_q(t)=|\{i\in P_q:x\in U_q(A,i)\}|.
\tag{4.4a}
\]

As \(t\) runs through all \(M\) offsets, every active phase sees exactly
\(H-q\) lower-containing offsets, \(H+q\) upper-containing offsets,
and \(2q\) bridge offsets. Hence

\[
 \sum_t\ell_q(t)=(H-q)k_q,
 \qquad
 \sum_tu_q(t)=(H+q)k_q,
 \qquad
 \sum_tb_q(t)=2qk_q.
\tag{4.5}
\]

### Corollary 4.2 (simultaneous scalar feasibility)

The offsets can be assigned to the \(R_0\) roots so that, simultaneously
for all \(q\le H\), the three totals over \({\cal A}_0\) are

\[
 \begin{aligned}
 L_{0,q}(x)&={H-q\over2m}Nk_q+\operatorname {poly}(m),\\
 U_{0,q}(x)&={H+q\over2m}Nk_q+\operatorname {poly}(m),\\
 B_q(x)&={q\over m}Nk_q+\operatorname {poly}(m).
 \end{aligned}
\tag{4.6}
\]

The aggregate error over all depths is \(o(W)\).

#### Proof

Use every offset once in each complete batch of \(M\) roots, and assign
the fewer than \(M\) remaining roots arbitrarily. A complete batch
contributes the three quantities in (4.5). Since

\[
 {R_0\over M}={N\over2m},
\]

the three main contributions are

\[
 {N\over2m}(H-q)k_q,
 \qquad
 {N\over2m}(H+q)k_q,
 \qquad
 {N\over2m}2qk_q.
\]

The incomplete batch contributes at most \(Mk_q\) at one depth.
Here \(M,H,k_1\) are polynomial in \(m\), while \(W\) is exponential.
Summing through \(H\) depths gives \(o(W)\). \(\square\)

The \({\cal A}_1\) class contributes exactly \(R_1k_q\) containing
traces to either sign. Adding this to (4.6) gives

\[
 {m-q\over2m}Nk_q+\operatorname {poly}(m),
 \qquad
 {m+q\over2m}Nk_q+\operatorname {poly}(m),
\tag{4.7}
\]

for the lower and upper containing-target counts. Since
\(Nk_q=N_q-r_q\) and \(\sum_qr_q<HN=o(W)\), these meet both exact
targets in (2.2), as well as the bridge target (2.3), with aggregate
error \(o(W)\). Hence the anchor coordinate, the tag census, and the
tagged orbit arithmetic do not furnish a statewise nonexistence theorem.

### Theorem 4.3 (no all-coordinate global-slot first-moment obstruction)

Fix an arbitrary physical frame at every root, and let \(\Omega\) be
the resulting set of \(T\) phase slots. Put

\[
 z_{e,0}={W\over T},
 \qquad
 z_{e,q}={N_q\over T}\quad(1\le q\le H)
\tag{4.8}
\]

for every \(e\in\Omega\). Then \(z\) is an exact feasible point of the
global-slot nested first-moment LP, whose constraints are slotwise
survival monotonicity, the displayed depth totals, and the coordinate
vacancy moments:

\[
 1\ge z_{e,0}\ge z_{e,1}\ge\cdots\ge z_{e,H}\ge0,
 \qquad
 \sum_ez_{e,0}=W,
 \qquad
 \sum_ez_{e,q}=N_q.
\tag{4.9}
\]

It satisfies simultaneously, for every \(q,x\),

\[
 \boxed{
 \sum_{e\in{\cal B}_{q,x}}(1-z_{e,q})
 ={q\over m}(T-N_q),}
\tag{4.10}
\]

and its active middle mass in either \(x\)-sector is exactly \(W/2\).
Moreover, (4.8) is a convex combination of integral paired-common
stopping-tag assignments having exactly
\(W,N_1,\ldots,N_H\) active slots at the successive depths. Here
"paired-common" means that the lower and upper traces of one occurrence
share its tag; it does not mean that one identical phase profile is
repeated at every root or that prescribed SCD anchors are retained. The
convex-combination assertion concerns the nested-cardinality polytope:
an individual realization need not satisfy (4.10). The repeated-profile
construction below restores the collar equations integrally to the
coefficient-scale accuracy required here and has one depth-\(H\) slot
per root.

#### Proof

The monotonicity follows from
\(T\ge W>N_1>\cdots>N_H\). Equations (4.9) are immediate. By (3.1),

\[
 \sum_{e\in{\cal B}_{q,x}}(1-z_{e,q})
 ={qT\over m}\left(1-{N_q\over T}\right),
\]

which is (4.10). Each raw middle sector has size \(T/2\) by
(3.3), so multiplying by \(W/T\) gives \(W/2\).

For the last assertion, order the \(T\) slots uniformly at random and,
at depth \(q\), retain the first \(N_q\) slots (the first \(W\) at the
middle). Every realization is an integral nested tag assignment with
the exact cardinalities, while every slot has survival probability
\(N_q/T\). Averaging gives (4.8). \(\square\)

There is also an integral repeated-profile version at the accuracy
relevant here. Fix any nested \(P_q\subseteq\mathbb Z_M\) with
\(|P_q|=k_q\), and choose independently and uniformly an aligned frame
at every root. Let \(V_{q,x}^{P}\) be the number of bridge slots outside
\(P_q\). Then

\[
 \mathbb E V_{q,x}^{P}
 ={q\over m}(T-Nk_q).
\tag{4.11}
\]

For fixed \((q,x)\), this is a sum over the \(R_0\) relevant roots of
independent variables in \([0,2q]\). Hoeffding's inequality and a union
bound over the \(2mH\) pairs \((q,x)\) give one deterministic frame
assignment for which, uniformly in \(x\),

\[
 \left|V_{q,x}^{P}-\mathbb EV_{q,x}^{P}\right|
 \le 2q\sqrt{R_0\log(4mH)}
 \quad\hbox{for every }(q,x).
\tag{4.11a}
\]

Indeed the failure probability for one pair is at most
\(2(4mH)^{-2}\), so the union has probability strictly below one for
all large \(m\). Consequently

\[
 \sum_{q=1}^H
 \left|V_{q,x}^{P}-{q\over m}(T-N_q)\right|=o(W).
\tag{4.12}
\]

Indeed the total concentration error for one \(x\) is at most
\(\operatorname{poly}(m)\sqrt{N\log m}=o(W)\), while the floor mismatch
is

\[
 \sum_q{q r_q\over m}
 \le {H^2N\over m}=o(W).
\]

This proves that common nesting, integrality, and simultaneous
all-coordinate first moments create no coefficient-scale obstruction.
At the middle rank, the complement of \(P_1\) has size
\(T-Nk_1=E+W/(m+1)+r_1\ge E\). Choose the required \(E=o(W)\)
middle vacancies there, so no positive-depth history is removed. Their
sector error is at most \(E\), and hence creates no coefficient-scale
obstruction either.
The construction says nothing about collisions of actual targets, which
is exactly the remaining gate.

## 5. An exact statewise obstruction to sector separation

For a root in \({\cal A}_0\), split its \(2q\) bridge phases into two
classes:

* an internal bridge has \(x\in X_{A,i}\) but
  \(x\notin L_q(A,i)\);
* an exterior bridge has \(x\notin X_{A,i}\) but
  \(x\in U_q(A,i)\).

There are exactly \(q\) phases of each kind. This follows directly from
(1.1)--(1.3): the lower interval deletes \(q\) positions of the middle
window, while the upper interval adds \(q\) new positions.

Let \(G_q(x)\) be the number of selected exterior bridges at depth \(q\).
There are at most \(qR_0\) selected internal bridges, and therefore

\[
                         B_q(x)\le qR_0+G_q(x).
\tag{5.1}
\]

Let the paired image at depth \(q\) have size \(N_q-h_q\), so it has
\(h_q\) holes in either signed layer. Equations (2.4)--(5.1) imply

\[
 h_q+G_q(x)
 \ge
 \left({q\over m}N_q-qR_0\right)_+
 =
 {q\over m}\left(N_q-{T\over2}\right)_+.
\tag{5.2}
\]

This yields an exact macroscopic tradeoff.

### Theorem 5.1 (spill-erasure statewise cut)

Put \(q_0=\lceil m^{1/4}\rceil\) and
\(Q=\lfloor\sqrt m/2\rfloor\). Then

\[
 \boxed{
 \sum_{q=q_0}^{Q}h_q+
 \sum_{q=q_0}^{Q}G_q(x)
 \ge
 \left(
 {1-e^{-1/4}\over2}-{1\over16}+o(1)
 \right)W.}
\tag{5.3}
\]

Consequently, with

\[
 D_{\rm deep}=2\sum_{q=q_0}^Hh_q,
\]

one has (0.10). If every exterior bridge is suppressed throughout this
range, then (0.11) follows.

#### Proof

Uniformly for \(q\le Q\),

\[
 {N_q\over W}=\exp(-q^2/m+o(1)),
\qquad
 {T\over W}=1+o(1).
\tag{5.4}
\]

In particular \(N_q>T/2\) throughout the displayed range for all large
\(m\). Summing (5.2), the first term is

\[
\begin{aligned}
 \sum_{q=q_0}^{Q}{q\over m}N_q
 &=
 \left(\int_0^{1/2}t e^{-t^2}\,dt+o(1)\right)W\\
 &=
 \left({1-e^{-1/4}\over2}+o(1)\right)W.
\end{aligned}
\tag{5.5}
\]

The omitted range below \(q_0\) contributes \(o(W)\). The second term is

\[
 \sum_{q=q_0}^{Q}{qT\over2m}
 =\left({1\over16}+o(1)\right)W.
\tag{5.6}
\]

Equations (5.2), (5.5), and (5.6) prove (5.3). Multiplication by two
gives (0.10)--(0.11). \(\square\)

The no-go is precisely targeted. At the middle rank, assigning the
\({\cal A}_0\) phases whose owners avoid \(x\) to the avoiding sector
looks like a clean separation. One might then stop each such phase
before its first upper trace crosses into the \(x\)-containing sector.
At positive depth those same histories are needed to cross from a lower
target avoiding \(x\) to an upper target containing \(x\). Eliminating
that collar transport loses a positive linear number of paired targets.
The middle owners themselves may remain as tag-zero occurrences; the
obstruction concerns their positive-depth histories. The paired
representative theorem cannot repair the missing images.

The cut is sharp at the level of anchor-status incidences: (5.1) is
equality when every available internal bridge is retained, and (2.4) is
equality when all signed holes lie on the adverse anchor side.
Corollary 4.2 realizes the complementary lower, upper, and bridge
moments to aggregate \(o(W)\). Hence no stronger contradiction follows
from the one-coordinate status census alone; any further obstruction
must use target identities or common-history geometry.

### Proposition 5.2 (the all-coordinate sum is the trivial capacity cut)

Let a selected paired family at depth \(q\) have \(n_q=N_q-h_q\)
occurrences and injective coordinate projections. For each coordinate
\(x\), let \(I_q(x)\) and \(G_q(x)\) count its selected internal and
exterior bridges. Then

\[
 \sum_x I_q(x)=\sum_xG_q(x)=qn_q.
\tag{5.8}
\]

Summing the strongest coordinatewise spill inequalities gives exactly

\[
 q(T-n_q)\ge0.
\tag{5.9}
\]

Thus the equally weighted sum of all coordinate spill inequalities is
only the trivial capacity cut. Together with the feasible point in
Theorem 4.3, the displayed coordinate first-moment and global-slot
nesting constraints admit no linear separator. This statement does not
exclude a nonuniform target-derived coordinate potential, a
target-geometric obstruction, or a prescribed-anchor obstruction.

#### Proof

Every selected occurrence has exactly \(q\) coordinates in
\(X\setminus L_q\) and exactly \(q\) in \(U_q\setminus X\), proving
(5.8). Since \(I_q(x)\le qR_0=qT/(2m)\), Lemma 2.1 gives

\[
 G_q(x)\ge {q\over m}N_q-h_q^+(x)+h_q^-(x)-{qT\over2m}.
\tag{5.10}
\]

There are \(h_q\) missing targets of either sign, so

\[
 \sum_xh_q^+(x)=(m+q)h_q,
 \qquad
 \sum_xh_q^-(x)=(m-q)h_q.
\tag{5.11}
\]

Sum (5.10) over the \(2m\) coordinates and use (5.8)--(5.11). The
result is

\[
 qn_q\ge2qN_q-2qh_q-qT=2qn_q-qT,
\]

which is precisely (5.9). \(\square\)

Conversely, (5.3) shows what every positive construction must do:

\[
 \sum_{q=q_0}^{Q}G_q(x)
 \ge
 \left(
 {1-e^{-1/4}\over2}-{1\over16}-o(1)
 \right)W
\tag{5.7}
\]

whenever \(D_{\rm deep}=o(W)\). Since one tagged occurrence contributes
at most \(H\) depths, at least a constant multiple of \(W/H\)
distinct exterior-bridge histories must survive. They may still be
bundled into \(o(W/H)\) physical paths; (5.7) is an incidence
requirement, not by itself a component lower bound.

## 6. Two exact positive skeletons

The preceding cut does not say that the required cross-sector histories
cannot be correlated. Two exact constructions show why a universal
anchor-only no-go is false. They are separate skeletons; no compatibility
between the SCD frames of Section 6.1 and the paired frames of Section
6.2 is asserted.

### 6.1 Full-SCD tag-\(H\) anchors

Fix any full symmetric-chain decomposition of \(B_{2m}\). Every root
\(A\in\binom{[2m]}k\) lies on a unique chain segment

\[
 A=C_A(-H)\subset C_A(-H+1)\subset\cdots\subset C_A(H).
\tag{6.1}
\]

Write \(z_1,\ldots,z_{2H}\) for the labels added along this segment.
Since \(k_H=1\), rotate the common aligned phase convention so that
\(P_H=\{0\}\). At this distinguished phase, place the labels as
follows, starting at phase zero:

\[
 z_H,z_{H-1},\ldots,z_1,z_{H+1},z_{H+2},\ldots,z_{2H},
\tag{6.2a}
\]

and place the other \(m-H\) labels arbitrarily in the complementary
arc. The first \(H\) positions form \(C_A(0)\setminus A\). Removing the
first \(q\) of those positions leaves
\(\{z_1,\ldots,z_{H-q}\}\), while adding the next \(q\) positions gives
\(\{z_1,\ldots,z_{H+q}\}\). Thus the distinguished phase has exactly

\[
 L_q=C_A(-q),\qquad U_q=C_A(q).
\tag{6.2}
\]
Hence one literal
tag-\(H\) phase exists in every root, and the two signed maps are
globally injective at every depth.

At the deepest endpoint, put

\[
 f(A)=C_A(H)^c\in\binom{[2m]}k.
\tag{6.3}
\]

The map \(f\) is a permutation of the root layer and \(A\cap f(A)\) is
empty. Its exact anchor-status transition census is

\[
\begin{array}{c|cc}
 &f(A)\in{\cal A}_1&f(A)\in{\cal A}_0\\ \hline
 A\in{\cal A}_1&0&R_1\\
 A\in{\cal A}_0&R_1&R_0-R_1.
\end{array}
\tag{6.4}
\]

Indeed a root containing \(x\) must map to one avoiding \(x\). Since
\(f\) is a permutation, all \(R_1\) outputs containing \(x\) must come
from \({\cal A}_0\); the remaining count is forced. Thus the compulsory
deep anchors themselves already use cross-status transport.

This realizes only one tag-\(H\) phase per root. It does not group the
remaining \(N_q-N\) chains at shallower depths into the same root frames.

### 6.2 An almost-perfect pairing of the two root classes

Let \(Y=[2m]\setminus\{x\}\). Identify an \({\cal A}_1\) root
\(C\cup\{x\}\) with \(C\in\binom{Y}{k-1}\), and identify an
\({\cal A}_0\) root with a member of \(\binom Yk\).

### Lemma 6.1 (root-pair matching)

The inclusion graph

\[
 \binom Y{k-1}\longleftrightarrow\binom Yk
\]

has a matching saturating its left shore. It leaves exactly

\[
 R_0-R_1={H\over m}N=o(W/H)
\tag{6.5}
\]

unmatched \({\cal A}_0\) roots.

#### Proof

The graph is \((M,k)\)-biregular. For a left family \({\cal S}\), edge
counting gives

\[
 M|{\cal S}|\le k|N({\cal S})|.
\]

Since \(M>k\), Hall's condition holds. The leave is the shore-size
difference, which is (0.6). \(\square\)

For one matched inclusion \(C\subset C\cup\{y\}\), form the root pair

\[
 A_1=C\cup\{x\},\qquad A_0=C\cup\{y\}.
\tag{6.6}
\]

Let

\[
 K=[2m]\setminus(C\cup\{x,y\}),\qquad |K|=M-1.
\]

Choose a cyclic order on \(K\cup\{*\}\). Replace the marker by \(y\) to
obtain the frame at \(A_1\), and by \(x\) to obtain the frame at
\(A_0\).

### Lemma 6.2 (paired-frame owner ledger)

The two frames in (6.6) have exactly:

1. \(H\) phase pairs with the same middle owner; and
2. \(m\) phase pairs with distinct owners exchanged by
   \((x\,y)\).

For a common-owner phase, its two physical histories are alternative
anchored shores of one literal middle owner.

#### Proof

A fixed marker in a cyclic \(H\)-window deck lies in exactly \(H\)
windows. If the window contains the marker, its other \(H-1\) labels
form \(J\subset K\), and both owners equal

\[
 C\cup\{x,y\}\cup J.
\]

If the window avoids the marker, it is an \(H\)-set \(J\subset K\), and
the two owners are

\[
 C\cup\{x\}\cup J,\qquad C\cup\{y\}\cup J.
\]

There are \(M-H=m\) such windows. \(\square\)

This is a literal owner-preserving two-history source, not a global
solution. Choices made in distinct matched pairs need not be
trace-disjoint or history-compatible. Theorem 7.1 below rules out the
more symmetric scheme in which two complete class seeds are moved
independently; it does not rule out an exceptional global coupling of
these physical shores. The number \(H\) in Lemma 6.2 counts raw phase
pairs. Only those common-owner phases retained by the active profile
become usable shores, and selecting both members of one such pair would
duplicate its middle owner.

## 7. Independent two-orbit motion has linear cross-collision

We now close the direct extension of independent orbit symmetrization to
the paired all-depth setting.

At depth \(q\), let \(S_{1,q}^+\) be the set of \(x\)-containing upper
targets supplied by an internally injective \({\cal A}_1\) seed. Let
\(B_q^+\) be the upper-target support of its internally injective
\({\cal A}_0\) bridge occurrences. Apply independent uniform
\(g_1,g_0\in G_x\) to the two seeds.

### Theorem 7.1 (independent relative-motion obstruction)

Assume both class seeds use one aligned frame at every root, use the
same common-floor profile, and are internally injective in every typed
signed layer. Thus together they have exactly

\[
 n_q=Nk_q=N_q-r_q\le N_q
\tag{7.0b}
\]

active occurrences at depth \(q\). Put

\[
 \eta_q=\left(
 u_q^--(H-q)R_0-|S_{1,q}^+|
 \right)_+.
\tag{7.0}
\]

Assume, through \(q_0\le q\le\sqrt m\),

\[
 \sum_q\eta_q=o(W),
 \qquad
 \sum_q\left||B_q^+|-{q\over m}N_q\right|=o(W).
\tag{7.0a}
\]

These are necessary capacity conditions for any relative position of
the two seeds to have aggregate paired defect \(o(W)\). Then

\[
 \boxed{
 \sum_{q=q_0}^{\lfloor\sqrt m\rfloor}
 \mathbb E\,
 |g_1S_{1,q}^+\cap g_0B_q^+|
 \ge
 \left({1-e^{-1}\over2}+o(1)\right)W.}
\tag{7.1}
\]

Thus the independent two-orbit law cannot be supported on
\(o(W)\)-defect paired resolutions.

#### Proof

The \(x\)-containing lower target class has size \(u_q^-\). Across all
\({\cal A}_0\) roots, at most \((H-q)R_0\) raw lower phases contain
\(x\). Thus any relative position having \(z_q\) holes in that target
sector forces \(\eta_q\le z_q\). By definition,

\[
 |S_{1,q}^+|
 \ge u_q^--(H-q)R_0-\eta_q.
\tag{7.2}
\]

The same \({\cal A}_1\) occurrences give the upper support, because the
seed is paired and internally injective. The deterministic loss ratios
are \(O(H/m+q/m)\). More explicitly,

\[
 \sum_q\left(1-{|S_{1,q}^+|\over u_q^+}\right)|B_q^+|
 \le
 O\left({H+\sqrt m\over m}\right)\sum_q|B_q^+|
 +\sum_q\eta_q=o(W).
\tag{7.3a}
\]

Here \(N/N_q=O(1/m)\) uniformly in this range,
\(\sum_q|B_q^+|=O(W)\) by (7.0a), and
\(|B_q^+|\le u_q^+\) by within-class upper injectivity.

The group \(G_x\) is transitive on the \(x\)-containing upper layer.
Independence therefore gives exactly

\[
 \mathbb E
 |g_1S_{1,q}^+\cap g_0B_q^+|
 ={|S_{1,q}^+|\,|B_q^+|\over u_q^+}.
\tag{7.4}
\]

By hypothesis (7.0a),
\(\sum_q||B_q^+|-qN_q/m|=o(W)\). Combining
(7.3a)--(7.4) gives the stronger identity

\[
 \sum_q\mathbb E|g_1S_{1,q}^+\cap g_0B_q^+|
 =\sum_q|B_q^+|-o(W).
\tag{7.4a}
\]

Together with

\[
 \sum_{q=q_0}^{\lfloor\sqrt m\rfloor}{q\over m}N_q
 =\left({1-e^{-1}\over2}+o(1)\right)W
\tag{7.5}
\]

this proves (7.1). \(\square\)

The theorem does not exclude an exceptional correlated relative
position of the two seeds. It proves that such a position, if it exists,
has vanishing density among the group translates. Indeed, put
\(B=\sum_q|B_q^+|=(1-e^{-1})W/2+o(W)\) and let \(Z\) be the summed
intersection. Equation (7.4a) gives \(\mathbb E(B-Z)=o(W)\), while
every translate with \(Z=o(W)\) has \(B-Z=(1-e^{-1})W/2-o(W)\).
Markov's inequality therefore gives probability \(o(1)\) for such a
translate. Moreover, by (7.0b), a cross intersection of size \(C_q\)
forces at least \(r_q+C_q\) upper target holes at depth \(q\). Hence a
law supported on paired resolutions of aggregate defect \(o(W)\) is
impossible.

## 8. The exact exceptional-alignment potential

There is an exact statewise formulation of the remaining correlation
problem. Fix internally simple, commonly tagged seeds in the two root
classes, where internally simple means that within each typed signed
layer each class contributes at most one occurrence to any target. For
each typed signed layer \(j=(q,\sigma)\), let

\[
 S_{11,j}\subseteq{\cal X}_{j,1}
\]

be the dominant \({\cal A}_1\) support in the target sector containing
\(x\), let

\[
 S_{01,j}\subseteq{\cal X}_{j,1}
\]

be the \({\cal A}_0\) spill support in that sector, and let

\[
 S_{00,j}\subseteq{\cal X}_{j,0}
\]

be the \({\cal A}_0\) support in the sector avoiding \(x\). Put

\[
 A_j={\cal X}_{j,1}\setminus S_{11,j},
\qquad B_j=S_{01,j}.
\tag{8.1}
\]

After normalizing the first class position, let one
\(h\in G_x\) move the second class.

### Theorem 8.1 (exact collision-plus-hole identity)

The aggregate cross-class collision plus hole defect of the combined
supports is exactly

\[
 \boxed{
 \Delta(h)=
 \sum_j\left(
 |{\cal X}_{j,0}\setminus S_{00,j}|
 +|A_j\mathbin\triangle hB_j|
 \right).}
\tag{8.2}
\]

#### Proof

No \({\cal A}_1\) trace lies in the sector avoiding \(x\), and

\[
 |{\cal X}_{j,0}\setminus hS_{00,j}|
 =|{\cal X}_{j,0}\setminus S_{00,j}|
\]

because \(h\in G_x\) permutes that whole sector. Thus its holes are
exactly the first term. In the sector containing \(x\), a point of
\(hB_j\setminus A_j\) already lies in \(S_{11,j}\) and is exactly one
cross collision. A point of \(A_j\setminus hB_j\) is exactly one
unrepaired dominant hole. These disjoint sets form
\(A_j\triangle hB_j\). \(\square\)

Identity (8.2) measures signed-layer collision and hole defect only;
middle-owner simplicity and all-depth history legality are additional
conditions. Randomizing \(h\) cannot beat the best deterministic \(h\).
Coefficient one within this two-seed architecture requires one
exceptional relative permutation satisfying

\[
 \sum_j|A_j\triangle hB_j|=o(W),
\qquad
 \sum_j|{\cal X}_{j,0}\setminus S_{00,j}|=o(W).
\tag{8.3}
\]

This target is stronger than matching the separate layer cardinalities.
The same physical histories and the same stopping tags occur at every
depth.

There is also a local warning about the quotient condition. For any
\(1\le q<H\), one can choose two occurrences from different anchored
classes with distinct middle owners and

\[
 \Theta_q(e_1)=\Theta_q(e_0)=(L,U),
\tag{8.4}
\]

but with

\[
 \Theta_{q+1}(e_1)=(L-\{y\},U+\{z\}),
\qquad
 \Theta_{q+1}(e_0)=(L-\{x\},U+\{z\}).
\tag{8.5}
\]

Here is an exact realization. Take \(|B|=k-1\), choose distinct
\(x,y\notin B\), and choose \(C\) disjoint from \(B\cup\{x,y\}\) with
\(|C|=H-q-1\). Put

\[
 L=B\cup\{x,y\}\cup C.
\]

Choose a disjoint \(2q\)-set \(R\), put \(U=L\cup R\), and choose two
distinct \(q\)-subsets \(D_1,D_0\subset R\). For the root
\(B\cup\{x\}\), begin the relevant cyclic segment with the elements of
\(D_1\), then \(y\), then the elements of \(C\), then
\(R\setminus D_1\). For the root \(B\cup\{y\}\), use the analogous
segment with \(D_0\), then \(x\), then \(C\), then
\(R\setminus D_0\). Choose one common next label \(z\notin U\) in the
two frames. These segments have lengths \(q,H-q,q,1\), respectively,
so (1.2)--(1.3) give (8.4), while the first coordinate deleted on
passing to depth \(q+1\) is respectively \(y,x\), and the first new
upper coordinate is \(z\). This proves (8.5). Thus two classwise
quotient systems need not have quotient-valid union: a common fibre can
merge and then split.

If both signed maps of the union are globally injective at every depth,
this example is automatically excluded and the cemetery lemma supplies
the quotient chain. With approximate pruning, however, deletions must be
history-closed; a separate layerwise repair can destroy common history.

## 9. Exact surviving theorem and implication scope

The proved positive facts are:

1. exact root-class sizes and an all-but-\(o(W/H)\) inclusion pairing;
2. exact physical paired frames with \(H\) raw common-owner shores;
3. one globally injective tag-\(H\) SCD anchor per root;
4. exact \(M+1\) tagged state-orbit census;
5. exact scalar collar feasibility by offset batching, plus an
   all-coordinate global-slot first-moment LP point and an integral
   repeated-profile realization with first-moment error \(o(W)\); and
6. the paired quotient representative theorem once global signed
   injectivity has been achieved.

The proved negative facts are:

1. sector-separated spill erasure has deep defect at least the positive
   constant in (0.11);
2. every low-defect state must retain the positive linear bridge
   incidence in (5.7);
3. independent relative motion has the linear collision floor (7.1);
4. two classwise quotient chains do not automatically compose; and
5. raw two-orbit transitivity disappears after the common tagged phase
   is fixed.

There is no additional obstruction from summing the coordinate cuts:
Proposition 5.2 reduces their total exactly to the trivial capacity
inequality (5.9).

What remains is the following single positive lemma.

> **Anchored exceptional-alignment lemma (open).** Construct one aligned
> promotion configuration at every root, with the calibrated common
> nested phase profile and its required vacancies, such that:
>
> 1. there is a history-closed pruning whose total induced
>    middle-plus-signed defect is \(o(W)\), after which the middle-owner
>    map and both active signed maps are injective at every depth and
>    the cemetery-valued paired maps form a quotient chain;
> 2. the vacancy sets satisfy the all-coordinate equations (3.2) up to
>    aggregate \(o(W)\);
> 3. the exterior bridge histories required by (5.7) land in the
>    dominant all-depth holes, equivalently the statewise analogue of
>    (8.3) holds;
> 4. the tag-\(H\) anchors agree with one background SCD, or the direct
>    word compiler is used instead of exact SCD completion; and
> 5. the physical cuts have an \(o(W/H)\)-component cover.

In the unrestricted common-floor formulation, a sufficient quantitative
version is the near-perfect configuration matching

\[
 \nu({\cal C}_{m,H})=N-o(N/\sqrt m),
\tag{9.1}
\]

whose matching property gives the history-closed injections and forces
the all-coordinate collar identities automatically. The offset batching
of Section 4 verifies only that the distinguished-coordinate marginal
does not obstruct such a matching. In the fixed-SCD formulation, the
sufficient object is the corresponding anchored representative together
with the common-root leave absorber.

Under item 1, the paired quotient-chain theorem supplies one integral
common history and the literal compiler yields \(W+o(W)\). Layerwise
\(o(W)\) collision and hole defect without history-closed pruning would
not suffice, by (8.4)--(8.5). Neither (9.1) nor the anchored absorber
matching is proved here.

Accordingly no constant-one theorem is claimed. The sharp conclusion is
that the two dominant anchored catalogues have enough scalar and
endpoint capacity, but coefficient one forces \(\Omega(W)\)
cross-sector bridge-depth incidences, hence \(\Omega(W/H)\) distinct
cross-sector histories, together with an exceptional targetwise
alignment. The natural status-separated and independent-orbit
constructions are rigorously impossible.
