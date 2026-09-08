# Saturating-core flags: exact literal rotor chronology

Date: 2026-07-25

Method: pure mathematics only.  No web search, computation, finite search,
solver, or long-running job is used.

## 0. Verdict

Put

\[
 n=2m+1,\qquad
 N_q=\binom{n}{m-q},\qquad
 W=N_0,\qquad M=N_1,\qquad
 d=W-M=\frac{2W}{m+2}.
\tag{0.1}
\]

Theorem 3.2 and Corollary 1.2 of
`MATH_ATTACK_AH_SATURATING_CYCLE_EXTENSION_20260725.md` are correct in
their stated scope.  They close the one-sided common-owner marginal
problem: for every fixed \(A\), one obtains nested owner-labelled flags
through \(H\le A\sqrt m\) whose total weighted overload is at most

\[
 dH=O_A(W/\sqrt m)=o(W).
\tag{0.2}
\]

They do not order those flags.  The balanced comparison vectors used to
prove (0.2) may be chosen independently at different depths, and the
abstract flow supplies no literal last-occurrence chronology.

This report proves the exact chronology theorem that can be fused with
that bridge.  If \(L_q(X)\) denotes the prescribed nested core flags and
\(Q(X)\) their deletion queues, form the weighted directed transition
graph of Section 2.  A path cover with \(C\) paths and portal weight \(J\)
has a literal one-sided realization of exact length

\[
 \boxed{W+H(C+d)+J.}
\tag{0.3}
\]

Hence a sufficient one-sided Gaussian-window lemma within this
priority-cylinder architecture is

\[
 \boxed{HC+J=o(W).}
\tag{0.4}
\]

No marginal or Hall term remains in (0.4).  This report does not prove
(0.4), and therefore does not prove the constant-one conjecture.

Three further unconditional chronology conclusions are obtained.

1.  The saturating core has a one-component, zero-portal literal lift at
    radius one.
2.  At radius two, put
    \(T_i=S_{i+1}\cap S_{i+2}\).  The exact portal cost is the number of
    adjacent equal \(T_i\)'s.  If only \(M_2\) rank-\((m-2)\) targets are
    missing from the \(T_i\)'s, then

    \[
      J\le N_1-N_2+M_2=O(W/m)+M_2.
      \tag{0.5}
    \]

3.  For the natural saturating-cycle order, a collision-distance statistic
    \(\delta_q\) gives the rigorous architecture-specific lower bound

    \[
      \boxed{
      L\ge W+
      \left(\left\lceil\frac{\delta_q}{q}\right\rceil-d-1\right)_+.}
      \tag{0.6}
    \]

    Thus \(\delta_q/q=\Omega(W)\) rules out width plus \(o(W)\) while
    preserving that owner order and those rotor prefixes.  In particular,
    positive-density \(\delta_q\) suffices at any fixed depth, but not when
    \(q\to\infty\).  The saturating-cycle theorem gives no lower bound on
    \(\delta_q\), so (0.6) is not asserted to obstruct the published
    cycle.

The bridge has therefore moved the exact frontier from vertical
factorability to horizontal flagged chronology, but it has not solved the
latter.

## 1. Audit of the AH bridge

Let

\[
 S_0,X_0,S_1,X_1,\ldots,S_{M-1},X_{M-1},S_0
\tag{1.1}
\]

be the saturating alternating cycle.  Thus the \(S_i\)'s are all members
of \(V_1=\binom{[n]}{m-1}\), the \(X_i\)'s are distinct middle sets, and

\[
 X_i=S_i\cup S_{i+1}.
\tag{1.2}
\]

Write \(U=\{X_i\}\) and \(E=V_0\setminus U\), so \(|E|=d\).

### Proposition 1.1 -- the omitted facet SDR is exact

For \(m\ge6\), every \(\mathcal A\subseteq E\) satisfies

\[
 |\partial\mathcal A|\ge|\mathcal A|.
\tag{1.3}
\]

Consequently \(E\) has a system of distinct rank-\((m-1)\) facet
representatives.

#### Proof

Put \(a=|\mathcal A|\), and for \(a>0\) write

\[
 a=\binom{x}{m},\qquad x\ge m,
\]

in generalized-binomial notation.  Since

\[
 \frac{|E|}{\binom{2m-1}{m}}
 =\frac{4(2m+1)}{(m+1)(m+2)}\le1
 \qquad(m\ge6),
\]

one has \(x\le2m-1\).  The Lovasz--Kruskal--Katona inequality gives

