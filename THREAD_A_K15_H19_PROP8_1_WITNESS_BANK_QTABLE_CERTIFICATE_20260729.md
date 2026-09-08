# Thread A: the H19 adaptive witness-bank and maximal-Q collar certificate

Date: 2026-07-29

Status: solver-free exact reduction for separated, fixed-core braid collars.
It distinguishes the overly strong literal transport of every selected
\(M_0\) pin from the useful adaptive theorem, which recreates every target
whose last safe witness is lost.  The direct c0520 braid fails the adaptive
capacity cut; the direct c0440 braid survives with one exceptional cell of
slack.  No c0440 assignment is certified here.

## 1. The theorem-faithful baseline

The baseline is not the stored 6438-letter prefix.  It is the unique
entrywise-maximal reconstruction

\[
 A^0=A(M_0)
\tag{1.1}
\]

frozen and solver-independently verified in

```text
scratch/thread_a_k15_h19_m0_a0_baseline_20260729.json
scratch/build_thread_a_k15_h19_m0_a0_baseline_20260729.py
```

The artifact has file SHA

```text
12a59780e8920469b385250bdb95ec9265259b2f0c9dac05c51f9262587ec09f
```

and records

```text
A0 word SHA                 8304799efb9e98a69d328a828a33792c9803326cb93bd1da3c7a2d5dd861382e
canonical M0 artifact SHA   17b87828b3a14c2698da666a88126900fdf9ecd9c7439662bb0af592c9a5259a
```

Only \(5700\) of the \(6438\) source positions agree with the stored prefix.
All collar calculations below use the `a0` and `m0` arrays in this artifact.

Put \(L=6438\).  A cell is \(c=(\ell,s)\), with

\[
 1\le\ell\le3,\qquad 0\le s\le L-\ell,\qquad
 I(c)=\{s,\ldots,s+\ell-1\},
\tag{1.2}
\]

and cells are numbered depth-major.  Define

\[
 \theta_0(c)=\bigvee_{p\in I(c)}A^0_p,\qquad
 \mathcal W_0(S)=\{c:\theta_0(c)=S\}.
\tag{1.3}
\]

A deterministic scan gives

\[
 |\{S:\mathcal W_0(S)\ne\varnothing\}|=16362,\qquad
 \sum_S|\mathcal W_0(S)|=19310,
\tag{1.4}
\]

with \(13982\) unique-witness targets.  The compact encoding
`[[target,[cell IDs]],...]` has SHA

```text
5c146b5c36fd9e23f78810d1f3cee4e73a6268d7109ff03e1f494df9eedc48ee
```

and

\[
 \mathcal W_0(7682)=\{6437\},\qquad
 \mathcal W_0(7683)=\{12874\}.
\tag{1.5}
\]

The selected pin \(m_0(S)\) is read from the frozen `m0` array.  It is always
an exact \(A^0\)-witness, but it need not be the least occurrence in
\(\mathcal W_0(S)\); this distinction occurs for \(380\) targets.

## 2. Gap geometry and two different defect ledgers

For a three-seam move

\[
 T=A\mid B\mid C\mid D
 \longmapsto
 T'=A\mid\epsilon_C(C)\mid\epsilon_B(B)\mid D,
\tag{2.1}
\]

write \(B=T[a,u)\), \(C=T[u,v+1)\), and \(b_C=v-u+1\).  The old and new
source gaps are

\[
 G_-=\bigcup_{s\in\{a,u,v+1\}}\{s,s+1,s+2\},
\qquad
 G_+=\bigcup_{s\in\{a,a+b_C,v+1\}}\{s,s+1,s+2\}.
\tag{2.2}
\]

Let

\[
 \mathcal E_\pm=\{c:I(c)\cap G_\pm\ne\varnothing\};
\qquad |\mathcal E_\pm|\le36.
\tag{2.3}
\]

There are two different ledgers.

First, the **strict selected-pin defect** is

\[
 D_-=
 \{S\in\mathcal C_0\setminus\{7682,7683\}:
             I(m_0(S))\cap G_-\ne\varnothing\}.
\tag{2.4}
\]

The literal subcase that transports every particular selected \(M_0\) pin
requires \(D_-=\varnothing\).  This is stronger than target preservation.

Second, for the adaptive theorem define the last-safe-witness set

\[
 R_-=
 \{S\in\mathcal C_0:
      \mathcal W_0(S)\subseteq\mathcal E_-\}.
\tag{2.5}
\]

Targets outside \(R_-\) retain a safe occurrence after core transport.
Targets in \(R_-\) are not a no-go: they become mandatory exceptional
services.  Both ledgers are computed by scanning at most thirty-six old
cells.

### Proposition 2.1 (strict transport is universally blocked)

For the frozen selected \(M_0\), every possible three-position source gap
\(\{g,g+1,g+2\}\), \(0\le g\le6435\), meets at least five selected \(M_0\)
pins outside \(\{7682,7683\}\).  The coverage histogram over the \(6436\)
gap starts is

\[
\begin{array}{c|rrrrrrrr}
\text{pins met}&5&6&7&8&9&10&11&12\\ \hline
\text{gap starts}&6&61&206&484&853&1210&1520&2096.
\end{array}
\tag{2.6}
\]

