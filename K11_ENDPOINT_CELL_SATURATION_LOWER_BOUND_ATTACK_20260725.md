# Endpoint-cell saturation in a hypothetical length-465 word

Date: 2026-07-25

## 0. Status

This note does **not** prove \(\nu(11)\ge 466\).  The certified global
interval remains

\[
\boxed{465\le \nu(11)\le 477}.
\]

It proves a new necessary condition for equality.  Fix one selected witness
for every mask in ranks one through six, and let \(u_L,u_R\in\{0,1,2,3\}\)
be the two rank-five/rank-six common-endpoint defects.  In each endpoint
colour \(q\in\{L,R\}\), at least

\[
\boxed{93-u_q}
\]

common central edges are supported by four *consecutive* nested physical
cells of lengths \(1,2,3,4\), with target ranks

\[
a<b<5<6,\qquad 1\le a<b\le4.
\]

At least \(27-u_q\) of them have the exact rank pattern

\[
\boxed{3,4,5,6}.
\]

Consequently every hypothetical length-465 word has at least

\[
\boxed{n_3\ge 27-\min(u_L,u_R)\ge24}
\]

literal rank-three entries.  Here \(n_3\) denotes the number of physical
entries of cardinality exactly three.

If the word has the unique boundary rank-six literal allowed by the audited
rank-truncation theorem, the constants improve to

\[
\boxed{96-u_q,\qquad 30-u_q,\qquad
       n_3\ge30-\min(u_L,u_R)\ge27.}
\]

The theorem couples four ingredients which had previously appeared mostly as
separate ledgers: the rank-six delay-three band, exact ownership of all 561
rank-one-through-rank-four masks, the two common-endpoint matchings, and the
short physical-cell boundary losses.  It is stronger than merely requiring
full last-occurrence depth: every one of the counted four-cells is occupied
by four *selected, globally distinct target masks*.

No solver, finite search, or probabilistic assertion is used.

## 1. Frozen equality setup

Let

\[
A=(A_1,\ldots,A_{465})
\]

be a hypothetical nonzero universal word on \([11]\).  Select one witnessing
interval for every rank-six mask.  There are

\[
M_6=\binom{11}{6}=462
\]

such intervals.  Equal-rank targets are incomparable, so their selected
intervals are pairwise nonnested.  Ordering them by left endpoint also orders
them by right endpoint.  Since \(465=462+3\), the standard endpoint-order
lemma puts the \(i\)-th selected interval inside

\[
[i,i+3].
\]

Hence every selected rank-six witness has length at most four.  Moreover,
every physical interval of length at least four contains one selected
rank-six witness: for an interval beginning at \(i\le462\), the selected
interval indexed by \(i\) lies in its first four positions.  (No length-four
interval begins after position 462.)  Therefore **every** interval whose OR
has rank at most five has length at most three.

Choose one witness for every target of ranks one through five.  All these
witnesses consequently have length at most three.  Within one fixed rank,
their left endpoints and right endpoints are distinct.

Fix one endpoint colour.  The proof below is written for right endpoints;
reversing the word proves the left version.  Let

\[
E_5,E_6\subseteq[465]
\]

be the selected right-endpoint sets for ranks five and six.  Both have size
462.  Put

\[
C=E_5\cap E_6,
\qquad |C|=462-u,
\qquad 0\le u\le3.                 \tag{1.1}
\]

At an endpoint in \(C\), the selected rank-five interval is a proper suffix
of the selected rank-six interval.  These common endpoints are exactly the
edges of the right-colour central matching.

For each endpoint \(e\), let

\[
\ell_e=
\#\{\hbox{selected witnesses of ranks }1,2,3,4
       \hbox{ ending at }e\}.                    \tag{1.2}
\]

Since every target is selected once,

\[
\sum_{e=1}^{465}\ell_e
=\sum_{s=1}^{4}\binom{11}{s}
=11+55+165+330
=561.                                             \tag{1.3}
\]

## 2. The endpoint-cell saturation theorem

Call \(e\in C\) **saturated** when \(\ell_e=2\), and let \(z_R\) be the
number of saturated right endpoints.