\[
 |\partial\mathcal A|
 \ge\binom{x}{m-1}
 =\binom{x}{m}\frac{m}{x-m+1}
 \ge a.
\]

Hall's theorem proves the last assertion.  \(\square\)

There is also a cycle-specific proof.  Every \(S_i\) has the two distinct
core supersets \(X_{i-1},X_i\), and hence at most \(m\) omitted middle
supersets.  Counting facet incidences gives

\[
 m|\mathcal A|
 \le m|\partial\mathcal A|.
\]

### Proposition 1.2 -- exact scope of the weighted flag corollary

Fix \(A>0\) and \(H\le A\sqrt m\).  The common core flow and arbitrary
nested flags on \(E\) give one owner-labelled nested flag family
\(\widetilde L\) with

\[
 \sum_{q=1}^H\frac{O_q(\widetilde L)}{c_q}
 \le dH=o(W).
\tag{1.4}
\]

#### Proof audit

At depth \(q\), let \(a_q\) be the balanced core load of total mass
\(M=W-d\).  Uniformly for \(q\le A\sqrt m\),

\[
 \lambda_q=\frac{W}{N_q}=O_A(1),
 \qquad
 \frac d{N_q}=\frac{2\lambda_q}{m+2}<1
\tag{1.5}
\]

for sufficiently large \(m\).  Put

\[
 p=\left\lfloor\frac{M}{N_q}\right\rfloor,
 \qquad
 c=\left\lfloor\frac W{N_q}\right\rfloor.
\]

Then \(c\in\{p,p+1\}\).  If \(c=p+1\), every full balanced quota entry is
at least \(p+1\), while every core load is at most \(p+1\).  If \(c=p\),
the full high set has exactly \(d\) more entries than the core high set;
enlarge the latter by any \(d\) core-low positions.  In either case there
is a balanced full-mass vector \(b_q\ge a_q\).

The arbitrary omitted flags contribute a nonnegative load \(e_q\) of
total mass \(d\).  Therefore

\[
 \sum_S(a_q(S)+e_q(S)-b_q(S))_+
 \le\sum_S e_q(S)=d.
\]

Minimizing over balanced vectors gives \(O_q\le d\), and summing with
\(c_q\ge1\) proves (1.4).  \(\square\)

The owner labels and the vertical nesting are common at all depths.  The
vectors \(b_q\), however, were selected separately.  Proposition 1.2 is
therefore a weighted-marginal theorem, not a zero-overload common balanced
flow theorem.  Nothing below uses the stronger false interpretation.

The SDR-inserted Hamilton Johnson cycle also must not be confused with a
literal two-window braid.  If an omitted owner \(Z\) is inserted in the
edge of colour \(S\subset Z\), both incident edge colours are \(S\), whose
union is \(S\), not \(Z\).  The valid coefficient-one first-band word is
the colour word \(S_0,S_1,\ldots,S_{M-1},S_0\), followed by the omitted
middle masks.

## 2. The exact flagged priority-transition graph

Give every core owner \(X\in U\) a nested lower flag

\[
 X=L_0(X)\supset L_1(X)\supset\cdots\supset L_H(X),
 \qquad |L_q(X)|=m-q.
\tag{2.1}
\]

Write its deletion queue and base as

\[
 Q(X)=(x_0,\ldots,x_{H-1}),
 \qquad
 L_q(X)=X\setminus\{x_0,\ldots,x_{q-1}\},
 \qquad B(X)=L_H(X).
\tag{2.2}
\]

Define a weighted directed graph \(\mathcal R_H\) on these flagged owners.
For

\[
 Y=X-\{x_0\}+\{a\},\qquad a\notin X,
\tag{2.3}
\]

put an arc \(X\to Y\) in either of the following cases.

* **Nonqueued arc:** for some \(b\in B(X)\),

  \[
   Q(Y)=(x_1,\ldots,x_{H-1},b),
   \qquad \delta(X,Y)=0.
   \tag{2.4}
  \]

* **Priority-\(j\) arc:** for some \(0\le j\le H-1\),

  \[
   Q(Y)=(x_1,\ldots,x_j,a,x_{j+1},\ldots,x_{H-1}),
   \qquad \delta(X,Y)=H-j.
   \tag{2.5}
  \]

Empty displayed ranges are omitted.

### Theorem 2.1 -- literal priority-cover theorem

If \(\mathcal R_H\) has a vertex-disjoint directed path cover with \(C\)
paths and total arc weight

\[
 J=\sum_{XY}\delta(X,Y),
\tag{2.6}
\]

