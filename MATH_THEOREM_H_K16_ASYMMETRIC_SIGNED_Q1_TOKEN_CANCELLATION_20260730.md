# The repaired asymmetric K16 carrier: signed q1 token cancellation and its exact Farkas gate

Date: 2026-07-30

Lane: H

Status: solver-free structural theorem and a source-specific literal token
certificate. Its original catalogue boundary is superseded by
MATH_THEOREM_H_K16_ASYMMETRIC_PEELING_FARKAS_AND_C8_ORBIT_DESCENT_20260730.md,
which proves the C3--C5 compound no-go and the sharp C8 escape.

## 0. Result and boundary

Let \(z\) be coordinate \(15\), and use the repaired carrier

    scratch/k16_asymmetric_triangle_orbit_repair_20260729.json
    SHA-256 6044bd63b7281c358c6c33399ccf2dd15143f783535cb6fe6b85a797c04affdc

This note proves the following.

1. Every spanning two-factor of \(J(16,8)\) has a single cross-shore
   parameter \(t\). Relative to the repaired no-cross carrier, its four q1
   sector masses change by

   \[
   (\Delta L_{\bar z},\Delta L_z,\Delta U_{\bar z},\Delta U_z)
      =(t,-t,-t,t).
   \tag{0.1}
   \]

   Cross seams create slack on the two formerly exact sectors, but every
   unit is paid for by one occurrence from each of the two 1430-unit slack
   sectors. Cross compensation is a quota-bank transfer, not free q1 repair.

2. For a compatible packet, q1 cancellation is literal and colourwise:
   added minus deleted multiplicity at colour \(C\) must be at least the
   negative of its old slack. In a pure \(B\)-rail packet, upper-q1
   cancellation is equality at every colour. Equivalently, the packet's
   old-colour-to-new-colour arrows form an Eulerian directed circulation.

3. Every new provider of one of the 45 residual lower-q2 targets is a
   \(BBB\) path and uses at least one new \(BB\) edge. Such an edge moves a
   baseline-unique \(B\)-upper token. A token move is self-neutral only if
   its old and new upper colours agree; otherwise a remote return-token path
   is mandatory. Repairing \(g\) distinct lower holes needs at least
   \(\lceil g/2\rceil\) distinct new \(BB\) edges, hence at least 23 here.
   In a pure-\(B\) packet these edges induce at least 23 token arrows.

4. A complete linear Farkas alternative is given for any saved additive
   packet catalogue. It cleanly separates this signed-q1 gate from the later
   quota-bank/port Hall problem.

The original audited short-cycle summaries contain 75, 95, 180, and 988 deep-safe
positive circuits of lengths two, three, four, and five, respectively, and
none is individually q1-safe. They do not store the signed colour columns of
those circuits. Individual failure does not imply a common Farkas ray.
Therefore the results proved up to this point in the note do not by
themselves claim that pairs or larger packets are impossible.

## 1. Four q1 sectors of the \(A\mid B\) split

Write

\[
 A=\binom{[15]}8,\qquad
 B=\{z\}+\binom{[15]}7,\qquad
 N=|A|=|B|=\binom{15}7=6435.
\tag{1.1}
\]

Partition the q1 colours into

\[
\begin{array}{c|c|c}
\text{sector}&\text{colours}&\text{size}\\ \hline
L_{\bar z}&\binom{[15]}7&6435,\\
L_z&\{z\}+\binom{[15]}6&5005,\\
U_{\bar z}&\binom{[15]}9&5005,\\
U_z&\{z\}+\binom{[15]}8&6435.
\end{array}
\tag{1.2}
\]

An \(AA\) edge contributes to \(L_{\bar z}\) and \(U_{\bar z}\); a
\(BB\) edge contributes to \(L_z\) and \(U_z\); and an \(AB\) edge
contributes to \(L_{\bar z}\) and \(U_z\).

### Theorem 1.1 (exact cross-shore surplus transfer)

Let \(F\) be any spanning two-factor of \(J(16,8)\). There is an integer
\(t\ge0\) such that

\[
 |E_{AB}(F)|=2t,\qquad
 |E_{AA}(F)|=|E_{BB}(F)|=N-t.
\tag{1.3}
\]

Consequently the four q1 occurrence masses are

\[
\begin{array}{c|cccc}
 &L_{\bar z}&L_z&U_{\bar z}&U_z\\ \hline
\text{mass}&N+t&N-t&N-t&N+t.
\end{array}
\tag{1.4}
\]

If all four q1 sectors are covered, their total excesses above load one are

\[
 t,\qquad 1430-t,\qquad 1430-t,\qquad t
\tag{1.5}
\]

in the order of (1.4). In particular \(0\le t\le1430\).

#### Proof

The degree sum on \(A\) is

