# Odd APH: temporary-cart resource dichotomy and uniform compound closure

**Date:** 2026-08-06  
**Scope:** the Anchored Pre-Head Bootstrap lemma `APH` from
`MATH_AUDIT_ODD_PACKAGE_DEPENDENCY_CLOSURE_20260806.md`  
**Method:** a punctured linear-word resource theorem, anchored one-head
transport, and a temporary-cart scheduling argument; no computation or
search  
**Verdict (superseded by independent audit):** **DO NOT CITE THE APH
CLOSURE CLAIM.**  The abstract resource dichotomy and the displayed endpoint
identities survive, but the occurrence-labelled construction is false as
written.  Exact cross-source collisions occur before the proposed records
are installed, and the three global composition joins are not supplied by
the cited dependencies.  See
`MATH_AUDIT_ODD_APH_TEMPORARY_CART_DICHOTOMY_20260806.md`, SHA-256
`2a33e7b1019a88ccb57eff11041f1394405f5c044f3180933e6e0c6f2c63cb1a`.
The proof-safe reusable content here is the resource dichotomy and literal
endpoint algebra only; APH remains open.

## 1. Punctured suffix and atoms

Use

\[
 A=00,\qquad B=20,\qquad C=22,\qquad H=02,\qquad M=11.
\tag{1.1}
\]

Delete the protected first connector `p_1` from a balanced cyclic connector
word.  The remaining work suffix is a linear word \(w\) satisfying

\[
                       |\#A(w)-\#C(w)|\le 1.
\tag{1.2}
\]

An **ordinary head atom** is either

* a transition segment `A B^s C` or `C B^s A`; or
* an adjacent neutral pair `B B`.

The literal paths in
`MATH_THEOREM_ODD_SOURCE_INTERNAL_DOUBLE_HEAD_BOOTSTRAP_20260806.md`
turn either atom into two heads, at zero signed charge and without using the
protected first connector.

Delete the `B`'s from \(w\), retaining the order of the remaining extremes;
call the result \(\bar w\).  A transition edge of \(\bar w\) represents the
corresponding transition atom in \(w\).

## 2. Exact punctured resource dichotomy

### Theorem 2.1 (two atoms or one bounded four-extreme atom)

Let \(w\) be a linear word of length at least ten satisfying (1.2).  Then at
least one of the following holds.

1. \(w\) contains two block-disjoint ordinary head atoms.
2. \(w\) contains four consecutive vertices of \(\bar w\) of type `AACC` or
   `CCAA`, and the physical interval from the first to the fourth contains at
   most nine connector blocks.

#### Proof

Consider the transition edges of the binary path \(\bar w\).

If their matching number is at least two, two matched transition edges give
two block-disjoint transition atoms in \(w\).

Suppose their matching number is at most one.  If both extreme multiplicities
are at least two, then \(\bar w\) cannot have zero transitions.  It cannot
have three transition edges, since the first and third would be disjoint.
It also cannot have exactly two: the two edges must share their middle
vertex, so the middle colour run has size one and is the only run of that
colour, contradicting that both colour multiplicities are at least two.
Hence there is exactly one transition, and

\[
                    \bar w=A^pC^q\quad\hbox{or}\quad C^pA^q,
                    \qquad p,q\ge2.
\tag{2.1}
\]

Take the last two extremes on the first side of the transition and the first
two on the second.  Write \(g_1,g_2,g_3\) for the three intervening `B`-run
lengths.  If \(g_1\ge2\) or \(g_3\ge2\), an adjacent `BB` in that run is
disjoint from the transition atom, giving outcome 1.  If \(g_2\ge4\), that
one run contains two disjoint `BB` atoms, again giving outcome 1.  Otherwise

\[
                         g_1\le1,\qquad g_2\le3,\qquad g_3\le1,
\]

so the four-extreme interval has length at most

\[
                           4+1+3+1=9.
\]

This is outcome 2.