then all prescribed core flags have a literal contiguous-OR realization
of exact length

\[
 \boxed{M+HC+J.}
\tag{2.7}
\]

Initializing one arbitrary nested flag for each omitted owner separately
gives a one-sided literal realization of all \(W\) owner flags of length

\[
 \boxed{W+H(C+d)+J.}
\tag{2.8}
\]

Every prescribed flag set in (2.1) is witnessed by a contiguous interval
ending at its owner's marked endpoint.

#### Proof

Initialize a path whose first owner has queue (2.2) by writing

\[
 \{x_0\},\{x_1\},\ldots,\{x_{H-1}\},B(X).
\tag{2.9}
\]

At the last position the actual last-occurrence state begins

\[
 (B(X),\{x_{H-1}\},\ldots,\{x_0\},\ldots).
\tag{2.10}
\]

Its prefix unions of sizes \(m-q\) are exactly the sets \(L_q(X)\).

For a nonqueued arc (2.4), append

\[
 B(X)-\{b\}+\{a\}.
\tag{2.11}
\]

Move-to-front subtraction changes (2.10) into a state beginning

\[
 (B-b+a,\{b\},\{x_{H-1}\},\ldots,\{x_0\},\ldots).
\tag{2.12}
\]

The first \(H\) singleton blocks after the base are
\(b,x_{H-1},\ldots,x_1\), so their reverse deletion order is precisely
the queue in (2.4).  The prefix of size \(m\) is \(Y\).

For a priority-\(j\) arc, append

\[
 \{a\},\{x_{j+1}\},\ldots,\{x_{H-1}\},B(X).
\tag{2.13}
\]

This word has length \(H-j+1\).  Its final state begins

\[
 (B,\{x_{H-1}\},\ldots,\{x_{j+1}\},
   \{a\},\{x_j\},\ldots,\{x_0\},\ldots),
\tag{2.14}
\]

whose first \(H\) singleton blocks have reverse deletion order (2.5).
Again their union with \(B\) is \(Y\).  Thus an ordinary arc costs one
new letter and a priority-\(j\) arc costs one plus its weight \(H-j\).

A path with \(t\) owners consequently costs

\[
 (H+1)+(t-1)+\sum\delta=t+H+\sum\delta.
\]

Summing over the path cover proves (2.7).  A one-owner omitted flag costs
\(H+1\); adding the \(d\) omitted owners to (2.7) proves (2.8).
Every claimed witness is a prefix union of an actual last-occurrence state,
hence the union of a literal contiguous interval.  \(\square\)

For a full signed radius-\(H\) prefix, initialize \(H\) upper singleton
markers as well.  The same proof replaces the term \(H(C+d)\) in (2.8)
by \(2H(C+d)\).  The upper queues are endogenous; the AH bridge does not
prove that their marginal loads are balanced.

### Lemma 2.2 -- exact portal-loop identity

Every arc of \(\mathcal R_H\) satisfies

\[
 \boxed{
 \delta(X,Y)=
 \sum_{q=1}^H\mathbf1_{\{L_q(X)=L_q(Y)\}}.}
\tag{2.15}
\]

#### Proof

For a nonqueued arc, direct use of (2.4) shows that every depth changes.
For a priority-\(j\) arc, when \(q\le j\),

\[
 L_q(Y)=L_q(X)-\{x_q\}+\{a\},
\]

whereas for \(q\ge j+1\), the first \(q\) entries of (2.5) include \(a\)
and give

\[
 L_q(Y)=L_q(X).
\]

There are exactly \(H-j\) such loop depths.  \(\square\)

Combining Theorem 2.1 with the balanced core flags of the AH bridge proves
the following exact sufficient chronology statement.

### Corollary 2.3 -- the one-sided priority-cylinder rotor gate

For every fixed \(A\), the lower Gaussian band has a literal word of length
\(W+o(W)\) if one can choose the balanced core flags and a path cover in
\(\mathcal R_H\) such that

\[
 \boxed{
 HC+
 \sum_{XY}\sum_{q=1}^H
 \mathbf1_{\{L_q(X)=L_q(Y)\}}
 =o(W).}
\tag{2.16}
\]

Indeed, \(Hd=O_A(W/\sqrt m)=o(W)\), and every balanced core depth has
positive floor and therefore covers every target in \(V_q\).

Statement (2.16) is **UNPROVED**.  It is a horizontal flagged path-cover
problem within the arcs (2.4)--(2.5).  The abstract flow controls the
vertex marginals in \(\mathcal R_H\), but supplies no transition arcs;
longer unrestricted MTF connectors are not classified here.

