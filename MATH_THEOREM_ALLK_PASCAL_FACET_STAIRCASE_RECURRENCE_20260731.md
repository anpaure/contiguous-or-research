# A dimension-uniform Pascal facet/staircase recurrence

Date: 2026-07-31  
Status: unconditional structural lemmas and an exact conditional odd-to-even
recurrence; the compiler-extension hypothesis is not proved in all
dimensions

## 0. Result and scope

Let \(V\) have size \(2r-1\), let \(z\notin V\), and put

\[
 W=\binom{2r-1}{r}=\binom{2r-1}{r-1},\qquad N=2W.
\]

There is one dimension-uniform operation behind both the flat promoted
answers at k=8,10,12,14 and the nonflat promoted answer at k=16.

* A lower-rainbow rank-\(r\) Johnson cycle is replaced, slot for slot, by
  its rank-\((r-1)\) edge-facet cycle.
* A rooted lower-rainbow Johnson path is replaced, slot for slot, by one
  root facet followed by its edge facets.
* The old vertex traces and the new top-marked facet traces partition the
  complete rank-\(r\) layer on \(V\cup\{z\}\).
* A window of \(q+1\) consecutive facet entries is exactly a window of
  \(q\) consecutive parent vertices. Thus marked shadow service is the
  parent shadow service shifted by one, not a new independent hierarchy.

The remaining difference between the finite answers is one staircase
parameter \(a\). With \(d=d(2r)\), the first \(a\) carrier rows use \(d\)
physical letters and the remaining \(N-a\) rows use \(d+1\). The promoted
k=8,10,12,14 answers have \(a=0\). The promoted k=16 answer has

\[
                 a=6386,
 \qquad (\rho_1,\rho_2,\rho_3)=(0,0,6384),
\]

where \(\rho_j\) is the last start of an internal coordinate run of length
at most \(j\). Hence the same theorem covers the full and partial Pascal
substitutions.

Here "full Pascal" at k=8,10,12,14 is a deck statement: their plain and
marked shores are the two complete Pascal layers. It does not say that each
archived child chronology is the literal edge-facet trace of the archived
immediately preceding answer. K10 is a global rethread and the successful
K12/K14 lifts use specially chosen parent carriers. The recurrence theorem
below specifies the extra trace compatibility needed for a literal lift.

The exact recurrence proved below has three inputs beyond the parent trace:

1. a cut/seam socket condition for the finitely exposed shadow rays;
2. the one-jump run condition and scalar staircase budget; and
3. one simultaneous maximal-common-cap lower matching.

The first two are carrier data. The third is the smallest remaining
compiler condition: neither ordinary Hall nor a containment SDR implies it.
Consequently this note proves no new unconditional value of \(\nu(k)\), and
in particular does not change the present k=17 bounds.

## 1. Rooted Pascal traces

### Definition 1.1 (cycle trace)

Let

\[
 C=(C_0,\ldots,C_{s-1})
\]

be a rank-\(r\) Johnson cycle. Indices are cyclic and

\[
                         F_i=C_{i-1}\cap C_i.        \tag{1.1}
\]

It is a **Pascal cycle trace** when the \(F_i\) are distinct.

### Definition 1.2 (rooted path trace)

Let

\[
 C=(C_0,\ldots,C_{s-1})
\]

be a rank-\(r\) Johnson path. Choose a rank-\((r-1)\) root facet
\(F_0\subset C_0\), and put

\[
                         F_i=C_{i-1}\cap C_i
                         \quad(1\le i<s).            \tag{1.2}
\]

It is a **rooted Pascal path trace** when the \(F_i\) are distinct. In
particular \(F_0\ne F_1\).

A **perfect Pascal trace system** is a vertex-disjoint collection of such
cycles and rooted paths whose vertex traces partition
\(\binom Vr\) and whose facet traces partition \(\binom V{r-1}\).

The root facet is not artificial. A path on \(s\) vertices has only
\(s-1\) edge facets; the root facet is exactly the missing Pascal slot. It
is the endpoint hole used in the finite intersection lifts.

### Proposition 1.3 (unconditional perfect-system supply)

A perfect Pascal cycle trace system exists for every \(r\ge2\).  For
\(r=1\), the unique vertex together with the empty root facet is the trivial
perfect rooted path trace.

#### Proof

The middle-levels incidence graph between
\(\binom V{r-1}\) and \(\binom Vr\) is \(r\)-regular and bipartite, with
\(W\) vertices on each shore. By bipartite one-factorization it has two
edge-disjoint perfect matchings. Their union is a spanning 2-factor.

