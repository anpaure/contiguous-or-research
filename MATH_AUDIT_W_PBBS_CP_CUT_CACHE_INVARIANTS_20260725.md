# PBBS nonlocal chords for covering-prefix flags: cache cuts, colour closure, and special-coordinate descent

Date: 2026-07-25

Pure mathematics only.  No computation, search, or generic rounding theorem
is used.

## 0. Exact verdict

There are two independent conservation laws for a PBBS-based attack on the
covering-prefix gate.

1.  For an arbitrary covering full-flag transversal, cache promotions which
    preserve a shallow upper flag have only the corresponding duplicate
    budget.  If (e_s) is the number of promotions from cache position (s),
    then
    
    \[
       \sum_{s=1}^q e_s\le W-\binom n{k+q}.
       \tag{0.1}
    \]
    
    At the full top this gives the exact rotor identity
    
    \[
       e_{\rm rot}=\binom n{k+H}+D_H-p,
       \qquad D_H\ge0,
       \tag{0.2}
    \]
    
    for a (p)-path forest.  In particular
    (e_{\rm rot}\ge\binom n{k+H}-p).

2.  In the odd projected PBBS model, every natural edge has a distinct lower
    depth-one colour.  If (D) is the set of deleted natural edges, (C) the
    inserted non-PBBS chords, and the final forest has (p) paths, then
    
    \[
       |D|=|C|+p,
       \tag{0.3}
    \]
    
    and the chord lower colours, together with the (p) terminal lower
    flags, are exactly the colours of (D).  A chord joining the tail of the
    cut at (A) to the head of the cut at (B) forces the colour-indexed cut
    below (which may coincide with one of the two endpoint cuts):
    
    \[
       \chi(A,B)
       =f^{-1}\!\left((A\cup f^2B)^c\right)\in D.
       \tag{0.4}
    \]

Moreover the deleted natural edges must hit every short positive-residence
interval.  Hence, if \(\nu_H(P)\) is the maximum number of pairwise
edge-disjoint such intervals,

\[
   |C|\ge \nu_H(P)-p.
   \tag{0.5}
\]

Combining (0.1) and (0.5), a critical return family cannot be repaired only
by first-upper-neutral normalized ports.  It requires genuinely
upper-recoding chords.  This is an obstruction to that architecture, not to
\(\mathrm{CP}_A\): every self-paying star chord has abundant local rotor
lifts, so a global correlated chord matching can evade it.

Finally, deleting a fixed special coordinate from the odd projected PBBS
gives an exact even middle-layer radius-one path cover whose internal lower
flags cover every depth-one target once.  It does **not** automatically give
a balanced full depth-one transversal.  Lower completion has a
one-forbidden-facet list-matching constraint forced by the incoming bridge,
and upper completion is a separate capacitated inclusion-flow condition.

## 1. The upper-cache cut hierarchy

Let

\[
   \mathcal X=\binom{[n]}k,
   \qquad W=|\mathcal X|,
   \qquad 1\le H\le\min(k,n-k).
   \tag{1.1}
\]

A full useful state over (X\in\mathcal X) is represented by an ordered
deletion queue and an ordered cache

\[
   \alpha(X)=(a_1,\ldots,a_H)\subset X,
   \qquad
   \beta(X)=(b_1,\ldots,b_H)\subset[n]\setminus X.
   \tag{1.2}
\]

Its signed depth-(q) flags are

\[
   L_q(X)=X\setminus\{a_1,\ldots,a_q\},
   \qquad
   U_q(X)=X\cup\{b_1,\ldots,b_q\}.
   \tag{1.3}
\]

For an owner-changing bridge-one arc

\[
   X\longrightarrow Y=X-a_1+b,
   \tag{1.4}
\]

the exact queue--cache rule is as follows.  The target deletion queue is

\[
   \alpha(Y)=(a_2,\ldots,a_H,x)
   \tag{1.5}
\]

for some unused (x\in X\setminus\{a_1,\ldots,a_H\}).  If
(b=b_s\) belongs to the source cache, the arc is a promotion from cache
position (s), and

\[
   \beta(Y)=(a_1,b_1,\ldots,\widehat{b_s},\ldots,b_H).
   \tag{1.6}
\]

If (b\notin\{b_1,\ldots,b_H\}), the arc is a rotor shift, and

\[
   \beta(Y)=(a_1,b_1,\ldots,b_{H-1}).
   \tag{1.7}
\]

### Theorem 1.1 (upper-flag preservation is exactly shallow promotion)

For every owner-changing bridge-one arc and every (1\le q\le H),

