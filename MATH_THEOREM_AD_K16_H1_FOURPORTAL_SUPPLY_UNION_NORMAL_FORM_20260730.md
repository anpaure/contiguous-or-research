# K16 H1 four-portal supply-union normal form

Date: 2026-07-30  
Lane: AD  
Status: **proved exact for the frozen joint13 support; UNSOLVED/UNKNOWN**

## 1. Frozen scope

The source word is

```text
scratch/k16_h2_to_h1_p0.h1.word
SHA-256 ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a
```

and the editable flat-coordinate blocks are

\[
B_0=[0,2),\quad B_1=[2,6),\quad B_2=[6,9),\quad B_3=[9,13),
\]

corresponding to physical positions

```text
{0,1}, {4486,4487,4488,4489}, {6438,6439,6440},
{12869,12870,12871,12872}.
```

The independently audited geometry and the previous exact occupancy model are

```text
scratch/ad_k16_h1_four_portal_geometry_20260730.audit.json
SHA-256 3263ab64f540e5552f810f2dbf919d6b18da89310162ff8746c0f099e9b4a9d0

scratch/ad_k16_h1_fourportal_joint13_occupancy_20260730/model.cnf
SHA-256 251229383ec319a744fea37bd2f3f89bdf59e638727677166f0eaa7751ecd9bb

scratch/ad_k16_h1_fourportal_joint13_occupancy_20260730/model.map.json
SHA-256 f624e5684fe58c122d43371c16fbd4e1c8db9b9ae8a84930d3b9cf59a4758f31.
```

Deleting the thirteen editable cells leaves exactly 55 residual targets
\(R\).  Every \(T\in R\) contains coordinate \(c=6\).  Every literal
residual witness meets exactly one editable block, and each target has the 29
audited local charts

\[
             \alpha=(T,b,I,N),
\]

where \(I\) is a nonempty interval of \(B_b\) and \(N\subseteq T\) is the
exact residual need after adjoining the fixed prefix/suffix base.  There are
\(55\cdot29=1595\) charts before normalization.

All theorems below are restricted to arbitrary substitutions on these
thirteen cells.  They do not assert that an unrestricted length-12,873
solution can be moved into this support.

## 2. Exact union-blocker criterion

Choose one chart \(\alpha_T=(T,b(T),I_T,N_T)\) for every \(T\in R\).  For
a block \(b\) and a noncommon coordinate \(q\ne6\), define the blocker union

\[
 U_{b,q}=\bigcup_{\substack{T\in R:\ b(T)=b,\ q\notin T}} I_T.       \tag{2.1}
\]

### Theorem 2.1 (exact union-blocker normal form)

The following statements are equivalent.

1. Some universal word is obtained by changing only the thirteen frozen
   support cells, with no restriction on the number of changed cells.
2. There is one chart per residual target such that
   \[
      I_T\setminus U_{b(T),q}\ne\varnothing
      \qquad(T\in R,\ q\in N_T\setminus\{6\}).                    \tag{2.2}
   \]
3. There are Boolean supply flags \(X_{p,q}\), for editable flat cell \(p\)
   and \(q\ne6\), and one chart per target satisfying
   \[
   \begin{aligned}
     X_{p,q}&=0 &&(p\in I_T,\ q\notin T),                         \tag{2.3}\\
     \bigvee_{p\in I_T}X_{p,q}&=1
        &&(q\in N_T\setminus\{6\}).                              \tag{2.4}
   \end{aligned}
   \]

#### Proof

Assume a supported universal word.  Choose one actual literal witness for
each residual target.  Safe-gap localization turns it into one of the 29
local charts.  If \(q\in N_T\), some edited cell of the chosen \(T\)-witness
contains \(q\).  No chosen witness for a target omitting \(q\) can cross that
cell: every cell of a literal \(U\)-witness is a submask of \(U\).  Thus
(2.2) holds.

Condition (2.2) gives (2.3)--(2.4) by taking
\(X_{p,q}=1\) exactly when \(p\notin U_{b,q}\).  Conversely,
(2.3)--(2.4) imply (2.2) immediately.

Finally assume (2.2), and put at each editable cell

\[
 C_p=\bigcap\{T:p\in I_T\},                                      \tag{2.5}
\]

with the empty intersection interpreted as \(\mathtt{0xffff}\).  Every
nonempty intersection contains bit 6, so no \(C_p\) is zero.  Moreover

