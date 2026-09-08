# Every PBBS hook angle has a selected common-pivot leaf-plucking C6

**Date:** 2026-08-05  
**Method:** rooted-Dyck inverse algebra and the exact hook action--angle
coordinates; no search  
**Status:** unconditional for `h>=3`, `b>=1`, subject only to the standard
exact periodic-BBS action--angle correspondence already used in the PBBS
component census.  The theorem lifts the hook chain from action profiles to
**every hook angle torus**.  It does not by itself choose a simultaneous
loose forest among all of the resulting C6s.

## 1. Hook angles are chip necklaces

Put

\[
                       m=h+b,
        \qquad n=2m+1,
        \qquad q=2h-1 .
\tag{1.1}
\]

For the hook action

\[
                         \lambda=(h,1^b),
\tag{1.2}
\]

the exact angle set has the following standard concrete model:

\[
 {\cal N}_{q,b}
 =\left\{(x_0,\ldots,x_{q-1})\in{\mathbb Z}_{\ge0}^q:
                  \sum_jx_j=b\right\}/C_q .
\tag{1.3}
\]

Thus an angle is a necklace of `b` indistinguishable chips on the `q`
vacancy positions of the long soliton.

Here is a rooted-Dyck description of the same coordinates.  Regard a Dyck
word with action `(h,1^b)` as a plane forest.  It has one distinguished
spine of length `h`; every other edge is a leaf.  At each of the first
`h-1` spine vertices there is one leaf bank before and one after the spine
child.  At the last spine vertex the terminal spine leaf is
indistinguishable from the other leaf children, leaving one bank rather
than two.  Hence there are

\[
                         2(h-1)+1=q
\tag{1.4}
\]

cyclic leaf banks.  Their occupancies are the vector in (1.3).

Equivalently, apply one simultaneous peak deletion.  The result is the
mountain

\[
                         1^{h-1}0^{h-1}.
\tag{1.5}
\]

It has `2h-1=q` insertion gaps.  The original word is recovered by
inserting `b+1` copies of the peak `10` into those gaps, with at least one
copy in the central gap between the up-run and down-run.  One central copy
is the terminal edge of the long spine.  After removing that mandatory
copy, the remaining `b` inserted peaks form an arbitrary weak composition
on the `q` gaps.  This proves the rooted-word/composition bijection
directly, including the slot count and multiplicities.

The hook specialization of the periodic-BBS action--angle theorem says
that rooted PBBS evolution cyclically advances these banks (by a unit in
`Z/qZ`), and that the necklace class is exactly the action torus.  The
component theorem for hooks proves that each such torus is one physical
PBBS cycle.  This model gives the component count in
`MATH_THEOREM_PBBS_SOLITON_GAP_FORCES_EXPONENTIALLY_MANY_SELECTED_CYCLES_20260805.md`:
the internal-symmetry summands there are precisely the rotation-stabilizer
strata of (1.3).

We will use one elementary insertion fact.  If `D` has action
`(h,1^(b-1))`, appending and prepending a primitive leaf give

\[
                         D10,
                \qquad   10D .
\tag{1.6}
\]

In the cyclic bank order these add one chip to the two banks immediately
after and immediately before the root cut.  Those banks are consecutive
on the vacancy circle.  Consequently, after choosing the origin of the
circle, if `D` has occupancy `y`, the two words in (1.6) have angles