\[
   U_q(X)=U_q(Y)
   \quad\Longleftrightarrow\quad
   \text{the arc is a promotion from a cache position }s\le q.
   \tag{1.8}
\]

#### Proof

Suppose first that (b=b_s).  If (s\le q), the first (q) entries of
the target cache are (a_1) together with
(b_1,\ldots,b_q\) after deleting (b_s).  Therefore

\[
\begin{aligned}
 U_q(Y)
 &=X-a_1+b_s+\{a_1,b_1,\ldots,\widehat{b_s},\ldots,b_q\}\\
 &=X+\{b_1,\ldots,b_q\}=U_q(X).
\end{aligned}
\]

If (s>q), then

\[
   U_q(Y)=X+\{b_s,b_1,\ldots,b_{q-1}\},
\]

which differs from (U_q(X)) because the cache entries are distinct.
For a rotor shift, (b\) lies outside the entire source cache and

\[
   U_q(Y)=X+\{b,b_1,\ldots,b_{q-1}\}\ne U_q(X).
\]

These are all owner-changing bridge-one cases.  \(\square\)

### Theorem 1.2 (exact fibre-component identity)

Choose one full useful state over every owner, and let (F) be a spanning
directed bridge-one path forest with (p) paths.  Fix (q\le H).  For a
rank-((k+q)) target (U), let (t_U) be its selected load and let (c_U)
be the number of components, isolated vertices included, in the subforest
on the (t_U) states whose arcs preserve (U_q=U).  Put

\[
   C_q=\sum_{U:t_U>0}c_U.
   \tag{1.9}
\]

Then

\[
   \sum_{s=1}^q e_s=W-C_q,
   \tag{1.10}
\]

and the number of path arcs changing (U_q) is exactly

\[
   C_q-p.
   \tag{1.11}
\]

If the selected flags cover every rank-((k+q)) target, then

\[
   C_q\ge N_q^+:=\binom n{k+q},
   \tag{1.12}
\]

and consequently

\[
   \boxed{\sum_{s=1}^qe_s\le W-N_q^+,}
   \qquad
   \boxed{e_{\rm change}(q)\ge N_q^+-p.}
   \tag{1.13}
\]

At (q=H), every promotion preserves the full top and every rotor changes
it.  Hence, with

\[
   D_H=C_H-N_H^+\ge0,
\]

one has the exact identity

\[
   \boxed{e_{\rm rot}=N_H^++D_H-p.}
   \tag{1.14}
\]

#### Proof

By Theorem 1.1 the (U_q)-preserving arcs are exactly the promotions counted
by (e_1+\cdots+e_q).  Inside one nonempty (U)-fibre they form a linear
forest on (t_U) vertices with (c_U) components, hence have
(t_U-c_U) edges.  Summing and using \(\sum_Ut_U=W\) proves (1.10).
The whole forest has (W-p) edges, so subtraction gives (1.11).  Coverage
gives at least one nonempty fibre for each of the (N_q^+) targets, proving
(1.12)--(1.13).  The specialization (q=H) is (1.14). \(\square\)

For the even central layer (n=2m,k=m),

\[
   W-N_1^+=\binom{2m}m-\binom{2m}{m+1}
   ={W\over m+1}.
   \tag{1.15}
\]

For the odd projected PBBS owner layer (n=2m+1,k=m+1),

\[
   W-N_1^+
   =\binom{2m+1}{m+1}-\binom{2m+1}{m+2}
   ={2W\over m+2}.
   \tag{1.16}
\]

Thus first-upper-neutral seams have only Catalan-order capacity in either
model.  Balance is not needed for (1.13); support is enough.  Under exact
floor/ceiling balance, (1.15)--(1.16) are literally the complete duplicate
budgets.

## 2. The canonical PBBS lower-colour bijection

Now let (N=2m+1), and let

\[
   f:\binom{[N]}m\longrightarrow\binom{[N]}m
   \tag{2.1}
\]

be the canonical parenthesis/PBBS permutation.  Consecutive states (A)
and (fA) are disjoint.  Put (g=f^2), and associate to (A) the projected
owner

\[
   X_A=[N]\setminus A\in\binom{[N]}{m+1}.
   \tag{2.2}
\]

The directed projected PBBS factor (P) has natural edge

\[
   e_A:X_A\longrightarrow X_{gA}.
   \tag{2.3}
\]

### Lemma 2.1 (natural edge colours are a bijection)

For every (A),

\[
   X_A\cap X_{gA}=fA.
   \tag{2.4}
\]

Consequently (e_A\mapsto fA) is a bijection from the (W) natural
edges onto all rank-(m) lower depth-one targets.

