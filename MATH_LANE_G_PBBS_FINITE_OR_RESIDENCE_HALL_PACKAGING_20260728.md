# Lane G update: PBBS all-depth factors versus finite-OR residence, packaging, and Hall

Date: 2026-07-28

Method: pure mathematics and audit of existing exact certificates only. No
new SAT search, finite search, or web input is used.

## 0. Decision

For a set word \(A=(A_1,\ldots,A_L)\) on \([k]\), write

\[
 (DA)_i=A_i\cup A_{i+1}.
\]

Put

\[
 r=\lceil k/2\rceil,\qquad
 W=\binom kr,\qquad
 \Lambda=\sum_{j=1}^{r-1}\binom kj,
\]

and let \(d=d(k)\) be the least integer satisfying

\[
 dW+\binom{d+1}{2}\ge\Lambda.
\tag{0.1}
\]

The exact finite-OR lower bound is

\[
 \nu(k)\ge B(k):=W+d.
\tag{0.2}
\]

The PBBS/all-depth Johnson factor does not by itself give an optimal
finite-OR word. It supplies a promising middle-layer factor and many nested
shadow witnesses, but the conversion requires three logically independent
zero-defect gates.

1. **Residence.** The final middle chronology \(T\), after all components
   are cut and sewn, must lie in the image of \(D^d\). Equivalently, every
   internal coordinate 1-run of \(T\) has length at least \(d+1\).
   Complete PBBS shadow support is existential over phase starts and does
   not imply this universal run condition.

2. **Packaging and exterior coverage.** The PBBS components must be turned
   into one length-\(W\) central path, without losing the upper witnesses
   needed after the unique length-\(d\) boundary collar. Johnson seams are
   useful but are not logically required at positive slack; a non-Johnson
   seam is legal if it preserves residence and the OR shadows.

3. **Lower Hall.** For the depth-\(d\) maximal erosion and sandwich core,
   the exact lower compiler graph must have a matching saturating all
   \(\Lambda\) lower targets. Complete lower shadows prove at most positive
   degree in the coarse occurrence graph. They do not prove Hall in the
   named-cell graph. An exact \(k=7\) certificate has complete two-sided
   shadows and residence but fails cyclic Hall.

These three gates can be summarized by the exact obstruction vector

\[
 \boxed{
 \mathbf{Obs}_d(T)
 =\bigl(\rho_d(T),\ U(T),\ \delta_H(T)\bigr),}
\tag{0.3}
\]

where \(\rho_d\) is residence loss, \(U\) is the number of uncovered upper
targets in the linear chronology, and \(\delta_H\) is the lower compiler
Hall deficiency. In the depth-\(d\) sandwich architecture, a PBBS conversion
proves \(\nu(k)=B(k)\) exactly when it produces a middle permutation with

