# Lane W: a single-promotion PBBS collar and the exact two-core braid obstruction

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or probabilistic rounding theorem is used.

### Audit scope notice

The cap criterion in Theorem 4.2 is exact for the explicit cyclic lower
queue (2.2), together with path reversal; arbitrary terminal queue fillers
give a larger list of legal caps. The separated-star theorem in Section 5
is conditional on compatible radius-\(H\) endpoint completions for all
pieces. Equations (7.1)--(7.2) are in the odd projected PBBS model, whereas
the collar in Sections 1--4 is even; their ambient \(W\)'s must not be
identified. Finally, the QCF ledger in Section 8 is conditional on
owner-disjoint substituted baselines, declared target coverage, and the
cluster applicability inequalities stated there. These qualifications do
not alter the explicit collar formulas or its \(W+2H\operatorname{Cat}_m\)
literal ledger.

## 0. Outcome

Fix \(A>0\), put

\[
 H=\lceil A\sqrt m\rceil,\qquad Q=[2m],\qquad
 W=\binom{2m}{m},\qquad
 B={W\over m+1}=\operatorname {Cat}_m.
\]

For all sufficiently large \(m\), \(H<m\). This note gives one genuine
positive full-state construction and one exact no-go for the most natural
PBBS crossing circuit.

1. Cut every row of an exact \((2m+1,m)\)-wreath factor at a fixed
   coordinate \(\infty\). The remaining even-ground owners are \(B\)
   complementary Johnson geodesics of \(m+1\) owners, and they partition
   \(\binom Qm\).
2. Every such geodesic has an explicit radius-\(H\) full-state lift. Its
   first edge is one singleton promotion and every later edge is a rotor.
   Hence the selected states have exactly
   \[
      p=B={W\over m+1}=o_A(W/H)
   \]
   bridge-one paths and compile literally with exact length
   \[
      \boxed{W+2HB=W+o_A(W).}
   \]
3. The collar preserves complete interval columns. At every depth
   \(q\le H\), all lower flags are cyclic \((m-q)\)-intervals. The upper
   boundary is a correlated interpolation: it has exactly one repeated
   value per row, rather than the \(q+1\)-fold repetition produced by the
   earlier entry-neutral cache. The complements of the upper flags use one
   fixed multiset of cyclic starts, independent of \(q\).
4. At depth one the upper flags are unconditionally exactly balanced.
   Lower depth-one balance is exactly a two-choice capacitated cap
   matching. At depths \(q\ge2\), simultaneous balance remains an
   unproved half-necklace interval-load theorem. Thus the construction
   solves chronology and literal length, but it does **not** prove
   \((\mathrm{CP}_A)\).
5. A genuine nonlocal positive braid also exists: common-facet PBBS pieces
   whose left insertion alphabet and right removal alphabet are disjoint
   concatenate in arbitrary order into one bridge-one path.
6. The canonical zero-winding two-core atlas cannot supply the needed
   joins. In the Gaussian range its induced Johnson graph is exactly two
   disjoint odd cycles. If the active window length is \(s\le H\), every
   atlas-confined bridge path has at most \(s+1\) owners. The physical
   two-row packet therefore needs two paths and has a nonvanishing
   initialization ratio. Cross-atlas or cross-core chords are mandatory.

The corrected sandwich/QCF accounting is explicit. Actual bridge-one joins
cost only the next baseline owner. No sandwich or QCF chart is charged at
an internal join. A separately paid hard seam costs \(4H-1\), or
\(7H+3S-3\) for the audited cluster chart of span \(S\), and therefore
must occur only \(o(W/H)\) times at bounded normalized span.

## 1. Special-coordinate wreath geodesics

Let \(\Omega=Q\cup\{\infty\}\). An exact odd wreath factor partitions
\(\binom\Omega m\) into \(B\) cyclic wreath rows. In one row, cut at the
unique odd-graph edge which omits \(\infty\), and retain the rank-\(m\)
owners avoiding \(\infty\). They form a Johnson geodesic

\[
 P=(X_0,X_1,\ldots,X_m),\qquad X_m=Q\setminus X_0,
\]

with

\[
 X_{t+1}=X_t-a_t+b_t\qquad(0\le t<m).
\]

The labels \(a_0,\ldots,a_{m-1}\) order \(X_0\), and
\(b_0,\ldots,b_{m-1}\) order \(Q\setminus X_0\). Define the cyclic word

