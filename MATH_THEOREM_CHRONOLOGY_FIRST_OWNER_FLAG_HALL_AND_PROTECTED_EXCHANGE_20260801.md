# Chronology-first owner/flag Hall and protected attachment exchange

**Date:** 2026-08-01  
**Status:** exact reduction and exact sufficient exchange theorems.  This
does not assert that the required `k=17` flag table exists.

## 0. Verdict

Fix one rooted suffix-flag table which is already exact on every named
strict-lower colour.  The remaining owner/chronology problem can be written
without first freezing one of the nine owner attachments at every root.

For every possible attachment of a root `q` to an owner `o`, record the set
`P(q,o)` of flagged roots which can literally precede `q`.  An owner
attachment perfect matching `D` chooses one such column at every root.  The
chosen columns form an ordinary bipartite predecessor graph `B_D`.

The following are equivalent:

1. the fixed flag table admits a one-per-root, one-per-owner literal
   directed cycle cover;
2. some owner attachment perfect matching `D` makes `B_D` satisfy Hall;
3. some perfect matching `D` in the root--owner incidence graph satisfies

   \[
      D({\cal A}_X)\ge |X|\qquad(X\subseteq R),
   \]

   where `${\cal A}_X` is the set of attachment columns having at least one
   legal predecessor in `X`.

This is the chronology-first owner/flag Hall theorem below.  It keeps every
named lower palette exact because the flags themselves never move.

There is also a literal augmentation theorem.  Starting from an attachment
matching `D` and a maximum predecessor matching `M`, build the ordinary
alternating-cycle exchange digraph of `D`, but retain an exchange arc only
when it preserves the `M`-edge at that root.  If an unmatched head can take
an attachment seeing the Dulmage--Mendelsohn reachable tail shore and that
attachment can be returned to its old owner through protected exchange
arcs, toggling the resulting owner cycle creates an augmenting path.  Thus
the chronology matching grows by one while the complete named lower flag
table remains unchanged.

The frozen `k=17` rooted tables fail before this mechanism: some root is a
universal singleton Hall cut, having no legal successor under any of its
nine attachments.  No owner-only alternating cycle can repair such a row;
one must use a palette-neutral trade of the rooted flags themselves.

## 1. Rooted flags and attachment columns

All objects below may be literal objects or aligned quotient occurrences.
In the quotient interpretation parallel phase-labelled incidences are kept
as distinct columns.

Let `R` be the set of rooted `(r-1)`-sets and `O` the set of rank-`r`
owners, with

\[
                         |R|=|O|=N.
\]

Let `I` be their aligned containment multigraph.  For `k=17`, `N=1430`
and `I` is 9-regular on both shores.

At every root `q` fix a complete rooted flag

\[
 q=C^q_0\mathbin{\dot\cup}C^q_1\mathbin{\dot\cup}\cdots
      \mathbin{\dot\cup}C^q_{d-1}.                 \tag{1.1}
\]

Assume that, over all roots, the required suffixes

\[
 C^q_0,\quad C^q_0\cup C^q_1,\quad\ldots,\quad
 C^q_0\cup\cdots\cup C^q_{d-1}=q                 \tag{1.2}
\]

have the prescribed named multiplicities.  In the exact `k=17` face each
required lower necklace occurs once.

An **attachment column** `a` consists of an aligned incidence

\[
                    q(a)\subset o(a).               \tag{1.3}
\]

Its missing singleton `o(a)-q(a)` is the oldest class of the state at its
head root.

For such a column define `P_F(a) subseteq R` to be the set of aligned roots
`p` for which the literal transition from the fixed flag at `p` to the
fixed flag at `q(a)`, with incoming owner `o(a)`, is legal.  In a common
literal gauge this means

\[
 o(a)=p\cup q(a),                                   \tag{1.4}
\]

\[
 o(a)-q(a)\subseteq C^p_{d-1},                     \tag{1.5}
\]

and

\[
 C^{q(a)}_{i+1}\subseteq C^p_i
       \qquad(0\le i<d-1).                          \tag{1.6}
\]

The entering coordinate and the age-zero refresh identity are then forced
by the two complete partitions.  For `d=3`, (1.5)--(1.6) are exactly the
three survivor containments in the authenticated nine-attachment audit.

Write `${\cal A}(q)` for the attachment columns rooted at `q`, and
`${\cal A}` for their union.  A set `D subseteq {\cal A}` is an **owner
transversal** when

\[
 |D\cap{\cal A}(q)|=1\quad(q\in R),\qquad
 |\{a\in D:o(a)=o\}|=1\quad(o\in O).               \tag{1.7}
\]

Thus `D` is simply a perfect matching of `I`, with parallel aligned
incidences retained.

Given `D`, form the predecessor graph