\[
 2|E_{AA}|+|E_{AB}|=2N,
\]

and the same equation on \(B\) has \(E_{BB}\) in place of \(E_{AA}\).
Hence \(|E_{AB}|\) is even, say \(2t\), and (1.3) follows. The edge-type
contributions above give (1.4). Subtract the sector sizes in (1.2). Since

\[
 N-\binom{15}6=6435-5005=1430,
\]

one obtains (1.5), whose nonnegativity gives the bound on \(t\).
\(\square\)

The repaired source has \(t=0\). Its exact shore histograms are

\[
\begin{array}{c|c}
L_{\bar z}&1^{6435}\\
L_z&1^{3660}2^{1260}3^{85}\\
U_{\bar z}&1^{3675}2^{1230}3^{100}\\
U_z&1^{6435}.
\end{array}
\tag{1.6}
\]

Thus \(L_{\bar z}\) and \(U_z\) are tight colour banks. A mixed packet with
\(t\) cross pairs injects exactly \(t\) duplicate occurrences into each
tight bank while removing exactly \(t\) occurrences from each slack bank.

## 2. Exact signed cancellation

Let the old q1 load of literal colour \(C\) be \(m_C\ge1\), and put

\[
 s_C=m_C-1.
\tag{2.1}
\]

For a base-relative packet \(P\), let \(D_C(P)\) and \(A_C(P)\) be the
numbers of deleted and added occurrences of \(C\), and define

\[
 \Delta_C(P)=A_C(P)-D_C(P).
\tag{2.2}
\]

Both lower and upper q1 colours are separate coordinates.

### Theorem 2.1 (colourwise packet criterion)

A literal final edge set obtained from the old factor by \(P\) is q1
complete if and only if

\[
 \boxed{\Delta_C(P)\ge-s_C\quad\text{for every q1 colour }C.}
\tag{2.3}
\]

If \(P_1,\ldots,P_h\) are mutually compatible base-relative packets whose
edge deltas add, their union is q1 complete if and only if

\[
 \sum_{j=1}^h\Delta_C(P_j)\ge-s_C
 \quad(C\text{ arbitrary}).
\tag{2.4}
\]

#### Proof

The final load is

\[
 m_C-D_C(P)+A_C(P)=1+s_C+\Delta_C(P).
\]

Its positivity is (2.3). Additivity gives (2.4). \(\square\)

For two fixed circuits, (2.4) is the exact cancellation test. A debt in a
tight colour can be repaired only by a credit in that same literal colour.
The number of debts, their orbit names, or their total multiplicity do not
replace (2.4).

For overlapping or sequential circuits, frozen columns need not add. In
that case Theorem 2.1 remains exact after computing the final deleted and
added edge multisets, but summing the original one-circuit columns is not
proof-safe.

## 3. The upper-token circulation on the \(B\)-rail

For a \(BB\) edge \(e=XY\), call

\[
 \kappa(e)=X\cup Y\in U_z
\tag{3.1}
\]

its upper token. In the repaired carrier every colour in \(U_z\) occurs on
exactly one old edge.

Consider a pure-\(B\) packet deleting \(e_1,\ldots,e_h\) and adding
\(f_1,\ldots,f_h\). Pair these lists arbitrarily, or use the canonical
same-tail pairing for a head-permutation circuit, and draw the arrows

\[
 \kappa(e_i)\longrightarrow\kappa(f_i).
\tag{3.2}
\]

### Theorem 3.1 (Eulerian token criterion)

The pure-\(B\) packet preserves upper q1 if and only if the directed
multigraph (3.2) has equal indegree and outdegree at every token colour.
Equivalently,

\[
 \{\!\{\kappa(e_i):1\le i\le h\}\!\}
 =
 \{\!\{\kappa(f_i):1\le i\le h\}\!\}.
\tag{3.3}
\]

Hence its nonloop arrows decompose into directed cycles. Two individually
unsafe pure-\(B\) circuits cancel exactly when their signed upper-token
vectors are negatives of one another. A family cancels exactly when its
aggregate token graph is Eulerian.

#### Proof

For token \(U\), added occurrences are the arrows entering \(U\), and
deleted occurrences are the arrows leaving \(U\). Thus its signed load
change is indegree minus outdegree. The old \(U_z\) bank has 6435 colours,
6435 occurrences, and load one at every colour. A pure-\(B\) packet retains
6435 total \(BB\) edges. Upper-q1 completeness therefore forces load one,
not merely positive load, at every colour. This is zero divergence at every
vertex, equivalent to (3.3) and to an Eulerian circuit decomposition.
\(\square\)

The complementary statement holds for a pure-\(A\) packet with exact lower
token \(e\mapsto X\cap Y\in L_{\bar z}\).