At a lower vertex \(F\), its two neighbours \(C,C'\) are distinct rank-\(r\)
supersets of \(F\), so

\[
                         C\cap C'=F.
\]

Suppress every lower vertex and colour the resulting Johnson edge \(CC'\)
by \(F\). Every upper vertex has degree two, and every lower colour occurs
once. The projected components are therefore Pascal cycle traces whose
vertices and facets partition the two required layers. \(\square\)

Opening any projected cycle at one edge preserves a perfect rooted path
trace: use the deleted edge colour as the root facet at the exposed
endpoint. Thus neither the slot count nor the basic Pascal partition is an
existence problem. The difficulty is selecting the two matchings and their
openings so that upper service, residence, sockets, and the compiler hold
simultaneously. This is exactly where the decorated-middle-levels work
enters.

An accepting decorated Middle Levels 2-factor supplies strictly more: its
diamond matching lifts to a child Johnson path forest whose lower edge
colours enumerate the complete rank-\((r-1)\) layer and whose upper edge
colours enumerate the complete rank-\((r+1)\) layer. Hence the Decorated
Middle Levels 2-Factor Theorem would discharge the basic Pascal system and
the entire \(q=1\) socket ledger at once. It would not by itself supply
residence, \(q\ge2\) service, or the lower common-cap compiler.

## 2. The exact shadow-shift identity

### Lemma 2.1 (facet windows are one-step-shorter vertex windows)

For a Pascal cycle trace, for every \(q\ge1\),

\[
 \boxed{
 \bigcup_{j=0}^{q}F_{i+j}
 =\bigcup_{j=0}^{q-1}C_{i+j}.}
                                                               \tag{2.1}
\]

Indices are cyclic. For a rooted path trace the same identity holds when
\(0\le i\) and \(i+q<s\).

#### Proof

The two distinct sets \(F_i,F_{i+1}\) are rank-\((r-1)\) facets of \(C_i\),
so

\[
                         F_i\cup F_{i+1}=C_i.         \tag{2.2}
\]

This includes \(i=0\) on a rooted path because both \(F_0\) and \(F_1\)
are distinct facets of \(C_0\). Taking the union of (2.2) for
\(i,i+1,\ldots,i+q-1\) proves (2.1). \(\square\)

### Corollary 2.2 (full Pascal middle partition)

For a perfect Pascal trace system, the traces

\[
                         A_C=C,
 \qquad                  B_F=\{z\}\cup F             \tag{2.3}
\]

enumerate every rank-\(r\) subset of \(V\cup\{z\}\) exactly once.

#### Proof

The \(A\)-shore is exactly \(\binom Vr\). The \(B\)-shore is \(z\) joined
to the perfect facet partition \(\binom V{r-1}\). The shores are disjoint
and each has \(W\) entries. \(\square\)

### Corollary 2.3 (all-depth service transfer)

Suppose an old target \(S\subseteq V\), \(|S|\ge r\), has a declared
occurrence as the union of \(q\) consecutive vertices of one parent trace.
If the corresponding \(q+1\) facet positions exist, then the child has the
two literal occurrences

\[
 S=\bigcup_{j=0}^{q-1}A_{i+j},
 \qquad
 \{z\}\cup S=\bigcup_{j=0}^{q}B_{i+j}.              \tag{2.4}
\]

Thus the marked depth-\(q\) palette is the old depth-\((q-1)\) palette with
\(z\) added. No transfer matrix or separate depth-by-depth construction is
needed.

For a rooted path there is exactly one unmatched parent **occurrence** at
each window length: the terminal suffix. For an opened cycle, a length-
\(q+1\) window loses exactly the \(q\) cyclic starts crossing the cut.
These are the complete cut-debt rays. Therefore a sufficient linearization
condition is:

> every target has a protected occurrence avoiding the chosen cuts, or its
> lost occurrence belongs to a declared new-seam socket of the same value.

This is an occurrence condition. Counting distinct colours or checking
only \(q=1\) is insufficient.

## 3. Residence loses exactly one unit under the facet map

Fix a coordinate \(x\in V\). On a cyclic vertex trace, \(x\in F_i\) if
and only if \(x\in C_{i-1}\cap C_i\). Hence every proper cyclic positive
run of length \(\ell\) in \(C\) becomes a positive run of length
\(\ell-1\) in \(F\). An all-one trace remains all one. On a rooted path
the same assertion holds for every internal run; only the two boundary
runs depend on the root facet and orientation.

Consequently:

* if parent runs have length at least \(d+2\), both its vertex and facet
  traces support flat depth \(d\);
* if parent runs have only length \(d+1\), its facet trace supports \(d\)
  physical letters per row, but need not support \(d+1\).

The first case is the clean depth-drop mechanism used by the full-facet
11 -> 12 and 13 -> 14 lifts. The second case is the equal-depth mechanism
first exposed at 15 -> 16.

## 4. The one-jump staircase

Let

\[
 T=(T_0,\ldots,T_{N-1})
\]

be a linear ordering of the full child middle layer. Fix
\(0\le a\le N\), use physical positions \(0,\ldots,N+d-1\), and set

\[
 I_i=
 \begin{cases}
 [i,i+d-1],&i<a,\\
 [i,i+d],&i\ge a.
 \end{cases}                                           \tag{4.1}
\]

Equivalently, the omitted deadlines are

\[
                 0,1,\ldots,d-2,\quad a+d-1.          \tag{4.2}
\]

For \(d=1\), the initial list in (4.2) is empty.

### Lemma 4.1 (exact one-jump run criterion)

The maximal envelopes

\[
 E_p=\bigcap_{i:p\in I_i}T_i                       \tag{4.3}
\]

recover every row \(T_i\), allowing an empty \(E_p\), if and only if every
internal coordinate run \([u,v]\) satisfies

\[
 v-u+1\ge
 \begin{cases}
 d,&u\le a,\\
 d+1,&u>a.
 \end{cases}                                           \tag{4.4}
\]

Equivalently, with the short-run frontier \(\rho_j(T)\),

\[
 \rho_1=\cdots=\rho_{d-1}=0,
 \qquad \rho_d\le a.                                  \tag{4.5}
\]

#### Proof

An internal run \([u,v]\) has a safe physical position precisely in

\[
                         [e_{u-1}+1,v],               \tag{4.6}
\]

where \(e_i\) is the right endpoint of \(I_i\). If \(u\le a\), then
\(e_{u-1}=u+d-2\), so (4.6) is nonempty exactly when the run has length at
least \(d\). If \(u>a\), then \(e_{u-1}=u+d-1\), giving length at least
\(d+1\). Boundary runs impose no condition. Applying this coordinatewise
proves (4.4), and grouping by run length gives (4.5). \(\square\)

When \(T\) is a rank-\(r\) Johnson path and \(r>d\), every active block in
(4.3) has at most \(d+1\) consecutive rows and hence nonempty intersection.
Thus the \(E_p\) are nonempty automatically.

### Lemma 4.2 (exact staircase capacity)

The number of available proper-prefix lower cells is

\[
 dN+\binom{d+1}{2}-a.                                \tag{4.7}
\]

If

\[
 \Lambda_{2r}=\sum_{s=1}^{r-1}\binom{2r}{s},
 \qquad
 \Delta_{2r}=dN+\binom{d+1}{2}-\Lambda_{2r},         \tag{4.8}
\]

then the scalar lower-cell condition is exactly

\[
                              a\le\Delta_{2r}.        \tag{4.9}
\]

#### Proof

The staircase heights are \(d-1\) before \(a\) and \(d\) afterwards.
Their threshold vector is

\[
                    (\tau_1,\ldots,\tau_d)
                    =(0,\ldots,0,a).
\]

The monotone-deadline capacity identity subtracts
\(\sum_j\tau_j=a\) from the full triangular catalogue, proving (4.7)--
(4.9). \(\square\)

The specializations are now transparent.

* \(a=0\): every row is a depth-\(d\) row. This is the full facet
  substitution seen at k=8,10,12,14.
* \(a>0\): the first \(a\) rows are one physical letter shallower. Their
  one-letter extensions are cap owners; later rows are already facet
  owners. This is the partial substitution at k=16.

## 5. Why the mixed cap/facet owner row is automatic

Assume the initial part of \(T\) is a consecutive marked facet trace,

\[
                         T_i=\{z\}\cup F_i.           \tag{5.1}
\]

For \(i<a-1\), the depth-\(d\) one-letter extension of the shallow row is

\[
 \bigcup_{p=i}^{i+d}E_p
 =T_i\cup T_{i+1}
 =\{z\}\cup C_i.                                    \tag{5.2}
\]

The first equality is the overlap of two consecutive \(d\)-letter rows;
the second is Lemma 2.1 at \(q=1\). Every row \(i\ge a\) is deep, so its
depth-\(d\) owner is the facet target \(T_i\) itself. Only the single hinge
row \(i=a-1\) needs a local equality/socket check.

Therefore \(a\) is literally the number of cap-mode rows, up to the one
hinge, and \(N-a\) is the facet-mode suffix. The k=16 values

\[
                 a=6386,
 \qquad N-a=6484
\]

are exactly its observed rank-\(9\)/rank-\(8\) owner census.

This proves the requested slot preservation: changing a complete cycle or
the nonroot vertices of a rooted path from caps to their edge facets changes
no row count, and the staircase changes no physical length.

## 6. The exact compiler gate

After Lemma 4.1, let \(E_p\) be the nonempty maximal envelopes. Let
\(\mathcal L\) be all nonempty child targets of rank below \(r\), and let a
**cell** mean an available proper physical interval. Choose an injective
assignment

Before the simultaneous problem, even the new singleton has one exact unary
gate.

### Lemma 6.0 (top-singleton socket)

A physical position \(p\) may be capped to the one-letter cell \(\{z\}\)
without changing any middle row if and only if

\[
 z\in E_p                                                   \tag{6.0a}
\]

and, for every owner row containing \(p\),

\[
 \{z\}\cup
 \bigcup_{q\in I_i\setminus\{p\}}E_q=T_i.                  \tag{6.0b}
\]

#### Proof

After replacing \(E_p\) by \(\{z\}\), the left side of (6.0b) is exactly
the maximal possible OR on row \(i\). Thus (6.0a)--(6.0b) are sufficient.
They are necessary because every legal final letter is contained in its
maximal envelope: if an alternative word realizes row \(i\) after putting
\(\{z\}\) at \(p\), its other letters are contained in the other \(E_q\),
so (6.0b) must hold. \(\square\)

This is the smallest new-coordinate compiler condition. It is unary and
cheap, but not automatic from the Pascal partition. The promoted k=16
scaffold has exactly one such position, \(p=6389=a+d\), the facet/cap
hinge. This explains why the 49-facet bridge is compiler-relevant even
though middle coverage and internal shadows were already automatic.

The remaining lower targets are simultaneous. Choose an injective assignment

\[
                         \mu:\mathcal L\longrightarrow\mathcal C.
                                                               \tag{6.1}
\]

Define the maximal common cap

\[
 A_p(\mu)=E_p\cap
 \bigcap_{S:p\in\mu(S)}S.                            \tag{6.2}
\]

### Theorem 6.1 (smallest fixed-scaffold compiler condition)

For the fixed chronology and staircase, a simultaneous lower compiler exists
if and only if some injective \(\mu\) satisfies

\[
 A_p(\mu)\ne\varnothing,                              \tag{6.3}
\]

\[
 \bigcup_{p\in I_i}A_p(\mu)=T_i
 \quad(0\le i<N),                                    \tag{6.4}
\]

and

\[
 \bigcup_{p\in\mu(S)}A_p(\mu)=S
 \quad(S\in\mathcal L).                              \tag{6.5}
\]

#### Proof

The forward implication chooses one witnessing cell for each lower target.
Distinct targets cannot use the same cell. Intersecting all selected labels
produces (6.2); it contains the original compiler letters, while remaining
inside every protected row and selected target. Hence no required bit is
lost and no forbidden bit can be gained, giving (6.3)--(6.5).

Conversely, (6.2)--(6.5) themselves define the desired nonempty word and
realize every lower and middle target. \(\square\)

This is one integral correlation condition, not another carrier hierarchy.
Ordinary Hall, scalar area, the cap--facet containment matching, and
targetwise individual providers do not imply it. The chain-aligned
two-position counterexample in
MATH_THEOREM_GUARDED_CONVEX_LAMINAR_COMMON_CAP_COMPILER_20260731.md
already separates all of those weaker statements from (6.3)--(6.5).

A proof-sufficient all-dimensional replacement is the following precise
target.

> **Pascal guard-bank lemma.** The lifted scaffold admits a sound incidence
> bank with complete point/row/selected-edge trace guards, convex target
> neighbourhoods, and all interval-capacity inequalities.

If this lemma holds, earliest-deadline greedy produces \(\mu\) and the trace
guards prove (6.3)--(6.5). This is strictly stronger than necessary, but is
the smallest currently available compiler theorem with a transparent
integral proof.

## 7. Conditional odd-to-even recurrence

### Theorem 7.1 (Pascal facet/staircase lift)

For \(k=2r\), let \(d=d(k)\). Suppose the odd ground set \(V\) carries:

1. a perfect Pascal trace system;
2. a linear braid \(T\) of all plain vertex traces and top-marked facet
   traces which is a rank-\(r\) Johnson path;
3. an integer \(a\le\Delta_{2r}\) satisfying (4.5), with the initial
   \(a+1\) rows lying on one marked facet trace and the hinge satisfying its
   local extension equality;
4. a protected old upper-service map together with sockets for every
   exposed plain cut ray and marked terminal/cut ray; and
5. the maximal-common-cap assignment of Theorem 6.1.

Then there is a universal word on \(V\cup\{z\}\) of length

\[
                         N+d=B(2r),                  \tag{7.1}
\]

and therefore

\[
                         \boxed{\nu(2r)=B(2r)}.       \tag{7.2}
\]

#### Proof

Corollary 2.2 gives every middle target exactly once. Lemmas 4.1 and 4.2
give a nonempty row-exact staircase of the lower-bound length with enough
scalar cells. The protected parent occurrences give every upper target
omitting \(z\), and Lemma 2.1 gives every upper target containing \(z\);
the socket hypothesis supplies precisely the occurrences exposed by cuts.

Because the row intervals are chain aligned, the union of any consecutive
block of carrier rows is the union of one contiguous physical interval.
Thus every upper occurrence transfers literally. Theorem 6.1 supplies all
lower targets while preserving every middle row. Hence the physical word is
universal and has length (7.1). The monotone-deadline lower bound supplies
the reverse inequality. \(\square\)

### Corollary 7.2 (depth-drop full-facet recurrence)

If every parent vertex component has cyclic/internal runs at least \(d+2\),
then its facet component has runs at least \(d+1\). If the chosen braid
creates no shorter seam run, take \(a=0\). Conditions 1--4 of Theorem 7.1
then follow from the perfect Pascal system, protected parent service, and
the finite cut-socket ledger. Only Theorem 6.1 remains.

This is the dimension-uniform explanation of the full-facet 11 -> 12 and
13 -> 14 lifts. It is also proof that residence does not need to be
re-solved depth by depth on a favourable depth drop.

### Corollary 7.3 (equal-depth partial recurrence)

If parent vertex runs are only at least \(d+1\), their facet runs are at
least \(d\). Put all ordinary \(d\)-runs in the shallow prefix and choose

\[
                         \rho_d(T)\le a\le\Delta_{2r}.             \tag{7.3}
\]

Require every later facet fragment either to come from an over-resident
parent component or to have its short boundary run repaired by a seam.
Then the same recurrence applies. This is exactly the structural role of
the large shallow facet rail, four-edge collar, and over-resident 45-cycle
at 15 -> 16.

## 8. What is inherited, and what is not

| property | dimension-uniform conclusion |
|---|---|
| child middle count | automatic from the perfect Pascal trace system |
| slot count | automatic for cycles and rooted paths |
| marked \(q=1\) caps | automatic internally from \(F_i\cup F_{i+1}=C_i\) |
| deeper marked shadows | automatic internally by (2.1) |
| depth-drop residence | automatic before seams |
| equal-depth residence | exact one-jump condition (4.5) |
| cut losses | exactly the exposed occurrence rays; sockets required |
| scalar lower capacity | exactly \(a\le\Delta_{2r}\) |
| integral lower compiler | **not inherited**; Theorem 6.1 is the missing gate |

Thus the owner/facet exchange is a genuine recurrence, not merely a census
of the k=16 word. It collapses all internal marked shadow conditions to one
parent window identity. The only nonlocal obstruction left after a good
braid is the simultaneous common-cap matching.

## 9. Finite audit

The independent script

    scratch/audit_allk_pascal_facet_staircase_recurrence_20260731.py

does the following without reading solver state:

1. exhausts 16,312 binary traces and verifies Lemma 4.1;
2. checks 51,480 instances of (2.1) on the two exact k=15 cycles;
3. verifies the full Pascal split and zero short-run frontier for the
   promoted k=8,10,12,14 carriers; and
4. verifies for k=16 the full middle Pascal partition,
   \((\rho_1,\rho_2,\rho_3)=(0,0,6384)\), \(a=6386\), and literal recovery
   of the frozen variable-staircase chronology from answers/k16.word; and
5. finds exactly one top-singleton pin-safe socket, at physical position
   6389.

It writes

    scratch/allk_pascal_facet_staircase_recurrence_20260731.audit.json

and explicitly records that no all-dimensional existence theorem is being
claimed.