### Theorem 2.1

\[
\boxed{z_R\ge93-u_R.}                            \tag{2.1}
\]

The left-endpoint analogue is

\[
\boxed{z_L\ge93-u_L.}                            \tag{2.2}
\]

### Proof

There are only three suffix cells of lengths one, two, and three at an
interior endpoint.

* If \(e\in C\), the selected rank-five witness already occupies one of
  those short cells.  Hence \(\ell_e\le2\).  By definition of \(z_R\),

  \[
  \sum_{e\in C}\ell_e\le |C|+z_R.
  \tag{2.3}
  \]

* The set \(E_5\setminus C\) has size \(u\).  At such an endpoint the
  selected rank-five witness occupies one short cell, so at most two lower
  witnesses can end there.

* Exactly three endpoints are outside \(E_5\).  At each of them at most
  three lower witnesses can end.

Ignoring the beginning of the word, these observations give the preliminary
upper bound

\[
\sum_e\ell_e
\le (462-u)+z_R+2u+9
=471+u+z_R.                                      \tag{2.4}
\]

The first two physical endpoints force three units of additional loss.

At endpoint 1, membership in \(C\) is impossible: there is only one nonempty
suffix interval, so two distinct ranks cannot be represented there.  If
\(1\in E_5\setminus C\), the rank-five singleton leaves no lower cell,
whereas (2.4) allowed two.  If \(1\notin E_5\), there is only one physical
suffix cell, whereas (2.4) allowed three.  Thus endpoint 1 saves two units in
all cases.

At endpoint 2, if \(2\in C\), the distinct rank-five and rank-six witnesses
occupy both suffix cells, so no lower witness ends there; (2.3) allowed one.
If \(2\in E_5\setminus C\), at most one lower cell remains although (2.4)
allowed two.  If \(2\notin E_5\), only two suffix cells exist although
(2.4) allowed three.  Thus endpoint 2 saves one further unit in all cases.

Combining these losses with (1.3)--(2.4) gives

\[
561\le468+u+z_R,
\]

which is (2.1).  Reversal proves (2.2).  \(\square\)

### Theorem 2.2 (exact four-cell form)

Every saturated endpoint in Theorem 2.1 carries exactly the four suffix
cells of lengths \(1,2,3,4\).  Their selected target ranks are

\[
\boxed{a,b,5,6\quad\hbox{with}\quad1\le a<b\le4.} \tag{2.5}
\]

In particular the rank-five witness has length three and the rank-six
witness has length four.

### Proof

At a saturated common endpoint there are four distinct selected intervals:
two lower-rank intervals, the rank-five interval, and the rank-six interval.
The first three have length at most three and the last has length at most
four.  Four distinct suffix intervals under these caps must be exactly the
suffixes of lengths \(1,2,3,4\).  Physical containment strictly increases
the OR rank, proving (2.5).  \(\square\)

Thus (2.1) is not only an activity count.  It supplies at least \(93-u_R\)
literal four-step suffix flags, and (2.2) supplies the analogous prefix
flags.  Since a rank-five/rank-six target pair cannot share both physical
endpoints, the left- and right-colour matching edges are disjoint.  Therefore
the central forest contains at least

\[
\boxed{(93-u_L)+(93-u_R)=186-c}                 \tag{2.6}
\]

distinct saturated coloured edges, where \(c=u_L+u_R\) is its component
count.  Since \(c\le6\), there are at least 180.

## 3. Exact rank-pattern and literal-rank consequences

For one endpoint colour, let \(z_{ab}\) count the saturated flags whose two
lower ranks are \(a<b\).  Then

\[
\sum_{1\le a<b\le4}z_{ab}=z.                   \tag{3.1}
\]

Every saturated flag other than type \((3,4)\) uses a selected target of
rank one or rank two.  There are only

\[
\binom{11}{1}+\binom{11}{2}=11+55=66           \tag{3.2}
\]

such targets, and selected targets have distinct same-rank endpoints.
Consequently