In an upper-q1-complete mixed final factor, Theorem 1.1 gives the exact
correction. On \(U_z\), every deleted old token must still be restored at
the same colour, but there are exactly \(t\) unmatched added occurrences
after those restorations. Those \(t\) extra occurrences are the cross-bank
slack, and they cost \(t\) occurrences in each of \(L_z\) and
\(U_{\bar z}\).

## 4. Why every lower-q2 repair moves a unique upper token

Every residual lower-q2 target contains \(z\). Let

\[
 L=\{z\}\cup S,\qquad |S|=5.
\]

Any provider \(X_0X_1X_2\) lies wholly in \(B\). Its bow-tie normal form is

\[
\begin{aligned}
X_1&=\{z\}\cup S\cup\{p,q\},\\
X_0&=\{z\}\cup S\cup\{q,a\},\\
X_2&=\{z\}\cup S\cup\{p,b\}.
\end{aligned}
\tag{4.1}
\]

### Theorem 4.1 (unique-upper token tax)

Suppose \(L\) is not witnessed in the repaired source but is witnessed by
\(X_0X_1X_2\) after a rethread.

1. At least one of \(X_0X_1,X_1X_2\) is a new \(BB\) edge.
2. In a pure-\(B\), upper-q1-complete final factor the two upper colours

   \[
   U_a=\{z\}\cup S\cup\{p,q,a\},\qquad
   U_b=\{z\}\cup S\cup\{p,q,b\}
   \tag{4.2}
   \]

   are distinct. Each new provider edge therefore moves one
   baseline-unique upper token. It is locally token-neutral only when the
   old edge paired with it has the same upper colour.
3. If \(g\) distinct missing lower targets become witnessed, at least
   \(\lceil g/2\rceil\) distinct new \(BB\) edges occur. Thus repairing all
   45 present holes needs at least 23 such edges; in a pure-\(B\) packet
   they induce at least 23 token arrows. In a free
   \(C_{15}\)-equivariant repair the earlier orbit count strengthens this to
   30 physical seams.

#### Proof

All three owners contain \(z\), proving the \(BBB\) assertion. If both
provider edges were old, they would be the two old factor edges incident
with \(X_1\); hence they already formed the same three-state window and
would already have witnessed \(L\). This proves part 1.

The two unions in (4.2) agree exactly when \(a=b\). In that case the final
factor would contain two distinct \(BB\) edges of one upper colour. A pure
\(B\) upper-complete factor has exactly one edge per upper colour by Theorem
3.1, so \(a\ne b\). The token statement follows from the baseline load-one
property.

A factor edge belongs to only the two three-state windows immediately to
its left and right. It can therefore create at most two new lower-q2
targets. Counting new edges against \(g\) distinct gained targets gives the
ceiling bound. \(\square\)

The theorem is intentionally about unique upper colours. The analogous
lower-colour claim is false. In the actual repaired carrier,

\[
 (34109,34103,34135)
\tag{4.3}
\]

is a Johnson bow-tie with intersection \(34069\), one of the residual
holes. Its lower edge colours are \(34101\) and \(34071\), both of source
load two. Its upper colours are \(34111\) and \(34167\), both of source
load one.

Both edges in (4.3) are new. The old edges at its centre \(34103\) are

\[
 (34103,34151),\qquad(34103,38167),
\]

with upper colours \(34167\) and \(38199\). Replacing those two centre
edges by the bow-tie edges has local upper-token delta

\[
 \boxed{e_{34111}-e_{38199}.}
\tag{4.4}
\]

The unique old provider of \(34111\) is \((33855,34079)\). Thus the
isolated bow-tie is blocked by the singleton lost row \(38199\); a remote
inverse token transfer is mandatory. This is a literal source-specific
example, not a claim that the required inverse is globally impossible.

## 5. Exact Farkas obstruction for a saved packet catalogue

Fix a catalogue of base-relative packets whose q1 and deep columns are
additive on every compatible selection under consideration. Let

* \(D\) be the matrix of signed q1 columns \(\Delta(P)\);
* \(G\) be the matrix of signed service/deep columns;
* \(s\ge0\) be the baseline q1 slack vector; and
* \(d\ge0\) be the required deep demand vector.

Ignore integrality, upper bounds, port conflicts, and packet overlap. The
relaxed system is

\[
 Dy\ge-s,\qquad Gy\ge d,\qquad y\ge0.
\tag{5.1}
\]

### Theorem 5.1 (signed-q1 Farkas alternative)

System (5.1) is infeasible if and only if there are
\(\alpha,\beta\ge0\) such that, for every packet column \(P\),

\[
 \alpha^{\mathsf T}D_P+\beta^{\mathsf T}G_P\le0,
\tag{5.2}
\]

and