It remains to consider \(\min(\#A,\#C)\le1\).  By (1.2), \(\bar w\) has at
most three vertices, so the `B`'s lie in at most four linear runs.  If there
are not two disjoint adjacent `BB` pairs, then

\[
                     \sum_i\left\lfloor |G_i|/2\right\rfloor\le1.
\]

At most one run then has length two or three, and every other run has length
at most one.  Thus there are at most \(3+1+1+1=6\) copies of `B`, and

\[
                           |w|\le 6+3=9,
\]

contrary to the hypothesis.  Hence outcome 1 holds.  \(\square\)

The threshold ten is immaterial for an asymptotic theorem.  The finitely many
smaller semilengths can be absorbed into the finite base of a same-parity
induction.  The point is that puncturing at `p_1` does not create an
unbounded resource exception.

## 3. A private-trail one-head lemma

The raw one-head paths are

\[
\begin{array}{rcl}
 A|H&:&0002\to0011\to0101\to0110\to0200=H|A,\\
 B|H&:&2002\to2011\to1111\to0211\to0220=H|B,\\
 C|H&:&2202\to2112\to1212\to1122\to0222=H|C.
\end{array}
\tag{3.1}
\]

The only additional crossing needed at an atom origin is

\[
 M|H:
 1102\to1012\to0112\to0121\to0211=H|M.
\tag{3.2}
\]

Its reverse moves the mobile head right through a marked atom gap.  Every
strict state in (3.2) has a boundary marker outside the raw alphabet.

### Lemma 3.1 (anchored private-trail transport)

Convert one ordinary atom to two heads.  Leave the head farther from the
fixed right collar stationary.  If the atom produced an \(M^s\) gap between
that stationary head and the mobile head, first move the mobile head through
the gap using (3.2).  Then move it monotonically right through a still-raw
interval using the reverses of (3.1).

The resulting literal paths are source-disjoint.  At every macro or strict
state the stationary head, the private \(M^s\) trail, and the current local
state recover the atom origin, the number of completed crossings, and the
source word.

#### Proof

At a macro checkpoint the stationary and mobile heads delimit, in order,
the private \(M^s\) trail and the crossed raw prefix.  The selected atom type
and orientation recover its two source extremes, while replacing the trail
by the corresponding `B` gap recovers the source at the origin.  Every
completed swap preserves the order of the crossed raw blocks.

At a strict state, start at the stationary head, skip its recorded private
trail, and scan toward the collar.  Before the active window all blocks are
raw.  In the `A` and `C` rows of (3.1), the first nonraw value locates the
active window.  In the `B` row the only ambiguous values are one or two
copies of \(M\); they occur at the first nonraw boundary after the crossed
raw prefix.  If that boundary is adjacent to the private trail, its excess
over the recorded trail length is one or two and gives the microstep.
Equation (3.2) has the same endpoint-trail decoder.  Local mass, atom
orientation, and simplicity of the displayed path then recover the exact
microstep.  Inverting that step and the completed swaps recovers the unique
source.  \(\square\)

This lemma is stronger than the raw-interval statement in the earlier APH
audit exactly where needed: it allows the \(M^s\) gap created by the atom
itself.  It does not permit unrelated old `M` or tag banks in front of the
mobile head.

## 4. Two atoms create a source-independent temporary cart

Assume outcome 1 of Theorem 2.1.  Order the two atoms by distance from the
fixed right collar, calling them far and near.

1. Bootstrap the far atom.  Leave one head stationary and move the other
   right, through the still-raw tape, until it is immediately outside the
   fixed collar.
2. The moving head swaps through every block of the near atom, so that atom
   is translated by one block but its internal order and contiguity are
   unchanged.  Bootstrap it at the translated address, leave one head
   stationary, and move the other right until it is immediately to the left
   of the first mobile head.

The two mobile heads now form

\[
                              H|H
\tag{4.1}
\]

at one fixed, source-independent collar berth.  The two stationary origin
heads and their private trails retain both displaced atom records.

### Lemma 4.1 (decoder for the two-atom assembly)

The complete assembly in steps 1--2 is occurrence-labelled and leaves the
protected `p_1` row unchanged.

#### Proof

Lemma 3.1 decodes the far transport.  At its endpoint, the stationary far
trail and the mobile collar head recover the original word and hence the
deterministically selected translated near atom.  During the bounded near
bootstrap, those two fixed records locate the active atom support; the
literal atom paths and their orientation distinguish its microstep.  The
near transport then has its own private-trail decoder from Lemma 3.1.  Its
interval lies to the right of the far stationary origin and stops before the
parked far mobile head, so it meets no unrelated nonraw block.  All supports
lie in the punctured work suffix, hence `p_1` is untouched.  \(\square\)

The temporary cart may pass an isolated stationary origin head.  Literally,
an `HH` cart adjacent to an isolated `H` gives one maximal run `HHH`; passing
the sentinel only changes which adjacent two members are regarded as the
cart.  Suppress the duplicated macro checkpoint.  Before and after it, the
ordinary two-step double-head swap has one fixed head.  The private origin
record and deterministic sweep order identify the crossed sentinel.  Thus
the double-head visible-cart theorem extends to these finitely many protected
stationary sentinels without a new state or edge.

## 5. The noncircular schedule

On the two-atom face, perform the odd setup in the following order.

1. Assemble the temporary fixed-berth cart (4.1).
2. Use it for the marked/LIFO bulk serialization.  Treat the two private
   origin trails as protected atom supports.
3. Use the same cart to supply every formerly missing non-guardable crossing
   in Conditional Theorem 5.1 of
   `MATH_THEOREM_ODD_COLLAR_FIRST_DOUBLE_HEAD_SCHEDULING_20260806.md`.
   This creates the **permanent** connector-lattice double head at `p_1`.
4. Finalize the ordinary tape to the target alphabet under the permanent
   head.  Return the temporary mobile heads in near-to-far order through the
   target tape, using the complemented versions of Lemma 3.1.  Reunite each
   with its stationary origin head and reverse the atom retirement path.
5. Apply connector beta and the already proved monotone terminal
   accumulator with the permanent head.

The order in step 4 is forced.  The near mobile does not cross the far origin.
After the near atom is restored to its complemented target, the far mobile
crosses that now-raw target atom and then reaches its own origin.  Hence no
mobile return meets a foreign private trail.

### Theorem 5.1 (APH on the two-disjoint-atom face)

Assume the already proved literal atom paths, double-head visible-cart
theorem, marked/LIFO bulk theorem, connector beta, and monotone terminal
accumulator.  If the punctured work suffix has two block-disjoint ordinary
head atoms, then the Anchored Pre-Head Bootstrap lemma holds.

#### Proof

Lemmas 3.1 and 4.1 construct the fixed-berth temporary cart before any bulk
tag or protected residual is written.  Therefore the implication cycle

\[
  \text{fixed head}\Rightarrow\text{tagged tape}
     \Rightarrow\text{fixed-head setup}
\]

is broken: the first head is supplied directly from untouched source atoms.
Once it exists, every hypothesis of the marked/LIFO and conditional
fixed-collar theorems is available.  The latter produces a permanent head
independent of the temporary atom records.  The target-oriented inverse
private-trail paths retire the two temporary atoms without touching `p_1`.
The permanent head then supplies connector beta and the post-beta theorem.
Every stage has the decoder stated in the cited theorem or in Lemmas 3.1 and
4.1.  \(\square\)

## 6. The bounded compound face has a uniform four-head construction

By Theorem 2.1, the only asymptotic source face not covered by Theorem 5.1
contains a physical interval of at most nine blocks whose reduced extremes
are `AACC` or `CCAA`.  It is enough to treat the first orientation; the
second is its spatially reflected/complemented version.

Write the source interval as

\[
                 A B^u A B^v C B^w C,
        \qquad u,w\le1,\quad v\le3,
\tag{6.1}
\]

and put

\[
                         D=B^uM^vB^w.
\tag{6.2}
\]

Bootstrap the middle opposite pair by the source-internal theorem:

\[
 A B^u A B^v C B^w C
       \longrightarrow
 A B^u H H M^v B^w C.
\tag{6.3}
\]

Move this first double head right through \(M^vB^wC\).  The order of the
crossed blocks is preserved, so

\[
 A B^u H H M^v B^w C
       \longrightarrow
 A D C H H.
\tag{6.4}
\]

Now move the train \(C|HH\) left through \(D\).  One step through a block
\(Y\in\{B,M\}\) is

\[
             Y|C|HH\longrightarrow C|Y|HH
                    \longrightarrow C|HH|Y.
\tag{6.5}
\]

During the first arrow the old `HH` is a fixed sentinel.  During the second
arrow, the visible double head moves left through \(Y\), while the just moved
`C` fixes the side of the active window.  Iterating (6.5) gives

\[
                         A D C H H
             \longrightarrow A C H H D.
\tag{6.6}
\]

Convert the now adjacent outer `A|C` while the old head remains fixed:

\[
                         A C H H D
             \longrightarrow H H H H D.
\tag{6.7}
\]

Regard the left pair in (6.7) as the new stationary origin head and the
right pair as the old, now mobile, head.  Move the latter right through
\(D\):

\[
                         HH_{\rm new}HH_{\rm old}D
             \longrightarrow HH_{\rm new}DHH_{\rm old}.
\tag{6.8}
\]

There are two small pieces of information which (6.8) by itself forgets.
First, four literal heads do not remember whether the source orientation was
AACC or CCAA.  Before exporting the old mobile head, change the new
stationary pair by one literal edge to

\[
 R_+=H|M\quad\hbox{for AACC},\qquad
 R_-=M|H\quad\hbox{for CCAA}.
\tag{6.9}
\]

Both have mass four and contain a stationary literal head.  They are
distinct from the raw alphabet and from one another.

Second, when \(v=0\) and \(u+w=1\), the word
\(D=B^uM^vB^w\) forgets on which side the lone \(B\) occurred.  Keep the
standard construction above when \(w=1\); its exported origin record is

\[
                         R_\pm|B|HH_{\rm mobile}.
\tag{6.10}
\]

When \(u=1,w=0,v=0\), use instead the following reflected train order:

\[
\begin{aligned}
 A B A C C
 &\longrightarrow A B HH_{\rm old} C\\
 &\longrightarrow HH_{\rm old} A B C\\
 &\longrightarrow HH_{\rm old} B A C\\
 &\longrightarrow HH_{\rm old} B HH_{\rm new}\\
 &\longrightarrow B HH_{\rm old}HH_{\rm new}\\
 &\longrightarrow B R_\pm HH_{\rm mobile}.
\end{aligned}
\tag{6.11}
\]

The old head is the stationary record and the new head is the mobile cart.
Every arrow is respectively the middle bootstrap, double-head transport,
an outer-\(A\) swap guarded by the old head, the guarded
\(A|C\to HH\) path, one double-head swap through \(B\), and the one-edge
record write.  Thus the lone-left-\(B\) record is

\[
                         B|R_\pm|HH_{\rm mobile},
\tag{6.12}
\]

which is literally different from (6.10).  If \(v>0\), the \(M^v\) run
separates \(B^u\) from \(B^w\); if \(u=w\), no side bit is needed.
Consequently (6.9)--(6.12) are a persistent injective origin record in every
case.  The exported pair is an occurrence-labelled temporary cart and may
continue through the still-raw suffix to the fixed collar berth.

### Lemma 6.1 (compound checkpoint decoder)

Every macro and strict state in (6.3)--(6.8) recovers the source interval,
its physical address, the active substep, and the orientation of (6.1).

#### Proof

During (6.3), the growing \(M\)-trail locates the unique middle transition;
the fixed outer `A,C`, together with \(u,w\le1\), recover the support.  The
strict states of `B|C -> C|M` contain the displayed nonraw marker, and the
final `A|C -> HH` path is simple.

At a checkpoint of (6.4), the word has the normal form

\[
                  A B^u P|HH|S,
             \qquad PS=M^vB^wC.
\tag{6.13}
\]

The visible head gives the split \(P|S\), and concatenation recovers
\(v,w\).  At a checkpoint of (6.5)--(6.6), it has the normal form

\[
                  A P|C|HH|S,
             \qquad PS=D.
\tag{6.14}
\]

Again the head and the adjacent `C` give the split and recover \(u,v,w\).
At strict states, the unchanged head in the first arrow of (6.5), or the
unchanged `C` and one visible head in the second, locates the active token
path.  Its endpoint type is determined by the next symbol of \(D\), and its
chosen simple path determines the microstep.

Equation (6.7) has the old fixed head immediately beside its simple
`A|C -> HH` path.  After (6.7), the stationary left pair and \(D\) give the
provisional origin geometry at every state of (6.8).  The record \(R_\pm\)
then gives the source orientation.  The \(M\)-separator gives \(u,w\) when
\(v>0\), while (6.10) and (6.12) give the lone-\(B\) side when
\(v=0,u+w=1\).  Every strict state of the alternative path (6.11) has the
old fixed head or the newly created head immediately beside its active
window.  Therefore the record, geometry, and simple local path recover the
source and microstep throughout the later outward transport.  Two different
sources or stages cannot meet.  \(\square\)

## 7. Exact reverse to the complemented source

First consider every branch except the lone-left-\(B\) branch (6.11).

After the permanent `p_1` head has been installed and the ordinary work tape
has been finalized to the target alphabet, return the old mobile head to the
right end of \(D\).  Restore \(R_\pm\) by its one-edge inverse to
\(HH_{\rm new}\), and reverse (6.8):

\[
              HH_{\rm new}DHH_{\rm old}
                 \longrightarrow HH_{\rm new}HH_{\rm old}D.
\tag{7.1}
\]

Retire the **new** left pair by the explicit complemented path
\(HH\to C|A\), keeping the old right pair fixed:

\[
              HH_{\rm new}HH_{\rm old}D
                 \longrightarrow C A HH_{\rm old}D.
\tag{7.2}
\]

Reverse the train move (6.5), now with the complemented outer letters:

\[
                         C A HH D
             \longrightarrow C D A HH.
\tag{7.3}
\]

Next reverse (6.4) in the complemented orientation, moving the old head left
through \(M^vB^wA\):

\[
 C B^u M^vB^w A HH
       \longrightarrow
 C B^u HH M^vB^w A.
\tag{7.4}
\]

Finally retire the middle atom:

\[
 C B^u HH M^vB^w A
       \longrightarrow
 C B^u C B^v A B^w A.
\tag{7.5}
\]

The last word is exactly the connectorwise complement of (6.1).

For the lone-left-\(B\) branch, return the new mobile head to
\(B|R_\pm|HH_{\rm new}\), restore \(R_\pm\) to \(HH_{\rm old}\), and use
the literal reverse sequence

\[
\begin{aligned}
 B HH_{\rm old}HH_{\rm new}
 &\longrightarrow HH_{\rm old}BHH_{\rm new}\\
 &\longrightarrow HH_{\rm old}BCA\\
 &\longrightarrow HH_{\rm old}CBA\\
 &\longrightarrow CBHH_{\rm old}A\\
 &\longrightarrow C B C A A.
\end{aligned}
\tag{7.6}
\]

The five arrows respectively reverse the last old-head swap in (6.11),
retire the outer new head to its complemented order \(C|A\), move that
outer \(C\) left through \(B\), move the old head right through \(C|B\),
and retire the middle old head to \(C|A\).  The endpoint
\(C B C A A\) is the complement of \(A B A C C\).

Every reverse move has the same fixed-sentinel decoder as its forward move, and
the permanent `p_1` head supplies an additional phase signature throughout.

### Theorem 7.1 (uniform compound four-head atom)

Every bounded compound interval furnished by outcome 2 of Theorem 2.1 has
pairwise source-disjoint setup and teardown paths which export a temporary
fixed-berth double-head cart and restore the exact complemented source.
All paths avoid the protected first connector.

#### Proof

Equations (6.3)--(6.8) give setup and Lemma 6.1 gives its decoder.  The
interval lies wholly in the punctured work suffix, and the outward cart stops
outside the protected collar, so `p_1` is unchanged.  Equations (7.1)--(7.5)
give teardown to the literal complement.  The reverse decoder and permanent
head signature prove mutual disjointness.  Reflection/complement gives the
`CCAA` orientation.  \(\square\)

## 8. Retracted asymptotic APH claim

**This section is invalidated by the independent audit cited at the top of
the file.**  In particular, Corollary 8.1 does not follow: the setup paths
intersect before their records are written, and the protected-island,
sentinel-crossing, and reserved-collar joins remain open.  The text below is
retained only to identify the superseded intended implication.

Combining Theorems 2.1, 5.1, and 7.1 gives

### Corollary 8.1

For every punctured near-balanced work suffix of length at least ten, the
Anchored Pre-Head Bootstrap lemma holds.  Hence the pre-head odd dependency
cycle is not an asymptotic obstruction.

The proof-safe frontier is therefore

\[
 \boxed{
 \begin{array}{l}
 \text{post-beta terminal: closed},\\
 \text{pre-head APH for every sufficiently large odd source: closed},\\
 \text{full odd composition: pending one independent dependency/decoder audit},\\
 \text{finitely many suffixes of length below ten: outside this theorem.}
 \end{array}}
\]

## 9. Exact dependency and finite-base scope

For the odd parameterization \(k=2m-1\), the work suffix in the cited
source-internal theorem has \(m-1\) connector blocks.  Thus the length-ten
resource theorem applies for

\[
                             m\ge11,\qquad k\ge21.
\]

This is enough for an asymptotic additive-constant induction.  It does not
settle the finite odd cases \(k=17,19\); equality is presently certified only
through \(k=16\), and those two dimensions must remain explicit finite-base
obligations.

Corollary 8.1 uses the following theorem interfaces and no others:

1. the literal transition/neutral atom setup and retirement paths;
2. the fixed-\(p_1\) shadow-clock lift for every edge wholly in the work
   suffix;
3. double-head transport and the marked/LIFO bulk theorem;
4. the conditional fixed-collar accumulator, with its formerly missing
   non-guardable crossings supplied by the temporary cart;
5. exact connector beta and the monotone post-beta terminal accumulator.

An independent composition audit must still check three scope joins:

* deleting two zero-charge atom supports from the bulk cancellation input is
  accepted by the marked/LIFO theorem;
* its visible-cart decoder remains valid when the cart crosses the finitely
  many stationary \(H|M\), \(M|H\), or single-\(H\) origin records; and
* the temporary cart berth is physically disjoint from the two blocks used
  to create the permanent first-connector head.

The local paths above prove the missing APH construction; they do not silently
upgrade any of those cited theorem scopes.
