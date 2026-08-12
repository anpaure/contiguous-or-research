# Depth-two support-four role conversion and protected Hall projections

Date: 2026-08-01

Status: unconditional literal depth-two packet, exact opened projection
audit, sharp support minimum, and protected extension in each of the two
depth-two Hall projections.  A common owner-injective, root-balanced
one-copy extension is not proved.

## 0. Outcome

The smallest clean Boolean role converter is a Johnson square.  Its two
directed phases are the two orientations of one four-cycle.  They use the
same four roots, four distinct lower colours, and four distinct owners.
Their relative functional signature is

```text
(attachment parity, predecessor parity)=(-1,+1).
```

After deleting opposite orientations of one seam, the two three-edge
phases export exactly the one attachment return and the two predecessor
returns required by the opened rolling-reset interface.  In particular,
the open packet changes the role of an adjacent port without using the
forbidden seam owner at all.

The packet is literally a depth-two second-order walk.  Moreover, it can
be protected while extending either exact depth-two integral projection:

1. all lower colours with middle-root capacity two; or
2. all lower colours with injective owners.

These are separate extensions.  Their common ordered-diamond extension,
acyclicity, and occurrence-level embedding in the same carrier remain the
correlation gate.

## 1. The Boolean square

Let `K` have rank `m-2`, and choose distinct labels `x,y,z,w` outside
`K`.  Put

\[
\begin{aligned}
 V_0&=K+x+z,&V_1&=K+x+y,\\
 V_2&=K+y+w,&V_3&=K+z+w,
\end{aligned}                                                \tag{1.1}
\]

with indices modulo four.  Define

\[
                  L_i=V_i\cap V_{i+1},\qquad
                  U_i=V_i\cup V_{i+1}.                       \tag{1.2}
\]

Explicitly,

\[
\begin{array}{c|cccc}
i&0&1&2&3\\ \hline
L_i&K+x&K+y&K+w&K+z,\\
U_i&K+x+y+z&K+x+y+w&K+y+z+w&K+x+z+w.
\end{array}                                                   \tag{1.3}
\]

All four lower colours are distinct, and all four owners are distinct.
Let

\[
 {\cal F}=\{V_i\longrightarrow V_{i+1}:i\in\mathbb Z_4\},
 \qquad
 {\cal R}=\{V_{i+1}\longrightarrow V_i:i\in\mathbb Z_4\}.  \tag{1.4}
\]

### Theorem 1.1 (literal depth-two square)

Both `F` and `R` are literal depth-two owner-exact cycle components on
this support.  Each uses every root, lower colour, and owner in (1.1)--
(1.3) exactly once.

#### Proof

Take the cyclic lower word

\[
                         L_0,L_1,L_2,L_3.                    \tag{1.5}
\]

Consecutive lower values are distinct Johnson neighbours.  Moreover

\[
       L_{i-1}\cup L_i=V_i,
       \qquad
       L_{i-1}\cup L_i\cup L_{i+1}=U_i.                     \tag{1.6}
\]

The depth-two second-order-walk theorem therefore gives `F`.  Reading
(1.5) backwards gives `R`.  Equation (1.3) gives exactness. \(\square\)

Thus this is not merely an unflagged Johnson circuit.  It is a literal
depth-two flag circuit.

## 2. Exact opened signature

Delete the seam atom `V0 -> V1` from `F` and the opposite seam atom
`V1 -> V0` from `R`.  The remaining phases are

\[
 \begin{aligned}
 {\cal F}^{\circ}&:
       V_1\longrightarrow V_2\longrightarrow V_3\longrightarrow V_0,\\
 {\cal R}^{\circ}&:
       V_0\longrightarrow V_3\longrightarrow V_2\longrightarrow V_1.
 \end{aligned}                                               \tag{2.1}
\]

### Theorem 2.1 (one attachment path and two predecessor paths)

The symmetric difference of the head--owner attachments in the two open
phases is the alternating path

\[
             V_0-U_3-V_3-U_2-V_2-U_1-V_1.                  \tag{2.2}
\]

The symmetric difference of the tail--head matchings is the disjoint
union of

