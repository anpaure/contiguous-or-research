# Endpoint monodromy obstructs the natural paired-alpha braid

## 1. Outcome

The most economical proposed globalization of the local ECO coordinate
roles was to use an MNW `alpha` switch at one boundary and its antipodal
copy at a second boundary.  This does **not** preserve complementary path
endpoints.

The obstruction is an elementary permutation invariant.  A switch through
an `alpha` 6-cycle cyclically permutes three path tails.  The antipodal copy
has the same orientation and therefore induces the same 3-cycle, not its
inverse.  Two such boundaries have endpoint monodromy `pi^2 != id`.

There are two useful strengthenings.

1. The reverse-complement `alpha` pattern is the natural candidate for the
   opposite local orientation, but it lives on a different triple of Dyck
   roots.  Even if oriented inversely, it is not an inverse boundary on the
   same three strands.
2. More generally, a loose-tree schedule of single `alpha` boundaries can
   never be endpoint-safe: a leaf strand is moved by its unique incident
   switch and can never be restored.  Pairing every tree hyperedge with its
   antipodal copy still fails, because a leaf is acted on twice by the same
   3-cycle.

Thus the known loose spanning trees of flipping tuples, which are ideal for
joining cycles into a Hamilton cycle, cannot be reused as a factor-preserving
antipodal braid.  Any surviving construction must contain genuine
monodromy cycles, use an inverse boundary created after a state change, or
use at least three compatibly phased copies of a 3-cycle.  This is precisely
the noncommutative step which the current Catalan schedule does not provide.

## 2. Endpoint monodromy

Let

\[
 P_i:s_i\leadsto t_i\qquad(1\le i\le r)
\]

be vertex-disjoint oriented paths.  Assume the terminal endpoints are all
distinct.  At a transversal boundary, cut every participating path once and
reconnect the left strands to the right strands according to a permutation
`pi` of their labels.  Several such boundaries may be performed, in a common
left-to-right order along the evolving strands.

### Lemma 2.1 (monodromy product)

If the successive boundary permutations are

\[
                         \pi_1,\pi_2,\ldots,\pi_h,
\]

then the path beginning at `s_i` ends at

\[
                    t_{\Pi(i)},\qquad
                    \Pi=\pi_h\pi_{h-1}\cdots\pi_1.       \tag{2.1}
\]

In particular, if initially `t_i=bar(s_i)` for distinct antipodal pairs,
then the final paths retain those antipodal endpoint pairs if and only if

\[
                              \Pi=\operatorname{id}.      \tag{2.2}
\]

#### Proof

After the first boundary, the strand from `s_i` follows the old right strand
labelled `pi_1(i)`.  At the next boundary its label becomes
`pi_2(pi_1(i))`, and induction gives (2.1).  Under the antipodal hypothesis,
the unique terminal endpoint complementary to `s_i` is `t_i`; hence (2.2)
is necessary and sufficient.  \(\square\)

This lemma is independent of the internal lengths of the exchanged
segments and of the graph in which the paths live.  It is the topological
part of every endpoint-safe segment braid.

## 3. The `alpha` boundary has order three

The parameterized MNW flipping tuple is

\[
 \alpha(w)=
 \{1w11000,\ 1w10100,\ 1w10010\}.                  \tag{3.1}
\]

Its alternating 6-cycle meets the three corresponding factor cycles in one
edge each.  Taking symmetric difference with that 6-cycle removes those
three factor edges and inserts the other three edges of the 6-cycle.  On
oriented tails this is one of the two cyclic permutations

\[
                              \pi=(1\ 2\ 3)
             \quad\hbox{or}\quad \pi^{-1}=(1\ 3\ 2).              \tag{3.2}
\]

It is never a transposition or the identity: the switch joins the three
cycles cyclically into one component.

### Proposition 3.1 (the antipodal mate has the wrong orientation)

Take a second copy of the same local boundary at the antipodal translate
of the three oriented factor cycles.  The complement half-turn preserves
the cyclic orientation of every strand, so the second boundary induces the
same permutation `pi` as the first.  The two-boundary monodromy is

\[
                              \pi^2=\pi^{-1}\ne\operatorname{id}.   \tag{3.3}
\]

Consequently an `alpha` switch and its natural antipodal copy do not form an
endpoint-safe braid.

#### Proof

The antipodal translate changes every local vertex and edge by the same
half-turn, without reversing the order in which the three oriented strands
enter and leave the boundary.  It therefore preserves the cyclic
reconnection order (3.2).  Lemma 2.1 gives (3.3).  \(\square\)

