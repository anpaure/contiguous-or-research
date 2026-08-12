# K16-to-K17 Pascal occurrence selection: exact interval criterion and an opposite-choice no-go

Date: 2026-07-31  
Status: general interval lemmas proved; the fixed-carrier no-go is solver-free and independently replayed  
Scope: the fixed K16 carrier `scratch/k16_true_fourfilter_endpoint_reroot_targets_20260731.word`

## 0. Result

Let

\[
T=(T_0,\ldots,T_{12869})
\]

be the authenticated K16 middle carrier, and let

\[
c_p=T_p\cup T_{p+1}\qquad(0\le p<12869)
\]

be its rank-nine edge colours.  Every rank-nine mask occurs at least once.
The proposed even-to-odd Pascal lift selects one physical occurrence of each
rank-nine colour and orders the 11440 colours by their selected positions.

This selection problem is **infeasible for this carrier**.  The obstruction
is already supported on two upper targets and one repeated colour:

\[
\begin{array}{c|c}
\text{upper target}&\text{forced choice for colour }0x0bf5\\ \hline
0x1bf5&\text{edge position }9176,\\
0x0ff5&\text{edge position }10616.
\end{array}
\]

The colour `0x0bf5` occurs only at those two positions.  Hence the two
targets cannot both be consecutive unions in the selected shadow word.

This does **not** obstruct K17, a different K16 carrier, a rethreaded edge
deck, or a two-shore construction not obtained by selecting one occurrence
of every edge colour from this fixed chronology.

## 1. Abstract occurrence-selection model

Let a physical line have positions `0,...,N-1`.  Each position has a colour
\(c_p\) from a finite set \({\cal C}\), and let

\[
O(c)=\{p:c_p=c\}.
\]

Choose one occurrence

\[
x_c\in O(c)\qquad(c\in{\cal C})
\tag{1.1}
\]

and list the colours in increasing order of \(x_c\).  Distinct colours
cannot select the same physical position, so this is a well-defined word.
For a set target \(S\), call a colour **good** when \(c\subseteq S\) and a
**blocker** otherwise.

For a physical interval \(I=[a,b]\), define

\[
G_I(S)=\{c\subseteq S:x_c\in I\},\qquad
B_I(S)=\{c\not\subseteq S:x_c\in I\}.
\]

### Theorem 1.1 (fixed-choice interval criterion)

For a fixed selection \(x\), the selected shadow word has a consecutive
subword with union exactly \(S\) if and only if some physical interval
\(I=[a,b]\) satisfies

\[
B_I(S)=\varnothing,
\qquad
\bigcup_{c\in G_I(S)}c=S.
\tag{1.2}
\]

#### Proof

The selected colours whose positions lie in a physical interval form a
consecutive subword.  Its union is \(S\) exactly when every selected colour
inside is good and those good colours cover \(S\).

Conversely, take any consecutive subword and let \(a,b\) be the selected
positions of its first and last colours.  The selected positions in
\([a,b]\) are exactly that subword, so (1.2) holds. \(\square\)

### Theorem 1.2 (individual-feasibility criterion)

There exists *some* selection \(x\) for which \(I=[a,b]\) witnesses \(S\)
if and only if

\[
O(c)\setminus I\ne\varnothing
\quad\text{for every blocker }c,
\tag{1.3}
\]

and

\[
\bigcup_{\substack{c\subseteq S\\O(c)\cap I\ne\varnothing}}c=S.
\tag{1.4}
\]

#### Proof

Condition (1.3) is precisely the ability to select every blocker outside
\(I\).  Condition (1.4) is precisely the ability to select enough good
colours inside \(I\) to cover \(S\).  These choices are independent across
colours.  All remaining good colours may be selected arbitrarily. \(\square\)

Thus individual feasibility is not a Hall problem: each colour is an
independent variable, and a single interval is checked coordinatewise.

## 2. The maximal-right-endpoint lemma

Put \(m_c=\min O(c)\) and \(M_c=\max O(c)\).  For a fixed left endpoint
\(a\), define

\[
b_S(a)=
\min\bigl(\{M_c-1:c\not\subseteq S,\ m_c\ge a\}\cup\{N-1\}\bigr).
\tag{2.1}
\]

### Theorem 2.1 (maximal blocker-avoidable interval)

An interval \([a,b]\) satisfies (1.3) if and only if

\[
b\le b_S(a).
\tag{2.2}
\]

