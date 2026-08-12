# A single sharp pivot has an unconditional protected MSW Hamilton host

**Date:** 2026-08-07  
**Method:** explicit geodesic buffering and the endpoint-preserving
MSW/MNW Hamiltonization theorem  
**Status:** unconditional owner/topology theorem.  It protects one complete
sharp pivot and a depth-sized local residence buffer inside a Hamilton cycle.
It does not prove that the rest of that Hamilton cycle is resident, has the
complete arbitrary-width upper deck, or admits one global literal antecedent
and compiler.

## 0. Outcome

Let

\[
 G=ML_{m+1}
 =Q_{2m+1}\left[\binom{[2m+1]}m\cup
                    \binom{[2m+1]}{m+1}\right].
\tag{0.1}
\]

Regard the rank-\((m+1)\) shore as the owner shore.  Let

\[
 T_0,T_1,\ldots,T_h\in\binom{[2m+1]}{m+1}
\tag{0.2}
\]

be any shortest Johnson geodesic, and assume

\[
                         3h\le m-1.                 \tag{0.3}
\]

Then the incidence lift

\[
 T_0, T_0\cap T_1, T_1,ldots,
 T_{h-1}\cap T_h, T_h                             \tag{0.4}
\]

is contained in a Hamilton cycle of \(G\).

More strongly, (0.2) extends by \(h\) owner transitions on each side to a
shortest rank-\((m+1)\) Johnson geodesic with \(3h\) transitions whose
complete incidence lift is contained in one Hamilton cycle.  On this
protected owner interval:

* every coordinate changed by the central pivot has a positive run of at
  least \(h+1\) owners;
* every other nonconstant run shorter than \(h+1\) meets one of the two
  protected interval endpoints;
* all immediate lower colours are distinct; and
* all immediate upper colours are distinct.

Thus the former topology question for **one** sharp pivot is closed: it is
not merely contained in a two-factor, but in an actual Hamilton cycle.  The
construction uses the endpoint-preserving MSW/MNW Hamilton cycle already
proved in
`MATH_THEOREM_MSW_ENDPOINT_AUGMENTED_HAMILTONIZATION_EQUIVALENCE_20260805.md`.

The qualification “one” is load-bearing.  The theorem does not prescribe
several independently labelled pivot paths in one MSW factor.

## 1. Put the pivot in normal form

Because (0.2) is a shortest geodesic, after naming its exchanged labels it
has the form

\[
 T_j=C\cup\{b_1,\ldots,b_j\}
       \cup\{a_{j+1},\ldots,a_h\},
       \qquad 0\le j\le h,                           \tag{1.1}
\]

where

\[
 |C|=m+1-h                                             \tag{1.2}
\]

and \(C,A=\{a_1,\ldots,a_h\},B=\{b_1,\ldots,b_h\}\)
are pairwise disjoint.

Condition (0.3) permits a partition

\[
 C=C^-\mathbin{\dot\cup}C^+
       \mathbin{\dot\cup}C^0,
 \qquad |C^-|=|C^+|=h,                               \tag{1.3}
\]

and it leaves at least \(2h+1\) coordinates outside
\(C\cup A\cup B\).  Choose disjoint sets

\[
 D^-,D^+,
 \qquad |D^-|=|D^+|=h,                               \tag{1.4}
\]

and one further coordinate \(z\), all outside \(C\cup A\cup B\).

Start at

\[
 \widetilde T_{-h}=(C\setminus C^-)\cup A\cup D^-.
\tag{1.5}
\]

In the next \(h\) steps exchange the members of \(D^-\) for the members of
\(C^-\), in any fixed bijective order.  This reaches
\(T_0=C\cup A\).  Perform the central exchanges

\[
                         a_i\longmapsto b_i
                         \quad(1\le i\le h),          \tag{1.6}
\]

and then exchange the members of \(C^+\) for the members of \(D^+\).
The result is an owner sequence

\[
 \widetilde T_{-h},\ldots,\widetilde T_0=T_0,ldots,
 \widetilde T_h=T_h,ldots,\widetilde T_{2h}          \tag{1.7}
\]

with \(3h\) transitions.

All \(3h\) leaving labels

\[
                         D^-\cup A\cup C^+            \tag{1.8}
\]

are distinct, as are all \(3h\) entering labels

\[
                         C^-\cup B\cup D^+,           \tag{1.9}
\]

and the two displayed sets are disjoint.  Hence (1.7) is a shortest
Johnson geodesic.  Every owner in it avoids \(z\).

## 2. Every short owner geodesic sits in a complementary MSW geodesic

We use a general elementary lifting fact.

### Lemma 2.1 (owner-geodesic completion)

Let \(\Omega\) be a \(2m\)-set and let

\[
 Y_0,Y_1,\ldots,Y_t\in\binom\Omega{m+1}              \tag{2.1}
\]

be a shortest Johnson geodesic with \(t\le m-1\).  There is a
complementary geodesic

\[
 X_0,X_1,\ldots,X_m\in\binom\Omega m,
 \qquad X_m=\Omega\setminus X_0,                     \tag{2.2}
\]

such that

\[
                         X_j\cup X_{j+1}=Y_j
                         \quad(0\le j\le t).          \tag{2.3}
\]

#### Proof

