# Protected factor braids and the exact Pascal regeneration state for RSB

Date: 2026-07-31  
Lane: K, downstream Regenerative Shadow--Braid (RSB)  
Status: exact fixed-segmentation equivalence; exact compact carrier-side
state; exact conditional odd-spine induction; no uniform regeneration
theorem and no new all-\(k\) equality claim

## 0. Verdict

The central input can be weakened from a decorated Hamilton cycle to the
corrected **componentwise decorated Middle Levels 2-factor**.  Its physical
lift is already a spanning Catalan path forest, provided every marked
factor component contains an unmarked occurrence and is off the binary
cycle face.  Component merging is therefore downstream chronology work,
not a central existence hypothesis.

For that downstream work there is an exact protected state.  It has five
correlated coordinates:

1. literal fragment occurrences, orientations, openings and both labels of
   every cut or seam;
2. the short-run event stream and endpoint run collars needed by the chosen
   staircase schedule;
3. an occurrence-aware upper-shadow service ledger;
4. the chain-aligned starts, deadlines, envelopes and positional pins; and
5. the exact maximal-common-cap compiler boundary relation.

These coordinates compose associatively.  Residence and upper service use
deterministic word monoids.  The compiler uses natural join followed by
existential projection.  For a fixed sealed segmentation, an accepting root
tuple is **equivalent** to a literal RSB certificate in that segmentation.

Two useful compressions are proved.

* If a source factor has a complete fixed-window flag tower and is cut in
  \(c\) well-separated places, the complete upper-debt state has at most
  \(cq\) target labels at depth \(q\), hence at most

  \[
                 c\binom{t+1}{2},\qquad t=k-r,                 \tag{0.1}
  \]

  labels over the upper tower.
* For an arbitrary-width \(c\)-block braid, each prefix- or suffix-OR chain
  has at most \(k-r+1\) distinct values.  Relative to the invariant internal
  bank, the complete live upper set has size at most

  \[
       |H_0|+\binom c2(k-r+1)^2,                                \tag{0.2}
  \]

  where \(H_0\) is the baseline upper-hole set.

There is no analogous compiler compression in the current theorem.  The
exact compiler boundary relation is the coarsest state valid against
arbitrary future natural-join continuations.  Bounded conflict rank is not
bounded adhesion.  A genuinely finite-width induction therefore needs an
extra separator theorem, such as a block-aligned path decomposition of the
exact common-cap system, or a Pascal-preserved guarded-flow/atomic-pressure
certificate.

This yields a rigorous conditional induction.  Let \({\cal G}_{2m+1}\) be
a family of *regenerative* odd states, which includes any auxiliary
facet/diamond factor needed by the next lift, not merely an optimal word.
If the exact odd-to-even and odd-to-odd Pascal relations are left-total on
every state of \({\cal G}_{2m+1}\), then one regenerative base
proves \(\nu(k)=B(k)\) in every subsequent dimension.  The extra child
hypotheses are stated in Theorem 7.1.

The verified cases do not prove that left-totality.  They instead expose
the right state:

* \(k=13\) and \(k=15\) use different lower/upper seam economies;
* \(k=14\) and \(k=16\) have tiny named upper defect rays, but globally
  regenerated compilers;
* the optimal \(k=16\) word is **not** a flat depth-three word; and
* the direct authenticated \(k=15\to17\) four-sector formula needs at least
  60 new upper-\(q=1\) edges and at least 61 deleted factor edges.

The nonflat \(k=16\) endpoint is nevertheless highly structured.  It is a
single-jump staircase on a two-cycle facet rail.  The jump leaves one
protected \((d+1)\)-collar of the long cycle and the entire short cycle as
a balanced facet bridge.  This gives the first exact candidate even
regeneration primitive and explains the observed numbers 45 and 49.

Thus the theorem supplies a recursive RSB language and an exact missing
transition statement.  It does not supply the transition.

## 1. Exact terminal acceptance is the general staircase criterion

Fix \(k\), a central rank \(r\),

\[
       W=\binom kr,\qquad d=d(k),\qquad L=W+d,                 \tag{1.1}
\]

where \(d(k)\) is the deadline lower-bound depth.  A terminal RSB
certificate consists of the following data.

* A rank-\(r\) chronology

  \[
              T=(T_0,\ldots,T_{W-1})                           \tag{1.2}
  \]

  which enumerates \(\binom{[k]}r\) and whose interval unions cover every
  target of rank greater than \(r\).
* Strictly increasing starts and deadlines giving chain-aligned physical
  intervals \(I_i\subseteq[0,L-1]\).
* Nonempty caps \(\Gamma_p\) contained in the maximal envelopes

  \[
                    E_p=\bigcap_{i:p\in I_i}T_i,                \tag{1.3}
  \]

  such that the capped letters still reproduce every row \(T_i\).
* An injective assignment of every nonempty target below rank \(r\) to a
  lower cell, with one maximal common cap

  \[
       A_p=\Gamma_p\cap
       \bigcap_{S:\,p\in M(S)}S                                \tag{1.4}
  \]

  which is nonempty and reproduces every middle row and every assigned
  lower target.

These are exactly C1--C3 of the master staircase--pin--common-cap theorem.
They imply a universal word of length \(W+d\).  Conversely, within the
fixed chronology, schedule, cap and pin fibre, every universal word yields
such an assignment.

This is the acceptance notion used below.  It is deliberately more general
than the flat condition \(D^dA=T\).  The latter is a useful sufficient
subclass, not a normal form.

### Proposition 1.1 (the flat subclass is not without loss)

The authenticated optimal words have the following ordinary derivative
profiles:

\[
\begin{array}{c|c|c|c}
k&d&|D^dA|&\text{rank histogram}\\ \hline
13&3&1716&7^{1716}\\
14&2&3432&7^{3432}\\
15&3&6435&8^{6435}\\
16&3&12870&8^{6484}9^{6386}.
\end{array}                                                    \tag{1.5}
\]