## 3. What the saturating chronology proves at the first two radii

Orient the core cycle as

\[
 X_0,X_1,\ldots,X_{M-1},X_0
\]

and assign

\[
 L_1(X_i)=S_{i+1}=X_i\cap X_{i+1}.
\tag{3.1}
\]

Put

\[
 x_i=X_i\setminus S_{i+1},
 \qquad
 a_i=X_{i+1}\setminus S_{i+1}.
\tag{3.2}
\]

### Theorem 3.1 -- unconditional radius-one chronology

Every natural core edge \(X_i\to X_{i+1}\) is a nonqueued radius-one arc.
Thus, after breaking the cycle at one edge, the core has \(C=1\) and
\(J=0\).  Retaining one isolated flag for every omitted owner gives length

\[
 \boxed{W+d+1=W+O(W/m).}
\tag{3.3}
\]

#### Proof

The next deletion label is

\[
 x_{i+1}=X_{i+1}\setminus S_{i+2}.
\]

If \(x_{i+1}=a_i\), then

\[
 S_{i+2}=X_{i+1}-a_i=S_{i+1},
\]

contrary to the distinctness of the saturating lower vertices.  Therefore
\(x_{i+1}\in X_{i+1}-a_i=S_{i+1}=L_1(X_i)\), which is exactly the
nonqueued condition (2.4) for \(H=1\).  Formula (3.3) is (2.8) with
\(H=C=1\) and \(J=0\).  \(\square\)

The simpler first-band colour word has length \(W+1\) if the omitted
depth-one flags are not required; (3.3) records the cost of retaining the
owner-labelled omitted flags from the AH bridge.

### Theorem 3.2 -- exact radius-two chronology

Define

\[
 T_i=S_{i+1}\cap S_{i+2},
 \qquad
 X_i\supset S_{i+1}\supset T_i.
\tag{3.4}
\]

These flags are priority-compatible around the entire natural core cycle.
The edge \(i\to i+1\) has portal weight one exactly when

\[
 T_i=T_{i+1},
\tag{3.5}
\]

and otherwise has weight zero.

#### Proof

Write

\[
 y_i=S_{i+1}\setminus S_{i+2}.
\]

Then the queue of \(X_i\) is \((x_i,y_i)\).  Since

\[
 X_{i+1}=S_{i+1}\cup S_{i+2},
\]

one has

\[
 x_{i+1}=X_{i+1}\setminus S_{i+2}
 =S_{i+1}\setminus S_{i+2}=y_i.
\tag{3.6}
\]

Thus the first queue entry shifts correctly.  Moreover

\[
 T_i=S_{i+2}-a_i,
 \qquad
 T_{i+1}=S_{i+2}-y_{i+1}.
\tag{3.7}
\]

If \(T_i\ne T_{i+1}\), then \(y_{i+1}\in T_i=B(X_i)\), so (2.4) is a
nonqueued arc.  If \(T_i=T_{i+1}\), then \(y_{i+1}=a_i\), and (2.5) is
the priority-\(1\) arc \((y_i,a_i)\), of weight one.  These exhaust the
two cases.  \(\square\)

Let

\[
 M_2=N_2-|\{T_i:i\in\mathbb Z_M\}|
\tag{3.8}
\]

be the number of missing rank-\((m-2)\) labels.  Break the cycle at one
edge.  A linear sequence of \(M\) terms taking \(K\) distinct values has
at most \(M-K\) equal adjacent pairs.  Hence Theorem 3.2 gives

\[
 \begin{aligned}
 J
 &\le M-(N_2-M_2)\\
 &=N_1-N_2+M_2\\
 &=\frac{4N_1}{m+3}+M_2.
 \end{aligned}
\tag{3.9}
\]

In particular, \(M_2=O(W/m)\) implies \(J=O(W/m)\).  Initializing the
omitted radius-two flags and appending every still-missing depth-two target
literally gives length at most

\[
 \boxed{W+2(d+1)+J+M_2.}
\tag{3.10}
\]

Thus \(M_2=o(W)\) already gives a literal one-sided three-rank word of
length \(W+o(W)\), while \(M_2=O(W/m)\) gives the sharper
\(W+O(W/m)\) estimate.

One sharp-scale sufficient radius-two graph target is therefore:

> Find a saturating cycle whose lower Hamilton cycle misses only
> \(O(W/m)\) rank-\((m-2)\) edge colours.