\[
 V_0^- -V_3^+ -V_2^- -V_1^+,
 \qquad
 V_1^- -V_2^+ -V_3^- -V_0^+.                               \tag{2.3}
\]

The tail--lower attachment difference is similarly the path

\[
             V_1-L_1-V_2-L_2-V_3-L_3-V_0.                  \tag{2.4}
\]

#### Proof

In `F^o`, the head--owner pairs are

\[
                  (V_2,U_1),(V_3,U_2),(V_0,U_3),            \tag{2.5}
\]

whereas in `R^o` they are

\[
                  (V_1,U_1),(V_2,U_2),(V_3,U_3).            \tag{2.6}
\]

Alternating (2.5) and (2.6) gives (2.2).

The three tail--head atoms in `F^o` are

\[
 V_1^-V_2^+,\quad V_2^-V_3^+,\quad V_3^-V_0^+,
\]

and those in `R^o` are

\[
 V_2^-V_1^+,\quad V_3^-V_2^+,\quad V_0^-V_3^+.
\]

Their alternating components are exactly (2.3).  The tail--lower pairs
are `(Vi,Li)` in the forward phase and `(V(i+1),Li)` in the reverse
phase, for `i=1,2,3`, giving (2.4). \(\square\)

### Corollary 2.2 (reset parity)

On the closed square, the relative head--owner attachment is a four-cycle,
and the relative predecessor permutation is translation by two on
`Z_4`.  Hence their signs are respectively

\[
                              (-1,+1).                       \tag{2.7}
\]

This is the same parity signature as the two phases of an even rolling
reset.  Unlike a Boolean hex, the square can carry the odd attachment
return.

## 3. Literal role conversion at one port

Let `A,B` be adjacent rank-`m` roots, with

\[
       A=I+z,\qquad B=I+y,\qquad |I|=m-1.                  \tag{3.1}
\]

Choose `x in I`, put `K=I-x`, and choose

\[
                         w\notin A\cup B.                   \tag{3.2}
\]

Then (1.1) has `V0=A` and `V1=B`.  Its deleted seam owner is

\[
                         U_0=A\cup B.                       \tag{3.3}
\]

The two open phases (2.1) contain neither orientation of the seam and use
only the three different owners `U1,U2,U3`.  Consequently they form an
owner-changing role-conversion interface between the free port states
`B -> A` and `A -> B` without selecting the opposite orientations of
owner (3.3).

This statement is local.  To insert it in a one-copy carrier, its two
internal roots and its three owner/lower resources must be reserved from
the ambient factor, and the two open phases must contract to the same
exterior.  Theorem 2.1 proves the exact boundary signature needed for that
contraction; it does not supply the ambient reservation.

## 3A. A simultaneous q-port bank

The preceding construction can be made simultaneously resource-disjoint
over every port of the Boolean q-gon, using only one fresh coordinate.

Use the q-gon notation

\[
 A_i=S+z+a_i,\qquad B_i=S+a_i+a_{i+1},
 \qquad |S|=m-2,                                           \tag{3A.1}
\]

on a 2m-point ground.  Assume

\[
                         3\le q\le m.                       \tag{3A.2}
\]

Choose \(s\in S\) and choose one coordinate

\[
       w\notin S\cup\{z,a_0,\ldots,a_{q-1}\}.               \tag{3A.3}
\]

The latter exists because the displayed q-gon uses \(m+q-1\le2m-1\)
coordinates.

For each \(i\), instantiate the square with

\[
 K_i=(S-\{s\})+a_i,\qquad
 x_i=s,\quad y_i=a_{i+1},\quad z_i=z,\quad w_i=w.           \tag{3A.4}
\]

Its four roots are

\[
\begin{aligned}
 V_{i,0}&=A_i,&V_{i,1}&=B_i,\\
 V_{i,2}&=(S-s)+a_i+a_{i+1}+w,&
 V_{i,3}&=(S-s)+a_i+z+w.                                  \tag{3A.5}
\end{aligned}
\]

### Theorem 3A.1 (resource-disjoint q-port role-conversion bank)

For \(3\le q\le m\), the q squares in (3A.4) have:

1. pairwise distinct internal roots;
2. pairwise distinct companion lower colours

   \[
   \begin{aligned}
   L_{i,1}&=(S-s)+a_i+a_{i+1},\\
   L_{i,2}&=(S-s)+a_i+w,\\
   L_{i,3}&=(S-s)+a_i+z;
   \end{aligned}                                           \tag{3A.6}
   \]

3. pairwise distinct companion owners

   \[
   \begin{aligned}
   U_{i,1}&=S+a_i+a_{i+1}+w,\\
   U_{i,2}&=(S-s)+a_i+a_{i+1}+z+w,\\
   U_{i,3}&=S+a_i+z+w;
   \end{aligned}                                           \tag{3A.7}
   \]

4. no collision of a companion root, lower colour, or owner with the
   original q-gon resource of the corresponding rank.

The two open bank phases are therefore

\[
\begin{aligned}
 {\cal P}^{\rm rev}_i:\quad&
 B_i\longrightarrow V_{i,2}\longrightarrow V_{i,3}
     \longrightarrow A_i,\\
 {\cal P}^{\rm fwd}_i:\quad&
 A_i\longrightarrow V_{i,3}\longrightarrow V_{i,2}
     \longrightarrow B_i.                                 \tag{3A.8}
\end{aligned}
\]

They use identical root, lower, and owner sets.  The first phase replaces
the reflected-reverse new port \(B_i\to A_i\); the second replaces the
forward old port \(A_i\to B_i\).  Neither phase uses the seam lower colour
\(S+a_i\) or seam owner \(S+z+a_i+a_{i+1}\).

#### Proof

Every original q-gon root contains \(s\) and omits \(w\), while every
internal root in (3A.5) omits \(s\) and contains \(w\).  Hence the two
root banks are disjoint.  Among the internal roots, the \(V_{i,2}\) are
distinguished by the adjacent unordered pairs
\(\{a_i,a_{i+1}\}\), the \(V_{i,3}\) by \(a_i\), and the two types by
the presence of \(z\).

All companion lower colours omit \(s\), whereas every original q-gon
lower colour \(S+a_i\) contains \(s\).  Inside (3A.6), the three types
are separated by the presence of neither \(w,z\), of \(w\), or of \(z\),
and each type is injectively indexed by \(i\).

Every companion owner contains \(w\), whereas every original q-gon owner
omits it.  Inside (3A.7), \(U_{i,1}\) omits \(z\), \(U_{i,2}\) omits
\(s\), and \(U_{i,3}\) contains both.  Within each type, the same
adjacent-pair or single-label argument is injective.  This proves all
collision claims.  Equation (3A.8) is (2.1) at every port. \(\square\)

Thus the q-gon closed-doubleton obstruction has an exact simultaneous
depth-two role-conversion module at the level of literal roots and the two
immediate palettes.  It reserves \(2q\) internal roots and \(3q\)
lower/owner resources.  Showing that those resources can be removed from,
and returned to, one common one-copy ambient factor is still a global
protected ordered-diamond problem.

## 3B. Replacement-only ledger, superseded for serial composition

For one port, distinguish the four formal states

\[
\begin{array}{c|c|c|c}
\text{state}&\text{atoms}&\text{lower palette}&\text{owner palette}\\ \hline
D^-&B\to A&\{L_0\}&\{U_0\}\\
P^-&B\to V_2\to V_3\to A&\{L_1,L_2,L_3\}&\{U_1,U_2,U_3\}\\
P^+&A\to V_3\to V_2\to B&\{L_1,L_2,L_3\}&\{U_1,U_2,U_3\}\\
D^+&A\to B&\{L_0\}&\{U_0\}.
\end{array}                                                \tag{3B.1}
\]

Thus the atom-count history is

\[
                              1\longrightarrow3
                               \longrightarrow3
                               \longrightarrow1.            \tag{3B.2}
\]

If one insists on replacing a direct edge by an open path, only the middle
transition \(P^-\leftrightarrow P^+\) is count- and
resource-balanced.  The first transition deletes \(L_0,U_0\), adds
\(L_1,L_2,L_3,U_1,U_2,U_3\), and introduces the two internal roots.
The final transition is its inverse.