\[
\boxed{z_{34}\ge z-66\ge27-u.}                 \tag{3.3}
\]

For a right type-\((3,4)\) flag ending at \(e\), the four cumulative suffix
ORs have the form

\[
C,\quad C\cup\{x\},\quad C\cup\{x,y\},\quad
C\cup\{x,y,z\},                                \tag{3.4}
\]

where \(|C|=3\) and \(x,y,z\) are distinct coordinates outside \(C\).
In particular

\[
A_e=C
\]

is a literal rank-three entry.  Distinct flags of one endpoint colour use
distinct physical endpoints and distinct selected rank-three targets.  The
left-colour statement is symmetric.  Hence

\[
\boxed{
n_3\ge\max\{27-u_L,27-u_R\}
=27-\min(u_L,u_R)\ge24.}                        \tag{3.5}
\]

The two colours together give at least

\[
\boxed{(27-u_L)+(27-u_R)=54-c}                  \tag{3.6}
\]

distinct central-forest edges carrying exact selected
rank-\(3,4,5,6\) physical flags.  Their literal rank-three endpoints can
overlap between the two colours, so (3.5), not the sum in (3.6), is the valid
unconditional entry-count conclusion.

## 4. Strengthening in the boundary rank-six-literal branch

Assume now that the word contains the unique literal rank-six entry allowed
by rank truncation.  The audited boundary-rigidity theorem places it at a
word endpoint.  Delete it.  Every target of ranks at most five survives in a
contiguous word of length 464.

Select one witness for every rank-five target in this compressed word.  With
462 equal-rank targets in 464 positions, the endpoint-order lemma gives
length at most three for rank-five witnesses and length at most two for every
rank-one-through-rank-four witness.

Fix right endpoints in the compressed word.  Let \(E_5\) be the 462 selected
rank-five endpoints, and let \(z\) count those carrying two selected lower
witnesses.  At an endpoint in \(E_5\), the number of lower companions is at
most two, and it is at most one unless the endpoint is counted by \(z\).  At
either of the two endpoints outside \(E_5\), at most two lower witnesses can
end.  This gives the preliminary capacity

\[
\sum_e\ell_e\le462+z+4.
\]

At endpoint 1, either a selected rank-five singleton leaves no lower cell or,
if rank five is absent, only one of the two provisionally allowed lower cells
exists.  Thus one unit is always lost, and

\[
561\le465+z.
\]

Therefore

\[
\boxed{z\ge96.}                                  \tag{4.1}
\]

The boundary rank-six singleton is isolated from both central endpoint
matchings.  All other selected rank-six witnesses survive the deletion, and
the rank-five/rank-six common endpoint matching has size \(462-u_q\).  At
most \(u_q\) of the 96 saturated rank-five targets are unmatched.  Every
matched one extends its length-three rank-five witness properly to a
rank-six witness of length at most four, and hence to length exactly four.
Thus, for each colour,

\[
\boxed{z_q^{(6)}\ge96-u_q.}                     \tag{4.2}
\]

Repeating the 66-target argument from Section 3 gives

\[
\boxed{z_{34,q}^{(6)}\ge30-u_q}                 \tag{4.3}
\]

and therefore

\[
\boxed{n_3\ge30-\min(u_L,u_R)\ge27.}           \tag{4.4}
\]

Since the singleton is unmatched in both colours, \(u_L,u_R\ge1\), while
the inherited component bound still gives \(u_L,u_R\le3\).  Summing the two
colours yields at least

\[
\boxed{192-c\ge186}                             \tag{4.5}
\]

saturated central edges and at least

\[
\boxed{60-c\ge54}                               \tag{4.6}
\]

exact rank-\(3,4,5,6\) flagged edges.

## 5. Conversion to genuine reservoir turns

The preceding flags can be coupled to the two-token reservoir, but one must
pay for forest endpoints and for the three units of rank-five endpoint-gap
slack.  This section records the exact conversion and also explains why it
still leaves room.

Consider a right type-\((3,4)\) saturated flag ending at position \(e\).
Write its four selected intervals and masks as