All entries in each displayed derivative row are distinct.  The profile
alone proves that the \(k=16\) optimum is not a flat depth-three carrier
word.  Independently, its frozen chain-aligned schedule, envelope, pin and
common-cap certificate proves acceptance by the general C1--C3 criterion.

#### Proof

Directly apply adjacent OR three times (twice at \(k=14\)) to the retained
literal words.  The first three rows agree with their certificate audits.
For `answers/k16.word`, the resulting 12,870 values are distinct and have
the displayed two-rank histogram.  This replay by itself says nothing about
the lower compiler.  The separately frozen general certificate realizes
the rank-eight chronology on its nonuniform chain-aligned intervals and
passes C1--C3.
\(\square\)

Any recursive state restricted to flat words therefore excludes a proved
optimal endpoint.

## 2. Corrected factor-level central input

Assume the corrected Decorated Middle Levels 2-Factor Theorem at the
relevant semilength.  Thus the factor has globally bijective selected upper
and lower turn representatives; selected shore types alternate on every
marked component; every marked component has an unmarked occurrence and is
off the binary cycle face.  Unmarked components use either residual
cross-matching phase.

The factor-to-diamond theorem gives a perfect diamond matching whose
physical lift is a spanning degree-at-most-two forest with exactly the
Catalan number of path components.  No Hamiltonicity, gluing tree, voltage,
or component merge is used in this implication.

This scope is load-bearing.  A wholly marked component may have both global
turn palettes correct and still lift to two rail cycles.  The corrected
all-marked exclusion cannot be dropped.

For RSB, regard every path of the lift as a sealed occurrence-labelled
fragment.  A subsequent component braid may join, reverse or rethread these
fragments.  If an alternating-circuit packet first changes the central
2-factor, it is a **regeneration node**: the terminal RSB state is recomputed
on its output.  The abstract alternating-circuit decomposition does not
preserve residence, deep shadows, or the compiler through intermediate
factors.

Thus the central assumption needed in this note is weaker than a decorated
Hamilton theorem, but it is still only a source of fragments.  It supplies
none of the acceptance fields in Section 1 automatically.

The positive \(ML(7)\) incidence-hex theorem is consistent with this
quantifier.  One hex repairs the first gap-Hall counterexample; among its
31 alternating hexes, 16 outputs are Hamilton, 10 are decorable, and 6
share a fixed forest decoration with the input.  The last class is the
strong transparent-transport face.  The present theorem needs only a
terminal decorated factor plus an accepting **joint** RSB root relation.
It therefore does not require fixed-decoration transparency through a
central repair packet.  Separate upper and lower rainbows still do not
replace the terminal joint decoration.

## 3. The exact protected fragment state

Let \(P=(P_0,\ldots,P_{n-1})\) be an oriented sealed fragment of rank-\(r\)
owner occurrences.  “Sealed” means that later operations may reverse or
join \(P\), but may not silently delete one of its internal edges.

### 3.1 Physical and palette state

Store:

1. all owner occurrence identifiers and the two oriented endpoints;
2. the opening/cut mode and the two deleted endpoint edges;
3. for every cut or candidate seam \(XY\), both

   \[
                     \chi^-(XY)=X\cap Y,\qquad
                     \chi^+(XY)=X\cup Y;              \tag{3.1}
   \]

4. every named protected occurrence span and port used by a later
   transition.

The paired label in (3.1) is essential.  A seam may duplicate a lower
colour while repairing an indispensable upper colour, or conversely.

### 3.2 Exact short-run event monoid

For every coordinate \(x\), store its initial and terminal positive-run
lengths, capped at \(d+1\), the all-one flag, and every maximal *internal*
positive run of length at most \(d\), with its occurrence endpoints.  Call
the resulting record \({\cal E}_d(P)\).

Compose the records by concatenating their two truncated run
decompositions.  Offset the events of \(Q\); coalesce the terminal
positive arm of \(P\) with the initial positive arm of \(Q\) exactly when
both boundary bits are one; and then reclassify every positive run touching
the new global left or right endpoint as an outer arm.  In particular, a
one-sided old arm becomes an internal run when the adjacent boundary zero
closes it, unless it still touches the other global endpoint.  Retain an
internal run exactly when its length is at most \(d\), cap outer lengths at
\(d+1\), and update the all-one flag.  Reversal exchanges the arms and sends
\([a,b]\) to \([n-1-b,n-1-a]\).

### Lemma 3.1 (short-run event composition)

The operation above is associative and reconstructs exactly all internal
positive runs of length at most \(d\) in any concatenation of sealed
fragments.

#### Proof

Every maximal run of the concatenation is obtained by concatenating the
literal run decompositions, coalescing across one-boundaries, and closing
arms at zero-boundaries.  The stated reclassification therefore produces
the literal run decomposition.  Capping at \(d+1\) loses no relevant
information: once a run has length greater than \(d\), positive extensions
cannot make it short.  Literal concatenation is associative, so the
truncated record is independent of parenthesization. \(\square\)

For the standard strict-residence subclass, acceptance is simply that no
nonendpoint event remains.  For a general arbitrary-start schedule, encode
omitted starts and deadlines by nondecreasing vectors \(\alpha,\tau\), and
let \(g_i=|\{j:\alpha_j\le i\}|\).  From the event record define

\[
 \rho_j^\alpha=\max\bigl(
   \{a:[a,b]\text{ is internal and }(b-a+1)+g_{b+1}\le j\}
   \cup\{0\}\bigr).                                  \tag{3.2}
\]

For a legal schedule, the exact safe-corridor theorem says that row recovery
is equivalent to

\[
                  \tau_j\ge\rho_j^\alpha\quad(1\le j\le d).    \tag{3.3}
\]