No state in (3B.1) repeats an owner internally.  However, (3B.1) is not
by itself a legal sequence of exact one-copy factor switches: the
\(1\to3\) expansion and \(3\to1\) contraction require either an explicit
two-edge compensation elsewhere, an accounted physical-length charge, or
a host in which the direct q-gon atoms were opened before the common
factor was selected.

There is a second exact warning.  The two closed square phases are

\[
             D^-\cup P^+,\qquad D^+\cup P^-.                \tag{3B.3}
\]

They are valid four-edge directed cycles with identical resources, but
they saturate \(A,B\) inside an isolated square component.  Consequently
(3B.3) is a literal closed role-conversion switch, not automatically a
splice into the exterior q-gon chronology.  The open middle pair
\(P^-,P^+\) is the useful interface; Theorem 2.1 records exactly the
external returns still required.

For the q-port bank, multiply every entry in (3B.1)--(3B.2) by \(q\).
The middle \(3q\to3q\) exchange remains perfectly balanced.  The two
outer transitions have edge-count discrepancy \(2q\).  Therefore
Theorem 3A.1 proves a phase-paired alternative bank under that replacement
interpretation.  It is not the right serial architecture.  The later
direct-plus-opposite-return construction keeps a direct q-gon atom and one
oppositely oriented return path in every state, giving four equal-size
states and eliminating this artificial count discrepancy; see
MATH_THEOREM_QPORT_RESIDENT_RAIL_ROLE_CONVERTER_20260801.md.

## 4. Support four is sharp

### Theorem 4.1 (minimal clean orientation converter)

A closed Johnson circuit whose edges have pairwise distinct lower colours
and pairwise distinct owners and which admits both directed orientations
has at least four edges.  The square above attains four.

#### Proof

A two-edge circuit is the two orientations of one Johnson edge.  Both have
the same owner and lower colour; this is exactly the closed doubleton.

Every triangle in a Johnson graph has one of two forms.  Write two roots
as `S+a,S+b`, where `|S|=m-1`.  A common-neighbour classification gives
either

\[
                         S+a,S+b,S+c,                        \tag{4.1}
\]

in which all three edge intersections are `S`, or

\[
                 S+a,S+b,(S-f)+a+b,                         \tag{4.2}
\]

in which all three edge unions are `S+a+b`.  Thus every triangle repeats
one complete palette.  It cannot be clean.  Equations (1.1)--(1.4) give a
clean four-cycle. \(\square\)

This is a structural minimum, not a search observation.

## 5. Protected extension in the root-cap-two projection

Now use the depth-two ground `[2m+1]`.  Let

\[
 {\cal L}={ [2m+1]\choose m-1},\qquad
 {\cal R}={ [2m+1]\choose m}.                              \tag{5.1}
\]

Preselect, for each `Li` in (1.3), its two incident square roots
`Vi,V(i+1)`.  Thus the four square roots are saturated at capacity two.

### Theorem 5.1 (protected square b-matching)

The preselected square extends to an incidence set `J` satisfying

\[
 d_J(S)=2\quad(S\in{\cal L}),
 \qquad
 d_J(Q)\le2\quad(Q\in{\cal R}).                            \tag{5.2}
\]

Equivalently, the exact-lower/root-cap-two projection can always be chosen
to contain the Boolean square.

#### Proof

Delete the four selected lower colours and the four saturated square
roots.  A remaining lower set `S` is contained in at most one deleted
root.  Indeed, if it were contained in two adjacent square roots, it would
be their rank-`(m-1)` intersection, one of the deleted `Li`.  Opposite
square roots intersect only in `K`, of rank `m-2`, and cannot both contain
`S`.

Every residual lower vertex therefore retains at least

\[
                             (m+2)-1=m+1                    \tag{5.3}
\]

root neighbours.  For any residual family `X`, write `d_X(Q)` for the
number of its members contained in `Q`.  Since `d_X(Q)<=m`,

\[
 \begin{aligned}
 \sum_{Q\ {\rm residual}}\min(2,d_X(Q))
 &\ge {2\over m}\sum_{Q\ {\rm residual}}d_X(Q)\\
 &\ge {2(m+1)\over m}|X|\\
 &\ge2|X|.
 \end{aligned}                                               \tag{5.4}
\]

