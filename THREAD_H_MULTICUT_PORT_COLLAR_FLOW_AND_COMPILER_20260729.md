# Multi-cut surgery: oriented port flow, collar states, shadows, and compiler absorption

Date: 2026-07-29

Status: proved an exact separated-collar multi-cut theorem, an exact
state-expanded replacement when segments are short, exact targetwise shadow
and compiler ledgers, and exact finite constraints for the current
\(k=15\) degree-only factor. No existence claim is made for the resulting
finite gate.

The principal conclusion is that multi-cut surgery is a valid replacement
for the refuted one-seam assertion, but it is not cheap component splicing.
The correct object is a labelled oriented port flow coupled to a residence
state, targetwise shadow rows, and a physical compiler flow.

## 1. Setup

Put

\[
 r=\left\lceil {k\over2}\right\rceil,\qquad
 W={k\choose r},\qquad
 \Lambda=\sum_{j=1}^{r-1}{k\choose j},
\tag{1.1}
\]

and let \(d=d(k)\) be the least integer such that

\[
 dW+{d+1\choose2}\geq\Lambda.
\tag{1.2}
\]

Write

\[
 \sigma=dW+{d+1\choose2}-\Lambda.
\tag{1.3}
\]

Let

\[
 F=C_1\sqcup\cdots\sqcup C_c
\tag{1.4}
\]

be a physical rank-\(r\) Johnson two-factor on all \(W\) middle vertices,
so every old factor edge is a rank-one Johnson transition. Choose
\(b_a\geq1\) cut edges on \(C_a\), and put

\[
 b=\sum_{a=1}^{c}b_a.
\tag{1.5}
\]

Deleting the cuts gives \(b\) path segments, with isolated vertices allowed.
A direct physical surgery chooses one orientation of every segment and
adds \(b-1\) seams to form one middle chronology. Thus

\[
 b-1=(c-1)+(b-c).
\tag{1.6}
\]

Only \(c-1\) seams are forced by topology; each additional cut creates one
additional routing obligation.

For a sequence \(T=(T_0,\ldots,T_{n-1})\), define its maximal linear
depth-\(d\) erosion by

\[
 E_j^{\max}=
 \bigcap_{\substack{0\leq i<n\\i\leq j\leq i+d}}T_i,
 \qquad 0\leq j<n+d.
\tag{1.7}
\]

For a transition \(T_i\to T_{i+1}\), put

\[
 A_i=T_i\setminus T_{i+1},\qquad
 B_i=T_{i+1}\setminus T_i.
\tag{1.8}
\]

The sets \(A_i,B_i\) may have size greater than one at a relaxed seam.

## 2. Exact factorability and the residence transversal

### Lemma 2.1 (exact depth-\(d\) antecedent criterion)

There exists a word \(E\) of nonempty letters satisfying

\[
 D^dE=T
\tag{2.1}
\]

if and only if

\[
 B_i\cap A_j=\varnothing
\quad
(0\leq i<j\leq n-2,\ 1\leq j-i\leq d)
\tag{2.2}
\]

and every letter of \(E^{\max}\) in (1.7) is nonempty.

When these conditions hold, \(E^{\max}\) itself satisfies (2.1).

#### Proof

Every antecedent letter at position \(j\) is contained in every carrier
set whose depth-\(d\) window contains \(j\), so \(E_j\subseteq E_j^{\max}\).
Nonemptiness of (1.7) is necessary.

Coordinatewise, a member of \(B_i\cap A_j\) has an internal positive carrier
run beginning after transition \(i\), ending at transition \(j\), and having
length \(j-i\). Therefore (2.2) is precisely the absence of an internal
positive run of length at most \(d\). Binary erosion followed by dilation
recovers a trace exactly under this condition; boundary runs may be shorter
because the source word extends \(d\) positions past the carrier. Hence
\(D^dE^{\max}=T\). \(\square\)

For a Johnson chronology with Johnson seams and \(d<r\), nonemptiness is
automatic: at most \(d\) coordinates can disappear from the intersection
of \(d+1\) consecutive rank-\(r\) states. It must be checked separately for
rank-\(s>1\) seams.

For every coordinate \(x\), call a cyclic positive run of length at most
\(d\) bad. Its closed edge span consists of its entering edge, all internal
edges, and its leaving edge.

### Lemma 2.2 (exact old-defect cut transversal)

Every retained segment is internally depth-\(d\) resident if and only if
the selected cut set meets the closed span of every old bad run.

#### Proof

An old bad run survives wholly inside one retained segment exactly when no
edge of its closed span is cut. Reversal preserves its length. \(\square\)

This condition removes old internal defects. New defects formed across
seams still require collar compatibility.

## 3. Literal ports and the topology flow

For a segment \(P_i\), let \(P_i^+\) and \(P_i^-\) denote its two
orientations. Their initial and terminal physical rank-\(r\) states are
literal ports.

A connector option

\[
 a:(i,\varepsilon)\longrightarrow(j,\eta)
\tag{3.1}
\]

contains:

* the actual physical endpoint states;
* its removal and insertion sets \(A(a),B(a)\);
* its lower intersection and upper union;
* its phase and voltage when represented in a quotient catalogue; and
* its residence and shadow collar records.

Quotient endpoint adjacency without the physical phase is not a connector.