\[
 \mathbf{Obs}_d(T)=(0,0,0).
\tag{0.4}

The natural global construction—periodically cutting each PBBS component
into \(k\)-blocks and sewing those blocks—does not pass automatically. PBBS
homomesy balances each coordinate over a whole long component, but it does
not make every block rainbow, does not force zero residence defect in each
block, and gives no lower Hall inequality. Its exact surviving replacement
is a global segment-order/configuration problem described in Section 7.

The exact certificates for \(k=11,12,13,14\) show that all three gates can be
met, but they also calibrate the packaging obstruction:

* \(k=11\): a PBBS-derived depth-three resident, all-shadow carrier compiles;
* \(k=12\): a depth-two six-piece chronology is Hall-perfect;
* \(k=13\): the resident carrier first appears as two cycles, and a safe
  cross-cycle splice is required before compilation;
* \(k=14\): every five-piece braid in the audited class fails, while a
  six-piece braid is resident, upper-perfect, and Hall-perfect.

Thus PBBS is a viable seed, not a black-box proof. The exact open theorem is
a global PBBS segment selection whose residence, exterior, and named-cell
Hall constraints hold simultaneously at the optimal depth \(d(k)\).

## 1. The finite-OR carrier theorem

Let

\[
 T=(T_0,T_1,\ldots,T_{W-1})
\tag{1.1}
\]

be a chronology containing every rank-\(r\) mask exactly once. For the
cyclic discussion define its maximal depth-\(d\) erosion by

\[
 P_i=\bigcap_{h=0}^{d}T_{i-h},
 \qquad i\in\mathbb Z_W.
\tag{1.2}
\]

Call \(T\) depth-\(d\) resident if

\[
 D^dP=T.
\tag{1.3}
\]

Choose a core \(C\subseteq P\) satisfying

\[
 D^dC=D^dP=T.
\tag{1.4}
\]

For example, coordinatewise selecting positions in every 1-run with gaps at
most \(d+1\) gives such a core whenever (1.3) holds.

The lower physical cells are the cells in rows

\[
 A,DA,\ldots,D^{d-1}A
\tag{1.5}
\]

for words \(A\) in the sandwich

\[
 C_i\subseteq A_i\subseteq P_i.
\tag{1.6}
\]

Let \(\mathcal G_d(T,C)\) denote the exact named-cell compiler graph: its
left shore is the punctured lower ideal

\[
 \mathcal L_{<r}=\{S\subseteq[k]:1\le |S|<r\},
\tag{1.7}
\]

its right shore is the set of physical cells in (1.5), including the
triangular boundary cells created by linearization, and an edge means that
the target can be pinned to that cell within the sandwich while respecting
the coordinatewise witness constraints. Here “exact named-cell compiler
graph” means the PCSH graph after the sandwich witness system has been
fixed, for which the compiler theorem identifies simultaneous realizability
with a saturating matching; it is not the coarser graph recording only
individual target reachability.

Define

\[
 \delta_H(T,C)
 =\max_{\mathcal A\subseteq\mathcal L_{<r}}
   \bigl(|\mathcal A|-|N_{\mathcal G_d(T,C)}(\mathcal A)|\bigr)_+.
\tag{1.8}
\]

### Theorem 1.1 (finite-OR PBBS interface)

Suppose a PBBS-derived chronology \(T\) satisfies all of the following.

1. It lists every middle mask exactly once.
2. It is depth-\(d\) resident.
3. Every upper mask has a witness in \(T,D T,D^2T,\ldots\) which survives
   the chosen linear boundary.
4. For some valid depth-\(d\) sandwich core \(C\),
   \(\delta_H(T,C)=0\).

Then there is a length-\(W+d\) universal OR word, and hence

\[
 \boxed{\nu(k)=B(k).}
\tag{1.9}
\]

#### Proof

Hall gives distinct lower cells for all targets in (1.7). The exact
coordinatewise witness criterion realizes those pins by one word
\(A\in[C,P]\). Equations (1.3)--(1.4) protect the middle row:

\[
 D^dA=T.
\]

Applying further derivatives gives

\[
 D^{d+q}A=D^qT,
\]

so the surviving upper witnesses cover the upper ideal. Cutting and adding
the single length-\(d\) boundary collar retains all lower cells selected by
the linear compiler. The resulting word has length \(W+d\) and covers every
nonzero mask. Equation (0.2) gives equality. \(\square\)

The theorem is deterministic. It asks for one chronology and one compiler
matching; it never sums independent rank leaves.

## 2. Exact residence and the PBBS phase gap

For a coordinate \(x\), record its membership in the cyclic chronology
\(T\) by a binary cyclic word. Let \(\mathscr R_x(T)\) be the multiset of
lengths of its maximal 1-runs. Define

\[
 \rho_d(T)
 =\sum_{x=1}^{k}
   \sum_{\substack{\ell\in\mathscr R_x(T)\\\ell\le d}}\ell.
\tag{2.1}
\]

### Theorem 2.1 (run characterization of residence)

For a cyclic chronology,

\[
 \boxed{
 D^dP=T
 \quad\Longleftrightarrow\quad
 \rho_d(T)=0
 \quad\Longleftrightarrow\quad
 \text{every coordinate 1-run has length at least }d+1.}
\tag{2.2}
\]

#### Proof

Fix one coordinate and one of its 1-runs of length \(\ell\). In the erosion
\(P_i=\bigcap_{h=0}^dT_{i-h}\), this run survives in exactly

\[
 (\ell-d)_+
\]

positions. Applying \(D^d\) dilates every surviving run by \(d\) positions
and recovers the original run if and only if \(\ell-d\ge1\). If
\(\ell\le d\), the run disappears entirely and cannot be recovered.
Apply this independently to every coordinate run. \(\square\)

For a linear chronology, the same statement holds for internal runs; the
first and last runs are handled by the truncated maximal erosion and the
length-\(d\) boundary collar.

Now let \(F\) be a PBBS Johnson 2-factor. On an oriented component write

\[
 T_{i+1}=T_i-\{u_i\}+\{v_i\}.
\tag{2.3}
\]

On the native odd ground \(k=2m+1\), PBBS owners have rank \(m\), whereas
the finite-OR convention uses the upper middle rank
\(r=m+1\). Apply complementation to every PBBS owner. This preserves
Johnson adjacency and turns the PBBS factor into a factor on the required
rank. A coordinate 1-run in the complemented chronology is a 0-run in the
original PBBS chronology. Thus finite-OR residence requires control of the
opposite/complement tower, not merely the lower PBBS intersections.

The PBBS corrected occurrence at depth \(q\) based at phase \(i\) is an
intersection of consecutive states. Complete PBBS support has quantifiers

\[
 \forall S\text{ at depth }q\quad
 \exists i\text{ with the correct intersection }S.
\tag{2.4}
\]

Residence instead requires a universal phase statement about every
coordinate run.

### Lemma 2.2 (one-level residence certificate)

If every phase of a Johnson component has a correct-rank lower intersection
through depth \(d+1\), then that component is depth-\(d\) resident.

#### Proof

Suppose a coordinate has a 1-run of length \(\ell\le d\). Start immediately
before its insertion and take the following \(d+1\) transitions. Both its
insertion and removal occur in this window. The removal is therefore not a
departure of an element of the initial state. Among the \(d+1\) departures,
at most \(d\) distinct initial elements disappear, so the intersection has
rank at least

\[
 r-d>r-(d+1),
\]

contradicting correct rank at depth \(d+1\). Thus every 1-run has length at
least \(d+1\), and Theorem 2.1 applies. \(\square\)

This lemma makes the quantifier gap exact. Full PBBS target coverage at
depths through \(d+1\) does not say that every phase is correct. Hence it
does not prove residence.

There is also a quantitative edit obstruction. Let

\[
 \mathcal B_{d+1}(F)
 =\{i:\text{the phase-}i\text{ depth-}(d+1)
          \text{ intersection has wrong rank}\}.
\tag{2.5}
\]

If a conversion retains the PBBS order inside segments and changes \(t\)
successor arcs, every bad window avoiding all changed arcs remains bad. One
arc belongs to at most \(d+1\) such windows. Therefore

\[
 \boxed{
 t\ge\frac{|\mathcal B_{d+1}(F)|}{d+1}}
\tag{2.6}
\]

is necessary for a resident segment extraction of this kind. PBBS all-depth
support gives no upper bound on \(|\mathcal B_{d+1}(F)|\).

## 3. Packaging is not component counting alone

Let the PBBS factor have oriented components

\[
 C_1,\ldots,C_p.
\]

A finite-OR optimum has only one central chronology. Thus all components
must be cut into oriented segments and those segments concatenated into one
length-\(W\) path. There is no budget for an independent length-\(d\) reset
at every component.

For a proposed concatenation \(T\), put

\[
 U(T)=
 \#\{\text{upper masks with no surviving linear witness in }D^qT\}.
\tag{3.1}
\]

Residence and upper coverage are local around a proposed seam only after all
internal PBBS defects have been removed. A seam may be Johnson,

\[
 |T_i\triangle T_{i+1}|=2,
\]

but the finite-OR theorem does not require this. At positive lower-bound
slack, the true condition is that the maximal erosion remain exact and the
upper masks remain witnessed. This is why non-Johnson mixed seams must not be
excluded from a general construction.

For bookkeeping, define

\[
 \operatorname{Pack}_d(F)
 =\{T:\ T\text{ is obtained by cutting, orienting, and ordering
 segments of }F,\ T\text{ lists every middle vertex once}}.
\tag{3.2}
\]

Then the exact PBBS packaging target before the lower compiler is

\[
 \boxed{
 \min_{T\in\operatorname{Pack}_d(F)}
 \bigl(\rho_d(T)+U(T)\bigr)=0.}
\tag{3.3}

Complete PBBS shadow support proves only that the uncut union of components
has zero cyclic upper holes. It does not imply (3.3): cuts can destroy unique
witnesses, and seams can create short runs.

## 4. Lower Hall is independent of residence and shadows

At equality length, the number of lower physical cells is exactly

\[
 dW+\binom{d+1}{2}=\Lambda+\sigma,
\tag{4.1}
\]

where

\[
 \sigma=dW+\binom{d+1}{2}-\Lambda
\tag{4.2}
\]

is the scalar slack. This count does not imply Hall.

For a fixed compiler graph, let

\[
 \delta(\mathcal A)=|\mathcal A|-|N(\mathcal A)|.
\]

In the general multirow compiler, linearization contributes the triangular
number

\[
 \binom{d+1}{2}
\tag{4.3}
\]

of extra physical cells across rows \(0,\ldots,d-1\). This scalar total is
not, by itself, a repair bound for an individual Hall witness.

There is, however, an exact symmetry obstruction for the fixed
duplicate-only bulk compiler used at \(k=11\). In that architecture a cut
duplicates a window of exactly \(d\) cyclic right vertices. If a free group
of order \(q\) acts on both shores, uncrossing produces an invariant Hall
witness whenever cyclic Hall fails, and its deficiency is a positive
multiple of \(q\). Hence, if

\[
 q>d,
\tag{4.4}
\]

no cut can repair a cyclic Hall failure in that duplicate-window
architecture. Even if linearization may also enlarge the admissible sets at
the \(d\) old boundary positions, the same conclusion holds under \(q>2d\).
This rigidity statement is not asserted for an arbitrary reoptimized
multirow core.

For the translation-equivariant \(k=11\) certificate,

\[
 q=11,\qquad d=3,\qquad q>2d,
\]

so cyclic Hall had to pass before the cut. The 63 quotient inequalities do
pass.

Most importantly, an exact \(k=7\), depth-two carrier is known with all of
the following properties:

* complete lower and upper shadows through depth two;
* residence at least three;
* upper first-shadow load at most two;
* 28 exterior-safe cuts.

Its cyclic compiler graph is Hall-deficient. Among the 28 safe cuts, 24 are
Hall-good and four are Hall-bad. Therefore

\[
 \boxed{
 \text{PBBS-style all-depth shadows + residence}
 \not\Longrightarrow
 \text{Hall-perfect compiler}.}
\tag{4.5}
\]

This is a literal finite counterexample to the black-box implication. It is
not a counterexample to the existence of a good cut or to a more global
carrier construction.

## 5. Exact calibration from \(k=11\) through \(k=14\)

The optimal-depth arithmetic is:

| \(k\) | \(r\) | \(W\) | \(\Lambda\) | \(d(k)\) | \(B(k)\) |
|---:|---:|---:|---:|---:|---:|
| 11 | 6 | 462 | 1023 | 3 | 465 |
| 12 | 6 | 924 | 1585 | 2 | 926 |
| 13 | 7 | 1716 | 4095 | 3 | 1719 |
| 14 | 7 | 3432 | 6475 | 2 | 3434 |

All four lower bounds are attained by exact, exhaustively verified words.
Their structural evidence is more informative than the bare equality.

### \(k=11\)

The coherent PBBS trade certificate gives a depth-three resident central
chronology with every upper shadow present. The depth-three sandwich
compiler is Hall-feasible and produces an exact word of length 465. The
independent PBBS-derived compiled word has SHA-256

```text
52d16a4b280601645e1d0265bf6f102c38667285e9c3ebbcadfd6f073b78ef59
```

This is the positive calibration that PBBS histories can satisfy all three
gates after a coherent global modification.

### \(k=12\)

The verified six-piece carrier has depth two, no structural residence
failure, and a SAT lower compiler covering all 1,585 lower targets. Its
926-entry word has SHA-256

```text
a29517e67dd3c9db5f773f5332b3e3e44197cfe79d3d8014ea0770c9bedeb482
```

The row profiles show genuine multirow use; the certificate is not a literal
bottom-row packing.

### \(k=13\)

The resident all-shadow seed is a two-cycle factor of lengths 1547 and 169.
Among 6,240 cross-cycle Johnson edges, 4,277 splices preserve depth-three
residence. The selected splice gives one middle path, and the depth-three
compiler produces the exact 1,719-entry word with SHA-256

```text
8d202e793d3317d2c3db76fef51f9d20d0e4e09fa2899a9686285cc01f4577d0
```

This proves that Hamiltonicity of the initial PBBS-like carrier is stronger
than necessary. A small-component resident factor plus safe packaging is the
right intermediate object.

### \(k=14\)

The exact carrier is assembled from six oriented pieces. In the replay, 159
endpoint-passing candidates leave 29 residence-passing candidates, and one
is simultaneously upper-perfect and Hall-perfect. The resulting word has
length 3434 and SHA-256

```text
7d94117099bbb46402e8f4edda718dae7eb10e2e5e34e9b588e08a198b43db17
```

Every five-piece braid in the audited predecessor class fails for the exact
two-resource reason: two unique upper colours are lost while only one repair
endpoint is exposed. The sixth piece supplies the second endpoint. This is a
packaging obstruction invisible to scalar shadow counts.

### Calibration verdict

The finite certificates support the sequence

\[
 \text{small-component all-shadow factor}
 \longrightarrow
 \text{resident multi-piece path}
 \longrightarrow
 \text{exact lower Hall matching},
\tag{5.1}
\]

not the stronger claim that one canonical PBBS orbit is already an optimal
carrier. They also show that the number of pieces required by a safe global
splice is not controlled by local 2/3/4-opt neighborhoods.

## 6. Attempted global construction: periodic PBBS blocks

Every canonical PBBS component has length \(\ell k\) for some integer
\(\ell\). The most direct global construction is:

1. choose one phase \(\theta_C\) on each component;
2. cut at
   \(\theta_C,\theta_C+k,\ldots,
     \theta_C+(\ell-1)k\);
3. regard the resulting \(k\)-state blocks as local packets;
4. order and sew all blocks into one central chronology;
5. run the optimal depth-\(d\) sandwich compiler.

PBBS homomesy says that over the whole length-\(\ell k\) component each
coordinate has the correct total number of uses. It does not imply the
blockwise conditions needed in step 3.

Write one block as

\[
 B=(T_0\to T_1\to\cdots\to T_k),
\]

so it has \(k\) transitions and \(k\) owner tails. Let \(c_B(x)\) and
\(a_B(x)\) be its departure and arrival counts, and put

\[
 \epsilon_B(x)=c_B(x)-1.
\tag{6.1}
\]

The block is rainbow only if

\[
 \epsilon_B(x)=0\qquad(x\in[k]).
\tag{6.2}
\]

The componentwise homomesy identity gives only

\[
 \sum_{B\subset C}\epsilon_B(x)=0
 \qquad(x\in[k]).
\tag{6.3}
\]

It permits nonzero opposite defects in different blocks. Likewise, define
the endpoint drift

\[
 \eta_B(x)=\mathbf 1_{T_k}(x)-\mathbf 1_{T_0}(x).
\tag{6.4}
\]

Telescoping the membership indicator gives the exact identity

\[
 \boxed{\eta_B(x)=a_B(x)-c_B(x).}
\tag{6.5}
\]

Thus departure-rainbow does **not** imply arrival-rainbow for an open
PBBS block. Under (6.2) one has

\[
 a_B(x)=1+\eta_B(x).
\]

On a PBBS component of minimal length \(\ell k\) with \(\ell>1\),
\(T_k\ne T_0\) at every phase, since equality would make the orbit period
divide \(k\). Hence every untouched \(k\)-block on a long component has
\(\eta_B\ne0\) and is not a closed local packet.

For completeness, define its owner-occupation imbalance by

\[
 \delta_B(x)=\sum_{i=0}^{k-1}\mathbf 1_{T_i}(x)-r.
\tag{6.6}
\]

A block becomes a literal cyclic-coordinate packet precisely when

\[
 \epsilon_B(x)=\eta_B(x)=\delta_B(x)=0
 \qquad(x\in[k]).
\tag{6.7}
\]

Indeed, \(\eta_B=0\) closes the block, and then (6.2) and (6.5) say that
every coordinate departs and arrives exactly once. Its membership states
therefore form one cyclic interval. Equation (6.6) gives interval length
\(r\), and ordering coordinates by their departure phases recovers the
literal cyclic packet. The converse is immediate.

Over a whole PBBS component the \(\eta_B\)'s telescope, while homomesy
balances the \(\epsilon_B\)'s and \(\delta_B\)'s. These are only three
zero-sum identities. They do not pair opposite defects at compatible seams.
Consequently the periodic construction must change at least one successor
arc per long \(k\)-block if it insists on closed local packets. The finite-OR
problem permits open blocks, but then their drift and short-run constraints
must be solved globally.

Finally, assume optimistically that phases make every block rainbow and
residence-perfect. The lower compiler graph of the sewn chronology still
need not be Hall-perfect by (4.5). Therefore periodic block extraction fails
as a theorem at three exact places:

\[
 \boxed{
 \text{block rainbow/FIFO} ;\quad
 \text{block and seam residence} ;\quad
 \text{named-cell Hall}.}
\tag{6.8}

This is not a no-go against a correlated choice of phases and seams. It
shows that component homomesy and all-depth target coverage do not supply
that choice.

## 7. A viable global replacement: joint segment configuration

The finite certificates suggest replacing periodic blocks by a global
segment configuration.

Cut the PBBS components at a set of arcs and allow both orientations of each
resulting segment. A configuration consists of:

1. a path ordering using every segment once;
2. a choice of every seam, Johnson or non-Johnson;
3. the maximal depth-\(d\) erosion and a valid sandwich core;
4. a matching of every lower target to a named compiler cell.

Residence blockers are local forbidden patterns in the ordered segment
sequence. Upper targets impose surviving-witness clauses. Lower targets and
cells impose one global Hall matching. Let

\[
 \mathfrak T_d(F)
 =\{T\in\operatorname{Pack}_d(F):\rho_d(T)=0, U(T)=0\}.
\tag{7.1}

### Theorem 7.1 (exact global PBBS construction gate)

A PBBS factor \(F\) yields an optimal depth-\(d\) finite-OR construction by
segment packaging if and only if there are

\[
 T\in\mathfrak T_d(F)
\]

and a valid core \(C\) for which

\[
 \boxed{
 \delta_H(T,C)=0.}
\tag{7.2}
\]

#### Proof

Sufficiency is Theorem 1.1. Conversely, a depth-\(d\) sandwich construction
obtained by cutting and sewing \(F\) determines its segment order \(T\).
Exact middle coverage puts \(T\) in \(\operatorname{Pack}_d(F)\), its
erosion identity gives \(\rho_d(T)=0\), upper coverage gives \(U(T)=0\),
and its lower witness assignment is a matching saturating the compiler
graph. Thus (7.2) holds. \(\square\)

This theorem is an equivalence, but it is not yet an existence proof. It
does identify the right global construction: select chronology and compiler
matching together. Optimizing phase cuts first and asking for Hall later can
freeze a Dulmage--Mendelsohn obstruction, exactly as the \(k=15\) finite
frontier demonstrates.

There is a useful necessary residence pre-cut. If
\(\mathcal B_{d+1}(F)\) is the bad-window set in (2.5), every segment system
whose internal PBBS order is retained must cut a hitting set of those
windows. Equation (2.6) is the first lower bound on the number of cuts. After
that, the new seams must be screened against the same run condition rather
than merely Johnson adjacency.

## 8. Precise remaining obstruction

The PBBS/all-depth Johnson factor solves the wrong quantifier order:

\[
 \forall\text{ target }S\ \exists\text{ a good phase/history}.
\tag{8.1}
\]

The finite OR compiler needs

\[
 \exists\text{ one packaged chronology }T\
 \forall\text{ residence windows, upper targets, and lower Hall cuts}.
\tag{8.2}

The exact missing theorem is therefore:

> **PBBS resident-Hall packaging theorem.** At the optimal depth \(d(k)\),
> some global segment configuration of the PBBS all-depth factor has no
> short coordinate run, preserves every upper target, and has a
> Hall-perfect lower sandwich graph.

No current PBBS theorem proves (8.2), and the \(k=7\) certificate rules out
deducing the Hall clause from the first two clauses. Conversely, the exact
\(k=11\)--\(14\) certificates show that no scalar or parity obstruction
prevents the three clauses from coexisting. What is missing is a global
selection theorem—most naturally a joint segment-order/Hall configuration
theorem—not another rankwise shadow count.

## 9. Audited inputs

The finite-OR normal form and the distinction between forced lower-bound
facts and chosen carrier structure come from
EXACT_OR_FORMULA_SYSTEMATIZED_UNDERSTANDING_20260728.md. The residence and
multirow sandwich interface is checked against
MATH_DEPTH_D_SANDWICH_MULTIROW_COMPILER_20260727.md; the cut-specific Hall
rigidity and the \(k=7\) counterexample are checked against
MATH_GOOD_CUT_PCSH_20260727.md and
MATH_BULK_PCSH_COMPILER_20260727.md. The PBBS orbit divisibility and
componentwise homomesy inputs are those audited in
MATH_ATTACK_O2_FIRST_SHADOW_FACTOR_20260724.md.

The finite calibration artifacts are
scratch/pbbs_k11_res3_conn_multirow_465.word,
scratch/k12_intersection_sixpiece_hallpass_001.word,
scratch/K13_EXACT_1719_REPRO.md, and
scratch/k14_exact_3434_evidence.md. No new local SAT result is used in this
note.