This is the capacitated Hall condition.  Integral max flow completes
(5.2). \(\square\)

The conclusion permits the square to remain a cycle component.  It does
not make the other edge owners injective or the remaining components
acyclic.

## 6. Protected extension in the owner-injective projection

Let

\[
                  {\cal O}={ [2m+1]\choose m+1}.             \tag{6.1}
\]

Preselect the four distance-two incidences

\[
                              L_i\longmapsto U_i.            \tag{6.2}
\]

Each incidence (6.2) has physical middle facets `Vi,V(i+1)`.

### Theorem 6.1 (protected square owner SDR)

The four assignments (6.2) extend to an injection

\[
                    \phi:{\cal L}\longrightarrow{\cal O},
                    \qquad S\subset\phi(S).                 \tag{6.3}
\]

Thus the exact-lower/owner-injective projection can also always be chosen
to contain the Boolean square.

#### Proof

Delete the four selected lower sets and owners.  A remaining lower set is
contained in at most two of the deleted owners.

To see this, all four owners lie in `K+{x,y,z,w}` and each contains `K`
plus three of the four displayed labels.  If a lower set `S` is contained
in one of them, put

\[
                            h=|S-K|.                         \tag{6.4}
\]

If `h=1`, then `S` contains all of `K` and is one of the four deleted
`Li`.  For a residual `S` one has `h>=2`, and at most `4-h<=2` of the
four owners contain it.  A set using a coordinate outside the displayed
support is contained in none of them.

Before deletion, the distance-two containment graph has degrees

\[
        a={m+2\choose2}\quad\hbox{on }{\cal L},
        \qquad
        b={m+1\choose2}\quad\hbox{on }{\cal O}.              \tag{6.5}
\]

Every residual left vertex has degree at least `a-2`, and every residual
right vertex has degree at most `b`.  Hence for every residual family `X`,

\[
        (a-2)|X|\le b|N(X)|,
        \qquad
        a-2-b=m-1\ge1.                                      \tag{6.6}
\]

Thus `|N(X)|>=|X|`.  Hall's theorem extends (6.2) to (6.3).
\(\square\)

This projection does not control middle-root degrees or topology.

## 7. Exact consequence for the q-gon gate

At one reflected-reverse/forward q-gon port, the two conflicting atoms are

\[
                         B\longrightarrow A,
              \qquad     A\longrightarrow B,                \tag{7.1}
\]

with common owner `A union B`.  Section 3 supplies an open support-four
replacement whose two phases have exactly the required role reversal and
do not use that owner.  Theorem 2.1 supplies the one attachment and two
predecessor returns, and Theorem 4.1 says no clean smaller Boolean circuit
can do so.

Theorems 5.1 and 6.1 further show that the connector is not excluded by
either depth-two marginal rounding problem, even when it is prescribed in
advance.

For \(3\le q\le m\), Theorem 3A.1 performs the role conversion
simultaneously at all q ports with no internal root, lower, or owner
collision.  This closes the finite local wiring problem, not its one-copy
ambient reservation.

What is not proved is the simultaneous statement

```text
one common ordered-diamond selection
+ the protected square
+ one-copy roots and owners
+ the required exterior contraction/topology.
```

The determinant-two ordered-diamond correlation remains.  Therefore the
square closes the local role-conversion algebra and both projected Hall
rows, but not the global one-copy q-gon composition.

## 8. Independent replay

The C++ replay

    scratch/audit_d2_support4_role_converter_20260801.cpp

was compiled and run with g++ in C++20, O3, NDEBUG mode on H100.  It
checks the square identities, literal second-order identities, resource
injectivity, attachment and predecessor components, reset parities, the
complete q-port collision ledger for every

    3 <= q <= m <= 24,

and the exact serial count/resource history (3B.1).  The retained output is

    scratch/audit_d2_support4_role_converter_20260801.out

with SHA-256 values

    source  ec2577cecb0ea220a513a2681ba15a1d22192ebc9c59f9cba2b1f81aa7412955
    output  80601f2ce280eedde690dd82b8ded825ded5d66063c69d2e68d3dfb62cda0b49

and terminal line

    only the middle 3->3 phase pair is resource/count balanced