\[
 w=(a_0,\ldots,a_{m-1},b_0,\ldots,b_{m-1})
\]

of length \(2m\), and write

\[
 I_w(s,d)=\{w_s,w_{s+1},\ldots,w_{s+d-1}\}
\]

with subscripts modulo \(2m\). Then

\[
 \boxed{X_t=I_w(t,m)\qquad(0\le t\le m).}
 \tag{1.1}
\]

The \(m+1\) owners in every row, over all \(B\) rows, partition
\(\binom Qm\). Put

\[
 Y_t=X_t\cup X_{t+1}=I_w(t,m+1)
 \qquad(0\le t<m).
 \tag{1.2}
\]

The \(mB=\binom{2m}{m+1}\) sets \(Y_t\), over all rows, partition
\(\binom Q{m+1}\). Indeed the \(m\) omitted owners of the cut odd wreath
are exactly

\[
 \{\infty\}\cup(Q\setminus Y_t),\qquad 0\le t<m.
\]

Exact odd middle ownership partitions all rank-\(m\) sets containing
\(\infty\), and complementation gives the assertion about the \(Y_t\)'s.

## 2. The single-promotion full collar

A full state over an owner \(X\) is specified by an ordered deletion queue
\(\alpha=(\alpha_1,\ldots,\alpha_H)\subset X\) and an ordered addition
cache \(\beta=(\beta_1,\ldots,\beta_H)\subset Q\setminus X\). Its flags
are

\[
 L_q=X\setminus\{\alpha_1,\ldots,\alpha_q\},\qquad
 U_q=X\cup\{\beta_1,\ldots,\beta_q\}.
 \tag{2.1}
\]

On the path (1.1), define

\[
 \alpha_t=(w_t,w_{t+1},\ldots,w_{t+H-1})
 \qquad(0\le t\le m).
 \tag{2.2}
\]

For the upper cache take

\[
 \boxed{
 \beta_0=(b_0,b_{m-1},b_{m-2},\ldots,b_{m-H+1}).}
 \tag{2.3}
\]

For \(1\le t\le H\), put

\[
 \boxed{
 \beta_t=(a_{t-1},a_{t-2},\ldots,a_0,
          b_{m-1},b_{m-2},\ldots,b_{m-H+t}),}
 \tag{2.4}
\]

where the \(b\)-tail is empty at \(t=H\). For \(H\le t\le m\), put

\[
 \boxed{\beta_t=(a_{t-1},a_{t-2},\ldots,a_{t-H}).}
 \tag{2.5}
\]

The formulas agree at \(t=H\).

### Theorem 2.1 (single-promotion bridge lift)

For every \(H<m\), (2.2)--(2.5) define a legal full useful state above
every \(X_t\). The edge \(X_0\to X_1\) is the bridge-one promotion of
\(b_0\) from cache position one. Every edge \(X_t\to X_{t+1}\) with
\(1\le t<m\) is a bridge-one rotor. Consequently the path word has exact
length

\[
 (m+1)+2H.
 \tag{2.6}
\]

#### Proof

The queue \(\alpha_t\) lies in the cyclic \(m\)-interval \(X_t\). Its
unused lower block is

\[
 I_w(t+H,m-H),
\]

and \(w_{t+H}\) lies in that block. Therefore

\[
 \alpha_{t+1}=(\alpha_{t,2},\ldots,\alpha_{t,H},w_{t+H})
\]

is the exact bridge queue recurrence.

Every entry of \(\beta_t\) is outside \(X_t\). At edge zero the entering
coordinate \(b_0\) is the first cache entry, so promotion gives (2.4) at
\(t=1\). Suppose \(1\le t<H\). The \(b\)-indices still in \(\beta_t\)
are at least \(m-H+t>t\), because \(H<m\). Hence the entering coordinate
\(b_t\) is not cached and lies in the residual upper block. A rotor
prepends \(a_t\) and evicts \(b_{m-H+t}\), giving \(\beta_{t+1}\). At
\(t\ge H\), the cache contains only previously removed \(a\)-labels, so
\(b_t\) is again residual and the rotor recurrence gives (2.5).

A full-state initialization costs \(2H+1\) letters and each of the \(m\)
bridge-one updates costs one further letter. This proves (2.6). \(\square\)

### Corollary 2.2 (exact global path and literal ledger)

Applying Theorem 2.1 to all \(B\) rows selects one full state above every
middle owner and gives exactly \(p=B\) bridge-one paths. Their total word
length is

