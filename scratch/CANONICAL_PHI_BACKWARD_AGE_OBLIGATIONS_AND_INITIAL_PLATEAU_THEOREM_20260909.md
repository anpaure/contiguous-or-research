# Canonical Phi: exact backward age obligations and a forced-age plateau

Date: 2026-09-09. Status: pure proof, no execution or search.

This gives a finite backward interface for a specified history boundary and
a uniform forced-age theorem for an explicit family. It does not infer that
locally admitted histories extend to a complete middle-layer factor.

## 1. Histories, strict predecessors, and the age convention

In an odd ground set of size2s+1 with s>=1, let lower states have rank s and
upper states rank s+1. Canonical Phi adds the zero at the first global minimum of the
ones-minus-zeros prefix walk. Its inverse removes the up-step immediately
after the last global minimum, including the empty prefix.

A strict transition P→Q means `Q⊂Phi(P)` and `P≠Q`. Write

\[
\iota(P,Q)=Q\setminus P,\qquad
\delta(P,Q)=P\setminus Q.
\]

Both are singleton coordinates. The full predecessor list of Q is obtained
by taking every z outsideQ, setting `P=Phi^{-1}(Q+z)`, and excluding `P=Q`.
There are exactlys strict predecessors: Q has s+1 containing uppers, their
Phi preimages are distinct, and exactly one is Q itself.

The age of x in a lower state is the number of consecutive lower states in
which x has been present since its last insertion. A permanent coordinate
can be assigned infinite age. Residence at leastq means every closed positive
run has at leastq states. Thus P→Q is legal at a known age boundary precisely
when the age of its deleted coordinate delta is at leastq.

For finite histories with an unspecified earlier past, every run born and
closed within the displayed history must satisfy the rule; ages of runs
already present at the first displayed state must be supplied separately.

## 2. A simple exact recurrence without residence filtering

For t>=0 define A_t(Q) as the coordinates that can remain present throughout
some strict history of t transitions ending at Q. Then

\[
A_0(Q)=Q,\qquad
A_{t+1}(Q)=Q\cap\bigcup_{P\in\operatorname{Pred}(Q)} A_t(P).
\tag{2.1}
\]

Therefore `Q\A_(q−1)(Q)` is exactly the set of coordinates whose age is
necessarily less thanq over all unrestricted strict histories. This is an
individual-coordinate statement: different coordinates in A_t may use
different histories.

The corresponding universal survival sets satisfy

\[
B_0(Q)=Q,\qquad
B_{t+1}(Q)=Q\cap\bigcap_{P\in\operatorname{Pred}(Q)} B_t(P).
\tag{2.2}
\]

In the full canonical graph the predecessor sets are nonempty. Under an
additional restriction that removes histories, empty predecessor families
must be marked infeasible, rather than treated as a source of vacuous age
certificates.

Equations(2.1)–(2.2) do not impose residence on other coordinates. Applying
them unchanged to a residence-filtered problem would be unsound.

## 3. Exact backward recurrence with residence and boundary obligations

For fixed q>=2, a backward state is

\[
(Q;R_1\supseteq R_2\supseteq\cdots\supseteq R_{q-1}),
\qquad R_1\subseteq Q.
\]

The meaning is: every x in R_t must remain present for the nextt steps
backward from Q. Equivalently, the already selected suffix of the history
requires its age at Q to be at leastt+1.

To choose a strict predecessor P of Q, it is necessary and sufficient that

\[
R_1\subseteq P.
\tag{3.1}
\]

Let d=delta(P,Q), the coordinate deleted by the forward edge. The new state
has, with R_q empty,