Consequently \(S\) is individually feasible if and only if, for some
\(a\) with \(b_S(a)\ge a\),

\[
\bigcup_{\substack{c\subseteq S\\O(c)\cap[a,b_S(a)]\ne\varnothing}}c=S.
\tag{2.3}
\]

#### Proof

A blocker can be selected outside \([a,b]\) precisely when it has an
occurrence left of \(a\) or right of \(b\).  If \(m_c<a\), the left option
already exists.  If \(m_c\ge a\), an outside choice exists precisely when
\(M_c>b\), equivalently \(b\le M_c-1\).  Taking the minimum over those
blockers proves (2.2).

For fixed \(a\), enlarging a blocker-avoidable interval to
\([a,b_S(a)]\) can only add available good colours.  Theorem 1.2 now gives
(2.3). \(\square\)

This is the strongest useful one-target reduction: one scans only left
endpoints, and the right endpoint is forced canonically.

## 3. Exact simultaneous formula

For every colour \(c\), let \(X_c\in O(c)\); this is a genuine choice
variable when \(|O(c)|>1\) and the fixed sole occurrence otherwise.
For an interval \(I\), let \(F_I\) be the union of the good colours having a
unique occurrence in \(I\).  The guard saying that \(I\) witnesses \(S\)
is exactly

\[
\bigwedge_{c\not\subseteq S}(X_c\notin I)
\quad\wedge\quad
\bigwedge_{u\in S\setminus F_I}
\left(
 \bigvee_{\substack{c\subseteq S,\ u\in c\\O(c)\cap I\ne\varnothing}}
 X_c\in O(c)\cap I
\right).
\tag{3.1}
\]

The simultaneous occurrence-selection problem is

\[
\bigwedge_S\ \bigvee_I \operatorname{Guard}(S,I).
\tag{3.2}
\]

Equations (3.1)--(3.2) are exact, not a relaxation.  They also identify the
correct dependency graph for any LLL attempt: two guards interact only
through repeated colours appearing in both formulas.

Unique blocker positions split the line into runs.  Every feasible interval
lies inside one such run.  Thus (3.2) has a finite local presentation even
though the selected shadow word is global.

## 4. Inherited middle-block witnesses

Return to a middle chronology \(T\) with edge colours
\(c_p=T_p\cup T_{p+1}\).  For an upper target \(S\), a maximal consecutive
block of vertices satisfying \(T_p\subseteq S\) is called an
\(S\)-compatible block.

### Lemma 4.1 (maximal compatible-block domination)

Every interval of middle vertices whose union is \(S\) is contained in a
maximal \(S\)-compatible block whose union is also \(S\).  Every edge colour
inside that block is a subset of \(S\).

#### Proof

Extend the interval in both directions while its vertices remain subsets of
\(S\).  The enlarged union still lies in \(S\) and contains the original
union \(S\), hence equals \(S\).  Each internal edge colour is the union of
two vertices contained in \(S\). \(\square\)

Therefore inherited witnesses have no blocker constraints at all; they only
need enough repeated good colours to retain occurrences inside the block.
This tempting sufficient family nevertheless fails for the fixed K16
carrier.

## 5. Exact K16 census

For the authenticated carrier:

\[
|T|=12870,\qquad |\{c_p\}|=11440,
\]

and the colour-occurrence histogram is

\[
1^{10111}\,2^{1229}\,3^{100}.
\tag{5.1}
\]

There are 1329 nontrivial occurrence variables.  Maximal compatible blocks
give the following exact census.

| target rank | targets | targets with an unconditional inherited witness | minimum movable-cover histogram among the rest |
|---:|---:|---:|---:|
| 10 | 8008 | 7047 | `1:871, 2:90` |
| 11 | 4368 | 4204 | `1:164` |
| 12 | 1820 | 1815 | `2:5` |
| 13 | 560 | 560 | — |
| 14 | 120 | 120 | — |
| 15 | 16 | 16 | — |
| 16 | 1 | 1 | — |

Thus 13763 targets are selection-independent; only 1130 remain.  Of those,
1035 have a one-variable inherited witness and 95 first require two
variables.  Even the one-variable private-witness Hall graph is deficient:
its maximum matching is

\[
906/1035.
\tag{5.2}
\]

So ordinary private SDR/Hall is not a possible proof.  This is only a
failure of that sufficient relaxation, not yet a no-go.

