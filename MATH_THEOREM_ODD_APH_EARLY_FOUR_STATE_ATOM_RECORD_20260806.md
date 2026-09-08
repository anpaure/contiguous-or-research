# Odd APH: an early four-state literal atom record removes the audited pre-record collisions

**Date:** 2026-08-06  
**Method:** copy-before-erase in the proved protected root/boundary register,
followed by anchored one-head transport; no computation or search  
**Status:** unconditional early-record and raw-transport theorem.  It repairs
item 1 of the minimal package in
`MATH_AUDIT_ODD_APH_TEMPORARY_CART_DICHOTOMY_20260806.md`.  It does not yet
construct the permanent fixed-collar double head.

## 1. Literal resources already available

Use

\[
 A=00,\quad B=20,\quad C=22,\quad H=02,\quad M=11.
\tag{1.1}
\]

The protected root/boundary register from the marked-corridor theorem has
four persistent states

\[
 Q_0=021,\qquad Q_1=012,
 \qquad Q_2=201,\qquad Q_3=210,             \tag{1.2}
\]

and literal paths

\[
 Q_0\leftrightarrow Q_1,\qquad
 Q_0\leftrightarrow111\leftrightarrow Q_2,\qquad
 Q_2\leftrightarrow Q_3.                   \tag{1.3}
\]

The register is disjoint from the active first connector and from the work
suffix.  Its persistent states have root value zero or two; the sole hub
has the already audited root/boundary signature `(1,1)`.  Thus the paths in
(1.3) avoid the old promotion/aperture linkage and have the fixed directed
shadow-clock lift.

Whenever a literal source interval is held unchanged, it may label a route
in (1.3): even if two projected routes share a register vertex, their full
states cannot agree unless their unchanged source intervals agree.  This is
the copy-before-erase principle used below.

## 2. Orient the two transition atoms toward the fixed right collar

Let the selected atom be chosen deterministically from the still-raw
reserved-collar work word.  There are three source types:

\[
                    BB,\qquad AB^sC,\qquad CB^sA.     \tag{2.1}
\]

For the first transition orientation, the source-internal paths give

\[
                    AB^sC\leadsto HHM^s.              \tag{2.2}
\]

Leave the left head stationary and move the right head toward the fixed
right collar.  It must first cross the private `M`-gap.

For the opposite orientation, move the left `C` right through the `B`-gap,
using the reflected literal rewrite

\[
                    C|B\leadsto M|C,
\]

and then use the reverse of the audited retirement path

\[
                    C|A\leadsto H|H.
\]

This gives

\[
                    CB^sA\leadsto M^sHH.              \tag{2.3}
\]

Again leave the left head stationary and move the right head toward the
collar.  Now the private gap lies behind the stationary head and is never
crossed.  Finally `BB` has the literal path `BB -> HH` and no private gap.

Thus only the `AB^sC` orientation has two transport phases: private-gap and
raw-tape transport.

## 3. The four-state early code

Assign the register meanings

\[
 \begin{array}{c|c}
 Q_0 & BB\text{, raw phase},\\
 Q_1 & CB^sA\text{, raw phase},\\
 Q_2 & AB^sC\text{, private-gap phase},\\
 Q_3 & AB^sC\text{, raw phase}.
 \end{array}                                      \tag{3.1}
\]

For `AB^0C`, write `Q_3` immediately, because there is no private phase.

### Theorem 3.1 (record-before-erase anchored-head theorem)

Suppose the selected atom and the interval from it to the fixed right collar
are still raw over \(\{A,B,C\}\).  Before altering the atom, write the
appropriate state from (3.1).  Bootstrap the atom by (2.2), (2.3), or the
neutral `BB` path.  Leave its left head at the atom origin and move only the
right head toward the collar.

On the `AB^sC` branch with \(s>0\), hold `Q_2` while crossing the whole
private `M^s` trail.  At the first macro checkpoint beyond that trail, hold
the tape fixed and traverse the one-edge register path

\[
                          Q_2\leftrightarrow Q_3.      \tag{3.2}
\]

Then continue through the raw interval.  The resulting setup and transport
paths are pairwise source-disjoint and preserve the active first-connector
row.

#### Proof

**Record writing.**  During the route from the idle register state to the
state in (3.1), the selected source atom is still literal.  Its physical
address, type, orientation, and gap length are therefore present in the
full state.  Copy-before-erase proves that two writing paths cannot merge.