\[
 B_D=(R^-,R^+;E_D),                                 \tag{1.8}
\]

where

\[
 p^-q^+\in E_D
 \quad\Longleftrightarrow\quad
 p\in P_F(D(q)).                                    \tag{1.9}
\]

Here `D(q)` is the unique selected attachment column at `q`.

## 2. Chronology-first owner/flag Hall theorem

For `X subseteq R^-`, put

\[
 N_D(X)=\{q\in R:P_F(D(q))\cap X\ne\varnothing\}. \tag{2.1}
\]

Also define the attachment-column cover

\[
 {\cal A}_X=
 \{a\in{\cal A}:P_F(a)\cap X\ne\varnothing\}.     \tag{2.2}
\]

### Theorem 2.1 (owner/flag Hall)

For a fixed exact rooted flag table `F`, the following are equivalent.

1. There is a literal directed cycle cover which uses every root once as a
   tail and once as a head, and every owner once.
2. There is an owner transversal `D` for which `B_D` has a perfect
   matching.
3. There is an owner transversal `D` such that

   \[
                D({\cal A}_X)\ge |X|
                \qquad(X\subseteq R).               \tag{2.3}
   \]

Every object in these equivalent statements retains all named lower
palettes certified by (1.2).

#### Proof

Let `D` be an owner transversal and let `M` be a perfect matching in
`B_D`.  Direct `p` to `q` when `p^-q^+ in M`, and colour the directed edge
by `o(D(q))`.  Every root has one outgoing and one incoming edge.  Equation
(1.7) uses every owner exactly once, while (1.9) makes every transition a
literal survivor turn.  The resulting permutation of `R` is the desired
directed cycle cover.

Conversely, attach to each head root the owner of its incoming turn.  The
owner colours are exact, so these attachments form an owner transversal
`D`; the directed turns form a perfect matching in `B_D`.

For fixed `D`, Hall says that `B_D` has a perfect matching exactly when
`|N_D(X)|>=|X|` for every `X`.  Because `D` contains exactly one column at
each head root,

\[
 |N_D(X)|
 =|\{q:D(q)\in{\cal A}_X\}|
 =D({\cal A}_X).                                    \tag{2.4}
\]

This proves the equivalence.  The flag at every root is unchanged and every
root is used once, so the named suffix multiset (1.2) is unchanged. `square`

The selected permutation may have several cycles.  Hamiltonicity requires
the usual proper directed subtour cuts.  In a cyclic quotient, nonzero
voltage and an upper-safe opening remain separate downstream conditions.

### Corollary 2.2 (exact owner-choice polytope)

Introduce one variable `z_a` per attachment column.  A literal cycle cover
exists if and only if the following system has a `0,1` solution:

\[
\begin{aligned}
 \sum_{a\in{\cal A}(q)}z_a&=1 &&(q\in R),\\
 \sum_{a:o(a)=o}z_a&=1 &&(o\in O),\\
 \sum_{a\in{\cal A}_X}z_a&\ge |X| &&(X\subseteq R),\\
 z_a&\in\{0,1\}.                                    \tag{2.5}
\end{aligned}
\]

For a fixed fractional `z`, the cut function

\[
 f_z(X)=\sum_{a\in{\cal A}}z_a
             {\bf1}_{P_F(a)\cap X\ne\varnothing}  \tag{2.6}
\]

is a weighted coverage function and hence submodular.  Therefore separation
of the relaxed cuts `f_z(X)>=|X|` is a submodular minimization problem.
This gives an exact fractional oracle.  It does **not** make (2.5) integral:
when every predecessor set is a singleton, (2.5) already contains the
three-index assignment/Latin-transversal problem.

## 3. A second exact formulation and one sufficient integrality condition

Form the tripartite turn hypergraph

\[
 {\cal H}_F\subseteq R^-\times R^+\times O          \tag{3.1}
\]

with an atom `(p,q,o)` whenever there is an attachment column `a` at `q`
with `o(a)=o` and `p in P_F(a)`.  Parallel phase labels may be retained on
atoms and forgotten only for support.

### Proposition 3.1

The fixed flag table has a literal owner-exact directed cycle cover if and
only if `${\cal H}_F` has a perfect matching.

This is just Theorem 2.1 with the attachment and predecessor choices made
simultaneously.  It also shows why no ordinary Hall theorem can hold for
arbitrary flag tables: general rainbow bipartite matching, equivalently
three-dimensional matching, is already a special case.

There is nevertheless a clean proof-grade sufficient condition.  Let `A_F`
be the vertex--atom incidence matrix of `${\cal H}_F`.

### Theorem 3.2 (balanced-turn rounding)

Suppose:

1. `A_F` is balanced (it has no odd square submatrix with exactly two ones
   in every row and column); and