Use orientation variables \(o_{i,\varepsilon}\), start/end variables
\(s_{i,\varepsilon},t_{i,\varepsilon}\), and connector variables \(z_a\),
all nonnegative binary. Impose

\[
 o_{i,+}+o_{i,-}=1,
\tag{3.2}
\]

\[
 \sum_{a\ {\rm into}\ (i,\varepsilon)}z_a
   =o_{i,\varepsilon}-s_{i,\varepsilon},
\qquad
 \sum_{a\ {\rm out\ of}\ (i,\varepsilon)}z_a
   =o_{i,\varepsilon}-t_{i,\varepsilon},
\tag{3.3}
\]

\[
 \sum_{i,\varepsilon}s_{i,\varepsilon}
 =\sum_{i,\varepsilon}t_{i,\varepsilon}=1.
\tag{3.4}
\]

Put \(y_{ij}=\sum_{a:i\to j}z_a\). For every nonempty proper segment set
\(X\), impose

\[
 \sum_{i,j\in X}y_{ij}\leq |X|-1.
\tag{3.5}
\]

### Lemma 3.1 (exact path topology)

The integral solutions of (3.2)--(3.5) are exactly the choices of one
orientation per segment and \(b-1\) literal connectors forming one directed
path through every segment.

#### Proof

Equations (3.3)--(3.4) give indegree and outdegree one except at one start
and one end. Hence the selected arcs form one directed path together with
possibly some directed cycles. Inequality (3.5) excludes every such cycle.
Conversely, a directed spanning path supplies all variables and satisfies
the inequalities. \(\square\)

For a cycle-first equivariant surgery in a free \(C_k\)-quotient (as at the
odd middle level), omit \(s,t\), require indegree and outdegree one, use
(3.5) only for proper \(X\), and select \(b\) connectors. The quotient
voltage is

\[
 v\equiv
 \sum_{i,\varepsilon}\beta_i^\varepsilon o_{i,\varepsilon}
 +\sum_a\alpha(a)z_a\pmod k.
\tag{3.6}
\]

Under this freeness hypothesis, the physical lift is one cycle exactly when

\[
 \gcd(v,k)=1.
\tag{3.7}
\]

With nontrivial stabilizers, phase-coset compatibility is an additional
port row and (3.7) alone is insufficient. In the free case one may then
choose one physical opening edge. Its upper last-witness losses must be
audited separately; appending the depth-\(d\) prefix recovers all cyclic
lower cells.

## 4. The separated collar theorem

Fix lower and upper audit depths \(0\leq Q_-\leq d\) and \(Q_+\geq0\), and put

\[
 Q=\max\{Q_-,Q_+,d\}.
\tag{4.1}
\]

Assume every retained segment has at least \(Q+1\) vertices. Then a
depth-\(q\) window with \(q\leq Q\), and a forbidden residence comparison
of span at most \(d\), can meet at most one seam.