#### Proof

Both (A) and (gA=f^2A) are disjoint from (fA).  They are distinct:
the audited PBBS period divisibility makes every (f)-orbit length a
multiple of (N=2m+1), so no (f^2)-fixed state exists.  Thus they are
distinct (m)-subsets of the ((m+1))-set ([N]\setminus fA), so their union is
that ((m+1))-set.  Taking complements gives (2.4).  The map (A\mapsto fA)
is a permutation. \(\square\)

### Theorem 2.2 (exact PBBS cut--chord colour closure)

Select one full useful state over every projected owner, covering every
rank-(m) lower depth-one target.  Let (F) be a spanning directed
bridge-one path forest with (p) paths.  Write

\[
   C=E(F)\setminus E(P),
   \qquad
   D=E(P)\setminus E(F),
   \qquad c=|C|.
   \tag{2.5}
\]

Then

\[
   \boxed{|D|=c+p.}
   \tag{2.6}
\]

The lower colours of the chords in (C) are pairwise distinct, avoid the
colours of every retained PBBS edge, and, together with the (p) lower
flags at the terminal owners of (F), are exactly

\[
   \{fA:e_A\in D\}.
   \tag{2.7}
\]

In particular, suppose (e_A,e_B\in D) and a chord joins the tail of the
first cut to the head of the second:

\[
   X_A\longrightarrow X_{gB}.
   \tag{2.8}
\]

Then (A\triangle gB) has size two, its chord colour is

\[
   S(A,B)=X_A\cap X_{gB}=(A\cup gB)^c,
   \tag{2.9}
\]

and the unique natural edge with that colour must also be cut:

\[
   \boxed{
   e_{\chi(A,B)}\in D,
   \qquad
   \chi(A,B)=f^{-1}\!\left((A\cup f^2B)^c\right).}
   \tag{2.10}
\]

#### Proof

The natural factor has (W) edges, while the path forest has (W-p).
It retains (W-p-c) natural edges, proving (2.6).

There are (W) selected lower depth-one flags and exactly (W) rank-(m)
targets.  Coverage therefore means that every target has load exactly one.
For every nonterminal path vertex its lower flag is the intersection colour
of its outgoing path arc.  Lemma 2.1 says that the retained natural arcs
already have distinct colours.  The remaining (c+p=|D|) flags are the
chord colours and the terminal flags, and they must be precisely the missing
natural colours.  This proves (2.7).

For (2.8), Johnson adjacency gives (2.9).  Lemma 2.1 says that the unique
natural edge with colour (S(A,B)) is indexed by (f^{-1}S(A,B)).
Equation (2.7) forces that edge into (D), proving (2.10). \(\square\)

This is a genuine PBBS conservation law.  It is stronger than matching
normalized port types: the selected cut set must also be closed under the
owner-labelled map \(\chi\).

## 3. Residence hitting and the forced shallow recoding

Write a natural projected PBBS cycle as

\[
   X_{i+1}=X_i-a_i+b_i.
   \tag{3.1}
\]

A positive residence of length (q\) is an identity

\[
   b_i=a_{i+q},
   \qquad 1\le q\le H.
   \tag{3.2}
\]

Its closed transition interval is

\[
   I(i,q)=\{e_i,e_{i+1},\ldots,e_{i+q}\}.
   \tag{3.3}
\]

In the PBBS omitted-label notation, (3.2) is exactly

\[
   \lambda_{r+2i+1}=\lambda_{r+2i+2q},
   \tag{3.4}
\]

the odd omitted-label gap (2q-1), with the conventional one-edge endpoint
shift included in (3.3).

Let \(\nu_H(P)\) be the maximum size of a pairwise edge-disjoint family of
intervals (3.3).

### Theorem 3.1 (every low-path braid pays a non-PBBS chord transversal)

Under the hypotheses of Theorem 2.2,

\[
   \boxed{p+|C|=|D|\ge\nu_H(P),}
   \qquad
   \boxed{|C|\ge\nu_H(P)-p.}
   \tag{3.5}
\]

#### Proof

Along any bridge-one owner path, the new coordinate inserted at one edge
enters the target lower base.  The deletion queue can move it toward its
head by at most one place per later edge.  Equivalently, the exact FIFO law
gives

\[
   b_i\notin\{a_{i+1},\ldots,a_{i+H}\}.
   \tag{3.6}
\]

Thus no interval (3.3) can be wholly retained as consecutive natural PBBS
edges of (F).  The omitted-edge set (D) meets every short-residence
interval.  Every edge of (D) meets at most one member of a pairwise
edge-disjoint family, so \(|D|\ge\nu_H(P)\).  Use (2.6). \(\square\)