Chain alignment is a separate requirement for transporting the nested upper
row tower.  Envelope nonemptiness and all cap/pin equations remain in the
compiler relation.  Thus \({\cal E}_d\), not a minimum-run scalar, is the
correct schedule-aware residence state.

### 3.3 Exact upper service

Store

\[
\begin{aligned}
 \operatorname{Tot}(P)&=\bigcup_iP_i,\\
 \operatorname{Pre}(P)&=\{\bigcup_{i=0}^jP_i\},\\
 \operatorname{Suf}(P)&=\{\bigcup_{i=j}^{n-1}P_i\},\\
 \operatorname{Deck}^+(P)&=\{\bigcup_{i=a}^bP_i\}.
                                                               \tag{3.4}
\end{aligned}
\]

For concatenation,

\[
\begin{aligned}
 \operatorname{Deck}^+(PQ)
  ={}&\operatorname{Deck}^+(P)\cup\operatorname{Deck}^+(Q)\\
    &\cup\{A\cup B:A\in\operatorname{Suf}(P),
                       B\in\operatorname{Pre}(Q)\},             \tag{3.5}
\end{aligned}
\]

with the analogous exact formulas for total, prefix and suffix chains.
This is associative because every interval is uniquely internal or crosses
the last join.

If a fragment will never be reopened, its internal deck may be replaced by
the family of required targets which it serves.  If later operations may
cut it, one must retain occurrence-labelled witness spans, not only target
values.

### Lemma 3.2 (prefix/suffix chain bound)

For rank-\(r\) owners on \([k]\), each of the distinct prefix- and
suffix-OR chains in (3.4) has at most \(k-r+1\) values.

#### Proof

The first value has rank \(r\).  Along a prefix or suffix chain the union
only grows, and every strict growth adds at least one of the remaining
\(k-r\) coordinates. \(\square\)

### 3.4 Exact compiler boundary relation

Take the complete Boolean system for the chain-aligned schedule, envelopes,
caps, pins, injective lower-target/cell assignment and maximal common caps.
For a processed module \(P\), expose every variable appearing in a
constraint not wholly sealed inside \(P\), and define

\[
 {\cal R}_P=\pi_{\partial P}\bigl(\operatorname{Sol}\Phi_P\bigr). \tag{3.6}
\]

This relation includes the live start/deadline choices, used target and cell
identities, cap bits, middle-row supply bits, protected-pin equations and
every selected lower-cell equation meeting the boundary.

For a literal seam relation \({\cal R}_e\), the exact update is

\[
 {\cal R}_{PQ}=\pi_{\partial(PQ)}
   ({\cal R}_P\Join{\cal R}_e\Join{\cal R}_Q).        \tag{3.7}
\]

Natural join is conjunction and projection is existential quantification,
so (3.7) is associative.

### Proposition 3.3 (coarsest exact compiler state)

Against arbitrary future natural-join continuations on the exposed
variables, \({\cal R}_P\) is the coarsest exact compiler state.

#### Proof

