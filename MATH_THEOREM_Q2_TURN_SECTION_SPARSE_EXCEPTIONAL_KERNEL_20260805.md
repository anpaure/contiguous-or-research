# The q2 turn-section gate has an exact Catalan-scale exceptional kernel

**Date:** 2026-08-05  
**Method:** pure counting and occurrence-labelled constraint reduction; no
computation, search, solver, or probabilistic input  
**Status:** unconditional exact reduction.  It does not prove that the
kernel is always feasible.

## 1. Setup

Let

\[
 Y_0,Y_1,\ldots,Y_{P-1}\in{\Gamma\choose r-2},
 \qquad |\Gamma|=2r-1,
\]

be the cyclic lower-turn word of a middle-levels Hamilton cycle, and assume
that every rank-`(r-2)` label occurs.  Put

\[
 Q={2r-1\choose r-2},\qquad
 \kappa=P-Q=\operatorname {Cat}_r.
\tag{1.1}
\]

For a label `Y`, let `O(Y)` be its set of occurrence positions and put
`m(Y)=|O(Y)|`.  Thus

\[
 \sum_Y(m(Y)-1)=\kappa.                            \tag{1.2}
\]

Retain an adjacent index `i` as a **q2 witness** only when
`Y_i\ne Y_(i+1)`.  It then has the rank-`(r-3)` colour

\[
 D(i)=Y_i\cap Y_{i+1}.                            \tag{1.3}
\]

For each `D in binom(Gamma,r-3)`, let

\[
 E_D=\{i:D(i)=D\}.                                \tag{1.4}
\]

Assume q2 surjectivity, namely `E_D` is nonempty for every `D`.  A
q2-complete turn section is equivalent to choosing one occurrence of every
`Y` so that every `D` has a witness whose two endpoint occurrences were
chosen.

The purpose of this note is to show that all genuine choice is confined to
only Catalan-many repeated occurrences and Catalan-many q2 classes.

## 2. Repeated occurrences form a small exceptional set

Let

\[
 \mathcal R=\{Y:m(Y)\ge2\},\qquad
 H=\bigcup_{Y\in\mathcal R}O(Y),\qquad h=|H|.
\tag{2.1}
\]

### Lemma 2.1 (exact surplus bounds)

\[
 |\mathcal R|\le\kappa,
 \qquad
 h=|\mathcal R|+\kappa\le2\kappa.                 \tag{2.2}
\]

#### Proof

Every repeated label contributes at least one to (1.2), so
`|mathcal R|<=kappa`.  Moreover

\[
 h=\sum_{Y\in\mathcal R}m(Y)
  =|\mathcal R|+\sum_{Y\in\mathcal R}(m(Y)-1)
  =|\mathcal R|+\kappa.
\]

This proves (2.2). \(\square\)

Call a q2 colour `D` **clean** if some index `i in E_D` has both endpoint
labels occurring uniquely in the whole turn word.  Otherwise call `D`
**exceptional**.

### Lemma 2.2 (at most four Catalan-many exceptional colours)

The number of exceptional q2 colours is at most

\[
                         2h\le4\kappa.             \tag{2.3}
\]

The total number of witness indices belonging to exceptional classes is
also at most `2h`.

#### Proof

Every witness for an exceptional colour touches a position in `H`; otherwise
its two endpoint labels would both be unique and the colour would be clean.
In the cyclic position graph, the `h` positions of `H` are incident with at
most `2h` adjacent indices.  Every exceptional witness is among those
indices. \(\square\)

Clean colours require no coordination: choose any clean witness.  Its
endpoint labels have only one occurrence each, so it is compatible with
every other possible section choice.

## 3. Exact positive two-local CSP

For each repeated label `Y`, introduce a variable

\[
                         a_Y\in O(Y).              \tag{3.1}
\]

For a witness index `i`, define the positive term

\[
 T_i(a)=
 \bigwedge_{Y\in\{Y_i,Y_{i+1}\}\cap\mathcal R}
            [a_Y=\text{the endpoint occurrence of }Y\text{ in }i].
\tag{3.2}
\]