### Corollary 3.2 (entry-neutral normalized ports are Catalan-limited)

For (1\le q\le H), let (C_{\rm change}(q)\) be the set of non-PBBS
chords which change the selected upper depth-(q) flag.  Then

\[
   \boxed{
   |C_{\rm change}(q)|
   \ge
   \nu_H(P)-p-(W-N_q^+).}
   \tag{3.7}
\]

In particular, in the odd PBBS model,

\[
   |C_{\rm change}(1)|
   \ge \nu_H(P)-p-{2W\over m+2}.
   \tag{3.8}
\]

#### Proof

At most (W-N_q^+) arcs of the entire path forest preserve (U_q), by
Theorem 1.2.  Hence at most that many of the chords in (C) preserve
(U_q).  Combine this with \(|C|\ge\nu_H(P)-p\). \(\square\)

If \(\nu_H(P)\) has critical order (W/H), while (H\asymp\sqrt m),
(3.8) forces critical order (W/H) genuinely first-upper-recoding chords.
Appending the audited (4H-1) QCF chart separately at every such cut then
has linear total charge.  This is a no-go for the **separately paid** QCF
architecture.  It is not a word-length lower bound: a direct bridge-one
chord uses one baseline transition and may replace the destroyed flags by
new balanced flags.

### Local escape: self-paying rotor stars

The preceding obstruction is not local.  Let (S=fA) be the natural lower
colour of (X_A), and write (X_A=S+a).  For every
(b\notin S+a), the chord

\[
   S+a\longrightarrow S+b
   \tag{3.9}
\]

has the same lower colour (S), so it pays for cutting (e_A) without
creating a new lower defect.  Choose a source deletion queue with head
(a), choose its cache to avoid (b), and choose any legal new queue tail.
The queue--cache theorem makes (3.9) a genuine rotor chord.  In the even
model the exact number of compatible ordered source/target state pairs is

\[
   ((m-1)_H)^2>0
   \tag{3.10}
\]

for (H<m).  Thus no degree, top-change, or local-state obstruction rules
out a globally correlated star-chord braid.

## 4. Special-coordinate descent to the even middle layer

Fix a coordinate \(\infty\in[N]\).  Restrict to those (A\in\binom{[N]}m)
with \(\infty\notin A\), equivalently to projected owners (X_A\) which
contain \(\infty\).  Delete \(\infty\) from the owner:

\[
   \overline X_A=X_A\setminus\{\infty\}
   \in\binom{[N]\setminus\{\infty\}}m.
   \tag{4.1}
\]

This is a bijection onto the even middle layer.  Retain a natural projected
PBBS edge exactly when both endpoint owners contain \(\infty\).

Put

\[
   \widehat W=\binom{2m}m,
   \qquad
   \widehat N_1=\binom{2m}{m-1}
   ={m\over m+1}\widehat W,
   \qquad
   p_0={\widehat W\over m+1}.
   \tag{4.2}
\]

### Theorem 4.1 (exact even path cover and complete internal lower row)

The retained graph in (4.1) is a disjoint union of directed paths, with
exactly \(\widehat N_1\) edges and (p_0\) paths.  Its internal lower
depth-one flags, after deleting \(\infty\), cover every rank-((m-1))
target exactly once.  Moreover these owner paths lift to radius-one
bridge-one paths.

#### Proof

By Lemma 2.1, a natural edge is retained exactly when its colour (fA)
contains \(\infty\).  Since (f) is a permutation, the retained edge count
is the number of rank-(m) sets containing \(\infty\), namely
(\widehat N_1\).  Their colours after deleting \(\infty\) run bijectively
through all rank-((m-1)) subsets of the remaining (2m) coordinates.

There is no directed retained cycle.  Indeed, let \(\mathcal O\) be such
an (f^2)-orbit.  Every (A\in\mathcal O) avoids \(\infty\), while every
(fA\in f\mathcal O) contains \(\infty\).  If (f\mathcal O=\mathcal O)
this is an immediate contradiction.  Otherwise the corresponding full
(f)-orbit is \(\mathcal O\sqcup f\mathcal O\), and \(\infty\) belongs to
exactly half its states.  The audited PBBS coordinate-homomesy theorem says
that a coordinate belongs to the fraction (m/(2m+1)\), not (1/2), of
every (f)-orbit.  This is again impossible.

Therefore the retained graph is a path forest.  Its path count is

\[
   \widehat W-\widehat N_1=p_0.
\]