2. `${\cal H}_F` has a fractional perfect matching.

Then `F` admits a literal owner-exact directed cycle cover.

#### Proof

For a balanced `0,1` matrix the set-packing polytope

\[
             \{x\ge0:A_Fx\le{\bf1}\}               \tag{3.2}
\]

is integral.  A fractional perfect matching has total weight `N`, by
summing its equations over the tail-root shore.  No packing has weight more
than `N`.  Hence (3.2) has an integral optimum of weight `N`.  Its `N`
disjoint tripartite atoms saturate all `N` vertices in each shore and form
a perfect matching.  Apply Proposition 3.1. `square`

Balancedness is a sufficient structural target, not a property currently
proved for the Boolean turn hypergraph.

## 4. Palette-preserving alternating owner repair

The preceding formulations identify a particularly small exact repair
move.  Fix an owner transversal `D` and a maximum matching `M` in `B_D`.
Orient every unmatched edge of `B_D` from `R^-` to `R^+` and every matched
edge from `R^+` to `R^-`.  Let

\[
 U^- = R^--V^-(M),\qquad U^+=R^+-V^+(M),            \tag{4.1}
\]

and let `X subseteq R^-` be the tail vertices reachable from `U^-` by
alternating paths.  Since `M` is maximum, no vertex of `U^+` is reachable.

Build the **`M`-protected owner exchange multidigraph** `E_(D,M)` on the
owner shore.  The current owner `o=D(q)` has an arc to an alternative
attachment column at owner `o'` through head `q` when that column exists
and either

* `q` is matched in `M`, say by `p^-q^+`, and
  `p in P_F(q,o')`; or
* the arc is explicitly marked as an augmenting arc at an unmatched head.

The first kind preserves the current `M`-edge at `q`.  Parallel attachment
columns remain distinct labelled arcs.  In particular a loop `o->o` may
replace the selected phase by another phase at the same root and owner.
Because `D` is a perfect matching, every owner `o` has a unique head
`q=D^{-1}(o)`; hence a nonloop directed owner cycle uses distinct heads and
is exactly a `D`-alternating cycle switch in the root--owner incidence
graph.  A labelled loop is the corresponding one-column parallel switch.

### Theorem 4.1 (protected attachment-cycle augmentation)

Assume `M` is not perfect.  Suppose there are

* an unmatched head `h in U^+`;
* an alternative attachment column `a` of `h`, with owner `o_1` (possibly
  `o_1=o_0` through a different aligned phase), satisfying

  \[
                    P_F(a)\cap X\ne\varnothing;     \tag{4.2}
  \]

* a directed path in the protected owner exchange multidigraph from `o_1`
  back to `o_0=D(h)`, not using the special head `h`; when `o_1=o_0`, the
  empty return path is allowed.

Then an owner-alternating cycle switch produces a new owner transversal
`D'` for which