Full depth-two support is more than sufficient.  This is the
two-sided-rainbow Hamilton-cycle gate: the upper union colours must remain
distinct while the next lower intersection colours have near-complete
support.  The AH marginal flow does not imply this horizontal property.

## 4. Exact zero-portal chronology of the natural cycle

For a coordinate \(z\), consider the cyclic binary word

\[
 (\mathbf1_{\{z\in X_i\}})_{i\in\mathbb Z_M}.
\]

A cyclic \(1\)-run is a maximal interval of consecutive owners containing
\(z\); a cyclic \(0\)-run is defined analogously.  Put

\[
 r_i=X_i\setminus X_{i+1}.
\tag{4.1}
\]

### Theorem 4.1 -- exact residence-run criterion

For \(1\le H<m\), the natural core cycle has a cyclic zero-portal literal
lift exposing exactly the consecutive-intersection and consecutive-union
flags in (4.3), whose displayed lower queue is the next \(H\) departure
labels and whose displayed upper queue is the previous \(H\) departure
labels, with a physically refined tail, if and only if every coordinate's
cyclic \(1\)-runs have length at least \(H+1\) and its cyclic \(0\)-runs
have length at least \(H\).

For the one-sided lower lift, only the \(1\)-run condition is required.

When the full condition holds, the state at \(X_i\) is forced at its
displayed prefix and may be written

\[
 \begin{aligned}
 B_i&=X_i\setminus\{r_i,r_{i+1},\ldots,r_{i+H-1}\},\\
 \Pi_i&=(B_i,
 \{r_{i+H-1}\},\ldots,\{r_i\},
 \{r_{i-1}\},\ldots,\{r_{i-H}\},\mathcal R_i),\\
 R_i&=([n]\setminus X_i)
      \setminus\{r_{i-1},\ldots,r_{i-H}\}.
 \end{aligned}
\tag{4.2}
\]

Here \(\mathcal R_i\) is an arbitrary ordered partition of the set
\(R_i\); subsequent updates need not preserve it as one block.

Its signed flags are

\[
 \boxed{
 \Gamma^-_{i,q}=\bigcap_{s=0}^{q}X_{i+s},
 \qquad
 \Gamma^+_{i,q}=\bigcup_{s=0}^{q}X_{i-s}.}
\tag{4.3}
\]

#### Proof

Assume first the run conditions.  During the next \(H\) transitions, no
coordinate newly entering the cycle can depart, and the \(H\) departure
labels \(r_i,\ldots,r_{i+H-1}\) are distinct members of \(X_i\).  Dually,
the previous \(H\) departures remain absent and are distinct.  Hence
(4.2) is an ordered partition prefix.

If \(a_i=X_{i+1}\setminus X_i\), then

\[
 B_{i+1}=B_i-\{r_{i+H}\}+\{a_i\}.
\tag{4.4}
\]

Appending \(B_{i+1}\) to the state in (4.2) puts \(B_{i+1}\) first,
leaves \(r_{i+H}\) as the new deepest lower singleton, shifts the other
lower singletons one place toward departure, and makes \(r_i\) the newest
upper singleton.  The remaining old blocks form an ordered partition
\(\mathcal R_{i+1}\) of the new residual set.  Thus the displayed prefix
is exactly that of \(\Pi_{i+1}\), and every transition uses one letter and
no portal.

The first formula in (4.3) follows because precisely
\(r_i,\ldots,r_{i+q-1}\) leave the original owner during the next \(q\)
steps and no new arrival can leave in that interval.  The second follows
by the reversed argument from the zero-run condition.

Conversely, in a zero-portal natural-departure lower rotor retaining the
next \(H\) departure labels, an arrival cannot itself occur among those
labels.  Its containing run therefore has length at least \(H+1\).  If
the displayed upper queue is required to be the previous \(H\) departures,
a departed coordinate may re-enter exactly when its label is falling out
of that queue, but not earlier.  Thus every zero-run has length at least
\(H\).  This proves necessity in
the stated natural-departure architecture.  General priority-prefix
transitions can re-enter from an upper singleton and are deliberately
outside this equivalence.  \(\square\)

### Theorem 4.2 -- natural-epoch cuts

For every \(1\)-run of length at most \(H\), take the circular interval of
transition edges from its entering boundary through its exit boundary;
call this family \(\mathcal I_H^-\).  Let \(\mathcal I_H^\pm\) additionally
contain the analogous intervals of all \(0\)-runs of length at most
\(H-1\).  For \(\star\in\{-,\pm\}\), let \(\tau_H^\star\) be the minimum
number of cycle edges meeting every interval of \(\mathcal I_H^\star\),
and put