If \({\cal R}_P\ne{\cal R}_{P'}\), choose a boundary valuation in their
symmetric difference.  Joining the formula which pins every boundary
variable to that valuation accepts exactly one of the two modules.  Hence
any summary identifying the two relations fails for that continuation.
\(\square\)

This is a logical minimality theorem for unrestricted continuations.  A
smaller state is possible only after proving a restriction on the physical
future.  For example, if the exact Boolean compiler system has a
block-aligned path decomposition of adhesion \(b\), separator dynamic
programming stores at most \(2^b\) Boolean boundary valuations.  Bounded
conflict rank alone does not bound \(b\).

## 4. Exact fixed-segmentation protected-braid theorem

Let a source occurrence chronology or factor be cut into sealed fragments,
oriented and reordered, and joined by literal Johnson seams to form one
linear rank-\(r\) chronology \(T'\).  Take the natural join of all fragment
and seam states of Section 3, keeping every shared occurrence and opening
identifier correlated.

### Theorem 4.1 (protected factor-braid equivalence)

Within the declared sealed segmentation, fix any extra
trace/socket/voltage/next-lift exports which the architecture declares.
The braid admits a terminal RSB certificate of length \(W+d\) **together
with those declared exports** if and only if the joint root relation has a
tuple satisfying all of the following.  If no extra export is declared,
Item 5 is vacuous.

1. The owner occurrences in \(T'\) enumerate \(\binom{[k]}r\), and every
   new seam is the declared literal Johnson edge.
2. The short-run event state and chosen \((\alpha,\tau)\) satisfy
   (3.3), schedule legality and chain alignment.
3. The upper deck in (3.5) contains every target above rank \(r\).
4. The root compiler relation (3.7) contains a valuation satisfying all
   envelope, cap, pin, middle-row and lower-target equations.
5. Every named trace/socket/voltage or next-lift export required by the
   chosen architecture is present in that same tuple.

When \(W+d=B(k)\), these conditions prove \(\nu(k)=B(k)\).

#### Proof

The physical join gives the literal owner chronology.  Lemma 3.1 and the
safe-corridor theorem give exact row recovery for the chosen schedule.
Equation (3.5) gives exact arbitrary-width upper service.  Equations
(3.6)--(3.7) give one common valuation of the complete compiler system, not
separate marginal witnesses.  The master staircase--pin--common-cap theorem
therefore produces a universal word of length \(W+d\).

Conversely, restrict any literal certificate in this segmentation to every
fragment and seam.  Its run events, interval witnesses and compiler
valuation belong to the corresponding relations, and their natural join
reconstructs an accepting root tuple.  This proves the equivalence.
\(\square\)

The theorem is not a claim that an accepting tuple exists.  It converts
existence into one exact correlated state problem.

## 5. Compact all-depth carrier state

The full deck is unnecessary when the source already has a fixed-window
flag tower and only sealed boundaries move.

Let the source consist of cycles, cut a total of \(c\) cyclic edges, and
obtain \(c\) oriented fragments.  Rejoin them by \(c-1\) edges into a
linear path.  For a depth \(q\), let \(\mu_q(U)\) be the number of source
cyclic \(q\)-edge windows whose union is \(U\).  Let

\[
 \delta_q^C(U)=\#\{\text{old }U\text{-windows meeting a cut}\},
 \qquad
 \eta_q^J(U)=\#\{\text{new }U\text{-windows meeting a join}\}. \tag{5.1}
\]

### Theorem 5.1 (cutwise all-depth debt identity)

For every upper target \(U\),

\[
              \mu'_q(U)=\mu_q(U)-\delta_q^C(U)+\eta_q^J(U).     \tag{5.2}
\]

Put

\[
 V_q(C)=\{U\in\tbinom{[k]}{r+q}:\mu_q(U)>0,
                    \ \mu_q(U)=\delta_q^C(U)\}.                \tag{5.3}
\]

If the source covers every rank-\((r+q)\) target by a \(q\)-edge window,
then the rejoined path does so if and only if

\[
                    V_q(C)\subseteq
                    \{U:\eta_q^J(U)>0\}.                         \tag{5.4}
\]

If every cut-to-cut fragment has more than \(q\) vertices, then the old
boundary family has exactly \(cq\) occurrences, the new family exactly
\((c-1)q\), and

\[
                         |V_q(C)|\le cq.                          \tag{5.5}
\]

Without the length hypothesis, (5.2)--(5.4) remain exact and (5.5) is
replaced by the literal union size of the boundary windows.

#### Proof

Every old window disjoint from all cuts lies in one fragment and transports
under orientation, since union is reversal-invariant.  These internal
windows cancel target by target.  The only deleted terms are (5.1)'s old
boundary windows and the only new terms are its join windows, proving
(5.2).  Under the stated source-coverage hypothesis, a required
rank-\((r+q)\) target not in \(V_q\) retains an internal witness.  A target
in \(V_q\) is restored exactly when it occurs at a new join, proving (5.4).
If every fragment is longer than \(q\), no \(q\)-window meets two cuts or
two joins.  Each cyclic cut lies in exactly \(q\) based windows and each
linear join in exactly \(q\), proving the counts. \(\square\)

Let \(t=k-r\).  The complete fixed-window upper state is therefore
specified by the first and last \(t\) owners of each fragment and at most

\[
                   \sum_{q=1}^t cq=c\binom{t+1}{2}               \tag{5.6}
\]

vulnerable target labels.  This is an \(O(ck^2)\) label state for bounded
\(c\).  It is not valid when upper completeness is known only through
arbitrary longer intervals or when a later operation may reopen a sealed
interior.

### Theorem 5.2 (arbitrary-width protected-ray bound)

Partition a baseline chronology into \(c\) blocks.  Let \(K\) be the
orientation-invariant union of their internal upper decks and let
\(X_{\rm old}\), \(X_{\rm new}\) be the old and new cross-block decks.
If \(H_0\) is the baseline upper-hole set and

\[
              V={\cal U}_{>r}\setminus K,                         \tag{5.7}
\]

then

\[
 V\subseteq H_0\cup X_{\rm old},
 \qquad
 |V|\le |H_0|+\binom c2(k-r+1)^2,                                \tag{5.8}
\]

and the reroot is upper-complete if and only if

\[
                              V\subseteq X_{\rm new}.             \tag{5.9}
\]

#### Proof

Every required target outside \(K\) is either already a baseline hole or
is witnessed by a baseline cross-block interval.  For each ordered pair of
first and last blocks, an interval value is one suffix value, the fixed
union of all intervening blocks, and one prefix value.  Lemma 3.2 bounds
the number of possibilities by \((k-r+1)^2\).  Finally the complete block
deck is exactly \(K\cup X_{\rm new}\), proving (5.9). \(\square\)

The useful special case is a small family of nested seam rays.  One seam
can serve several ranks by growing its interval one owner at a time.  The
theorem requires the literal OR identities, not merely the number of ray
slots.

## 6. A noncircular compiler interface

The root relation in Theorem 4.1 is exact but terminal.  For an inductive
existence proof, it may be replaced by any one of the following genuinely
constructive child certificates:

1. an explicit integral maximal-common-cap assignment;
2. a co-selectable guarded fractional Hall flow on the complete capped child
   atlas;
3. an atomic lopsided-LLL pressure witness for the complete conflict
   clutter; or
4. an exact block-aligned separator table of bounded adhesion whose
   terminal/root relation is nonempty and accepting.

Each alternative is evaluated on the same chronology, schedule, pins and
physical cells as the carrier state.  Separate Hall matchings, scalar
capacity, or rankwise caps do not suffice.

If the Boolean compiler formula has block-aligned adhesion at most \(b\),
its exact boundary relation has at most \(2^b\) Boolean valuations at a
separator.  This is only a representation bound; feasibility additionally
requires a nonempty accepting root relation.  Consequently an all-dimension
proof of

\[
                           b=\operatorname{poly}(d)               \tag{6.1}
\]

together with a right-total local transition table would give a finite
Pascal compiler state.  Neither the \(k=14\) nor the \(k=16\) certificate
currently proves (6.1).  The owner-filtered conflict rank bound \(d+1\)
does not imply it, because event dependency may be global.

## 6A. The single-jump two-cycle facet bridge

The ordinary derivative of a general staircase word need not be its owner
chronology, but a one-jump deadline schedule has an exact two-rank normal
form.

Let \(C=(C_0,\ldots,C_{N-1})\) be a rank-\(r\) chronology and let a word
\(A\) realize \(C_i\) on row interval \(I_i\).  Take tail starts \(s_i=i\)
and deadline thresholds

\[
                  \tau=(\underbrace{0,\ldots,0}_{d-1},a),
                  \qquad 0<a<N.                               \tag{6A.1}
\]

Thus

\[
 I_i=
 \begin{cases}
 [i,i+d-1],&i<a,\\
 [i,i+d],&i\ge a.
 \end{cases}                                                   \tag{6A.2}
\]

and row exactness is equivalently the mixed-depth identity

\[
 C_i=
 \begin{cases}
 (D^{d-1}A)_i,&i<a,\\
 (D^dA)_i,&i\ge a.
 \end{cases}                                                   \tag{6A.2a}
\]

### Lemma 6A.1 (single-jump derivative identity)

For \(0\le i<a-1\),

\[
                       (D^dA)_i=C_i\cup C_{i+1},                \tag{6A.3}
\]

and for \(a\le i<N\),

\[
                       (D^dA)_i=C_i.                            \tag{6A.4}
\]

At the unique hinge \(i=a-1\), (6A.3) holds if and only if the partial
next-row collar supplies every element of \(C_a\setminus C_{a-1}\).

#### Proof

For \(i<a-1\), the length-\((d+1)\) derivative window is exactly
\(I_i\cup I_{i+1}\).  Every letter in it is capped by at least one of
\(C_i,C_{i+1}\), and the two complete row intervals supply both sets.
For \(i\ge a\), the derivative window is exactly \(I_i\).  At \(a-1\),
the window contains all of \(I_{a-1}\) but omits the last position of
\(I_a\), giving precisely the stated hinge condition. \(\square\)

### Proposition 6A.1a (mixed-depth middle ownership)

More generally, let \(A\) have length \(2W+d\), and partition all
\(2W\) depth-\(d\) start positions into an old bank \(O\), an ordinary
marked bank \(M\), and a bridge bank \(B\), with

\[
                 O\mathbin{\dot\cup}M\mathbin{\dot\cup}B=[0,2W),
                 \qquad
                 |O|=W,\qquad |M|=W-h,\qquad |B|=h.             \tag{6A.4a}
\]

Suppose \(D^dA_i\), \(i\in O\), are the no-\(z\) rank-\(r\) values;
for \(i\in M\), write

\[
 D^{d-1}A_i=\{z\}\cup f_i,\qquad
 D^dA_i=\{z\}\cup U_i,
 \quad |f_i|=r-1,\quad |U_i|=r,                       \tag{6A.4b}
\]

and require \(f_i\subset U_i\) and the \(U_i\) to be pairwise distinct.
Finally, suppose \(D^dA_i\), \(i\in B\), are \(z\)-marked rank-\(r\)
values.  Select the mixed-depth owner value \(D^dA_i\) on \(O\cup B\) and
\(D^{d-1}A_i\) on \(M\).  These selected windows deliver the child middle
layer exactly once if and only if the old bank, after deleting \(z\), is
\(\binom{[2r-1]}r\), while the two selected marked banks together, after
deleting \(z\), are \(\binom{[2r-1]}{r-1}\), both as multisets.

The pairs \(f_i\subset U_i\), \(i\in M\), are fixed distinct incidences.
Completing them reduces exactly to Hall on the residual
\(h\)-by-\(h\) facet-containment graph.  This is a central diamond
completion only; each chosen residual incidence still needs a literal
upper socket and the common lower compiler.

#### Proof

The no-\(z\) and \(z\)-containing rank-\(r\) child targets are disjoint and
are in bijection with the two displayed old-coordinate layers.  This proves
the first equivalence.  Removing the already fixed distinct facet-owner
pairs leaves exactly the residual equal-shore containment graph, so Hall is
necessary and sufficient for a marginal completion. \(\square\)

Now let the odd parent be a directed lower-\(q=1\)-rainbow Johnson
2-factor on all rank-\(r\) subsets of \([2r-1]\).  Write an oriented edge
as \(T_iT_{i+1}\) and put

\[
                         X_i=T_i\cap T_{i+1}.                    \tag{6A.5}
\]

The \(X_i\) enumerate all rank-\((r-1)\) subsets.  At an owner \(T_i\),
the incoming and outgoing facets are distinct, so

\[
                         X_{i-1}\cup X_i=T_i.                    \tag{6A.6}
\]

Indeed, each facet omits one element of \(T_i\); equality of the omitted
element would make the two facets equal, contradicting rainbowness.

Adjoin a coordinate \(z\), and write \(z+X=X\cup\{z\}\).  The two rails

\[
                 T_i,\qquad z+X_i                              \tag{6A.7}
\]

together enumerate every rank-\(r\) subset of \([2r]\): the first rail is
the no-\(z\) shore and the second the \(z\)-shore.

Assume the parent factor has two directed cycles of lengths

\[
                         \ell=W-s,\qquad s,                       \tag{6A.8}
\]

and that literal Johnson connectors order the child chronology as a
rotation of the long \(z+X\) cycle, then all \(W\) no-\(z\) owners in an
arbitrary certified braid, then the short \(z+X\) cycle.  Fix a protected
tail size \(b<\ell\) and set

\[
                              a=\ell-b.                           \tag{6A.9}
\]

For the protected one-collar choice \(b=d+1\), this becomes

\[
 a=W-s-(d+1),\qquad |{\rm bridge}|=s+d+1,\qquad
 y_d=a+d-1=W-s-2,                                      \tag{6A.9a}
\]

where \(y_d\) is the exceptional omitted deadline in the tail-start
staircase.  These are bookkeeping consequences of the chosen architecture,
not a theorem that every even lift admits it.

In Theorem 6A.2, take this ordered child rail as the chronology \(C\) in
Lemma 6A.1, with \(N=2W\).

### Theorem 6A.2 (balanced two-cycle facet bridge)

If the hinge in Lemma 6A.1 passes, the marked projection of \(D^dA\)
consists of:

1. \(\ell-b\) distinct parent owners, obtained as unions of consecutive
   long-cycle facets; and
2. \(b+s\) distinct rank-\((r-1)\) facets, namely the uncontracted tail of
   the long cycle and the whole short cycle.

The missing parent-owner family also has size \(b+s\), and the containment
graph from the displayed facets to the missing owners has a perfect
matching.

If the parent linear index places the long cycle first and the short cycle
last, and the long rail is rotated to begin at parent index \(u\), then the
contracted owner sequence has at most two modular-shift pieces.  If the
contracted long-cycle arc crosses the chosen long-cycle indexing cut, both
pieces are nonempty and their shifts differ by exactly \(s\); if it does
not cross that cut, there is only one piece.

#### Proof

Equations (6A.3) and (6A.6) contract each of the first \(\ell-b\) consecutive
facet pairs to one parent owner.  Equation (6A.4) leaves the remaining
marked owners as their projected facets.  The short marked cycle lies after
the jump and is therefore wholly uncontracted.  This proves the two counts.

On either directed cycle, match every uncontracted outgoing facet \(X_i\)
to its successor owner \(T_{i+1}\).  By (6A.5) it is contained in that
owner.  The contracted pairs cover precisely the complementary successor
owners, so these maps are disjoint and saturate both bridge shores.

If the selected arc does not wrap in the chosen long-cycle coordinates,
its contraction is one shift piece.  Otherwise, starting at \(u\), the
first piece runs from \(u\) to \(\ell-1\).  At the large-cycle wrap the desired
next parent index is zero.  In arithmetic modulo \(W=\ell+s\), replacing shift
\(u\) by \(u+s\) sends the next sequence position to zero.  Hence the two
nonempty shifts differ by \(s\). \(\square\)

### Lemma 6A.3 (facet-ray recovery and internal deep inheritance)

For a directed Johnson path \(v_{a-1},v_a,\ldots,v_b\), put
\(e_i=v_{i-1}\cap v_i\).  If consecutive turn colours are distinct, then

\[
                   e_i\cup e_{i+1}=v_i,                         \tag{6A.14}
\]

and hence

\[
       D(e_a,e_{a+1},\ldots,e_b,v_b)
          =(v_a,v_{a+1},\ldots,v_b).                            \tag{6A.15}
\]

There is an analogous cyclic identity after adjoining the predecessor
owner as the left socket.  Consequently every deeper parent flag whose
whole occurrence is internal to the recovered string is inherited by the
facet bridge; only flags crossing one of its two ends enter the protected
boundary-debt ledger.

#### Proof

The two distinct facets in (6A.14) omit two distinct elements of the common
rank-\(r\) owner, so their union is that owner.  Apply this at every
position to get (6A.15).  Finally
\(D^q(DE)=D^{q+1}E\), so internal deeper strings transport.  A failure of
this argument can occur only when the required derivative window uses a
socket outside the displayed recovery string. \(\square\)

This theorem is a middle/schedule resource identity.  It does not prove
that the child connectors are upper-safe, that its row corridors are legal,
or that a common-cap compiler exists.  Those remain Rows 2--5 of the Pascal
relation below.

### Corollary 6A.4 (authenticated \(k=16\) anatomy)

For the retained endpoint,

\[
 W=6435,\quad (\ell,s)=(6390,45),\quad d=3,\quad b=d+1=4,
 \quad a=6386.                                                \tag{6A.10}
\]

The child carrier has top-bit trace

\[
                         1^{6390}0^{6435}1^{45}.                 \tag{6A.11}
\]

Its ordinary third derivative satisfies

\[
 (D^3A)_i=
 \begin{cases}
 C_i\cup C_{i+1},&0\le i<6386,\\
 C_i,&6386\le i<12870.
\end{cases}                                                   \tag{6A.12}
\]

Equivalently, the exact rank-eight owner chronology used by the compiler is

\[
       D^2A[0,6386)\ \Vert\ D^3A[6386,12870),                  \tag{6A.12a}
\]

byte-for-byte the frozen endpoint-rerooted carrier.  The first bank supplies
6,386 \(z\)-facets; the 49 marked entries of the second bank supply the
remaining facets; and the no-\(z\) part of the second bank supplies every
parent owner.

The contracted top projection has two parent-index pieces of lengths
1277 and 5109, with shifts 5113 and 5158; their difference is the short
cycle length 45.  The bridge has

\[
                            45+4=49                              \tag{6A.13}
\]

facets against 49 missing parent owners.  It is exactly one rooted
four-edge lower-shadow path plus the complete 45-edge lower-shadow cycle.
The containment graph has 128 edges and matching number 49.  The stronger
literal one-step socket graph has 96 edges and also has matching number 49,
so every missing marked parent owner has an occurrence-level \(q=1\)
extension in this certificate.  The no-top
rail is all 6,435 parent owners in four chunks of lengths 1278, 5112, 9 and
36.  In the strict \(\mathbb Z_{15}\) spiral coordinates these are
\(3\cdot426,12\cdot426,3\cdot3,12\cdot3\); the two cycles are cut at the
same sheet.

These statements are replayed independently from the final words and the
frozen rank-eight carrier in
MATH_THEOREM_K16_SHIFTED_CHUNK_FACET_SUBSTITUTION_ANATOMY_20260731.md,
MATH_THEOREM_K16_TWO_SHIFT_FACET_BRIDGE_ARITHMETIC_20260731.md, and
scratch/audit_k16_two_shift_facet_bridge_20260731.py, with the 96-edge
socket graph independently replayed by
scratch/audit_k16_d3_two_shift_facet_bridge_20260731.py.

## 7. Exact conditional Pascal induction

Let \({\cal A}_k\) be the set of accepting terminal tuples in Theorem 4.1
at the exact lower-bound length \(B(k)=W(k)+d(k)\).
Let \({\cal G}_{2m+1}\subseteq{\cal A}_{2m+1}\) be the regenerative odd
states.  Besides the optimal-word certificate, a state of \({\cal G}\) may
carry an auxiliary completed facet/diamond factor, its directed cycle/path
decomposition, residual phases and sealed-fragment relations needed by the
next Pascal lift.  In particular, Theorem 6A.2 makes a two-cycle
lower-rainbow factor plus one rooted collar a concrete even-transition
resource.

Define two literal transition relations:

\[
 {\cal P}_m^{\rm ev}\subseteq
     {\cal G}_{2m+1}\times{\cal A}_{2m+2},
 \qquad
 {\cal P}_m^{\rm odd}\subseteq
     {\cal G}_{2m+1}\times{\cal G}_{2m+3}.           \tag{7.1}
\]

A pair belongs to one of these relations only when one physical Pascal
lift/braid supplies all of the following on the child side.

1. **Central/owner row.**  Every child middle owner occurs exactly once.
   A corrected decorated 2-factor may be used as the central source; no
   Hamiltonicity is required.  All chosen residual phases and component
   openings are occurrence-labelled.  On the even branch, a
   slot-preserving cycle/path facet substitution may replace flat doubling,
   but its single-jump hinge must be checked literally.
2. **Residence row.**  The child short-run event record is evaluated at the
   child depth, and one legal chain-aligned \((\alpha,\tau)\) passes
   (3.3).  A parent record capped only at the old depth is not enough when
   the depth increases.
3. **Upper row.**  Either Theorem 5.1 clears every fixed-window debt, or
   Theorem 5.2 clears the exact arbitrary-width protected-ray set.
4. **Schedule/pin row.**  All child envelopes are nonempty and every
   positional cap and forced lower boundary target preserves the child
   middle rows.
5. **Compiler row.**  One of the four certificates in Section 6 holds for
   the complete child lower atlas.
6. **Export row.**  The odd child additionally exports the auxiliary
   factor, occurrence spans and compiler relation declared by
   \({\cal G}_{2m+3}\).

### Theorem 7.1 (left-total regenerative odd-spine induction)

Assume \({\cal G}_{2m_0+1}\ne\varnothing\).  If for every \(m\ge m_0\)
both relations in (7.1) are left-total on every state of \({\cal G}\),
meaning

\[
 \forall g\in{\cal G}_{2m+1}\quad
 \exists a\in{\cal A}_{2m+2}:(g,a)\in{\cal P}_m^{\rm ev},
                                                                    \tag{7.2}
\]

and

\[
 \forall g\in{\cal G}_{2m+1}\quad
 \exists g'\in{\cal G}_{2m+3}:(g,g')\in{\cal P}_m^{\rm odd},     \tag{7.3}
\]

then

\[
                       \nu(k)=B(k)                                 \tag{7.4}
\]

for every \(k\ge2m_0+1\), subject only to the already-proved deadline
lower bound in those dimensions.

#### Proof

Choose a regenerative base.  Equation (7.2) gives the next even accepting
state; Equation (7.3) gives the next regenerative odd state.  Iterate on
the odd spine.  Every accepted child supplies a universal word of length
\(B(k)\) by Theorem 4.1 and Section 1.  The deadline lower bound gives the
reverse inequality. \(\square\)

The left-total hypothesis is stronger than the existence of one isolated
edge and weaker than a deterministic formula: a finite-state path may
branch.  For the conclusion it would instead suffice to exhibit compatible
odd states \(g_m\) such that each \(g_m\) has both one accepting even child
and the chosen next odd child.  Left-totality is the convenient stronger
induction certificate; an unadorned infinite odd path would not certify the
even dimensions.

## 8. Exact calibration at \(k=13,14,15,16\)

The following table records the protected carrier state, not merely the
final numerical answer.

| \(k\) | physical braid | vulnerable upper state | immediate-lower debt | terminal schedule/compiler |
|---:|---|---|---|---|
| 13 | two cycles, one seam | empty internal-bank debt | one boundary-served facet | standard depth 3; full `COMP_3` |
| 14 | six pieces, five seams | four masks in three rays | none | standard depth 2; global compiler |
| 15 | two cycles, one seam | two masks in one nested ray | two boundary-served facets | standard depth 3; one-core compiler |
| 16 | four spiral source components, three topology connectors; two changed reroot seams | six masks in two rays | none | single-jump variable depth-3 schedule; global common cap |

The exact vulnerable upper masks and ray intervals are:

* \(k=14\):

  \[
  \{\mathtt{0x29ce},\mathtt{0x29de},
    \mathtt{0x352e},\mathtt{0x3b64}\},               \tag{8.1}
  \]

  with

  \[
  [2684,2685]\subset[2684,2686],\quad
  [691,692],\quad[1657,1658];                         \tag{8.2}
  \]
* \(k=15\): \([6389,6390]\subset[6387,6390]\), supplying
  \(\mathtt{0x4e79},\mathtt{0x6f79}\);
* \(k=16\): the two endpoint rays supply exactly

  \[
   \mathtt{0xb3cc},\mathtt{0xd3cc},\mathtt{0xd3ce},
   \mathtt{0xf3cc},\mathtt{0xdbce},\mathtt{0xfbce}.   \tag{8.3}
  \]

At \(k=13\), every upper target already has a component-internal witness.
At \(k=16\), all other 39,197 middle/upper values have internal witnesses.
The \(k=14\) internal bank misses exactly the four masks in (8.1).

The paired seam labels show why one lower-debt scalar is not a state.

* At \(k=13\), the seam recycles one lower cut colour but neither upper cut
  colour.
* At \(k=15\), the winning seam recycles neither lower cut colour; it
  recycles an indispensable upper cut colour, while the two missing lower
  colours are assigned to the two global boundary cells.

The compilers also differ.  The authenticated \(k=13\) solution is not in
the \(DA=DP\) one-core normal form used at \(k=15\).  The \(k=16\)
common-cap word is strongly asymmetric.  Thus neither one-core nor
equivariant compiler state contains all four bases.

Finally, the even lifts use two distinct regenerative packages.

1. The \(13\to14\) depth-drop lift uses a three-owner new-coordinate ear
   and two extra hinges.  It is not the raw derivative of the optimal
   \(k=13\) word: that word's \(D^2\) row has rank histogram
   \(5^1 6^{1715}7^1\), not a complete rank-six facet deck.
2. The \(15\to16\) plateau lift uses the separate authenticated
   four-filter \(k=15\) auxiliary package, whose derivative has every 6,435
   rank-seven mask plus one controlled rank-six exception.  It is not a
   flat lift of the canonical optimal word.  At the final-certificate level,
   however, Section 6A gives an exact regeneration relation to the retained
   \(k=15\) word: the plain rail is four chunks forming one rotation of
   each of its two carrier cycles, while the marked rail replaces one
   45-cycle and one rooted four-edge collar by their 49 facets.

Thus the present recursive state must retain auxiliary occurrence/factor
data (including the cycle closures and facet ports).  A literal optimal
word without that export is not known to be left-total; the proved
transition uses the exported occurrence, cycle and facet data.

## 9. Sharp current obstruction to totality

The direct authenticated \(k=15\to17\) four-sector formula is exact in
middle ownership and immediate lower colours, but its natural factor has:

\[
\begin{array}{c|c}
\text{physical cycles}&17\\
\text{minimum positive run}&2\\
\text{length-2 / length-3 runs}&3823/1386\\
\text{arbitrary-width upper holes}&4045.
\end{array}                                                    \tag{9.1}
\]

More strongly, every factor in that direct formula class has 60 disjoint
opposite-occurrence upper-\(q=1\) conflicts.  Any upper-\(q=1\)-complete
rethread must add at least 60 missing rank-ten edges; a Hamilton path must
delete at least 61 old factor edges.  Hence, within that direct-formula
factor, no rethread deleting at most 60 old edges can prove (7.3).  This
says nothing about a different factor or a global regeneration packet.

There are also scoped optimal-word obstructions.  The natural
\(k=14\to15\) facet source has 428 short-run defects whose four-edge collar
hypergraph has transversal number 247.  A segment-interior-preserving
bounded six-piece lift of that source is impossible.  These statements do
not exclude a global regeneration packet or a different auxiliary factor.

The exact remaining downstream theorem is therefore:

> **Uniform protected-regeneration gate.** Construct, for every
> regenerative odd state, one child Pascal braid which simultaneously
> clears the short-run/schedule state, the protected upper debt, and a
> noncircular common-cap compiler certificate, and exports the same joint
> state at the next odd dimension.

Central decorated-2-factor existence, separate turn rainbows, component
connectivity, ordinary Hall, and path-flow integrality do not imply this
gate.

## 10. Proved and conditional boundary

Proved here:

1. the flat-carrier restriction is refuted by the literal \(k=16\) optimum;
2. the exact schedule-aware short-run event monoid;
3. the exact fixed-segmentation protected-braid equivalence;
4. the cutwise fixed-window debt identity and its \(O(ck^2)\) state;
5. the arbitrary-width protected-ray bound;
6. coarseness of the exact compiler boundary relation;
7. the single-jump mixed-depth and balanced facet-bridge identities;
8. the conditional left-total odd-spine induction; and
9. the exact state-level reconciliation of \(k=13,14,15,16\).

Conditional or open:

1. the corrected Decorated Middle Levels 2-Factor Theorem in all
   dimensions;
2. bounded component/block supply for its physical lift;
3. a uniformly left-total odd-to-even or odd-to-odd Pascal relation;
4. bounded compiler adhesion, guarded-flow preservation, or atomic-pressure
   preservation under that lift; and
5. any all-\(k\) conclusion beyond the already authenticated dimensions.

## 11. Authoritative dependencies

The proof uses the exact scopes of:

* `MATH_THEOREM_CATALAN_DECORATED_TWO_FACTOR_MINIMAL_TRACE_TARGET_20260731.md`;
* `MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md`;
* `MATH_THEOREM_CATALAN_TERMINAL_DECORATION_AND_RSB_JOINT_TRANSITION_20260731.md`;
* `MATH_THEOREM_AD_RSB_DEPTH2_EROSION_DELTA_REGENERATION_GUARDS_20260731.md`;
* `MATH_THEOREM_A_BLOCK_REROOT_UPPER_SHADOW_LEDGER_20260731.md`;
* `MATH_THEOREM_MASTER_STAIRCASE_PINNED_COMMON_CAP_COMPILER_20260731.md`;
* `MATH_AUDIT_MONOTONE_DEADLINE_RUN_STAIRCASE_ARBITRARY_STARTS_20260731.md`;
* `MATH_K13_EXACT_1719_CERTIFICATE_20260728.md`;
* `MATH_K14_EXACT_3434_CERTIFICATE_20260728.md`;
* `K15_EXACT_6438_TWO_CYCLE_SEAM_CERTIFICATE_20260729.md`;
* `MATH_CERTIFICATE_K16_OPTIMAL_12873_TRUEFF_COMMONCAP_20260731.md`;
* `MATH_THEOREM_K16_SHIFTED_CHUNK_FACET_SUBSTITUTION_ANATOMY_20260731.md`;
* `MATH_THEOREM_K16_TWO_SHIFT_FACET_BRIDGE_ARITHMETIC_20260731.md`;
* `MATH_THEOREM_K16_NONFLAT_FACET_BRIDGE_PASCAL_NORMAL_FORM_20260731.md`;
* `MATH_AUDIT_K16_D3_TWO_SHIFT_FACET_BRIDGE_AND_CONDITIONAL_EVEN_LIFT_20260731.md`; and
* `MATH_THEOREM_AD_K17_K15_FOUR_SECTOR_FACTOR_AND_RETHREAD_GATES_20260731.md`.

No web search, SAT solve, or heavy enumeration was used in this theorem.