Consequently \(D_-\ne\varnothing\) for every genuine braid.  Thus the
literal all-\(M_0\)-pin transport subcase of Proposition 8.1 is empty.

#### Proof

A selected cell \([s,s+\ell-1]\) meets the gap \([g,g+2]\) exactly when

\[
 s-2\le g\le s+\ell-1.
\tag{2.7}
\]

Add \(1\) on this interval of gap starts for each frozen selected pin other
than \(7682,7683\).  The resulting difference-array prefix sums give (2.6),
whose minimum is five.  This calculation is independently rebuilt by the
verifier specified in Section 6. \(\square\)

This proposition does not obstruct the adaptive collar: it says only that
some selected pins must be replaced by alternate safe witnesses or by
exceptional services.

## 3. Endpoint-conditioned adaptive services

Let \(\eta\in\{s,p\}\) denote one of the endpoint tails

\[
\begin{aligned}
E^s_{6432,\ldots,6437}
  &=(17937,1585,1571,1603,3651,7267),\\
E^p_{6432,\ldots,6437}
  &=(17937,1585,1571,1603,3139,7267),
\end{aligned}
\tag{3.1}
\]

with \(E^\eta=A^0\) before position \(6432\).  Assume \(G_-\) and \(G_+\)
are separated from \(J=[6432,6437]\) in the exact sense of Proposition 8.1.

For a target \(S\in\mathcal C_0\), let \(\mathcal S_\eta(S)\) be the set of
safe final witnesses obtained as follows: take every old cell outside
\(\mathcal E_-\), evaluate its trace in \(E^\eta\), and transport that cell
to the new safe core.  Define the **endpoint-conditioned service set**

\[
 \mathcal R_\eta=
 \{S\in\mathcal C_0:\mathcal S_\eta(S)=\varnothing\}.
\tag{3.2}
\]

This definition automatically includes \(7682,7683\), because (1.5) is
destroyed by either endpoint tail.  It also includes every internal
last-witness loss not recreated accidentally in the terminal cells.  Every
target outside \(\mathcal R_\eta\) has an explicitly named safe final
witness; every target in \(\mathcal R_\eta\) must be assigned to a distinct
new exceptional cell in \(\mathcal E_+\).

### Lemma 3.1 (adaptive capacity cut)

Every separated fixed-core collar preserving \(\mathcal C_0\) through
endpoint branch \(\eta\) satisfies

\[
 |\mathcal R_\eta|\le|\mathcal E_+|\le36.
\tag{3.3}
\]

#### Proof

A final cell outside \(\mathcal E_+\) is a transported safe cell, so its
trace is already counted in \(\mathcal S_\eta\).  Hence every target in
\(\mathcal R_\eta\) needs a cell in \(\mathcal E_+\).  Different target
labels need different cells. \(\square\)

For the two direct authoritative-H19 braids:

\[
\begin{array}{c|c|c|c|c}
\text{move}&|R_-|&|\mathcal R_s|&|\mathcal R_p|&|\mathcal E_+|\\ \hline
\mathrm{FR}(3814,4556,5539)\ (\text{c0440})&33&35&35&36\\
\mathrm{RF}(688,2636,2650)\ (\text{c0520})&36&38&38&36.
\end{array}
\tag{3.4}
\]

Therefore c0520 is an exact adaptive capacity no-go.  The c0440 move has
exactly one exceptional dump cell of slack and is the surviving direct
candidate.

The rows in (3.4) are relative to the authoritative H19 parent.  They must
not be transferred to c0434, c0668, or any other child of c0440 without
rebuilding that child's old word and witness bank.

## 4. The maximal Q-table

The move gives a canonical new-core-to-old-core bijection

\[
 \psi:[0,L-1]\setminus G_+
      \longrightarrow[0,L-1]\setminus G_-.
\tag{4.1}
\]

A verifier derives \(\psi\) from the move.  After installing endpoint branch
\(\eta\), define the fixed new core \(F^\eta\) by transporting \(A^0\) away
from \(J\) and using (3.1) on \(J\).  Let

\[
 P'_p=\bigcap_{i=\max(0,p-3)}^{\min(W-1,p)}T'_i.
\tag{4.2}
\]

For exceptional pins \(\Pi\), reject any pin \((S,c)\) whose interval has a
fixed-core position with \(F^\eta_p\not\subseteq S\), and otherwise put

\[
 Q_p^\eta(\Pi)=
 \begin{cases}
 F^\eta_p,&p\notin G_+,\\[1mm]
 P'_p\cap\displaystyle\bigcap_{(S,c)\in\Pi:\ p\in I(c)}S,&p\in G_+.
 \end{cases}
\tag{4.3}
\]