\[
 \boxed{L=W+2HB.}
 \tag{2.7}
\]

For \(H=\lceil A\sqrt m\rceil\),

\[
 {p\over W/H}={H\over m+1}\longrightarrow0,\qquad
 {L-W\over W}={2H\over m+1}\longrightarrow0.
 \tag{2.8}
\]

Thus this exact factor class has no remaining chronology, integrality, or
literal-realizability loss.

## 3. Complete interval columns and the correlated upper interpolation

The lower flags are

\[
 \boxed{L_q(X_t)=I_w(t+q,m-q)}
 \qquad(0\le t\le m,\ 1\le q\le H).
 \tag{3.1}
\]

For the upper flags, empty \(b\)-ranges below are omitted. At \(t=0\),

\[
 \boxed{
 U_q(X_0)=X_0\cup\{b_0\}
                \cup\{b_{m-q+1},\ldots,b_{m-1}\}.}
 \tag{3.2}
\]

For \(1\le t<q\),

\[
 \boxed{
 U_q(X_t)=X_0
   \cup\{b_0,\ldots,b_{t-1}\}
   \cup\{b_{m-q+t},\ldots,b_{m-1}\}.}
 \tag{3.3}
\]

For \(q\le t\le m\),

\[
 \boxed{U_q(X_t)=I_w(t-q,m+q).}
 \tag{3.4}
\]

Equations (3.2) and (3.3) at \(t=1\) are identical. For
\(1\le t<q\), the passage from \(t\) to \(t+1\) replaces the high label
\(b_{m-q+t}\) by the low label \(b_t\). These labels are distinct because
\(q<m\). All later values are distinct cyclic intervals, and every value
after \(t=q\) omits an \(a\)-label which the boundary values contain.
Hence

\[
 \boxed{
 U_q(X_0)=U_q(X_1),\quad
 U_q(X_1),U_q(X_2),\ldots,U_q(X_m)
 \text{ are pairwise distinct}.}
 \tag{3.5}
\]

Thus the collar creates exactly one internal duplicate per row at every
depth. In particular it replaces the earlier \(q+1\)-fold entry-boundary
collision by the minimum pair forced by first-edge upper-flag preservation,
without adding a path, word position, or reset.

There is a useful two-sided column identity. For \(1\le t\le q\),

\[
 \boxed{Q\setminus U_q(X_t)=L_q(X_{m-q+t})
       =I_w(m+t,m-q).}
 \tag{3.6}
\]

Taking complements in (3.4) gives the remaining values. Therefore, as a
multiset of cyclic starts,

\[
 \boxed{
 \{Q\setminus U_q(X_t):0\le t\le m\}
 =\{I_w(s,m-q):s\in\mathcal C\},}
 \tag{3.7}
\]

where

\[
 \boxed{\mathcal C=(0,m+1,m+1,m+2,\ldots,2m-1)}
 \tag{3.8}
\]

is independent of \(q\). By (3.1), the lower starts are

\[
 \boxed{
 \{L_q(X_t):0\le t\le m\}
 =\{I_w(s,m-q):q\le s\le m+q\}.}
 \tag{3.9}
\]

This is the promised complete-column formulation: all depths use the same
physical row, not independently rounded residual vertices. The cyclic
indices in (3.1)--(3.9) define endpoint queues only; the emitted owner word
is the finite half-path \(X_0,\ldots,X_m\). No second half of the cyclic
row is emitted or counted.

## 4. What is balanced and what remains open

Put

\[
 N_q=\binom{2m}{m-q}=\binom{2m}{m+q}.
\]

Balanced signed depth-\(q\) loads mean that every target occurs
\(\lfloor W/N_q\rfloor\) or \(\lceil W/N_q\rceil\) times.

### Theorem 4.1 (unconditional upper depth-one balance)

For any independent orientations of the \(B\) special-coordinate paths,
the single-promotion collar is exactly balanced on the upper first band.

#### Proof

In one oriented row, (3.2)--(3.4) at \(q=1\) give

\[
 Y_0,Y_0,Y_1,\ldots,Y_{m-1}.
\]

The internal \(Y_t\)'s over all rows partition \(\binom Q{m+1}\). The
chosen first oriented edge union \(Y_0\) is therefore distinct from the
chosen first edge union of every other row. Hence exactly \(B\) targets
have load two and every other target has load one. Since