\[
 C=[e,e],\qquad K=[e-1,e],\qquad
 P=[e-2,e],\qquad Q^-=[e-3,e],                 \tag{5.1}
\]

of ranks \(3,4,5,6\), respectively.  Here and below the same letter denotes
an interval and its OR mask when no confusion is possible.

Assume that the rank-five vertex \(P\) has degree two in the central forest.
Its other incident rank-six witness \(Q^+\) shares the left endpoint of
\(P\).  Since \(P\) has length three, \(Q^+\) properly contains it, and every
rank-six witness has length at most four, necessarily

\[
Q^+=[e-2,e+1].                                  \tag{5.2}
\]

Let \(P^+\) be the other rank-five neighbour of \(Q^+\).  It shares the
right endpoint \(e+1\) and has length at most three.  Put

\[
p^+=|P^+|_{\rm interval}-1\in\{0,1,2\}.
\]

The right endpoints of \(P\) and \(P^+\) are consecutive physical
positions.  Hence they are consecutive in the global rank-five witness
order.  Their left-endpoint gap excess is exactly

\[
 \ell(P^+)-\ell(P)-1
 =2-p^+.                                        \tag{5.3}
\]

If \(p^+=2\), then \(P^+=[e-1,e+1]\).  Its physical overlap with \(P\)
is the interval \([e-1,e]\), whose OR is \(K\).  Since two distinct
five-set facets of \(Q^+\) intersect in a four-set,

\[
\boxed{K=P\cap P^+.}                            \tag{5.4}
\]

Thus \(K\) is a genuine lower turn colour of the reservoir path.  At the
same internal source vertex,

\[
\boxed{H=Q^-\cup Q^+}                           \tag{5.5}
\]

is a genuine rank-seven upper turn colour, represented physically by the
hull interval \([e-3,e+1]\).

If \(p^+<2\), equation (5.3) consumes at least one unit of left-endpoint gap
excess.  The 462 selected rank-five left endpoints lie in 465 positions, so

\[
\sum_{i=0}^{460}
 \bigl(\ell(P_{i+1})-\ell(P_i)-1\bigr)\le3.     \tag{5.6}
\]

Distinct right saturated flags give distinct consecutive pairs
\((P_i,P_{i+1})\).  Therefore at most three internal right flags fail
(5.4).  The reversed argument says that at most three internal left flags
fail their analogous turn realization.

The central forest has \(924-c\) edges.  On its 462 rank-five vertices the
total degree deficiency from degree two is

\[
2\cdot462-(924-c)=c.                            \tag{5.7}
\]

Consequently at most \(c\) rank-five vertices have degree below two.
For a right flag, the rank-five vertex \(P\) can fail to have its other
left-colour edge at at most \(u_L\) targets.  Even when that edge exists, the
new rank-six vertex \(Q^+\) can fail to have its outgoing right-colour edge
to \(P^+\) at at most \(u_R\) targets.  Thus at most
\(u_L+u_R=c\) right flags fail before the gap test.  The left-colour argument
is symmetric.  Combining this observation with (3.3) and (5.6) proves:

### Theorem 5.1 (marked reservoir turns)

In an arbitrary length-465 equality branch, the number of exact
rank-\((3,4,5,6)\) flags which convert to the adjacent genuine turn pair
\((K,H)\) in (5.4)--(5.5) is at least

\[
\boxed{24-u_R-c}
\]

in the right colour and at least

\[
\boxed{24-u_L-c}
\]

in the left colour.  Hence the two-token path system contains at least

\[
\boxed{48-3c\ge30}                              \tag{5.8}
\]

such marked coloured turns.

In the boundary rank-six-literal branch, work after deleting the literal
endpoint.  The 462 rank-five endpoints then lie in 464 positions, so the
right side of (5.6) is two rather than three.  Equations (4.3) and (5.7)
give at least

\[
\boxed{28-u_R-c,\qquad28-u_L-c}

\]

marked turns in the two colours, and therefore at least

\[
\boxed{56-3c\ge38}                              \tag{5.9}
\]

in total.