The projected PBBS has no positive residence of length one.  Deleting
\(\infty\), which is fixed throughout every retained edge, does not alter
the entry or exit times of any other coordinate.  The exact radius-one
queue criterion therefore lifts every retained owner path to a bridge-one
path.

This proves the theorem. \(\square\)

The last statement does not make the terminal lower flag arbitrary.  If
the last edge of a nontrivial path is

\[
 Z^-\longrightarrow Z=Z^- -d+c,
 \tag{4.3}
\]

then the radius-one queue recurrence forces

\[
 \alpha_1(Z)=x\in Z^-\cap Z.
 \tag{4.4}
\]

Thus the legal terminal lower targets are

\[
 \mathcal L(Z)=\{Z-x:x\in Z^-\cap Z\};
 \tag{4.5}
\]

the facet (Z-c=Z^-\cap Z), obtained by deleting the newly entered
coordinate, is forbidden.  A singleton path has the full facet list.

### Proposition 4.2 (exact lower terminal list gate)

The preloaded internal lower flags of Theorem 4.1 extend to an exactly
balanced even lower depth-one family if and only if the bipartite graph
from path terminals to rank-((m-1)) targets, with lists (4.5), has a
matching saturating every terminal.

#### Proof

Every target already has internal load one.  Since

\[
 \widehat W-\widehat N_1=p_0,
\]

balance requires the (p_0) terminal flags to be pairwise distinct,
raising exactly (p_0) target loads from one to two.  Formula (4.5) is
the exact bridge-compatible list at each terminal.  This is precisely the
stated matching problem. \(\square\)

### Proposition 4.3 (upper first balance is a separate flow gate)

Let \(\mu_\infty(U)\) be the load of an even rank-((m+1)) target (U)
among the forced upper depth-one flags of the internal retained edges.
Let \(\mathcal I_\infty\) be the (p_0) initial owners of the paths.
The upper depth-one flags can be completed to exact floor/ceiling balance
if and only if the bipartite inclusion network from
\(\mathcal I_\infty\) to rank-((m+1)) supersets has an integral flow with
one unit from every initial owner and target capacity interval

\[
   \left[(1-\mu_\infty(U))_+,\;2-\mu_\infty(U)\right].
   \tag{4.6}
\]

In particular it is necessary that

\[
   \mu_\infty(U)\le2\quad\text{for every }U.
   \tag{4.7}
\]

#### Proof

Every internal bridge arc forces the target's upper first flag to be the
union of its two endpoint owners.  Only the initial owner of each path has
a free upper first flag.  In the even middle layer the balanced loads are
one or two, and there are (p_0=\widehat W-\widehat N_1) duplicate units.
Thus a target of present load zero must receive at least one initial unit,
and a target of present load \(\mu\) can receive at most (2-\mu) units.
The flag chosen at an initial owner must contain it.  These are exactly the
lower and upper capacities in (4.6).  Integral flow decomposition is
equivalent to the desired flag assignment. \(\square\)

If (K=([N]\setminus\{\infty\})\setminus U), then

\[
 \mu_\infty(U)
 =\#\{A:A\cap f^2A=K,\ \infty\in fA\}
 \le \mu_P(K)\le3.
 \tag{4.8}
\]

The last inequality is the canonical PBBS first-upper theorem.  It gives
only the pointwise cap three.  No theorem currently forces every restricted
load \(\mu_\infty(U)\) to be at most two or proves the flow (4.6).  Hence
special-coordinate deletion proves the complete **internal** lower
depth-one row, but both terminal lower list-Hall and upper capacity flow
remain before one obtains two-sided balanced even depth-one flags, let
alone the full Gaussian flag tower.

## 5. Implication scope

Theorems 1.1--1.2 are universal for the covering-prefix bridge architecture.
They do not use PBBS, an SCD, or balance beyond support.  Theorems 2.1--3.1
are PBBS-specific and use the exact odd projected factor and its natural
lower-colour bijection.  The special-coordinate result is an odd-to-even
depth-one statement only.

The exact obstruction is therefore architectural:

* unchanged PBBS chronology must be cut at every short positive residence;
* all replacement chords must obey the owner-labelled \(\chi\)-closure;
* first-upper-neutral promotions have only (O(W/m)) capacity; and
* separately appending a QCF chart at a critical (W/H) family of seams
  returns to linear excess.

It is not a counterexample to \(\mathrm{CP}_A\).  Self-paying rotor chords
evade the shallow-promotion capacity, and the symmetric full bridge graph
has an exact uniform fractional circulation.  The unresolved theorem is a
single integral choice of \(\chi\)-closed chords, deletion queues, and
upper caches which simultaneously covers all flag targets and has
(o(W/H)) path components.