\[
 {W\over N_1}={m+1\over m},
\]

these are precisely the floor/ceiling loads. Reversing a row merely chooses
its other endpoint union as the duplicated target. \(\square\)

For the lower first band, write

\[
 d(S)=\#\{(P,t):0\le t<m,\ X_t\cap X_{t+1}=S\}.
\]

For one unoriented path let

\[
 E_0(P)=Q\setminus Y_0,\qquad E_1(P)=Q\setminus Y_{m-1}.
\]

The two orientations have the same internal meet multiset and choose,
respectively, \(E_0(P)\) or \(E_1(P)\) as the terminal lower flag.

### Theorem 4.2 (exact lower depth-one cap criterion)

The lower first band is exactly balanced if and only if one can choose one
of \(E_0(P),E_1(P)\) for every row so that target \(S\) receives selected
cap degree in

\[
 \boxed{\left[\max\{0,1-d(S)\},\ 2-d(S)\right].}
 \tag{4.1}
\]

Equivalently this is an integral left-perfect \(b\)-matching in the
two-choice row--cap graph. In particular \(d(S)>2\) is an immediate
obstruction. Mere coverage is equivalent to Hall's inequalities on the
targets with \(d(S)=0\).

#### Proof

Every row contributes its \(m\) internal meets and one terminal cap, so the
load of \(S\) is \(d(S)\) plus its selected cap degree. The balanced
depth-one loads are exactly one or two. Subtraction gives (4.1), and the
integral matching equivalence is immediate. \(\square\)

At depths \(q\ge2\), no exact-factor theorem presently proves balanced or
even covering loads for (3.7)--(3.9). The precise surviving statement is:

> **Half-necklace full-flag theorem \(\mathrm{HNF}_A\) (unproved).** For
> every fixed \(A\) and all sufficiently large \(m\), choose one exact odd
> wreath factor and orient each special-coordinate row so that, for every
> \(q\le H=\lceil A\sqrt m\rceil\), the two interval-column load tables
> (3.7) and (3.9) are simultaneously floor/ceiling balanced.

If only positive load is required, replace balance by coverage. Theorem
2.1 and Corollary 2.2 prove that \(\mathrm{HNF}_A\) implies the balanced
strengthening of \((\mathrm{CP}_A)\), with exact length (2.7). No QCF
appendage is needed for the selected flags themselves.

## 5. A genuine nonlocal positive braid

The special-coordinate construction solves chronology by changing the
factor representation. There is also an exact braid inside a prescribed
PBBS piece system.

Let \(F\) be an \((r-1)\)-set and let \(\mathcal A,\mathcal B\) be disjoint
coordinate alphabets, disjoint from \(F\). Suppose \(P_i\) is a directed
Johnson piece from

\[
 F+a_i\quad(a_i\in\mathcal A)
 \qquad\text{to}\qquad
 F+b_i\quad(b_i\in\mathcal B).
\]

Assume every internal positive residence exceeds \(H\), every insertion
label in the final \(H\)-edge collar of every piece lies in \(\mathcal A\),
and every removal label in the initial \(H\)-edge collar lies in
\(\mathcal B\).

### Theorem 5.1 (separated-star braid)

For every \(i,j\),

\[
 F+b_i\longrightarrow F+a_j
\]

is a Johnson edge satisfying the exact bridge-one residence condition.
Hence any ordering of pairwise owner-disjoint pieces concatenates into one
bridge-one path. If the pieces contain \(M\) owners in total, their exact
literal word length is

\[
 \boxed{M+2H.}
 \tag{5.1}
\]

#### Proof

The cross edge removes \(b_i\in\mathcal B\) and inserts
\(a_j\in\mathcal A\). Every insertion at or before the seam belongs to
\(\mathcal A\), while every removal at or after it belongs to
\(\mathcal B\). Since the alphabets are disjoint, no insertion can be
removed within \(H\) edges across the seam. The internal pieces already
have long positive residence. The exact FIFO queue theorem therefore lifts
the concatenation, and one initialization plus \(M-1\) updates costs
\(M+2H\). \(\square\)

Rainbow fixed-core PBBS parity pieces naturally provide the two disjoint
omitted-label alphabets. The additional common-facet/shadow-twin condition
is essential: without it the cross pair need not be a Johnson edge. What
is not proved is that all but \(o(W/H)\) canonical PBBS pieces can be
grouped into such compatible stars while retaining balanced full flags.