\[
                         [y+e_j],
                \qquad   [y+e_{j+1}]
\tag{1.7}

for some `j` modulo `q`.  Conversely every adjacent pair in (1.7) is
obtained in this way by placing the root cut between banks `j` and `j+1`.

The assertion follows directly in the plane-forest model: the two words
in (1.6) add a leaf as the last or first child of the virtual root, i.e. to
the two root-side banks.  It is also the usual one-unit-rigging insertion
in the hook action--angle coordinates.  In the peak-deletion model it is
even more literal: the appended or prepended peak disappears under the
first deletion and occupies the final or initial gap of (1.5), which are
adjacent after cyclic closure.

## 2. The repeated-hook deficit-three star

Let `D` be an arbitrary rooted Dyck word with action

\[
                         (h,1^{b-1}).
\tag{2.1}
\]

On a cyclic ground set of size `2m+1`, form the rank-`(m-1)` word

\[
                  0_{a_0}\,0_{a_1}\,0_{a_2}\,D .
\tag{2.2}

The three displayed zeros are exactly its forward-unmatched zeros.  Let
`c` be the down-step of `D` following its rightmost global maximum.  Put

\[
 K=[n]\setminus\bigl(H\cup\{a_0,a_1,a_2,c\}\bigr),
\tag{2.3}
\]

where `H` is the one-set of (2.2), and define, with subscripts modulo
three,

\[
 R_i=K+a_i,
 \qquad P_i=K+a_i+a_{i+1},
 \qquad Q_i=K+a_i+c .
\tag{2.4}
\]

Changing `a_i` to one consumes `a_i,a_(i+1)` and leaves `a_(i-1)` as the
forward root.  The three normalized Dyck words are

\[
                         D10,
                         10D,
                         1D0 .
\tag{2.5}

Their rightmost maximum is followed by the same physical zero `c`.
Therefore the usual forward/reverse cancellation gives all three old PBBS
factor shores

\[
                         P_i\longrightarrow Q_i .
\tag{2.6}

The first two shores have hook action `(h,1^b)`, while the third has the
promoted hook action

\[
                         (h+1,1^{b-1}).
\tag{2.7}

Thus this is a repeated-hook leaf-plucking star at action level.  The main
point is that it is also q2-neutral for **every** choice of the angle word
`D`.

## 3. One common companion deletion for arbitrary `D`

We prove common deletion literally.  Write

\[
                         D=U\,0_c\,V,
\tag{3.1}

where `U` ends at the rightmost height-`h` maximum.  Let `A` be the
longest prefix of `U` ending at height zero, and write

\[
                         U=A\,1_e\,B .
\tag{3.2}

The coordinate `e` is the first up-step of the unique height-`h` primitive
factor.  Because the action is a hook, every primitive factor before it is
a singleton leaf, and hence

\[
                         A=(10)^\alpha
\tag{3.3}

for some `alpha>=0`.  The path `B`, read from height zero, stays between
zero and `h-1` and ends at height `h-1`.

After the step `c`, the original path never reaches height `h` again.
Let `d` be the down-step following the rightmost later occurrence of
height `h-1`.  Such an occurrence exists immediately after `c`, and its
successor must be a down-step, since an up-step would return to height
`h`.  The coordinate `d` is a zero of `D`, distinct from `c`, so

\[
                         d\in K.
\tag{3.4}

For a normalized state `0_rE`, the inverse rooted-PBBS rule is

\[
 E=X0_sY,quad X\text{ ends at the rightmost maximum}
 \quad\Longrightarrow\quad
 f^{-1}(0_rE)=0_s\,\overline Y,1_r\,\overline X .
\tag{3.5}

Applying (3.5) once to the three words in (2.5), the owners `P_i`, rooted
at `c`, have Dyck words

\[
\begin{array}{c|l|c}
i&\text{Dyck word of }P_i&\text{reverse root }s_i\\ \hline
0&\overline V\,1_{a_0}1_{a_1}0_{a_2}\,\overline U&a_2,\\
1&\overline V\,0_{a_0}1_{a_1}1_{a_2}\,\overline U&e,\\
2&\overline V\,1_{a_0}0_{a_1}1_{a_2}\,\overline U&e.
\end{array}
\tag{3.6}
\]

Indeed `bar(V)` ends at height `h-1`.  In the first row the active word
`110` reaches the unique height `h+1`, so its following zero is `a_2`.
In the other two rows the maximum is `h`; in `bar(U)=bar(A)0_e bar(B)`
its rightmost occurrence is immediately before `e`.

Apply (3.5) a second time.  The three states
`X_i=f^(-1)(P_i)`, rooted at `s_i`, have Dyck words

\[
\begin{array}{c|l}
i&\text{Dyck word of }X_i\\ \hline
0&U\,1_c\,V\,0_{a_0}0_{a_1},\\
1&B\,1_c\,V\,1_{a_0}0_{a_1}0_{a_2}\,A,\\
2&B\,1_c\,V\,0_{a_0}1_{a_1}0_{a_2}\,A.
\end{array}
\tag{3.7}
\]

All three have the same reverse root `d`:

* In row zero the prefix `U1_c` reaches height `h+1`.  While reading `V`,
  its height is exactly two more than the height of the corresponding
  suffix of `D`.  Hence the rightmost height `h+1` occurrence corresponds
  to the rightmost post-`c` height-`h-1` occurrence in `D`, whose following
  zero is `d`.
* In rows one and two, `B` has height at most `h-1`, `B1_c` reaches
  height `h`, and during `V` the new height is one more than the original
  suffix height.  Again its rightmost maximum is followed by `d`.
  After `V`, the active tails `100` and `010` have height at most two,
  and `A=(10)^alpha` has height at most one.  Since `h>=3`, none can tie
  the maximum.

It follows that

\[
 f^{-2}(P_i)=P_i+s_i-d,
 \qquad
 P_i\cap f^{-2}(P_i)=P_i-d
 \quad(i=0,1,2).
\tag{3.8}

Thus the unchanged companion q1 row at all three `P_i` deletes the same
core coordinate `d`.  The common-deletion classification now proves that
the clean switch

\[
                         P_iQ_i\longmapsto P_iQ_{i+1}
\tag{3.9}

preserves the selected q2 multiset exactly.

## 4. Every required occurrence is selected

The two action types in (2.5)--(2.7) have top soliton gaps

\[
 h-1\ge2,
 \qquad
 h\ge3,
\tag{4.1}
\]

respectively.  By the spectral-gap forcing theorem, every outgoing q1
occurrence on every one of these PBBS components is uniquely max-height
selected.  This applies both to the three old shores (2.6) and to their
three unchanged companion shores at the `P_i`.

Consequently (3.9) is a literal **selected q1- and q2-neutral clean C6**.
No tie decision is used.

## 5. Exact angle action: one adjacent chip transfer

Let the base word `D` have occupancy vector `y` with total `b-1`.  By the
root-bank insertion rule (1.6), the two repeated-hook shores lie on the
physical hook components

\[
                         [y+e_j],
                \qquad   [y+e_{j+1}]
\tag{5.1}

for two consecutive vacancy positions.  The third shore lies on one
well-defined promoted-hook component of action `(h+1,1^(b-1))`.

Conversely, take any composition `x` of `b` and any `j` with `x_j>0`.
Put

\[
                         y=x-e_j.
\tag{5.2}

Choose the rooted representative of `y` whose cut lies between banks `j`
and `j+1`.  The construction above gives a selected q2-neutral C6 whose
two hook components are

\[
                   [x]
       \quad\text{and}\quad
                   [x-e_j+e_{j+1}].
\tag{5.3}

Hence every cyclic adjacent chip transfer has a literal physical lift.

## 6. The hook angle graph is connected

Let `G_(q,b)` be the graph on `N_(q,b)` whose edges are (5.3).  Then

\[
                         \boxed{G_{q,b}\text{ is connected}.}
\tag{6.1}

Indeed, before quotienting by cyclic rotation, adjacent unit transfers on
the `q`-cycle connect all weak compositions: orient the cycle toward slot
zero and move every chip one edge at a time until all `b` chips occupy
slot zero.  Passing to rotation classes preserves connectedness.

Combining (5.3) and (6.1) gives the angle-level lifting theorem.

### Theorem 6.1 (all-hook angle lifting)

For every `h>=3` and `b>=1`, the two-section of the selected
common-pivot q2-neutral PBBS C6 hypergraph, restricted to the physical
components of action `(h,1^b)`, contains the connected graph `G_(2h-1,b)`.
Every hook torus therefore has a literal leaf-plucking C6 portal to an
action-`(h+1,1^(b-1))` torus.

If the two necklaces in (5.3) are distinct, the C6 has one old edge on
each of three distinct PBBS components and is a genuine three-component
merger.  If they agree, the statement is still a valid q1/q2-neutral
physical switch but no three-component topology claim is made.  The case
`b=1` has only one hook torus and hence no angle multiplicity to remove.

This closes the angle-incidence gap left by the single explicit all-hook
chain: the exponentially many hook tori are not isolated from the
q2-neutral connector atlas.

### Corollary 6.2 (the full graded hook quotient is connected)

Fix `m` and take the union of all hook sectors

\[
       (h,1^{m-h}),
       \qquad 3\le h\le m.
\tag{6.2}
\]

The selected common-pivot q2-neutral C6 hypergraph induced on all their
physical angle tori is connected.  Indeed Theorem 6.1 connects every angle
inside one fixed hook sector, and every leaf-plucking hyperedge contains a
promoted vertex in the next sector

\[
       (h,1^b)\longrightarrow(h+1,1^{b-1}).
\tag{6.3}
\]

Iterating reaches the unique single-soliton torus `(m)`.  This is static
component-hypergraph connectedness.  It is not yet a loose-tree or
simultaneous-switch statement: an edge joining two already absorbed hook
vertices to an old promoted parent can have two cuts on one current rail.

## 7. Two disjoint lifts of one angle connector

Ground rotation preserves PBBS, the max-height section, and all q1/q2
identities above.  It also preserves the three angle necklaces, hence the
same physical component triple.  Every rank-`m` owner has full rotational
orbit because

\[
                         \gcd(m,2m+1)=1.
\tag{7.1}

One clean C6 uses six owners.  For two cyclic translates to meet, some
ordered pair of its six owners must be related by the chosen rotation.
Each ordered pair forbids at most one rotation.  Therefore at most 36 of
the `2m+1` translates meet a fixed copy.

### Corollary 7.1

For `2m+1>36` (in particular `m>=18`), every angle connector in Theorem
6.1 has two physically vertex-disjoint cyclic lifts on the same component
triple.

This is the exact local two-rail supply requested by the rigid-split
topology theorem.  It is not yet a simultaneous packing theorem for a
spanning family of angle connectors: many C6s can reuse a promoted hook
component, and their cut orders must still be coordinated.

## 8. Scope

Proved here:

1. a literal selected q1/q2-neutral C6 for every rooted base-hook angle;
2. its exact action on hook angles as one adjacent chip transfer;
3. connectedness of the entire hook-angle section of the connector
   hypergraph;
4. two disjoint physical rotations of each individual connector for all
   sufficiently large dimensions.

Not proved here:

1. a simultaneous loose forest through all hook tori;
2. compatibility of the many promoted-hook auxiliary components;
3. q3, residence, arbitrary upper, or common-cap preservation;
4. the all-dimensional `B(k)+O(1)` bound.