**Atom bootstrap.**  The register now fixes the ordered atom type.  Outside
the selected support the tape is raw.  Every strict state of the fixed
simple local bootstrap path is consequently located at the unique altered
support; reversing that local path recovers the literal atom.  Different
atom types have different register states.

**Private phase.**  The only nonraw source blocks outside the active local
window are the stationary origin head and the private `M` trail.  With `Q_2`
fixed, the reverse of the audited `M|H` path has the usual endpoint-trail
decoder.  The stationary head fixes the origin and the length of the
remaining trail fixes the completed crossing count.

At the endpoint of the private phase, the stationary head, the complete
trail, the mobile head, and `Q_2` still recover the source.  Therefore the
register edge (3.2) is itself copy-before-erase: its two endpoints and its
single physical edge cannot merge different source paths.

**Raw phase.**  The states `Q_0,Q_1,Q_3` identify respectively the neutral,
right-oriented transition, and left-oriented transition sources.  The
stationary origin head and the retained private trail locate the atom.  The
anchored one-head raw-interval theorem now applies: at a macro checkpoint
the two head positions give the completed block count, and at a strict state
the sole active nonraw window outside the protected origin gives the local
row and microstep.

The exact collision from the independent audit cannot survive.  Its two
routes were

\[
 AB^sCBZ\longrightarrow HM^sHMZ,
 \qquad
 AB^{s+1}CZ\longrightarrow HM^sHMZ.
\]

In the first route the displayed vertex is a raw-`B` strict state and hence
has register `Q_3`; in the second it is a private-trail checkpoint and hence
has register `Q_2`.  Their full states are distinct.

Every work edge is wholly in the reserved work suffix, while the register
edge is in the already protected boundary path.  Thus the active first row
is preserved as an unordered selected row throughout.  This proves the
theorem.  \(\square\)

## 4. The same principle fixes the two displayed compound collisions

The bounded `AACC/CCAA` construction has only two early bits:

1. the orientation `AACC` versus `CCAA`; and
2. on the exceptional \(v=0,u+w=1\) face, the side of the lone `B`.

Encode these four possibilities injectively by `Q_0,...,Q_3` **before the
first compound rewrite** and hold the chosen state until the late records
`R_+,R_-` and the side record have become literal.

### Corollary 4.1 (the audited compound intersections are separated)

With this early code, neither of the two exact intersections from the audit
is an intersection in the full state graph:

\[
 ABA CC\leadsto ABHHC
       \quad\hbox{versus}\quad
 AACBC\leadsto ABHHC,                         \tag{4.1}
\]

and

\[
                   AACC\leadsto HHHH
       \quad\hbox{versus}\quad
                   CCAA\leadsto HHHH.         \tag{4.2}
\]

#### Proof

The sources are still literal while their register records are written, so
copy-before-erase proves disjoint record setup.  The two routes in (4.1)
have opposite lone-`B` side bits and the two routes in (4.2) have opposite
orientation bits.  Hence the coincident work words are tensored with
different persistent register states.  The record is erased only after the
corresponding late literal record exists, so no information-free checkpoint
is introduced.  \(\square\)

This corollary repairs the two *identified* early compound collisions.  It
does not certify every strict state of the entire compound macro; such a
certification is unnecessary on the one-anchored-head route of Theorem 3.1
and remains separate for any future four-head route.

## 5. Exact remaining interface

Combine Theorem 3.1 with the reserved-collar one-atom theorem.  For every
odd \(k=2m-1\ge21\), after `p_1` and the two collar blocks are reserved,
one can create a source-recorded stationary origin and move one anchored
head through the untouched raw interval toward the common collar.

What is **not** proved here is that one anchored head can execute the entire
protected `G_1`/residual collar accumulator.  The exact remaining pre-head
statement is:

> **Anchored-catalyst collar lemma.**  Starting from the endpoint of Theorem
> 3.1, use the recorded mobile head to realize all at most four protected
> remote increments of the zipper-split fixed-berth accumulator, without
> crossing an unrecorded nonraw block, and end with `H|H` at the named collar
> berth while retaining the origin record.

Once that lemma is available, the fixed-head marked/LIFO theorem, connector
beta, and the proved post-beta accumulator compose.  Thus the early-record
problem is closed, but APH remains open at the anchored-catalyst collar
lemma and its protected-island/sentinel transport subcase.