\[
 \beta^{\mathsf T}d>\alpha^{\mathsf T}s.
\tag{5.3}
\]

#### Proof

Write (5.1) as

\[
 -Dy\le s,\qquad -Gy\le-d,\qquad y\ge0.
\]

The Farkas alternative gives nonnegative row multipliers
\((\alpha,\beta)\) with

\[
 -\alpha^{\mathsf T}D-\beta^{\mathsf T}G\ge0,\qquad
 \alpha^{\mathsf T}s-\beta^{\mathsf T}d<0,
\]

which are (5.2)--(5.3). Conversely, for any putative solution,

\[
 0\ge(\alpha^{\mathsf T}D+\beta^{\mathsf T}G)y
 \ge-\alpha^{\mathsf T}s+\beta^{\mathsf T}d>0,
\]

a contradiction. \(\square\)

A transparent sparse certificate chooses a set \(\mathcal P\) of q1
colours, puts \(\alpha=1_{\mathcal P}\), and verifies for every catalogue
packet \(K\)

\[
 \beta^{\mathsf T}G_K
 \le \operatorname{del}_{\mathcal P}(K)
      -\operatorname{add}_{\mathcal P}(K).
\tag{5.4}
\]

If \(\mathcal P\) lies in a tight sector, then
\(\alpha^{\mathsf T}s=0\), and (5.4) excludes every positive weighted
service demand. Packing, degree, or port-capacity inequalities may be
included with their usual nonnegative dual multipliers. A certificate for
the relaxed cone is a sound obstruction to every integral compatible
packet, although the converse need not hold after integrality and
compatibility are restored.

For upper-token cancellation alone in a pure-\(B\) catalogue, let
\(T=D|_{U_z}\) be the tight upper-token block. Gordan's theorem gives the
homogeneous form: a nonzero \(y\ge0\) with \(Ty=0\) exists if and only if
there is no colour potential \(\phi\) satisfying

\[
 \phi^{\mathsf T}T_P>0
 \quad\text{for every candidate }P.
\tag{5.5}
\]

The slack \(L_z\) rows still require \(D|_{L_z}y\ge-s|_{L_z}\); (5.5)
does not replace them.

The three-token chain \(a\to b,b\to c,c\to a\) shows why the absence of a
safe singleton or pair does not itself rule out a larger packet.

## 6. Relation to the quota bank and the exact remaining artifact

The quota-bank theorem in
THREAD_A_K16_ASYMMETRIC_123_ORBIT_PROVIDER_AND_QUOTA_FACTOR_THEOREM_20260729.md
selects service seams and then asks for colour-resolved endpoint Hall. The
present theorem is logically upstream:

1. signed q1 token columns must first admit colourwise cancellation;
2. the chosen columns must be compatible and preserve every deep survivor;
3. only then may residual ports pass to quota-bank matching/Hall completion.

Balanced q1 marginals do not imply step 1, and step 1 does not imply steps 2
or 3.

The saved post-repair short-cycle artifacts prove, at their stated
fixed-q2/fixed-q3 catalogue scope,

\[
\begin{array}{c|rrrr}
\text{circuit length}&2&3&4&5\\ \hline
\text{deep-safe positive circuits}&75&95&180&988\\
\text{also q1-safe}&0&0&0&0.
\end{array}
\tag{6.1}
\]

Those original JSON files store aggregate counts, histograms, and a bounded
maximum-example list, but not the complete per-circuit signed q1 catalogue
\(D_P\). That limitation has now been removed for the deep-safe gainful
C3--C5 core by

    scratch/k16_asymmetric_signed_compound_cycle_catalogue_20260730.json

The follow-up theorem cited in the status line turns its two-round peeling
certificate into one common integral Farkas potential and proves that no
nonempty nonnegative C3--C5 core combination is q1-feasible. It also proves
that this obstruction is sharp: a commuting C8 orbit gives a literal
108-to-93 descent. The general alternatives (5.1)--(5.5) remain the correct
framework for larger or auxiliary catalogues.

## 7. Lightweight audit

The replay files are

    scratch/audit_k16_asymmetric_signed_q1_token_ledger_20260730.py
    scratch/k16_asymmetric_signed_q1_token_ledger_20260730.audit.json

They hash-pin the repaired factor and the length-two-through-five aggregate
censuses. Without enumerating any circuit, the replay verifies:

* 12,870 distinct middle owners and only 6,435 \(AA\) plus 6,435 \(BB\)
  edges;
* the four literal q1 histograms (1.6);
* all 45 residual lower-q2 holes contain \(z\);
* the 23-edge counting floor;
* the aggregate counts (6.1); and
* every mask, edge, load, incumbent edge, and token delta in (4.3)--(4.4).

No SAT, CP, LP solver, cycle enumeration, remote job, or sustained local
computation was used.