\[
                  \nu(B_{D'})\ge\nu(B_D)+1.         \tag{4.3}
\]

Every named lower palette remains exact.

#### Proof

Prepend the special exchange `o_0 -> o_1` through `h` to the protected
return path.  This is a directed owner cycle.  Toggle `D` around it.  Every
head and owner on the cycle is used once after the toggle, so `D'` remains
an owner transversal.

Every old `M`-edge survives: heads outside the cycle are unchanged, heads
on the return path satisfy the protected-arc condition, and `h` was
unmatched.  Choose `x in P_F(a) cap X`.  By the definition of `X`, an
alternating path starts at an unmatched tail and ends at `x`.  Under `D'`
the new edge `x^-h^+` exists, and `h` is an unmatched head.  Appending this
edge to the alternating path and toggling it augments `M` by one.  The
rooted flags were not changed, so (1.2) remains exact. `square`

### Corollary 4.2 (exchange-complete sufficient condition)

If the hypothesis of Theorem 4.1 holds for every nonperfect pair `(D,M)`,
then the fixed exact flag table has an owner-exact directed cycle cover.

At most `N` augmentations are needed.  The moves consume no new resource:
they reconfigure the same owner matching and may reuse attachments later.

A convenient stronger hypothesis is:

1. the protected owner exchange digraph is strongly connected for every
   nonperfect `(D,M)`; and
2. for its reachable shore `X`, some unmatched head has some attachment
   column whose predecessor set meets `X`.

The first condition closes the return path and the second supplies the
special augmenting arc.

## 5. Why the frozen rooted-table obstruction is decisive for owner-only repair

Call a tail root `p` **universally dead** when

\[
          p\notin P_F(a)\qquad\text{for every attachment column }a.
                                                               \tag{5.1}
\]

Then `${\cal A}_{\{p\}}` is empty, so (2.3) fails for every owner
transversal `D`.  Equivalently `p^-` is isolated in every `B_D`.

The authenticated `k=17` full-static and rooted-static audits exhibit
exactly this phenomenon (with hundreds of zero-out roots, and an explicit
root `0` singleton witness).  Thus varying the nine attachments or taking
owner-alternating cycles cannot repair those particular tables.  The flags
must be changed jointly with the chronology.

## 6. Palette-neutral flag trades

Let `G` be the set of allowed rooted flags before one table is selected.
Make a resource--flag incidence matrix `A_low` whose rows record

* one flag at every root;
* every named strict-lower suffix colour; and
* the required type quotas.

An exact static table is a `0,1` vector `f` satisfying

\[
                         A_{low}f=b.                 \tag{6.1}
\]

A **palette-neutral flag trade** is an integer vector `g` such that

\[
 A_{low}g=0,qquad f+g\in\{0,1\}^{G}.               \tag{6.2}
\]

It changes literal flags while preserving every named lower palette and
every type count.  Differences of exact tables lie in the integer kernel
of `A_low`; conformal Graver moves give the canonical complete exchange
language, although their support is not known to be bounded.

### Theorem 6.1 (joint protected repair)

Let `(F,D,M)` be as above.  Suppose a palette-neutral trade and an
owner-alternating cycle produce `(F',D')` such that

1. every edge of `M` remains a legal flagged turn; and
2. for the old alternating reachable shore `X`, an unmatched head gains a
   predecessor in `X`.

Then `B_(F',D')` has a matching larger than `M`, while all named lower
palettes remain exact.

The proof is the last paragraph of Theorem 4.1; (6.2) supplies palette
preservation.  Iterating this statement gives a cycle cover whenever every
positive-deficiency state admits such a joint move.

This is the exact exchange theorem missing from an ownerwise construction.
It does not assert that the required bounded or regenerating trades exist.

## 7. Why ownerwise random flags fail

There are two independent failures.

First, independent sampling does not respect named palettes.  If a rank
has `m` required colours and `m` independently uniform emitted occurrences,
the probability that they form a bijection is

\[
                         {m!\over m^m}
          =\exp(-m+O(\log m)).                       \tag{7.1}
\]

For the central quotient ranks, `m` is already exponential in `k`.
Conditioning separately at each rank does not restore the nesting of the
suffix flags.

Second, independently sampled age flags almost never turn literally.  In
the hub type

\[
                    (r-d,1,1,\ldots,1),             \tag{7.2}
\]

a rooted flag has an ordered rail of `d-1` singleton age classes.  Once a
source flag and an adjacent target root are fixed, literal survival forces
all but at most the first singleton of the target rail.  Among
`(r-1)_(d-1)` possible ordered target rails, at most `r` are compatible.
Thus

\[
 \Pr(\text{literal turn})
       \le {r\over (r-1)_{d-1}}
       =\exp(-\Omega(d\log r)).                     \tag{7.3}
\]

There are only polynomially many adjacent root/attachment candidates per
root.  With `d=Theta(sqrt(k))`, the expected legal degree under independent
flags tends to zero.  The many dead rows in the finite `k=17` tables are
therefore the expected failure mode, not evidence that the nine attachment
choices were searched inadequately.

A viable random construction must reverse the quantifiers: generate flags
along literal turns, so survivor compatibility is automatic, and then
round the resulting correlated circulation while keeping the named suffix
palettes exact.

## 8. What can and cannot yet be proved asymptotically

The stationary pull-clock/rotor results supply fractional correlated age
flow.  They do not supply one labelled root and owner occurrence each, nor
an exact named-palette table in the same circulation.  Therefore they do
not currently imply a fractional perfect matching in `${\cal H}_F` for
some single exact `F`.

Either of the following would be a proof-grade asymptotic bridge:

1. **balanced correlated rounding:** construct an exact palette table `F`
   for which `${\cal H}_F` is balanced and fractionally perfect; Theorem
   3.2 then rounds it exactly;
2. **exchange-complete correlated rounding:** prove that palette-neutral
   flag trades together with protected owner cycles satisfy Theorem 6.1 at
   every positive-deficiency state; finite descent then gives an exact
   cycle cover.

The second target is weaker in spirit: it needs only one protected crossing
of the current DM shore, not random-like expansion of the entire turn
hypergraph.  For the GKS-based factorization, the candidate flag trades are
alternating cycles/paths in the central containment matching followed by
the exact low-colour transversal repair.  What remains unproved is that one
such composite trade always crosses the current shore while preserving the
already matched turns.

Consequently, a correlated flag-turn matching is plausible but is **not
yet proved asymptotically**.  The exact frontier is now the protected
crossing statement of Theorem 6.1, rather than ownerwise random expansion
or another search over the nine attachments of a frozen table.