These turns are now expressed directly in the reservoir notation: \(K\) is
one of the lower \(B\)-colours, while the complement of \(H\) is one of the
upper \(Y\)-colours.  The selected \(K\)-colours are distinct within each
endpoint colour.  The rank-three pin is literal, namely \(C=A_e\), and the
three successive one-coordinate increments in (3.4) are the physical
recency increments behind the two-token update.

### Component capacity and why it does not yet contradict equality

Let a reservoir component contain \(t\) rank-five states and let \(i_5\) of
them have degree two.  A marked right or left flag is based at one such
internal state.  At most two marked flags, one of each endpoint colour, can
be based at the same state; if both occur, they share the same upper turn
colour \(H=Q^-\cup Q^+\) but use two different lower endpoint colours.
If \(h\) is the number of distinct marked turn states and \(g\) is the
number of coloured flags supported by the component, then the exact local
capacity statement is

\[
\boxed{
\left\lceil\frac g2\right\rceil\le h\le g,
\qquad h\le i_5,
\qquad g\le2i_5.}                              \tag{5.10}
\]

Nonrepetition of the physical lower and upper turn *occurrences* does not
improve (5.10): two opposite-colour flags at one state describe one upper
turn occurrence and two distinct lower colours, not two repeated upper
occurrences.
Pigeonhole applied to (5.8)
shows that some one of the \(c\) components carries at least

\[
\left\lceil\frac{48-3c}{c}\right\rceil
\]

marked flags (and in the literal branch at least
\(\lceil(56-3c)/c\rceil\)).  However a long alternating component has far
more internal rank-five states than this.  Thus (5.10) does **not** force a
repeated rank-four or rank-seven colour.  A contradiction needs a stronger
fact tying marked flags to a much smaller subset of reservoir states, or a
cross-component pin collision.

This identifies the precise limit of the present coupling: the three units
of endpoint gap slack can hide at most three non-turn flags per direction,
but the remaining genuine turns still fit comfortably inside the abstract
two-token component capacities.

### Theorem 5.2 (a 38-state local countermodel)

No theorem using only one-component reservoir dynamics, the endpoint side,
and nonrepetition of the marked rank-four and rank-seven colours can bound a
component by 35 marked states.  In fact, there is one literal physical
rank-\(3/4/5/6\) fragment with 38 internal rank-five states, each supporting
both endpoint-colour flags, such that all 76 marked rank-four colours and all
38 marked rank-seven colours are distinct.

### Proof

Split the coordinates as

\[
[11]=U\mathbin{\dot\cup}\{p,q,r\},
\qquad |U|=8.                                   \tag{5.11}
\]

Use the proved smaller-layer-saturating cycle in the rank-three/rank-four
inclusion graph of \(B_U\).  It contains an alternating cycle

\[
T_0,W_0,T_1,W_1,\ldots,T_{55},W_{55},T_0,       \tag{5.12}
\]

where all \(T_i\in\binom U3\) are distinct, all
\(W_i\in\binom U4\) are distinct, and

\[
W_i=T_i\cup T_{i+1}.                            \tag{5.13}
\]

Take the first 41 rank-three vertices and the first 40 intervening
rank-four vertices.  For \(0\le i<40\), set

\[
x_i=
\begin{cases}
p,&i\equiv0\pmod3,\\
q,&i\equiv1\pmod3,\\
r,&i\equiv2\pmod3.
\end{cases}                                     \tag{5.14}
\]

Emit the literal word fragment

\[
T_0,\{x_0\},T_1,\{x_1\},\ldots,
T_{39},\{x_{39}\},T_{40}.                      \tag{5.15}
\]

Its consecutive triple ORs alternate between

\[
P_i=W_i\cup\{x_i\}\qquad(0\le i<40)           \tag{5.16}
\]

and

\[
R_i=T_{i+1}\cup\{x_i,x_{i+1}\}
\qquad(0\le i<39).                              \tag{5.17}
\]

Every one is a five-set.  The \(P_i\)'s contain one reserved coordinate and
the \(R_i\)'s contain two, so the two classes are disjoint.  Within each
class, equality would repeat a \(W_i\), or repeat both a \(T_{i+1}\) and its
period-three reserved pair.  Thus all 79 rank-five states are distinct.