## 6. Exact obstruction to the canonical two-core circuit

Let

\[
 \Gamma=(\gamma_0,\ldots,\gamma_{2s})
\]

be a cyclic list of \(2s+1\) distinct labels, let \(V_i\) be its cyclic
\(s\)-window starting at \(i\), and let \(K,K'\) be disjoint
\((r-s)\)-sets, disjoint from \(\Gamma\). Define the two-core atlas

\[
 \mathcal T=
 \{K\cup V_i:i\in\mathbb Z_{2s+1}\}
 \cup
 \{K'\cup V_i:i\in\mathbb Z_{2s+1}\}.
 \tag{6.1}
\]

### Theorem 6.1 (induced atlas graph)

If \(s\le r-2\), the rank-\(r\) Johnson graph induced by \(\mathcal T\) is

\[
 \boxed{C_{2s+1}\ \dot\cup\ C_{2s+1}.}
 \tag{6.2}
\]

#### Proof

If the smaller circular distance between the starts of \(V_i,V_j\) is
\(d\le s\), then

\[
 |V_i\cap V_j|=s-d.
\]

Within one core class, rank-\(r\) Johnson adjacency requires overlap
\(r-1\), equivalently \(|V_i\cap V_j|=s-1\), so \(d=1\). Across the two
core classes the overlap is at most \(s<r-1\). Thus the only edges are
the two cyclic-neighbor families. \(\square\)

### Theorem 6.2 (atlas-confined bridge toll)

Assume \(s\le r-2\) and \(H\ge s\). Every bridge-one path confined to one
cycle in (6.2) has at most \(s\) edges and \(s+1\) owners. Hence the full
atlas needs at least four bridge paths. For \(g\) owner-disjoint atlases,

\[
 p\ge4g,\qquad M=2g(2s+1),\qquad
 L-M=2Hp\ge8Hg,
 \tag{6.3}
\]

and therefore

\[
 {L-M\over M}\ge {4H\over2s+1}\ge {4s\over2s+1}.
 \tag{6.4}
\]

#### Proof

Along the forward cycle, edge \(i\) inserts \(\gamma_{i+s}\), and edge
\(i+s\) removes it. Thus a subpath with \(s+1\) edges contains a positive
residence of length \(s\le H\), which the exact FIFO queue law forbids.
The reverse orientation is identical. Covering \(2s+1\) vertices by paths
of at most \(s+1\) vertices needs at least two paths per cycle.
Initialization contributes \(2H\) per path. \(\square\)

The actual zero-winding physical packet consists of one length-\(s\) arc
in each core cycle. The two arcs cannot be joined inside the atlas, so an
atlas-confined compiler needs two paths. For \(g\) owner-disjoint packets,

\[
 M=2g(s+1),\qquad p\ge2g,\qquad
 {L-M\over M}\ge {2H\over s+1}.
 \tag{6.5}
\]

This is nonvanishing when \(s\le H\). Therefore the circular two-core
chart is not itself a coefficient-one crossing braid. A successful braid
must use owners outside the atlas, or cross-atlas shadow twins of the kind
in Theorem 5.1.

## 7. PBBS-wide conservation laws for any future braid

Two independently audited identities constrain a global repair.

First, in the odd projected PBBS factor, every natural edge has a distinct
lower depth-one colour. If \(D\) is the set of deleted natural edges,
\(C\) the inserted non-PBBS chords, and the final forest has \(p\) paths,
then

\[
 \boxed{|D|=|C|+p.}
 \tag{7.1}
\]

If a chord joins the tail indexed by \(A\) to the natural head indexed by
\(B\), its lower colour is

\[
 S(A,B)=(A\cup f^2B)^c.
\]

Exact lower depth-one coverage forces the unique natural edge with this
colour also to be deleted:

\[
 \boxed{f^{-1}(S(A,B))\in D.}
 \tag{7.2}
\]

The edge in (7.2) may coincide with one of the two named cuts; it is not
asserted to be a third distinct edge.

Second, let \(\nu_H\) be the maximum number of pairwise edge-disjoint PBBS
positive-residence intervals of residence at most \(H\), where an interval
of residence \(j-i\) is the closed edge set

\[
 \{e_i,e_{i+1},\ldots,e_j\}.
\]

Every bridge forest satisfies

\[
 \boxed{|C|\ge\nu_H-p.}
 \tag{7.3}
\]

At upper depth \(q\), a covering full-state forest has at most \(W-N_q\)
flag-preserving arcs. Therefore at least

\[
 \boxed{\bigl(\nu_H-p-(W-N_q)\bigr)_+}
 \tag{7.4}
\]

non-PBBS chords must genuinely recode that upper flag. At the top depth,
at least \(N_H-p=\Theta_A(W)\) arcs are rotors. Thus a critical return
family cannot be repaired only by entry-neutral promotions. The
single-promotion collar in Section 2 is consistent with this law: after
its one promotion, every remaining edge is a rotor.

These are architectural restrictions, not a no-go for \((\mathrm{CP}_A)\).
The separated-star family proves that genuine rotor chords can exist in
large complete compatibility blocks.

## 8. Corrected sandwich/QCF ledger

For an actual bridge-one path containing \(s\) owners, the exact useful
prefix length is \(s+2H\). Consequently a bridge class of
\(M_{\rm br}\) owners in \(p\) paths costs

\[
 M_{\rm br}+2Hp.
\]

Suppose the other owners are partitioned into owner-disjoint sandwich
atoms of total baseline \(M_{\rm sand}\), with substituted chart excess
\(E_{\rm sand}\), and

\[
 M_{\rm br}+M_{\rm sand}=W.
\]

If the remaining hard crossing borders are grouped into clusters of spans
\(S_j\), the audited multi-cut QCF chart gives

\[
 \boxed{
 L\le W+2Hp+E_{\rm sand}
       +\sum_j(7H+3S_j-3).}
 \tag{8.1}
\]

For the fixed-fibre normalized-port atoms, the exact substituted excess is

\[
 \boxed{
 E_{\rm sand}=\sum_q
   \bigl(N\bar R_q+(q-1)c_q\bigr),}
 \tag{8.2}
\]

provided the charged owner segments are globally disjoint. A one-border
QCF chart has exact length \(4H-1\).

The word **substituted** is essential. The atom chart replaces its owner
baseline; it is not appended to a separate \(W\)-owner word. Likewise an
internal bridge-one join already costs the next baseline owner and receives
no QCF charge. Under the special-coordinate construction,

\[
 M_{\rm br}=W,\qquad p=B,\qquad E_{\rm sand}=0,
\]

and there are no hard internal borders. Equation (8.1) reduces exactly to
(2.7).

If \(J\) seams are instead repaired independently, their \((4H-1)J\) cost
is \(o(W)\) only when \(J=o(W/H)\). Thus a critical
\(\Theta(W/H)\) family cannot be hidden in separately paid QCF charts.

## 9. Exact proved/conditional boundary

### Proved

1. Exact special-coordinate path count \(B=W/(m+1)\).
2. The single-promotion/otherwise-rotor full-state lift for every \(H<m\).
3. Exact literal length \(W+2HB\).
4. The complete lower and upper interval-column formulas
   (3.1)--(3.9), including exactly one upper duplicate per row at every
   depth.
5. Unconditional exact upper depth-one balance.
6. The exact lower depth-one two-cap matching criterion.
7. The separated-star nonlocal braid.
8. The induced two-cycle theorem and quantitative no-go for every
   atlas-confined two-core braid.
9. The conservation and corrected literal ledgers (7.1)--(8.2).

### Unproved

The half-necklace theorem \(\mathrm{HNF}_A\) is not proved. In particular,
exact odd middle ownership does not imply that the lower interval loads in
(3.9) cover every target, and the one-duplicate upper interpolation does
not imply global balance at \(q\ge2\). No claim of \((\mathrm{CP}_A)\) or
coefficient one is made.

The exact remaining PBBS-specific route is now one of the following.

* Prove \(\mathrm{HNF}_A\) for a rebundled exact wreath factor. Chronology
  and literal length would then be finished by Sections 2--3.
* Build enough cross-atlas separated-star groups to alter the deficient
  interval columns while obeying the colour closure (7.2) and the upper
  recoding budget (7.4).
* Exhibit a family of targets violating the two-cap or higher-depth
  interval Hall inequalities for every exact wreath factor; that would be
  a genuine obstruction to this special-coordinate architecture.

The normalized-port obstruction is therefore not the endpoint. A concrete
nonlocal bridge family exists, a stronger special-coordinate full-state
collar removes the path-count loss, and the canonical two-core circuit is
closed by an exact induced-graph theorem. What remains is precisely the
global balanced interval-column supply.