For an oriented segment \(P\), retain its last \(Q\) transitions and first
\(Q\) transitions as its terminal and initial collars. A connector
\(a:P\to P'\) is \(d\)-collar compatible if the concatenated terminal
collar, seam transition, and initial collar satisfies (2.2), and every
maximal-erosion footprint crossing the seam is nonempty.

For sign \(\varepsilon\in\{-,+\}\), define

\[
 \chi_q^-(X_0,\ldots,X_q)=\bigcap_{j=0}^{q}X_j,\qquad
 \chi_q^+(X_0,\ldots,X_q)=\bigcup_{j=0}^{q}X_j.
\tag{4.2}
\]

Let \(\mu_q^\varepsilon(R)\) be the old cyclic multiplicity of target \(R\).
For a selected cut edge \(e\), let \(L_{e,q}^\varepsilon(R)\) count the old
cross-cut windows labelled \(R\). For a proposed seam \(a\), let
\(G_{a,q}^\varepsilon(R)\) count the new cross-seam windows labelled \(R\).
For \(\varepsilon=-\), let
\(\partial_{i,\eta,q}^{L}(R)\) and
\(\partial_{i,\eta,q}^{R}(R)\) be the exact multiplicities of \(R\) among
the \(q\) truncated left or right boundary cells of the maximal fixed lower
row when \(P_i^\eta\) is respectively the first or last segment. For
\(\varepsilon=+\), set these boundary labels to zero.

### Theorem 4.1 (separated multi-cut protected splice)

Fix a \(Q\)-separated cut set satisfying Lemma 2.2. A choice of segment
orientations and seams gives a depth-\(d\) factorable physical middle path,
covers every prescribed lower target through depth \(Q_-\), and covers every
prescribed upper target through depth \(Q_+\) if and only if:

1. only \(d\)-collar-compatible connectors are selected;
2. the path equations (3.2)--(3.5) hold; and
3. for every prescribed sign \(\varepsilon\), every
   \(1\leq q\leq Q_\varepsilon\), and every target \(R\),
   \[
   \boxed{
   \mu_q^\varepsilon(R)
   -\sum_{e\ {\rm cut}}L_{e,q}^\varepsilon(R)
   +\sum_aG_{a,q}^\varepsilon(R)z_a
   +{\bf1}_{\varepsilon=-}
     \sum_{i,\eta}\left(
       \partial_{i,\eta,q}^{L}(R)s_{i,\eta}
       +\partial_{i,\eta,q}^{R}(R)t_{i,\eta}
     \right)
   \geq1.}
   \tag{4.3}
   \]

#### Proof

Lemma 3.1 gives one physical chronology. Every old short run was cut by
Lemma 2.2. Separation ensures that every newly formed forbidden run meets
one seam only, so collar compatibility is necessary and sufficient for
(2.2). The connector definition checks nonempty seam footprints, while old
segment footprints were already valid. Lemma 2.1 therefore gives a nonempty
depth-\(d\) antecedent.

Every new internal audited window either lies wholly in a retained segment
or crosses one selected seam. The unchanged, deleted, and gained internal
window multisets are disjoint and exhaustive. A fixed lower row has in
addition exactly \(q\) truncated cells at each linear endpoint, recorded by
the two \(\partial\)-terms. Upper carrier rows have no such cells. Thus the
left side of (4.3) is the exact new multiplicity, and its positivity is
target coverage. \(\square\)

For fixed cuts and orientations, all loss terms are constants and all gain
terms are additive arc labels. Thus Theorem 4.1 is a finite labelled
port-path flow with subtour cuts. It is not a scalar component-connectivity
criterion.

### Corollary 4.2 (exact occurrence census)

At an audited depth \(1\leq q\leq Q_\varepsilon\),

\[
 \sum_R\sum_eL_{e,q}^\varepsilon(R)=bq,\qquad
 \sum_R\sum_aG_{a,q}^\varepsilon(R)z_a=(b-1)q.
\tag{4.4}
\]

Hence the unavoidable aggregate occurrence loss is exactly \(q\),
independent of \(b\). Nevertheless as many as \(bq\) different last
witnesses can be endangered. Equation (4.4) concerns internal carrier
windows; the fixed lower row also has \(2q\) endpoint cells and therefore
has net aggregate gain \(q\) relative to the old cyclic row.

## 5. Short segments: the exact state-expanded replacement

Pairwise collars are false when a short segment lets a residence defect or
a shadow window cross two seams. There is nevertheless an exact finite
replacement.

Let \(\Sigma\) contain:

* the last \(d+1\) physical carrier states, with a boundary sentinel;
* the rolling intersections needed to test every completed or truncated
  maximal-erosion footprint;
* the last \(Q+1\) states needed for fixed-window labels;
* the current quotient phase or physical lift class; and
* any accumulated-union or intersection register used below.

The run-state rejects when appending a physical state creates
\(0\,1^\ell\,0\), \(1\leq\ell\leq d\), in some coordinate. Every oriented
segment and connector also rejects when a newly completed intersection of
at most \(d+1\) carrier states is empty. Initial states check all truncated
prefix footprints, and terminal acceptance checks all truncated suffix
footprints. Thus the state enforces both clauses of Lemma 2.1, not only its
short-run clause. Every oriented segment and connector is therefore a
finite partial transition on \(\Sigma\).

Expand a port to

\[
 (i,\varepsilon,\sigma),\qquad \sigma\in\Sigma,
\tag{5.1}
\]

and retain an arc only when traversing \(P_i^\varepsilon\) and its connector
maps \(\sigma\) to the entrance state of the next port.

The expanded master chooses exactly one state-orientation copy of every
original segment:

\[
 \sum_{\varepsilon,\sigma}o_{i,\varepsilon,\sigma}=1
 \qquad(i=1,\ldots,b),
\tag{5.2}
\]

For each expanded copy \(v=(i,\varepsilon,\sigma)\), impose the degree rows

\[
 \sum_{a\ \mathrm{\,into\,}v}z_a=o_v-s_v,
 \qquad
 \sum_{a\ \mathrm{\,out\ of\,}v}z_a=o_v-t_v.
\tag{5.3}
\]

Start variables are permitted only at copies whose entrance history is the
boundary-sentinel state; end variables are permitted only at
terminal-accepting copies. The global start/end equations (3.4) hold on
these expanded copies. Only the subtour rows (3.5) are projected to the
original segment indices. Thus an incoming arc and an outgoing arc cannot
use two different history copies of the same selected segment.

### Theorem 5.1 (state-expanded multi-cut equivalence)

For arbitrary segment lengths, a resident, nonempty-factorable oriented
multi-cut splice with all prescribed fixed-window shadows exists if and
only if the state-expanded port graph has an integral projected spanning
path satisfying (5.2)--(5.3), the expanded start/end equations (3.4), the
projected subtour equations (3.5), terminal acceptance, and every
target-emission row.

#### Proof

A physical splice has a unique entrance history at every segment and hence
lifts to a state-expanded path. Conversely, (5.2) and the projected path
rows give one copy of each segment in one chronology, and equality of
adjacent history states makes the local partial maps concatenate. The
sentinel gives the correct linear boundary rule. Every forbidden run,
every maximal-erosion footprint, and every fixed-window label is decided
when its last state is appended or at terminal acceptance. Lemma 2.1 then
gives a nonempty antecedent, so the accepted path has exactly the required
properties. \(\square\)

This is a finite generalized path-flow problem. It is not claimed to be
totally unimodular; the segment-once and subtour constraints remain integral
master constraints.

## 6. Unrestricted upper intervals

Fixed \(q\)-edge rows can be too strong for upper targets: a rank-\((r+q)\)
union may first occur after more than \(q\) edges. The exact replacement is
an accumulated-union reachability cut.

Fix an upper target \(U\). Form an automaton with states

\[
 (J,X),\qquad
 X\in{U\choose r},\quad X\subseteq J\subseteq U.
\tag{6.1}
\]

Every \((X,X)\) is a source and every \((U,X)\) is accepting. A selected
physical carrier arc \(X\to Y\), with \(Y\subseteq U\), gives

\[
 (J,X)\longrightarrow(J\cup Y,Y).
\tag{6.2}
\]

Let \(y_\alpha\) say that literal directed carrier arc \(\alpha\) is
selected. For a node set \(R\) containing every source and no accepting
node, let \(B_U(R)\) be the set of distinct physical arc labels leaving
\(R\). Impose

\[
 \boxed{\sum_{\alpha\in B_U(R)}y_\alpha\geq1.}
\tag{6.3}
\]

### Theorem 6.1 (exact upper reachability)

The selected chronology contains a contiguous interval with union \(U\)
if and only if every cut (6.3) holds.

#### Proof

A carrier interval lifts to the automaton with its running union, and an
accepting automaton path projects to a contiguous selected carrier path.
Every accepting path crosses every source-separating cut. Conversely, if no
accepting state is reachable, the reachable node set violates (6.3).
\(\square\)

The same construction with \(J\cap Y\) gives exact unrestricted
intersection reachability when it is wanted. For the fixed erosion rows,
the fixed-depth equations (4.3) are the relevant lower conditions.

The rows (6.3) may be separated lazily from an integral port solution or
implemented as conditional network flow. The auxiliary reachability network
is totally unimodular after the carrier arcs are fixed; the combined
orientation/port master is not.

## 7. Lower-owner current

Assume \(k=2r-1\) and the old two-factor has a globally rainbow immediate
lower edge colouring. Let \(r_L\in\{0,1\}\) indicate that lower colour \(L\)
survives internally. For a Johnson connector \(a\), let \(\ell(a)\) be its
intersection colour. Introduce \(h_L\) when \(L\) is delegated to the
literal compiler.

The exact immediate-lower coverage rows are

\[
 r_L+\sum_{a:\ell(a)=L}z_a+h_L\geq1.
\tag{7.1}
\]

If duplicates are forbidden, replace these by equality. A direct path has
only \(W-1\) middle transitions, so at least one \(h_L\) is unavoidable.
If every selected seam is Johnson and the immediate row is required to be
an owner-exact no-duplicate transversal, then exactly \(W-1\) immediate
lower colours occur and

\[
 \sum_Lh_L=1.
\tag{7.2}
\]

For a cycle-first surgery whose connectors are all Johnson and whose
immediate row is owner-exact, set every \(h_L=0\); the \(b\) connectors use
the \(b\) freed colours exactly once. The final physical opening creates
one literal lower demand. Without these Johnson and no-duplicate
hypotheses, only the inequalities (7.1) are valid and several compiler
demands may be necessary.

The immediate upper rows are similarly

\[
 r_U^+ +\sum_{a:u(a)=U}z_a\geq1.
\tag{7.3}
\]

These coloured current rows are part of the port master, not a consequence
of its unlabelled flow.

## 8. Exact collar and compiler damage

Assume now that the cut collars are disjoint, as in Theorem 4.1. At the
source row:

\[
 \begin{array}{c|c}
 \text{bank}&\text{number of positions}\\ \hline
 \text{stable transported old positions}&W-bd\\
 \text{discarded old cut collar}&bd\\
 \text{new seam plus endpoint collar}&(b+1)d.
 \end{array}
\tag{8.1}
\]

At the row whose carrier footprint has \(q+1\) vertices, the corresponding
counts are

\[
 W-bq,\qquad bq,\qquad (b+1)q.
\tag{8.2}
\]

Therefore the full discarded and new lower collars have sizes

\[
 b{d+1\choose2},
\qquad
 (b+1){d+1\choose2}.
\tag{8.3}
\]

These are changed cells, not automatically wasted cells.

Let \(P\) be the new maximal envelope. A joint one-core and literal compiler
for a flexible lower family \(\mathcal F\) is exactly the following finite
\(0\)-\(1\) system. Use core variables \(c_{p,x}\) and matching variables
\(f_{S,p}\). Here \(0\leq p\leq W+d-1\) in (8.4), while
\(0\leq p\leq W+d-2\) in the noncyclic adjacent-pair equation (8.5):

\[
 c_{p,x}\leq{\bf1}_{x\in P_p},
\tag{8.4}
\]

\[
 c_{p,x}+c_{p+1,x}\geq1
\quad\text{whenever }x\in P_p\cup P_{p+1},
\tag{8.5}
\]

\[
 \sum_pf_{S,p}=1,\qquad
 \sum_Sf_{S,p}\leq1,
\tag{8.6}
\]

\[
 f_{S,p}=0\quad(S\nsubseteq P_p),
\qquad
 f_{S,p}+c_{p,x}\leq1\quad(x\notin S).
\tag{8.7}
\]

### Theorem 8.1 (exact one-core compiler gate)

System (8.4)--(8.7) is feasible if and only if some one-core
\(C\subseteq P\), \(DC=DP\), has a physical occurrence matching saturating
\(\mathcal F\).

For fixed \(C\), the remaining problem is one ordinary bipartite max flow.

#### Proof

Equations (8.4)--(8.5) are the coordinatewise one-core equations.
Equations (8.6) are matching equations. If \(f_{S,p}=1\), (8.7) says
\(S\subseteq P_p\) and forbids every core coordinate outside \(S\), hence
\(C_p\subseteq S\subseteq P_p\). Conversely any core and matching assign
these variables. \(\square\)

Suppose an old physical matching \(M_0\) is retained on a target family
\(\mathcal R\) at stable positions. Let \(V_{\rm new}\) denote the entire
new source-position shore
\(V(P)=\{0,\ldots,W+d-1\}\), including stable and rebuilt-collar
positions. First require every frozen edge to remain legal for the chosen
new core:

\[
 C_{M_0(S)}\subseteq S\subseteq P_{M_0(S)}
 \qquad(S\in\mathcal R).
\]

Subject to this requirement, the exact residual condition is that

\[
 G_C\bigl[\mathcal F\setminus\mathcal R,\,
 V(P)\setminus M_0(\mathcal R)\bigr]
\tag{8.8}
\]

has a matching saturating \(\mathcal F\setminus\mathcal R\).
Equivalently, for every residual target shore \(X\),

\[
 |N_{G_C}(X)\setminus M_0(\mathcal R)|\geq |X|.
\tag{8.9}
\]

At most \(bd\) old literal assignments can be displaced at source level.
Additional fixed-row holes, including the \(h_L\) in (7.1), join the
residual target family. This is the exact sense in which the splice can be
absorbed without increasing word length.

The broader non-graded PCSH gate is also finite. Start with a finite
catalogue \(\Gamma\) of eligible lower pins \((t,i,S)\), and choose binary
variables \(u_{t,i,S}\) with one chosen pin for each required target \(S\)
and at most one chosen target at each derivative cell \((t,i)\). Let
\(\mathcal P(u)\) contain those chosen pins, every retained fixed lower pin,
and all middle pins \((d,i,T_i)\). For each coordinate \(x\) put

\[
 Q_x=[0,W+d-1]\setminus
 \bigcup_{\substack{(t,i,S)\in\mathcal P(u)\\x\notin S}}[i,i+t].
\tag{8.10}
\]

One common nonempty word realizes all lower and middle pins if and only if

\[
 x\in S\Longrightarrow [i,i+t]\cap Q_x\ne\varnothing
\tag{8.11}
\]

for every \((t,i,S)\in\mathcal P(u)\), and

\[
 \bigcup_xQ_x=[0,W+d-1].
\tag{8.12}
\]

Indeed, the maximal allowed source word \(A_p=\{x:p\in Q_x\}\) then has
exactly the selected and fixed interval unions. Conversely, every common
word supplies such \(u\)-variables and satisfies these conditions. This
gives a finite residual assignment-plus-hitting system. Ordinary
target-to-cell flow alone is not sufficient before (8.11)--(8.12) are
checked. In particular, inclusion of every middle pin is essential: it
forces

\[
 Q_x\subseteq\{p:x\in P_p\},
\]

where \(P\) is the maximal depth-\(d\) erosion, so the resulting word has
\(D^dA=T\), not merely \(D^dA\supseteq T\).

### Corollary 8.2 (the scalar meaning of \(\sigma\))

If \(a\) stable lower assignments are frozen, then

\[
 (\text{remaining lower cells})-(\text{remaining lower targets})
 =(dW+{d+1\choose2}-a)-(\Lambda-a)=\sigma.
\tag{8.13}
\]

Thus deadline slack is unchanged by freezing stable pins. It is only a
global cardinality surplus in the residual instance. It implies none of the
port rows (3.2)--(3.5), shadow rows (4.3), core constraints
(8.4)--(8.5), or Hall inequalities (8.9).

## 9. The exact \(k=15\) degree-only factor

The motivating artifact is

\[
\texttt{scratch/k15\_joint\_scaffold\_degreeonly\_r61.json}.
\]

Its SHA-256 is

\[
\texttt{5ad877cfa8f599d28fdddbcc0154c1bd4e73f850313ff3f8df59a5fd1f6089ac}.
\]

It is an exact \(C_{15}\)-equivariant degree-two owner factor, not a
resident or shadow-complete carrier.

### Proposition 9.1 (certificate-audited component and deficit census)

The quotient factor has three cycles. With one orientation their
\((\text{length},\text{voltage})\) pairs are

\[
 (244,11),\qquad(47,10),\qquad(138,0).
\tag{9.1}
\]

Their lift gcds are \(1,5,15\), giving the 21 physical cycles

\[
 3660,\qquad5\times141,\qquad15\times138.
\tag{9.2}
\]

The factor has:

\[
\begin{array}{c|c|c}
\text{defect}&\text{orbit count}&\text{physical count}\\ \hline
\text{residence, run length }2&27&405\\
\text{residence, run length }3&26&390\\
\text{lower rank }6&55&805\\
\text{lower rank }5&20&300\\
\text{upper rank }9&46&680\\
\text{upper rank }10&26&390\\
\text{upper rank }11&5&75.
\end{array}
\tag{9.3}
\]

Its physical upper-rank-nine load histogram is

\[
 0^{680}1^{2730}2^{1200}3^{305}4^{60}5^{30}.
\tag{9.4}
\]

#### Proof

The artifact chooses one lower-owner orbit at every quotient root and has
degree two. Direct component lifting gives (9.1)--(9.2). The physical audit
gives the counts in (9.3)--(9.4). Every residence-defect orbit has size
fifteen because coordinate rotation acts freely on its marked coordinate;
\(405/15=27\) and \(390/15=26\). \(\square\)

The explicit decoder is
\texttt{scratch/audit\_k15\_joint\_scaffold\_degreeonly\_r61\_overlay.py}
(SHA-256
\texttt{0b4cdcddc21e3f9baa0269d32e0674d688eafab95b36dc3cb7b6a7c3f37d6ad4});
its frozen audit output is
\texttt{scratch/k15\_joint\_scaffold\_degreeonly\_r61\_overlay.audit.json}
(SHA-256
\texttt{94ffed00bdfa112195617e16371015d617c94043c156d8a76f83a2d0c9fa6aff}).
The general surgery theorems above do not depend on this finite census.

One quotient edge orbit is not one physical cut. In the three quotient
components, one physical lift traverses the quotient cycle respectively

\[
 15,\qquad3,\qquad1
\tag{9.5}
\]

times. Deleting a full edge orbit therefore makes those numbers of cuts in
each relevant physical lift cycle. Exact quotient surgery must retain
quotient position, sheet phase or lift class, and orientation in every port.

### Theorem 9.2 (exact necessary direct-physical surgery scale)

Any phase-specific direct physical surgery which repairs all missing
rank-nine targets requires

\[
 b\geq681.
\tag{9.6}
\]

If every segment has at least eight vertices, so all fixed depths through
seven are separated, then

\[
 b\leq
 \left\lfloor{3660\over8}\right\rfloor
+5\left\lfloor{141\over8}\right\rfloor
+15\left\lfloor{138\over8}\right\rfloor
=797.
\tag{9.7}
\]

Hence the separated direct-physical gate lies in the exact necessary
corridor

\[
 \boxed{681\leq b\leq797.}
\tag{9.8}
\]

If the selected cuts destroy the last witnesses of \(h_{\rm cut}\) further
rank-nine targets, then

\[
 b-1\geq680+h_{\rm cut}.
\tag{9.9}
\]

#### Proof

Internal retained edges have exactly their old unions. Each new seam has one
union and can create at most one missing rank-nine target; a rank-\(s>1\)
seam creates rank at least ten. There are 680 missing physical rank-nine
targets and \(b-1\) seams, proving (9.6) and (9.9).

Eight vertices per segment are necessary for the separated
depth-seven subclass. A cycle of length \(L\) then has at most
\(\lfloor L/8\rfloor\) segments. Summing (9.2) proves (9.7). \(\square\)

At the lower endpoint \(b=681\), all 680 seams must be Johnson, must have
pairwise distinct unions equal to the 680 missing targets, and cannot spend
a seam solely on repairing a newly cut unique upper colour. In the
owner-exact normal form (7.2), the old immediate lower colours are rainbow,
so the seams must also use 680 distinct freed lower colours, leaving one
freed colour for the compiler. This is an exact coloured
port-perfect-matching condition coupled to the path flow. A broader PCSH
compiler may repair more than one freed colour, so this last lower-colour
conclusion is not imposed outside the owner-exact normal form.

The cut-transversal lower bound from residence alone is

\[
 b\geq\left\lceil{795\over15}\right\rceil=53,
\tag{9.10}
\]

because one cut edge lies in at most one bad run of each coordinate. It is
dominated by (9.6), but all 795 individual bad-run-span hitting rows still
have to hold. They form 53 rotation classes; one hit per class is sufficient
only in a genuinely equivariant cut construction.

### Quotient-equivariant alternative

A cycle-first \(C_{15}\)-equivariant surgery needs at least 46 cut and
connector **orbits** to create the 46 missing upper-\(q=1\) orbits. At the
lower endpoint, in the owner-exact cycle-first subclass of Section 7, the 46
connectors must pair the 46 freed lower-owner orbits bijectively with the 46
missing upper orbits, while the port flow produces one quotient cycle of
unit voltage. A broader PCSH repair does not impose this lower-owner
bijection.

Those 46 cut orbits expand to 690 physical cuts. The residence state and
all shadow rows must therefore be checked at every phase; a three-node
quotient component flow is not an exact substitute.

### Proposition 9.3 (two exact \(q=1\)-complete calibrations)

The two new selection artifacts have the following exact physical census.
All edit counts in the table are recorded radii from the same joint
scaffold; neither is asserted to be a minimum distance.

\[
\begin{array}{c|c|c|c|c}
\text{artifact}&\text{edits}&\text{quotient voltage}
 &\text{physical cycles}&\text{short positive runs}\\ \hline
\texttt{degree\_atmost96\_q1inc}&94&10&5\times1287&585+465=1050\\
\texttt{q1ham\_d93\_snapshot}&93&8&6435&570+480=1050.
\end{array}
\]

Both are degree-two quotient Hamilton selections and cover every physical
rank-nine target. Their physical rank-nine load histograms are respectively

\[
 1^{3900}2^{810}3^{265}4^{30},
 \qquad
 1^{3885}2^{840}3^{250}4^{30}.
\]

They are not resident and not deeper-shadow complete. The first has
physical holes

\[
 (r-2,r-3,r+2,r+3)=(835,315,228,15),
\]

and the second has

\[
 (r-2,r-3,r+2,r+3)=(820,330,228,15).
\]

The source files and SHA-256 values are

\[
\begin{array}{c|c}
\texttt{scratch/k15\_joint\_scaffold\_degree\_atmost96\_q1inc.json}
&\texttt{d0964d71cb74bb2956e645aede7253c999be28401e1df408164e7d1aea671e5e}\\
\texttt{scratch/k15\_joint\_q1ham\_d93\_snapshot.json}
&\texttt{76a83f012687f7382f8c140a51f1ad34702f9d393596d3d1d523a1c275c1e91f}.
\end{array}
\]

#### Proof/audit

Each file specifies 429 lower-owner choices. Expanding their endpoint
incidences gives quotient degree two and one quotient cycle. Voltage \(10\)
has gcd \(5\) with \(15\), hence five physical lifts of length \(1287\);
voltage \(8\) is a unit, hence one physical lift of length \(6435\).
Expanding all fifteen phases and counting literal edge unions gives the two
load histograms, each of which has total target count \(5005\) and weighted
edge count \(6435\). The same expansion gives the displayed coordinate-run
and deeper-shadow counts. The first file's \texttt{OPTIMAL} status belongs
to its stated feasibility model with radius at most \(96\): it certifies
feasibility, not that the observed distance \(94\) is minimal. The second is
a feasible incumbent, so its distance \(93\) is likewise not certified
minimal.
\(\square\)

For either calibration, Lemma 2.2 gives the necessary residence bound

\[
 b\geq\left\lceil{1050\over15}\right\rceil=70.
\]

Under eight-vertex separation, the trivial segment maxima are

\[
 5\left\lfloor{1287\over8}\right\rfloor=800,
 \qquad
 \left\lfloor{6435\over8}\right\rfloor=804.
\]

Because the initial rank-nine deficit is zero, the \(b\ge681\) argument does
not apply to these factors. If the cuts destroy the last occurrences of
\(h_{\rm cut}\) rank-nine targets, however, exact \(q=1\) preservation still
requires

\[
 h_{\rm cut}\leq b-1,
\]

with the lost target labels supplied by Johnson seam unions. The 3900 and
3885 singleton-loaded targets make this last-witness constraint substantial.
Thus these are positive calibrations for quotient connectivity and raw
\(q=1\) capacity, but negative calibrations for any claim that connectivity
or \(q=1\) completeness automatically supplies residence or deeper shadows.
Compared with the distance-61 factor, they confirm that component topology
is not the dominant multi-cut gate.

### Compiler capacity at the forced scale

The following collar arithmetic applies to the separated subclasses in
which the phase-expanded cut collars are disjoint. With overlapping cuts,
the exact union of the changed collars must replace the products below.

At \(k=15,d=3\), the baseline one-core literal family has

\[
 |\mathcal L_5|=\sum_{j=1}^{5}{15\choose j}=4943,
\tag{9.11}
\]

while \(\sigma=2928\).

For the minimal direct physical scale \(b=681\), the stable source bank has
at most

\[
 6435-3\cdot681=4392
\tag{9.12}
\]

positions. Even if every stable position is useful, at least

\[
 4943-4392=551
\tag{9.13}
\]

targets must use rebuilt collar positions. The old full lower collar has

\[
 681{4\choose2}=4086>\sigma
\tag{9.14}
\]

cells.

If the 690 physical cuts of a minimal 46-orbit equivariant surgery are
separated, the analogous figures are

\[
 6435-3\cdot690=4365,\qquad
 4943-4365=578,
\tag{9.15}
\]

and

\[
 690{4\choose2}=4140>\sigma.
\tag{9.16}
\]

Across all three lower rows, the separated stable bank has
\(3W-6b\) cells and the rebuilt collar has \(6(b+1)\) cells. Even granting
every stable cell a different target, the rebuilt collar must serve at
least

\[
 \Lambda-(3W-6b)=6(b+1)-\sigma
\tag{9.17}
\]

targets. This is (1164) targets at (b=681), and (1218) targets at
(b=690):

\[
 6\cdot682-2928=1164,
 \qquad
 6\cdot691-2928=1218.
\tag{9.18}
\]

Therefore, in either separated subclass, no proof can discard every changed
collar cell or charge every changed cell to \(\sigma\). Hundreds of rebuilt
collar positions must be reused by the physical Hall/compiler flow. These
numerical products are not asserted for overlapping orbit collars.

## 10. Calibration at \(k=13\)

The successful \(k=13\) factor had two physical cycles, and used
\(b=2\) cuts and one seam. It was resident and shadow-complete before
surgery. Of 24,960 oriented candidates, 6,032 preserved every upper shadow
and 1,092 also preserved exact depth-three residence.

The chosen seam recreated one of the two cut lower colours. The remaining
colour became one literal compiler demand, and a fresh physical lower
compiler matched all 4,095 targets. Thus it realizes precisely the sequence:

\[
\text{port flow}\longrightarrow
\text{collar test}\longrightarrow
\text{targetwise shadow ledger}\longrightarrow
\text{physical compiler}.
\tag{10.1}
\]

The final word is not one-core graded:

\[
 |\{i:(DA)_i\ne(DP)_i\}|=209,\qquad
 |\{i:(D^2A)_i\ne(D^2P)_i\}|=1.
\tag{10.2}
\]

It calibrates the broader PCSH gate (8.10)--(8.12), not automatic
one-core transport.

## 11. Exact finite gate and proved boundary

Relative to a fixed cut set, its resulting segment decomposition, and a
finite connector catalogue, the replacement multi-cut problem is the
following integral system:

1. cut-transversal rows for every old bad run;
2. orientation, start/end, port-degree, and subtour rows
   (3.2)--(3.5), or their cycle-first variant;
3. literal phase and unit-voltage rows in an equivariant cycle surgery;
4. the state-expanded residence transitions of Theorem 5.1, unless the
   separated collars of Theorem 4.1 apply;
5. immediate owner and upper colour currents (7.1)--(7.3);
6. every fixed-window target row (4.3);
7. accumulated-union reachability cuts (6.3) for unrestricted upper
   targets;
8. a nonempty maximal envelope; and
9. either the joint one-core/matching system (8.4)--(8.7), or the broader
   residual pin-selection constraints together with the PCSH system
   (8.10)--(8.12).

All selection variables in this system are binary. If the cuts themselves
are decision variables, one must add a genuine segment-partition layer.
Enumerate edge-rooted cyclic arcs \(P\): each candidate records an ordered
retained path together with its omitted boundary edge or edges. In
particular, a candidate may contain every vertex of an old cycle provided
it omits one specified opening edge; this is the legitimate \(b_a=1\) case.
Choose binary \(w_P\) with

\[
 \sum_{P\ni v}w_P=1\qquad\text{for every old middle vertex }v,
\]

Introduce cut variables \(c_e\), require

\[
 c_e+\sum_{P:\ e\text{ is internal to }P}w_P=1
 \qquad\text{for every old factor edge }e,
\]

link every recorded boundary edge of a selected \(P\) to \(c_e=1\), require
at least one cut on each old component, and link every orientation, state
copy, and port variable to its selected \(w_P\). These edge and vertex
exact-cover/nonoverlap rows are what make all chosen macrosegments arise
from one common cut set. They are unnecessary only when the cut
decomposition is fixed in advance.

When segment order is variable, global source positions are likewise not
fixed coefficients. The exact gate may be read as a finite two-stage
disjunction: first select and order an integral port path, then unfold its
physical chronology and solve the compiler systems of Section 8. A
monolithic formulation must instead add cumulative-length/order variables
linking every segment-local and seam-collar cell to its global index; the
PCSH intervals and frozen matching positions are evaluated at those linked
indices.

### Theorem 11.1 (multi-cut surgery consumer)

An integral solution of items 1--9 produces a nonempty word of length
\(W+d\) covering every nonempty target. Therefore, when \(d=d(k)\),

\[
 \nu(k)=W+d.
\tag{11.1}
\]

Conversely, every word constructed by this fixed multi-cut, literal-port,
one-core or PCSH architecture yields an integral solution of the
corresponding system.

#### Proof

Items 1--4 produce one depth-\(d\) factorable middle chronology through all
rank-\(r\) targets. Items 5--7 give every required fixed lower and
unrestricted upper carrier target. Item 8 supplies the maximal source
envelope. Item 9 assigns every remaining lower target in one common
nonempty source word while retaining the middle pins. The identity

\[
 D^{d+q}A=D^qT
\]

transfers all carrier upper witnesses to literal OR intervals. The word has
length \(W+d\), and the endpoint-blocker lower bound gives equality.

For the converse, read the selected cuts, segment orientations, connector
arcs, history states, target witnesses, and compiler assignments from the
constructed word. Each listed row is then necessary by the preceding
lemmas. \(\square\)

What remains unproved is feasibility. For the current \(k=15\) factor the
necessary separated direct corridor is already at \(681\)--\(797\) segments, and
the equivariant lane starts at 46 cut orbits with 690 phase-expanded cuts.
The main finite obstruction is a coloured, state-expanded port flow whose
selected arcs must simultaneously hit all shadow deficits and leave a
physical residual compiler matching. Component count alone contributes
almost no useful capacity information.

## 12. Adversarial audit

The theorem makes the following scope distinctions explicit.

* The \(k=15\) artifact is degree-only. Its 795 residence defects and
  shadow holes are active repair rows, not protected data.
* The numerical censuses in Propositions 9.1 and 9.3 are
  certificate-audited finite facts. The general multi-cut theorems do not
  use their enumeration.
* Pairwise collar compatibility is used only under the \(Q+1\)-vertex
  separation hypothesis. Short segments require Theorem 5.1.
* The 681 lower bound concerns phase-specific physical surgery. The
  46-orbit alternative is equivariant and must be expanded through all
  phases before residence or Hall is claimed.
* The occurrence identity loses only \(q\) cells in aggregate, but can
  destroy \(bq\) last witnesses.
* Changed collar cells are not wasted cells. Equations (9.14)--(9.16)
  explicitly show why a charge-to-\(\sigma\) proof cannot work.
* A target-to-cell matching is not a common word. Either the one-core
  equations or all PCSH hitting conditions must also pass.
* The finite system is not asserted to be polynomial or totally
  unimodular. Only the fixed-core compiler and fixed-carrier reachability
  subproblems are ordinary flows.