\[
 p_H^\star=\max\{1,\tau_H^\star\}.
\tag{4.5}
\]

Then:

1. \(p_H^-\) is exactly the minimum number of consecutive one-sided
   natural-departure epochs with independently recanonicalized boundary
   flags.  Their literal core length is

   \[
    \boxed{M+Hp_H^-.}
    \tag{4.6}
   \]

2. Cutting at a minimum transversal of \(\mathcal I_H^\pm\) gives a full
   signed natural-departure schedule with endogenous, recanonicalized
   boundary flags and literal core length

   \[
    \boxed{M+2Hp_H^\pm.}
    \tag{4.7}
   \]

   This is a sufficient schedule, not a minimum theorem for general
   endogenous upper queues.

3. If \(\mathcal I_H^\star\ne\varnothing\), then its transversal number
   has the exact circular-interval min--max form

   \[
    \boxed{
    \tau_H^\star
    =1+\min_e\nu((\mathcal I_H^\star)_e),}
    \tag{4.8}
   \]

   where \((\mathcal I_H^\star)_e\) is the family of intervals not
   containing \(e\), viewed on the line obtained by cutting at \(e\), and
   \(\nu\) is the maximum number of pairwise edge-disjoint intervals.

#### Proof

A one-sided natural-order component fails the lower run criterion exactly
when it contains both boundary transitions of a short \(1\)-run.  Every
interval in \(\mathcal I_H^-\) must therefore be cut, proving the necessity
and exactness assertion in item 1.  Conversely, after all such intervals
are hit, no component contains an internal short \(1\)-run.  Adding the
short \(0\)-run intervals gives the sufficient full signed construction in
item 2.  This extra cut condition need not be necessary near a
recanonicalized initial upper queue, which is why no full signed minimum is
claimed.

Coordinates already present at a component's initial endpoint create no
internal arrival; coordinates still present at its terminal endpoint may
be assigned the standard zero-toll dummy future departures.  Time reversal
and complementation supply compatible artificial past-departure markers at
the initial endpoint in the full signed construction.  Within \(H\) of a
cut these dummy labels replace the out-of-component symbols in (4.2), so
the boundary flags are recanonicalized.  A component with \(t\) owners
costs \(t+H\) one-sided and \(t+2H\) full signed.  This proves
(4.6)--(4.7).

For completeness, the terminal completion is exact.  Order the terminal
coordinates \(z_1,\ldots,z_m\) by increasing time of last entry, putting
coordinates present throughout first.  Exclude the latest \(z_m\), choose
any \(H\) of the other coordinates, and dummy-depart the chosen coordinates
in increasing last-entry order.  Immediately after the last entry of a
chosen \(z_t\), the \(m-t\) nonterminal contemporaries depart genuinely,
and among \(z_1,\ldots,z_{t-1}\) at most \(m-H-1\) are excluded.  Hence at
least

\[
 (m-t)+(t-1-(m-H-1))=H
\]

contemporaries depart before \(z_t\).  No terminal arrival is therefore
priority-active.  Reversing and complementing this construction gives the
initial signed completion used above.

For (4.8), choose one edge \(e\) in a circular hitting set.  The intervals
not hit by \(e\) form an interval family on a line, whose transversal
number equals its maximum disjoint-family size.  Hence a hitting set
containing \(e\) has minimum size
\(1+\nu((\mathcal I_H^\star)_e)\).  Minimizing in \(e\) proves item 3.
\(\square\)

Thus \(Hp_H^-=o(W)\) is necessary and sufficient for negligible
one-sided natural-epoch initialization, while \(Hp_H^\pm=o(W)\) is a
sufficient full signed condition.  Neither construction preserves the
prescribed AH flags at a cut.  Priority portals can beat these epoch
schedules and are governed instead by Theorem 2.1.

## 5. Balanced-histogram distance from literal horizontal diamonds

Keep the natural owner order \((X_i)\) and its first flags (3.1).  Let

\[
 P_0(i)=X_i\supset P_1(i)\supset\cdots\supset P_H(i)
\tag{5.1}
\]

be any exactly balanced core flag family supplied by the abstract AH flow.
Call edge \(i\) **durable** when every lower horizontal identity

\[
 \boxed{
 P_{s+1}(i)=P_s(i)\cap P_s(i+1)
 \qquad(0\le s<H)}
\tag{5.2}
\]

holds.  Let \(K\) be the number of nondurable edges.

For \(1\le q\le H\), define the natural window