Call \(\Pi\) Q-feasible if every \(Q_p\) is nonempty, every selected
interval has its exact label OR, and every four-letter OR is \(T'_i\).

### Lemma 4.1 (maximal-Q equivalence)

With the transported core fixed, a gap filling realizing all pins in
\(\Pi\) exists if and only if \(Q^\eta(\Pi)\) is feasible.

#### Proof

Every admissible gap letter is contained in (4.3), since it must lie in its
erosion envelope and in every selected label crossing its position.  Thus
any feasible filling is coordinatewise below \(Q\).  Such a filling proves
that \(Q\) is nonempty and supplies every required selected and middle bit.
The negative conditions and erosion envelopes prevent excess bits.  Hence
\(Q\) is itself feasible.  The converse is immediate. \(\square\)

Thus an empty row, missing selected bit, or missing middle bit is a monotone
exact Benders no-good.

## 5. Exact adaptive assignment theorem and no-go object

For \(S\in\mathcal R_\eta\), let \(\Gamma_\eta(S)\) be the exceptional cells
\(c\in\mathcal E_+\) for which the unary pin \((S,c)\) is Q-feasible.

### Theorem 5.1 (adaptive witness-bank collar)

A separated fixed-core collar preserving every target in \(\mathcal C_0\)
and using endpoint branch \(\eta\) exists if and only if there is an
injection

\[
 \alpha:\mathcal R_\eta\longrightarrow\mathcal E_+,
\qquad
 \alpha(S)\in\Gamma_\eta(S),
\tag{5.1}
\]

such that the full pin set

\[
 \Pi_\alpha=\{(S,\alpha(S)):S\in\mathcal R_\eta\}
\tag{5.2}
\]

is Q-feasible.  A passing assignment produces a literal word covering
\(\mathcal C_0\cup\{7267\}\), hence residual at most twenty.

#### Proof

All targets outside \(\mathcal R_\eta\) have named safe final witnesses.
Every target inside it must occur in \(\mathcal E_+\), and distinct labels
need distinct cells, proving necessity of an injection.  Lemma 4.1 gives
necessity of joint Q-feasibility.  Conversely, the safe bank plus a passing
\(\Pi_\alpha\) covers all of \(\mathcal C_0\); the endpoint branch supplies
\(7267\), and separation makes the two collars commute. \(\square\)

A positive certificate is the injection and its at most nine Q letters.
A solver-free negative certificate can be any of:

1. the capacity cut (3.3);
2. a unary Hall shore \(H\subseteq\mathcal R_\eta\) with
   \(|N_\Gamma(H)|<|H|\); or
3. a complete Benders decision DAG.

At a decision-DAG node, record forced and forbidden service-cell pins.
A leaf is certified either by a Q-obligation failure of the forced pins or
by a Hall shore in the residual unary graph.  An edge is residual precisely
when its service is unassigned, its cell is unused, it is not forbidden, and
adjoining it to the forced pins remains Q-feasible.  At an internal node choose one
unassigned service \(S\); its children force each such residual edge
\((S,c)\), and the child cell is deleted from all other rows.  A verifier
checks that the children exhaust the complete current neighborhood.  A
finite tree whose every leaf is certified proves that no injection can pass,
without trusting a solver or recomputing a matching.

The obstruction records are canonical:

```text
fixed_core_negative: pin, position, forbidden_mask
empty_row:            forced_pins, position
selected_positive:   forced_pins, target, cell, missing_mask
middle:               forced_pins, middle_index, missing_mask
hall:                 unassigned_targets, available_cells, H, N(H)
```

The Hall leaf is verified by direct neighborhood union; no maximum matching
call is required.

## 6. Proof-safe artifacts and checks

The strict-gap certificate is verified by

```text
scratch/verify_k15_h19_prop8_1_m0_gap_cover_nogo_20260729.py
scratch/verify_k15_h19_prop8_1_direct_service_ledgers_20260729.py
```

Their SHA-256 values are respectively

```text
711e8976b6358ff3c1a1078da4021730ccbf1999d724a0682e0b0884a0431511
1a32c76784c5ed595f9347300e41b54d691088729a48e57b12347c00673937ef
```

Both are based on the frozen \(A(M_0)\) artifact.  The second verifies every
entry of (3.4), including the complete service lists and their hashes.  A full adaptive
candidate verifier should:

1. hash and verify the frozen baseline artifact, including \(D^3A^0=T\),
   all selected \(M_0\) pins, \(\mathcal C_0\), and (1.4)--(1.5);
2. rebuild \(T'\), \(G_\pm\), \(\mathcal E_\pm\), and the core transport
   from the move;
3. verify Johnson legality, residence, every upper depth, and exact terminal
   separation;
4. install each endpoint tail and rebuild the safe final bank
   \(\mathcal S_\eta\) and service set \(\mathcal R_\eta\);
5. apply the capacity and unary Hall prefilters;
6. verify a positive injection/Q-table or every leaf and branch of the
   negative Benders DAG;
7. for a positive result, directly verify the final word, all safe witnesses,
   all exceptional services, \(D^3A=T'\), and the \(7267\) endpoint pin.

No matching, SAT, CP-SAT, or optimization call is needed in the verifier.
The producer may use remote search to find an assignment or a compact
decision DAG.

The exact negative scope is the selected move, the frozen \(A(M_0)\), its
fixed transported core, and the separated endpoint branch.  It does not
exclude an overlapping joint collar, a core-changing collar, a different
old common word, or the interior \(685/1581\) route.