\[
\boxed{R'_t=R_{t+1}\cup\{d\},\qquad 1\le t\le q-1.}
\tag{3.2}
\]

The old obligations decrease by one backward step. The new obligation
requires d, which is present at P, to have been present for q−1 earlier
states, making its age at the forward deletion at leastq. These are all
the constraints: no other coordinate is deleted on that edge.

Induction proves the following exact finite interface. For a prescribed
left boundary state P_* with actual ages alpha_x, a chosen reverse path is
valid if and only if every transition passes(3.1), every update is(3.2), and
the final obligations satisfy

\[
R_t\subseteq\{x\in P_*:\alpha_x\ge t+1\}
\quad(1\le t\le q-1).
\tag{3.3}
\]

This is a composable local datum: at a splice, carry the remaining nested
age requirements, rather than assuming all incoming coordinates are old.
An unspecified boundary is not permission to assign free mature ages.

To ask whether coordinatex can be deleted immediately after Q, start with
`R_t={x}` for everyt. The recurrence then checks its required age together
with all deletions in the chosen incoming history. To ask only whether Q
has any legal incoming history, start with all R_t empty.

There are finitely many such states. With no fixed left boundary, existence
of an infinite backward history is equivalent to reachability of a directed
cycle in this backward-state graph. Every individual obligation expires in
at mostq−1 steps, so such an infinite path genuinely discharges all of them.
This makes immediate deletion feasibility an exact finite decision for
arbitrary left-infinite strict residence-q walks.

It is still only a necessary local test for a complete factor. Such a walk
may revisit a named lower state, use incompatible incoming choices on
different visits, or conflict with reserved states or uppers elsewhere.
The graph does not impose a one-copy middle inventory, global connectivity,
target coverage, or a right-infinite continuation. Those are separate gates.

For q=1 there are no age obligations; every strict deletion is immediately
legal and the underlying predecessor graph is enough.

## 4. The named word family and a suffix-minimum lemma

Now use `2r+1` old positions followed by new positions a,b. Child lower states
have rankr+1. Choose r>=j>=0 and a Dyck word D of semilengthr−j. Define

\[
Q_j=0^j1^{j+1}D00.
\tag{4.1}
\]

It has length2r+3 and rankr+1, as required. Name its displayed plateau ones
`x_1,...,x_p`, where p=j+1. The final00 are the new coordinates. The Dyck
suffix may itself begin with more ones; they are not included in this named
plateau.

**Suffix-minimum lemma.** Let B be any child upper word. Suppose that from
a particular one-position x onward, B dominates the word

\[
1^mD00,\qquad m\ge1,
\]

coordinatewise. Then the inverse-Phi deletion position is at or before x,
except that when m=1 it can instead be the final coordinate b.

Proof: let h be the height immediately before x. Before the last two
positions the relative heights of `1^mD00` are strictly positive. At a they
are m−1; at b they are m−2. Turning additional zeros into ones only increases
these relative heights. If m>=2, all positions before b have height above h;
the final height of an upper word is+1, above its global minimum. No last
global minimum can occur after the position immediately before x. Its next
up-step is therefore at or before x.

For m=1 the only additional possible last-minimum position is a. To tie h
there must have been no zero-to-one change earlier in this suffix, including
a. If b remains zero, the upper's final height gives h=2, which cannot be
a global minimum. Thus the exceptional case has b=1, h=0, and the inverse
deletes b. This proves all cases of the lemma.

## 5. Uniform exact ages: the forced plateau theorem

**Theorem.** Fix q>=1 and put `m=min(q,j+1)`. In every strict history ending
at Q_j with at leastm incoming transitions, in which every positive run
born and closed within those transitions has length at leastq, one has

\[
\boxed{\operatorname{age}(x_t)=t\quad(1\le t\le m),}
\tag{5.1}
\]

and every other coordinate present at Q_j has age at leastm+1. In particular
the statement holds uniformly over all complete strict residence-q factors.

Proof by backward induction on t. Suppose the lastt−1 arrivals inserted
exactly `x_1,...,x_(t−1)` in reverse time order. At the next incoming upper B,
all Q_j ones at or after x_t remain present: none of the previously identified
inverse deletions removed them. The upper may additionally contain former
zero coordinates. Its suffix from x_t therefore dominates

\[
1^{j+2-t}D00.
\]

By the suffix lemma, inverse Phi removes x_t, an earlier plateau one, an
initial zero coordinate, or possibly the final b. A removed coordinate
equal to the just-adjoined upper coordinate would give the excluded
self-return, so any remaining case is an actual fresh forward insertion.

An initial zero or b is absent from the final Q_j. If it were inserted now,
it would have to be deleted again in fewer thant<=q subsequent steps, closing
a run shorter thanq. If an earlier plateau one x_i, i<t, were inserted now,
its later known fresh insertion yielding terminal agei would require an
intervening deletion, again closing the new run in fewer thant<=q steps.
Both alternatives are forbidden. Hence the inverse must remove x_t.

That coordinate is present in all the later t states and absent immediately
before them, so its terminal age is exactlyt. This proves the induction.
All other final coordinates survive allm backward transitions, proving their
age lower bound m+1. No global extension assumption is used.

This is slightly stronger than requiring exact ages only through q−1: when
the plateau is long enough, its q-th one has exact ageq as well.

## 6. Explicit age1/age2 cases and immediate deletion menus

For everyj>=0, the first displayed one is fresh at Q_j in every strict
history. For j>=1, all residence-at-least2 histories give the first two
displayed ones exact ages1 and2, and all other present coordinates age>=3.
For j=0 the displayed plateau has only one coordinate; the theorem gives
that coordinate age1 and all D-ones age>=2. It does not assert a fixed age
for the first D-one in arbitrary longer histories.

For comparison with the explicit two-step inverse calculation: when j=1
its only alternative inverse branch uses first added z=b and then w=u;
it inserts z and immediately deletes it. When j>=2, the analogous alternative
uses the penultimate initial zero followed by the last initial zero. These
branches explain why unfiltered strict two-step walks cannot simply be
substituted for residence-filtered histories. The theorem avoids needing
to enumerate such branches at largerq.

With the m incoming transitions required in Section5, or an actual valid
past/boundary certificate supplying them, if the displayed plateau has at
leastq−1 coordinates, (5.1) gives the
**complete immediate deletion menu** at Q_j, for every admitted residence-q
history:

\[
\boxed{\{\text{age-legal deletions at }Q_j\}
       =Q_j\setminus\{x_1,\ldots,x_{q-1}\}.}
\tag{6.1}
\]

The omitted coordinates have exact ages belowq. If p=q−1, all remaining
coordinates have age at leastq. If p>=q, the q-th plateau coordinate has
ageq and all remaining ones have age at leastq+1. Deleting any member of
the displayed menu after the fixed Phi insertion is therefore a legal
single transition, conditional on the incoming history.

If p<q−1, all plateau deletions are forbidden but the lower age bound on
the remaining D-ones is not enough for an exact menu. Equations(3.1)–(3.3)
give the appropriate further test.

## 7. An injective, age-safe head choice at the critical plateau length

For q>=3 set j=q−2, and assume r>=q−1 so D has at least one one. Write
`D=1R`. The entire displayed plateau has q−1 young coordinates; the exact
deletion menu is precisely the ones of D. In particular deleting the first
D-bit after the canonical Phi insertion gives

\[
0^{q-2}1^{q-1}D00
\longrightarrow
\boxed{0^{q-3}1^q0R00.}
\tag{7.1}
\]

The deleted D-bit has age at leastq in every admitted history. Distinct D
give distinct heads, since R is recovered from the fixed displayed prefix.
This is an explicit injective **single-edge** choice with the required age.

For q=3, the choice is `011D00 -> 1110R00`. The tempting alternative
`011D00 -> 110D00` deletes the second plateau one, whose exact age2 is
insufficient. This sharpens the earlier distinct-head injection without
claiming that freeing these heads completes a factor.

For q=2 the analogous j=0 state instead has canonical Phi add the new b;
deleting the first D-bit gives `1D00 -> 10R01`. The same age and injectivity
claims hold when D is nonempty. If no coordinate lies in the deletion menu,
there is no residence-q departure from that boundary state.

## 8. What can be passed through an induction

The reusable data are the nested backward age obligations with a genuine
boundary-age certificate, and the exact menu(6.1) for the stated family.
They allow one to verify an age-compatible splice without assuming a
particular entire incoming history. The explicit head choice(7.1) adds an
injective local allocation when the plateau has critical lengthq−1.

Neither arbitrary predecessor existence nor this injection supplies unused
middle vertices, unused incoming uppers, one-copy history consistency,
complete target coverage, or global connectivity. In particular this does
not reverse the proved obstruction to keeping the entire fixed-root
entrance bank. It specifies a valid local replacement and the exact remaining
boundary test, not an unproved all-dimensional completion.

## 9. Independent review

Root independently read and passed the complete proof. The induction-agent
[full independent audit](CANONICAL_PHI_PLATEAU_AGE_THEOREM_INDEPENDENT_AUDIT_20260909.md)
also passes Sections1–8, including the obligation recurrence and the t=q
boundary. Finite-frontier independently passed the complete note and supplied
the explicit s>=1 setup guard. The complete deletion menu retains Section5's
incoming-history-length or genuinely valid boundary requirement. No execution
was used in these reviews.