The consecutive four-window ORs alternate between

\[
W_i\cup\{x_i,x_{i+1}\}
\quad\hbox{and}\quad
W_{i+1}\cup\{x_i,x_{i+1}\}qquad(0\le i<39).   \tag{5.18}
\]

They are six-sets.  If two such sets had different reserved pairs they could
not be equal.  With the same pair, equality would repeat one of the distinct
\(W_j\)'s.  The only possible cross-index shift would change the residue
class modulo three, and hence changes the reserved pair.  Therefore all 78
rank-six states are distinct.  Equations (5.16)--(5.18) consequently form
one simple alternating middle-level path and automatically obey the
two-token recurrence and its no-lazy conditions.

For every \(1\le i\le38\), the triple window

\[
T_i,\{x_i\},T_{i+1}                             \tag{5.19}
\]

has an exact \((3,4,5,6)\) flag at both ends.  Its two marked rank-four
colours are

\[
K_i^L=T_i\cup\{x_i\},
\qquad
K_i^R=T_{i+1}\cup\{x_i\}.                      \tag{5.20}
\]

All 76 are distinct.  Indeed, a colour determines its reserved coordinate;
after removing that coordinate it determines its unique \(T_j\).  The only
\(T_j\) used twice is shared by consecutive flags, where the two reserved
coordinates are \(x_{j-1}\ne x_j\).

The two adjacent rank-six states around (5.19) add \(x_{i-1}\) and
\(x_{i+1}\), respectively.  These are distinct from each other and from
\(x_i\).  Their upper hull is therefore

\[
H_i=W_i\cup\{p,q,r\}.                           \tag{5.21}
\]

The \(W_i\)'s are distinct, so the 38 marked rank-seven colours \(H_i\) are
distinct as well.

Thus one component fragment contains 38 actual marked turn states and 76
coloured endpoint flags without a marked rank-four or rank-seven collision.
\(\square\)

The number 38 is not claimed to be the maximum possible.  Its role is
decisive for this attack: the desired all-component capacity below 36 is
false even for a literal physical fragment.  Any successful contradiction
must use completion to all 462 middle states, interaction between different
components or sectors, or the global ownership of ranks outside the marked
fragment.  No invariant of a single two-token state and its two turn colours
can supply the missing lower bound.

## 6. Relation to the existing equality template

The endpoint-saturation theorem previously guaranteed at least 93 selected
rank-six witnesses of maximum length and maximum last-occurrence depth.  The
present result is different: after paying the exact matching defect \(u_q\),
it proves that almost the same number of common rank-five/rank-six edges have
*all three lower physical cells occupied by selected target witnesses*.

The familiar consecutive-rank count \(27-u_q\) follows here from the sharper
four-cell occupancy count and the exact small-layer budget \(11+55=66\).
The new literal consequence (3.5), and its boundary-branch strengthening
(4.4), can be added directly to any unrestricted equality encoding as the
rank-histogram cuts

\[
n_3\ge27-\min(u_L,u_R)
\]

and

\[
n_3\ge30-\min(u_L,u_R)
\quad\hbox{when the rank-six literal is present}.
\]

These conditions do not contradict the current scalar profiles.  They expose
a more specific remaining obstruction: a length-465 word must realize at
least 180 selected four-cell flags (at least 186 in the literal branch), with
their shortest cells tied to globally owned low-rank masks, while also
realizing the already proved two-sided rank-four/rank-seven shadow system.
No current purely scalar or parity inequality proves those requirements
incompatible.

## 7. Exact conclusion

The attempted lower-bound strengthening stops at a structural theorem:

\[
\boxed{465\le\nu(11)\le477}
\]

remains the certified interval.  Any proof of \(\nu(11)\ge466\) must use
information beyond the one-dimensional endpoint capacities proved here,
most plausibly a collision or pin-survival obstruction coupling the
\(186-c\) saturated central edges to their opposite-endpoint shadows.