The distinction between "same boundary at the antipode" and "inverse
boundary" is essential.  An endpoint-safe two-boundary braid requires
`pi` followed by `pi^(-1)`, as in the abstract double switch of
`MSW_OUTER_DEPTH_ONE_DICHOTOMY.md`; antipodal translation supplies `pi`
followed by `pi`.

## 4. The mirror inverse is on different strands

Reverse-complement is the canonical way to reverse the local picture.  The
mirrored support of (3.1), writing `u=mu(w)`, is

\[
 \mu(\operatorname{supp}\alpha(w))=
 \{10110u0,\ 11010u0,\ 11100u0\}.                  \tag{4.1}
\]

It cannot equal the original support.

### Lemma 4.1 (support mismatch)

For every Dyck word `w`,

\[
             \operatorname{supp}\alpha(w)
                \ne \mu(\operatorname{supp}\alpha(w)).           \tag{4.2}
\]

#### Proof

The three words in (3.1) have final-descent lengths respectively

\[
                                  3,\ 2,\ 1.                        \tag{4.3}
\]

All three words in (4.1) have the same final-descent length

\[
                                  \ell(u)+1.                        \tag{4.4}
\]

The multisets (4.3) and (4.4) are different, proving (4.2).  \(\square\)

Thus, even when the mirrored boundary is oriented as the desired inverse,
it acts on another triple of owner paths.  It cannot be placed as the
second boundary of a local three-strand braid without first rerouting
ownership between the two triples.  That rerouting is the missing global
operation, not a consequence of the base `alpha` identity.

## 5. Loose-tree obstruction

Let `H` be a 3-uniform hypergraph whose vertices label factor paths and
whose hyperedges are available `alpha` boundaries.  A schedule chooses
some boundary occurrences and hence applies a 3-cycle to the tails at each
chosen hyperedge.

### Theorem 5.1 (leaf obstruction)

Suppose the incidence support of a nonempty schedule has a vertex `v`
belonging to exactly one selected boundary occurrence.  Then the schedule
is not endpoint-safe.

If the unique incident hyperedge is used together with one natural
antipodal copy, the schedule is still not endpoint-safe.

#### Proof

At one occurrence, the tail of `v` is sent to a different strand by the
nontrivial 3-cycle (3.2).  No later boundary involves `v`, so it cannot
return.  With one antipodal copy, Proposition 3.1 says that the same
3-cycle is applied twice; `pi^2` also moves every point.  Lemma 2.1 now
proves both claims.  \(\square\)

### Corollary 5.2

A nonempty loose hypertree of `alpha` boundaries is not an endpoint-safe
factor trade.  Nor does it become endpoint-safe by adjoining the natural
antipodal copy of every tree hyperedge.

#### Proof

Every finite nonempty loose hypertree has a leaf vertex.  Apply Theorem
5.1.  \(\square\)

This explains the precise mismatch between the Hamilton-cycle literature
and the present problem.  A loose spanning tree is designed so that each
new hyperedge introduces fresh leaf cycles and merges all factor cycles.
Endpoint-safe factor surgery requires the opposite topology: every moved
strand must lie on a closed monodromy dependency.

## 6. What remains possible

The obstruction is sharp.  It does not rule out:

1. three same-orientation occurrences on the same strands, since
   `pi^3=id`;
2. a genuine inverse boundary on the same strands;
3. a cyclic network of distinct flipping tuples whose permutation product
   is the identity at every owner; or
4. a noncommutative schedule which performs preparatory switches, recomputes
   owner triples, and only then creates the inverse boundary.

But none of these is supplied by the static ECO parent schedule or by the
known loose spanning tree.  In particular, an all-dimensional positive
theorem must establish an **endpoint-balanced hypergraph circulation**, not
merely connectivity or a spanning tree.

Combining this note with `MSW_ECO_INSERTION_AUDIT.md` and
`MSW_OUTER_DEPTH_ONE_DICHOTOMY.md` gives a clean fork:

* the unchanged fixed-coordinate MSW outer lift is already impossible at
  depth one;
* the natural paired-alpha repair is obstructed by endpoint monodromy; and
* the Mütze--Weber route still requires an endpoint-moving alternating
  circulation which is genuinely global and state-dependent.

In the signed `T`-join language of `MUTZE_WEBER_ENDPOINT_TJOIN.md`, the
alternating trails therefore cannot be supported on a loose tree of static
`alpha` charts.  Their chart-incidence support must contain enough cycles
to make every strand's permutation product trivial, in addition to
satisfying the ordinary degree boundary equations.  Total unimodularity of
the signed incidence system does not enforce this nonabelian monodromy
condition.