Write

\[
 Y_j=Y_0-\{p_1,\ldots,p_j\}+\{q_1,\ldots,q_j\}.
\tag{2.4}
\]

Its common core has size \(m+1-t\ge2\); choose distinct core elements
\(c_-,c_+\).  Define

\[
\begin{aligned}
 X_0&=Y_0-\{c_-\},\\
 X_{j+1}&=Y_j\cap Y_{j+1}=Y_j-\{p_{j+1}\}
               &&(0\le j<t),\\
 X_{t+1}&=Y_t-\{c_+\}.
\end{aligned}                                        \tag{2.5}
\]

Consecutive sets in (2.5) exchange, in order,

\[
 p_1\mapsto c_-,\quad
 p_{j+1}\mapsto q_j\ (1\le j<t),\quad
 c_+\mapsto q_t.                                     \tag{2.6}
\]

All leaving labels and all entering labels in (2.6) are separately
distinct and the two banks are disjoint.  Equations (2.3) follow directly.
Pair the remaining elements of \(X_0\) with the remaining elements of its
complement and append those exchanges.  After exactly \(m\) exchanges the
terminal set is \(\Omega\setminus X_0\), giving (2.2). \(\square\)

Apply the lemma to (1.7), with

\[
                         \Omega=[2m+1]\setminus\{z\},
 \qquad t=3h.                                        \tag{2.7}
\]

Every complementary rank-\(m\) geodesic in a \(2m\)-set is the image of
every other one under a coordinate permutation: map its ordered leaving
bank and ordered entering bank coordinatewise.  Therefore the path (2.2)
is a relabelled canonical MSW path.

## 3. Endpoint-preserving MSW Hamiltonization

The endpoint-augmented MSW theorem supplies, for every \(m\ge3\), a
Hamilton cycle in \(ML_{m+1}\) whose \(z\)-free half contains every edge of
the canonical family of complementary rank-\(m\) geodesics.  Apply a
coordinate permutation of \(\Omega\), fixing \(z\), which sends one
canonical MSW path to (2.2).

The resulting Hamilton cycle contains the complete incidence path

\[
 Y_0,X_1,Y_1,X_2,\ldots,X_t,Y_t,                     \tag{3.1}
\]

and hence contains the buffered pivot path (1.7), including the central
path (0.4).  This proves the Hamilton assertion in Section 0.

This invocation uses the support statement of the MSW/MNW construction,
not merely ordinary Hamiltonicity of the Middle Levels graph: its flipping
cycles preserve the complete chosen complementary geodesic.

## 4. Local residence and the two immediate palettes

Every \(a_i\) is present throughout the left buffer and remains present
until its central deletion.  Its protected positive run therefore has at
least \(h+1\) owners.  Every \(b_i\) is present from its central insertion
throughout the right buffer, again for at least \(h+1\) owners.

Members of \(C^-\) enter on the left and persist through the central and
right parts.  Members of \(C^+\) are present through the left and central
parts before leaving on the right.  Members of \(C^0\) persist throughout.
The only possibly shorter nonconstant runs are those of \(D^-\), which meet
the left endpoint, and those of \(D^+\), which meet the right endpoint.
They are precisely clipped boundary flags.

For a shortest set geodesic, the intersections of consecutive owners are
pairwise distinct: the prefix of entered labels and the suffix of unremoved
labels recover the transition index.  The same argument applies to their
unions.  Thus the protected path is both lower- and upper-\(q1\)-rainbow.

In the sharp-pivot normal form of
`MATH_THEOREM_SHARP_PIVOT_APERTURE_AND_RESIDENT_GEODESIC_PACKET_20260801.md`,
the central owners (1.1) are exactly the flat owners created by inserting
the pivot letter.  Its exact deck-transparency and two-ray compiler
statements therefore remain valid locally.  The present theorem supplies
the previously missing **one-pivot Hamilton owner host**.

## 5. Exact remaining boundary for the `B+1` route

The theorem does not by itself prove \(\nu(k)\le B(k)+1\).  Three global
rows remain outside its scope.

1. **Global residence.**  The protected interval is resident up to its two
   clipped flags.  The unprotected remainder of the MSW/MNW Hamilton cycle
   is not proved to have depth-\(h\) coordinate residence, and the two flags
   still need compatible exterior continuations.
2. **Deep upper deck.**  Local immediate upper colours are distinct, but
   the Hamilton theorem does not say that the complete owner chronology
   covers every rank above the owner layer at arbitrary width.
3. **One literal antecedent and compiler.**  The central pivot insertion is
   a literal local source block, but no theorem here factors the entire
   Hamilton owner cycle through one depth-\(h\) source word or transports
   one occurrence-labelled common-cap matching around the whole cycle.

Accordingly the proof-safe implication is

\[
 \boxed{
 \begin{array}{c}
 \text{one sharp flat pivot geodesic}\
 \Downarrow\\
 \text{a doubly-rainbow, locally resident protected interval}\
 \text{inside an actual Middle-Levels Hamilton cycle}.
 \end{array}}
\tag{5.1}
\]

The former component-joining obstruction is absent for this single-pivot
subproblem.  The remaining `B+1` obstruction is now the global
residence/deep-upper/literal-factor correlation, not Hamilton topology.