Allowing arbitrary physical intervals gives:

| active target rank | targets | exact feasible interval signatures |
|---:|---:|---:|
| 10 | 961 | 7377 |
| 11 | 164 | 1960 |
| 12 | 5 | 28 |

The maximum unique-blocker-free physical run has length 13.  All 1130
targets are individually feasible.  The next section shows why they are not
simultaneously feasible.

The census is reproduced by:

```text
scratch/analyze_k17_pascal_inherited_blocks_20260731.cpp
scratch/analyze_k17_pascal_private_witness_hall_20260731.cpp
scratch/build_k17_pascal_arbitrary_interval_cnf_20260731.cpp
```

## 6. Solver-free opposite-choice core

Let

\[
c=0x0bf5,qquad O(c)=\{9176,10616\}.
\tag{6.1}
\]

### Theorem 6.1 (fixed-carrier occurrence-selection no-go)

No choice of one occurrence of every rank-nine edge colour makes the
selected rank-nine word upper-complete.

#### Proof

Apply Theorems 1.1--1.2 and enumerate the unique-blocker-free runs for the
two targets below.

For

\[
S_1=0x1bf5,
\]

there is exactly one feasible interval signature, represented by physical
edge interval \([9175,9176]\).  Its unique colours have union
`0x1bb5`; the missing coordinate is bit 6, and its only available provider
is colour `0x0bf5` at occurrence 9176.  Hence every witness of \(S_1\)
forces

\[
x_c=9176.
\tag{6.2}
\]

For

\[
S_2=0x0ff5,
\]

there are exactly two feasible signatures, represented by intervals
\([10614,10616]\) and \([10615,10616]\).  In both, the unique good colours
have union `0x0fe5`; the missing coordinate is bit 4, and its only available
provider is `0x0bf5` at occurrence 10616.  The longer interval additionally
requires blocker `0x1fc5` to use its other occurrence 11791, but this does
not change the pivot requirement.  Thus every witness of \(S_2\) forces

\[
x_c=10616.
\tag{6.3}
\]

Equations (6.2) and (6.3) contradict (6.1). \(\square\)

The literal replay is

```text
python3 scratch/audit_k17_pascal_occurrence_selection_nogo_20260731.py
```

and returns `PASS_SOLVER_FREE_NOGO` against carrier SHA

```text
c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906
```

## 7. Hall and LLL verdicts

The private-witness Hall relaxation already fails by (5.2).  More
decisively, define bad events

\[
A_i=\{S_i\text{ has no witness}\},\qquad i=1,2.
\]

Under any probability measure supported on the two choices in (6.1),

\[
A_1=\{x_c=10616\},qquad A_2=\{x_c=9176\},
\]

so

\[
A_1\cup A_2=\Omega.
\tag{7.1}
\]

There is zero probability of avoiding all bad events.  Consequently no
symmetric, asymmetric, lopsided, cluster-expansion, or algorithmic LLL can
certify this instance; the issue is not a weak numerical criterion but an
empty feasible set.

The attractive local statistics—guards of span at most 13 and only 1329
choice variables—therefore do not imply simultaneous coverage.

## 8. What remains open and the correct repair target

The no-go is architecture-local.  A K17 induction must change at least one
of the following:

1. the K16 carrier chronology near one of the two forced windows;
2. the multiplicity/positions of colour `0x0bf5`;
3. the rule “select exactly one existing occurrence of every q1 colour”;
4. the source carrier itself; or
5. the U-shore ordering/domain itself, through a genuine edge rethread or
   another operation that changes physical occurrence positions.

Merely swapping the two shores does not help: the two forcing targets are
\(z\)-free, so their witnesses lie wholly inside the U shore.  Inserting
\(z\)-containing letters can only split such intervals, never create a new
\(z\)-free witness.

A useful first filter for a replacement carrier is its **forced-literal
graph**: create a literal \((c,p)\) when every feasible interval for a
target forces colour \(c\) to occurrence \(p\).  Opposite literals for one
colour give an immediate no-go as above.  Absence of opposite literals is
not sufficient—higher-order clauses can still conflict—but it is an exact,
cheap obstruction screen before Hall, LLL, or SAT.

The strongest positive theorem still missing is therefore not an LLL for
the present occurrence deck.  It is a rethreading or alternative-source
theorem producing a deck whose exact guard formula (3.2) has no forced
literal core and is simultaneously satisfiable.