Thus `T_i` contains zero, one, or two equalities.  A zero-equality term is
exactly a clean witness.

### Theorem 3.1 (sparse exceptional-kernel equivalence)

The turn word has a q2-complete section if and only if the following positive
two-local CSP is feasible:

\[
 \boxed{
 \exists(a_Y)_{Y\in\mathcal R}\in\prod_{Y\in\mathcal R}O(Y)
 \quad
 \forall D\text{ exceptional},\quad
 \bigvee_{i\in E_D}T_i(a).
 }
\tag{3.3}
\]

This instance has at most

\[
 \kappa\text{ variables},\qquad
 2\kappa\text{ total domain values},\qquad
 4\kappa\text{ constraints},\qquad
 4\kappa\text{ witness terms}.                   \tag{3.4}
\]

#### Proof

Given a q2-complete section, let `a_Y` be its chosen occurrence for every
repeated label.  The selected witness for each exceptional `D` then makes
one term in (3.3) true.

Conversely, suppose (3.3) is feasible.  Select occurrence `a_Y` for every
repeated label and the unique occurrence of every other label.  For an
exceptional `D`, a true term supplies a witness whose endpoint occurrences
are selected.  For a clean `D`, its fixed clean witness has two unique
endpoints and is therefore also selected.  Hence every q2 colour is witnessed
by an adjacent selected pair, which is precisely a q2-complete section.

The variable and domain bounds are Lemma 2.1.  Lemma 2.2 bounds both the
number of exceptional classes and all of their witness terms. \(\square\)

## 4. Singleton propagation leaves fewer than three Catalan-many classes

Let

\[
 M={2r-1\choose r-3}.
\tag{4.1}
\]

If `A` is the number of retained unequal adjacent indices, q2 surjectivity
gives

\[
 \sum_D(|E_D|-1)=A-M\le P-M.                      \tag{4.2}
\]

The binomial and Catalan identities give the exact value

\[
 P-M
 =\frac{6rP}{(r+1)(r+2)}
 =\frac{3r}{r+2}\,\kappa
 <3\kappa.                                        \tag{4.3}
\]

### Corollary 4.1 (forced-core reduction)

Every original singleton class `E_D={i}` forces the occurrence choices at
its repeated endpoints.  If two such forces disagree, no q2-complete section
exists.  If they agree, substitute them, delete satisfied classes, delete
incompatible witness terms, and repeat whenever a remaining constraint has
only one surviving witness term.

After this unit propagation stabilizes, the residual CSP still has the exact
equivalence (3.3), but it contains fewer than `3 kappa` constraint classes.
Together with (3.4), its complete occurrence-labelled size is `O(kappa)`.

#### Proof

A singleton class has only one possible witness, so its endpoint choices are
necessary.  Substitution therefore preserves equivalence.  Initially the
number of nonsingleton classes is at most

\[
 \sum_D(|E_D|-1)=A-M<3\kappa.
\]

Unit propagation can only remove classes and witness terms, never create a
new class. \(\square\)

## 5. What this proves and what remains

The q2 section gate is not a generic exponentially large independent-
transversal problem.  Once q2 surjectivity of the turn word is known:

* all labels outside at most `kappa` repeated-label fibres are forced;
* every q2 colour with a unique-unique witness is automatically harmless;
* every genuine incompatibility lies in an explicit positive two-local CSP
  on at most `2 kappa` occurrence values and at most `4 kappa` witness terms;
* after forced singleton propagation, fewer than `3 kappa` q2 classes remain.

This is a strict kernelization, not an existence proof.  In particular, two
singleton q2 classes can force different occurrences of the same repeated
turn label, giving a real obstruction.  An all-dimensional construction must
therefore arrange compatibility inside this Catalan-scale exceptional core;
ordinary large-list Haxell or local-lemma estimates cannot see the forced
singleton mechanism.