\[
 \Gamma_{i,q}=\bigcap_{s=0}^{q}X_{i+s}.
\tag{5.3}
\]

Let \(I_q\) be the number of indices for which
\(|\Gamma_{i,q}|\ne m-q\).  For valid windows put

\[
 h_q(S)=|\{i:\Gamma_{i,q}=S\}|,
 \qquad S\in V_q.
\tag{5.4}
\]

Let \(\mathcal B_q\) be the class of balanced core load vectors of total
mass \(M\), and define

\[
 \begin{aligned}
 \delta_q
 &=M-\max_{b\in\mathcal B_q}
       \sum_{S\in V_q}\min\{h_q(S),b(S)\}\\
 &=I_q+\min_{b\in\mathcal B_q}
       \sum_{S\in V_q}(h_q(S)-b(S))_+.
 \end{aligned}
\tag{5.5}

The second equality follows from
\(\sum_S h_q(S)=M-I_q\).

### Theorem 5.1 -- collision-distance bound

For every \(1\le q\le H\),

\[
 \boxed{\delta_q\le qK.}
\tag{5.6}
\]

#### Proof

If all edges in the cyclic \(q\)-window starting at \(i\) are durable,
repeated use of (5.2) gives

\[
 P_q(i)=\bigcap_{s=0}^{q}X_{i+s}=\Gamma_{i,q}.
\tag{5.7}
\]

Thus the natural window is valid and agrees with the prescribed balanced
flag at every index whose \(q\)-window avoids the nondurable edges.  One
nondurable edge belongs to exactly \(q\) cyclic \(q\)-windows.  Hence at
most \(qK\) indices disagree or are invalid.

Let \(b^*\) be the actual balanced histogram of the flags \(P_q(i)\).
The common occurrences at the agreeing indices give

\[
 \sum_S\min\{h_q(S),b^*(S)\}\ge M-qK.
\]

Maximizing over balanced \(b\) and using (5.5) proves (5.6).  \(\square\)

At depth two, every natural window is valid because consecutive
\(S_{i+1},S_{i+2}\) are distinct facets of their common owner.  Put

\[
 r=N_1-N_2,\qquad
 M_2=|\{S:h_2(S)=0\}|,
 \qquad
 D_2=|\{S:h_2(S)\ge2\}|.
\tag{5.8}
\]

Since \(M/N_2=(m+3)/(m-1)<2\) for \(m>5\), the balanced core loads are
one or two, with exactly \(r\) high entries.  Relative to the all-one
baseline, the natural excess is

\[
 \sum_{h_2(S)>0}(h_2(S)-1)=r+M_2.
\]

Placing the \(r\) high quotas on duplicated cells saves
\(\min\{r,D_2\}\).  Therefore

\[
\boxed{
 \delta_2=M_2+\max\{0,r-D_2\}.}
\tag{5.9}
\]

### Lemma 5.2 -- one-position diamond law

Suppose consecutive word positions mark distinct middle owners \(X,Y\),
and both last-occurrence states have a lower useful prefix consisting of
one base block followed by \(H\) singleton deletion blocks.  If the update
from \(X\) to \(Y\) preserves all \(H\) displayed depths, then, writing
their flags as \(P_s(X),P_s(Y)\),

\[
 P_{s+1}(X)=P_s(X)\cap P_s(Y)
 \qquad(0\le s<H).
\tag{5.10}
\]

#### Proof

Write the state at \(X\) as

\[
 (B,\{x_{H-1}\},\ldots,\{x_0\},\ldots).
\]

Let \(Z\) be the update mask, which is the target base and therefore has
size \(|Z|=|B|=m-H\).  Put

\[
 k=|Z\cap\{x_0,\ldots,x_{H-1}\}|,
 \qquad t=|Z\setminus X|,
 \qquad s=|B\setminus Z|.
\]

Counting the entries of \(Z\) gives

\[
 s=k+t.
\tag{5.10a}
\]

After the update, the block following \(Z\) is \(B\setminus Z\), followed
by the \(H-k\) surviving old singleton blocks.  The target useful prefix
therefore forces \(s\le1\).  If \(s=0\), then \(k=t=0\) and the marked
middle owner remains \(X\).  If \(s=1,k=1,t=0\), the residual singleton
from \(B\) replaces the absorbed old singleton and the owner again remains
\(X\).  Since \(X\ne Y\), the only possible case is

\[
 s=1,\qquad k=0,\qquad t=1.
\]

Thus, for unique \(b\in B\) and \(a\notin X\), the new base is
\(Z=B-b+a\), the old base leaves the singleton \(b\), and the next deletion
queue is

\[
 (x_1,\ldots,x_{H-1},b).
\]

Direct substitution gives (5.10) at every depth.  \(\square\)

### Theorem 5.3 -- natural-order literal lower bound

Suppose a literal word covers all \(W\) middle masks, retains the natural
cyclic order on the core owners, marks every core owner in a state whose
minimal lower useful prefix consists of the base followed by the \(H\)
singleton deletion blocks prescribed by (5.1), permits an arbitrarily
refined older tail, and uses arbitrary connectors between consecutive
marked owners.
Then for every \(q\le H\),

\[
 \boxed{
 L\ge W+
 \left(
   \left\lceil\frac{\delta_q}{q}\right\rceil-d-1
 \right)_+.}
\tag{5.11}
\]

#### Proof

A single update between two consecutive marked useful prefixes forces
every horizontal identity (5.2) by Lemma 5.2.  Hence a nondurable natural
edge requires at least one
intervening word position.  After the best linear cut, at least
\((K-1)_+\) such intervening positions remain.  The \(M\) core owners
therefore require

\[
 L\ge M+(K-1)_+.
\]

Independently, covering the \(W\) distinct middle targets requires
\(L\ge W\), because one endpoint exposes at most one target of a fixed
rank.  Since \(W=M+d\), taking the maximum of these two bounds gives

\[
 L\ge W+(K-d-1)_+.
\tag{5.12}
\]

Theorem 5.1 gives \(K\ge\lceil\delta_q/q\rceil\), proving (5.11).
\(\square\)

In particular, \(\delta_2\ge\varepsilon W\) would imply

\[
 L\ge(1+\varepsilon/2-o(1))W
\tag{5.13}
\]

inside this architecture.  No such lower bound on \(\delta_2\), or on any
\(\delta_q\), follows from the published saturating-cycle theorem.

Theorem 5.3 does not obstruct reordering the owners, nonminimal split-base
states, or abandoning the prescribed balanced flags.  Priority portals
are allowed in its connectors; they pay through the necessary intervening
positions.

## 6. Exact remaining lemma and adversarial audit

The smallest positive statement isolated here within the flagged
priority-cover route is:

> **Balanced flagged rotor path-cover lemma -- UNPROVED.**  For every fixed
> \(A>0\), with \(H=\lceil A\sqrt m\rceil\), choose the balanced nested
> core flags of Theorem 1.1 of the AH report so that their graph
> \(\mathcal R_H\) has a directed path cover satisfying
> \[
> HC+\sum_{XY}\delta(X,Y)=o(W).
> \]

Theorem 2.1 proves that this lemma gives a literal one-sided central band
at width plus \(o(W)\), including the omitted owners and all their chosen
flags.  A full signed constant-one proof additionally needs the endogenous
upper flags of the same chronology to satisfy the corresponding coverage
ledger; the one-sided AH bridge does not prove that.

The main claims were independently audited.  The following scope checks
are essential.

1.  Corollary 1.2 closes weighted marginal overload, not a common exact
    full-mass balanced comparator.
2.  Theorem 2.1 is a sufficient and exact accounting theorem for the
    priority-cylinder arcs (2.4)--(2.5).  It does not classify every longer
    arbitrary MTF connector.
3.  The portal weight is literally the number of equal consecutive lower
    flags, by (2.15); it is not a separate reset estimate.
4.  Balanced depthwise histograms alone do not control (2.15).  At
    Gaussian depth, even the crude support quantity
    \(\sum_{q\le H}(N_1-N_q)\) is of order \(HW\), so that crude
    support-deficit estimate alone cannot prove (2.16).
5.  The residence-run theorem is restricted to zero-portal
    natural-departure queues.  The priority construction of Section 2
    deliberately permits short runs and upper-singleton re-entries; its
    lower priority-loop cost is accounted exactly.
6.  The collision-distance obstruction is restricted to the natural core
    order and prescribed minimal lower useful prefixes, with arbitrarily
    refined older tails.  No positive-density value of \(\delta_q\) has
    been proved for a saturating cycle.
7.  The radius-two conclusion is genuine and literal, but conditional on
    the explicit horizontal statistic \(M_2=o(W)\); the stronger
    \(M_2=O(W/m)\) gives the sharper \(W+O(W/m)\) length.  The abstract AH
    flow supplies no such estimate.

Accordingly, the common-owner marginal problem is closed for this core,
but literal rotor chronology remains open in this route at the flagged
path-cover condition above.  Unrestricted longer MTF connectors could
constitute a different chronology route.