\[
 q\in C_p\quad\Longleftrightarrow\quad p\notin U_{b,q}.           \tag{2.6}
\]

Every \(C_p\) on \(I_T\) is a submask of \(T\), while (2.2) and (2.6)
supply every bit of \(N_T\).  Adjoining the exact fixed base of the chart
therefore gives literal OR exactly \(T\).  The other 65,480 targets retain a
fixed-only witness.  This constructs a universal supported word. \(\square\)

The flags in item 3 are existential certificates; equality with the full
intersection in (2.5) need not be imposed.  If a flag is true, (2.3) proves
that its coordinate is present in the actual intersection.  Conversely one
may set all true-intersection flags to one.  Thus the 195 reverse-equality
rows in the older occupancy model are unnecessary after existential
projection.

## 3. Four-block targetwise decomposition

For a local supply pattern \(X_b\), let

\[
 S_b(X_b)=\{T\in R:\text{some chart of }T\text{ in }B_b
                         \text{ satisfies (2.3)--(2.4)}\}.         \tag{3.1}
\]

### Corollary 3.1 (four-set union criterion)

The joint13 support is feasible if and only if there are four independently
chosen local supply patterns such that

\[
                  S_0(X_0)\cup S_1(X_1)\cup S_2(X_2)\cup S_3(X_3)=R. \tag{3.2}
\]

Indeed, after the four supply patterns are fixed, every target independently
chooses any serving block and chart.  Conditions (2.3) for those individual
choices jointly guarantee that every asserted supply survives all selected
target intersections.  There is no capacity constraint on a block or cell.

This is an exact decomposition, not a relaxation: the only global coupling
is the requirement that the four served-target sets cover \(R\).

### Corollary 3.2 (bounded obstruction certificate)

For fixed chart choices, every failed condition has a certificate consisting
of

* one demanded triple \((T,I_T,q)\); and
* at most \(|I_T|\le4\) selected charts of targets omitting \(q\), whose
  intervals cover \(I_T\).

To prove this, take an inclusion-minimal subfamily covering \(I_T\).  Every
member has a private cell of \(I_T\), and these private cells are distinct.
Hence the subfamily has at most \(|I_T|\) members.  With explicit chart
selectors, the resulting lazy no-good has arity at most five.  With five-bit
chart codes, the same no-good is one clause of length at most 25.  This is an
exact separator for a chart-choice master.

## 4. Sharp target-local chart dominance

For a chart \(\alpha=(T,I_\alpha,N_\alpha)\), write
\(P_\alpha(X)\) for the conjunction (2.3)--(2.4).  Every residual target
omits at least one tracked coordinate.

### Lemma 4.1 (exact implication criterion)

For two charts \(\alpha,\beta\) of the same target,

\[
P_\alpha\Longrightarrow P_\beta                                  \tag{4.1}
\]

if and only if

\[
 I_\beta\subseteq I_\alpha                                      \tag{4.2}
\]

and, for every \(q\in N_\beta\setminus\{6\}\),

\[
 q\in N_\alpha\setminus\{6\}\quad\text{and}\quad
 I_\alpha\subseteq I_\beta.                                    \tag{4.3}
\]

#### Proof

The zero constraints for any coordinate omitted by \(T\) imply (4.2), and
if (4.2) fails a flag outside \(I_\alpha\) falsifies the corresponding
\(\beta\)-row while preserving \(P_\alpha\).  For a coordinate required by
\(\beta\), implication is impossible unless it is required by \(\alpha\).
Even then, the sole true supply for that coordinate may be placed at any cell
of \(I_\alpha\); it is forced to meet \(I_\beta\) exactly when
\(I_\alpha\subseteq I_\beta\).  Coordinates are independent, proving both
necessity and sufficiency. \(\square\)

If \(N_\beta\setminus\{6\}\ne\varnothing\), (4.2)--(4.3) force equal
intervals; this catalogue has only one chart for an interval, so there is no
strict domination.  Strict domination occurs exactly when \(\beta\) has
common-bit-only need and its interval is properly contained in
\(I_\alpha\).

There are 30 ordered strict implication pairs and exactly 16 dominated
charts.  The normalized representatives are:

* for \(T\in\{\mathtt{0x28c9},\mathtt{0x38c9},\mathtt{0x39c9},
  \mathtt{0x79c9}\}\), retain \([2,2]\) and delete \([2,3],[2,4],[2,5]\);
* for \(T\in\{\mathtt{0x946d},\mathtt{0xd46d}\}\), retain \([8,8]\) and
  delete \([6,8],[7,8]\).

Thus 1,579 charts remain.  They form an antichain under pairwise logical
implication.  This proves that there is no further target-local deletion by
single-chart dominance; it does not rule out a more global or differently
extended encoding.

## 5. Supply-only quotient and exact compact CNF

Semantically, chart variables can be projected out altogether:

\[
 \exists X\ \bigwedge_{T\in R}\ \bigvee_{\alpha\in\mathcal A_T}P_\alpha(X).
                                                                    \tag{5.1}
\]

This is the exact supply-only quotient.  Of the \(13\cdot15=195\) possible
noncommon supply pairs, exactly \((p,q)=(2,8)\), physical position 4486 and
bit 8, has no positive occurrence in any retained need.  It can be fixed
false.  All 194 remaining pairs have distinct positive-incidence signatures,
and also distinct combined positive/blocker signatures.  Hence no additional
pair can be removed or identified by the elementary unused/duplicate-column
rules.  No stronger general minimality claim is made.

For an executable extension of (5.1), use five little-endian code bits per
target.  The code chooses one retained chart; unused codewords are forbidden.
Five bits are information-theoretically minimal only for this explicit
one-codeword-per-chart representation, since some targets retain 29 charts.
This is not a lower bound on arbitrary extended formulations.

The exact model census is:

| variable family | count |
|---|---:|
| target chart-code bits | \(55\cdot5=275\) |
| live supply bits | 194 |
| **total** | **469** |

| clause family | clauses | literals |
|---|---:|---:|
| invalid codewords | 181 | 905 |
| selected need has supply | 10,301 | 70,296 |
| selected omitter blocks supply | 22,587 | 135,522 |
| **total** | **33,069** | **206,723** |

For comparison, retaining all 1,595 charts gives the independently checked
pre-normalization census 469 variables, 33,428 clauses, and 208,893 literals.
The sixteen exact dominance deletions save 359 clauses and 2,170 literals.

## 6. Frozen artifacts and independent audit

```text
scratch/build_ad_k16_h1_fourportal_joint13_supplycode_cnf_20260730.py
SHA-256 461fdd2c57484f426f4706c7cbb6bbab72298821bb80c498f66691945e0af0ca

scratch/ad_k16_h1_fourportal_joint13_supplycode_20260730/model.cnf
SHA-256 0deab4e51bea5de51aab831ab3dace796caaa651d86614befcff078f48305eb8

scratch/ad_k16_h1_fourportal_joint13_supplycode_20260730/model.map.json
SHA-256 2c89b0f77e830139a7cb2027a1f76a6e2698efef88b1ee9b3b50fdb1606825f2
payload SHA-256 b93237175aa43430d0ba5910b99cd4e2ef7ff818c0149aadb73a086cfef8c330

scratch/decode_verify_ad_k16_h1_fourportal_joint13_supplycode_20260730.py
SHA-256 4011fc4e6df1cedc9254bc7a4ee94195f0aa37bec80a0adf880aa6e8b03dd966

scratch/audit_ad_k16_h1_fourportal_joint13_supplycode_independent_20260730.py
SHA-256 9c675b9876b602cfe15df95deed81f5e3cb992ad187ad9b4f1efd512bdf83533

scratch/ad_k16_h1_fourportal_joint13_supplycode_20260730/model.independent_audit.json
SHA-256 d7e7b917bababca25dc5de5d100c01f3cbfdd593d0cc8c6751d5520507aa316b
payload SHA-256 081812a9bd0c620be1939925eea72762b7cb23e267eb35429802428d0fc0bbd5
```

The independent auditor does not import or execute the builder.  It derives
the exact implication relation, the 16 deletions, the 194 live supply pairs,
the variable allocation, and all 33,069 clauses in order from the older
audited occupancy map.  It reports `PASS_UNSOLVED_UNKNOWN`.  The decoder was
also tested fail-closed on an empty assignment: it rejected before producing
either output artifact.

No SAT solver was launched and the already running raw H100 model was not
duplicated.  The reduced model has no SAT assignment and no UNSAT proof at
present.  Its status is exactly **UNSOLVED/UNKNOWN**, and it does not change
the authenticated bracket

\[
                         12873\le \nu(16)\le12874.
\]
