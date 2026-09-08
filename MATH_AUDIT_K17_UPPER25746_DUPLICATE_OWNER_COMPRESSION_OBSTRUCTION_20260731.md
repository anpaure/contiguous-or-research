# The (K=17) lifted word: duplicate-owner census and an opposite-choice obstruction

Date: 2026-07-31  
Status: exact scoped theorem and literal replay; no global (K=17) no-go

## 1. Scope and source

The source is the authenticated literal word

```text
answers/k17_upper25746.word
```

of length (25,746), SHA-256

```text
f8ea81ab1f8f1280f638e7e607b32a7dd53fc541b30fe1005db8aae692be031b.
```

It is the one-coordinate lift of the exact (K=16) word, as defined and
verified in `MATH_THEOREM_K17_EXPLICIT_25746_UPPER_20260731.md`.  The earlier
theorem records the length gap (25,746-B(17)=1433); it does not define
that number as an owner count.  The audit accompanying this note is an
independent literal derivation of the owner count.

The obstruction below concerns the following natural but restricted
compression model:

1. retain the existing first-rank-nine occurrences of this fixed word;
2. select exactly one occurrence for each rank-nine label;
3. demand that rank-ten targets remain consecutive unions in the selected
   rank-nine owner word.

This is precisely the upper-transfer gate one would need before applying a
fixed-owner common-cap compiler.  It is not a no-go for changing letters,
changing first-middle labels, or rethreading the carrier.

## 2. Exact meaning of a first-middle owner

For a physical start (s), put

\[
 U(s,q)=\bigvee_{p=s}^{q}A_p
\]

and let

\[
 F_s=\min\{q\ge s:|U(s,q)|\ge9\},
\]

when this set is nonempty.  Start (s) has a **first-middle owner** iff

\[
 |U(s,F_s)|=9.
\]

Its occurrence is the triple

\[
               (s,F_s,T_s),\qquad T_s=U(s,F_s).
\]

If the first crossing jumps from rank below nine to rank above nine, or the
suffix never reaches rank nine, the start is ownerless.  This is the literal
first-middle definition from the deadline-staircase normal form; it is not
an arbitrarily chosen witness interval.

The replay gives

\[
 \begin{array}{c|r}
 \text{first-middle occurrences}&25,743\\
 \text{distinct rank-nine labels}&24,310=\binom{17}{9}\\
 \text{ownerless starts}&3\quad(25743,25744,25745)\\
 \text{repeat excess}&25,743-24,310=1,433.
 \end{array}
\]

The exact label-multiplicity histogram is

\[
 1^{22979},\qquad2^{1230},\qquad3^{100},\qquad4^1.
\]

The lift decomposition is also exact:

* labels not containing the new coordinate have (12,869) occurrences,
  (11,440) distinct labels, and repeat excess (1,429);
* labels containing the new coordinate have (12,874) occurrences,
  (12,870) distinct labels, and repeat excess (4).

Thus the numerical equality with the certified length gap is genuine, but
it is only a counting identity.  It does not identify repeated owner
occurrences with deletable physical letters.

## 3. Exact adjacency-viability lemma

Let every rank-nine label (T) have a finite set (O(T)) of occurrences
on a line.  A transversal chooses exactly one member of every (O(T)).

### Lemma 3.1

Let (a<b) be occurrences of distinct labels (A,B).  There is a
transversal in which (a,b) are consecutive selected occurrences iff no
third label (C\notin\{A,B\}) has

\[
                         O(C)\subset(a,b).
\tag{3.1}
\]

#### Proof

If (3.1) holds for some (C), every choice for (C) lies strictly between
(a) and (b), so the two endpoints cannot be consecutive.

Conversely, if (3.1) fails for every third label, choose (a) for (A),
(b) for (B), and for every other label independently choose one
occurrence outside ((a,b)).  The resulting transversal contains no
selected occurrence strictly between (a) and (b).  Hence they are
consecutive. \(\square\)

This is an iff criterion, not a necessary-only pruning test.

### Lemma 3.2

Let (V) have rank ten.  A one-occurrence-per-label owner word represents
(V) as a consecutive union iff it has an adjacent selected pair of
distinct rank-nine facets of (V).

#### Proof

Every label in a segment whose union is (V) must be a rank-nine subset of
(V).  A segment has at least two labels.  Since the transversal contains
each label only once, any adjacent two labels in that segment are distinct
facets of (V), and two distinct rank-nine facets of a rank-ten set have
union (V).  The converse is immediate. \(\square\)

Lemmas 3.1 and 3.2 give a complete, solver-free catalogue: enumerate the
occurrences of the ten facets of (V), test their unions, and reject a pair
exactly when (3.1) supplies an intervening forced label.

## 4. The two-target opposite-choice core

The repeated label

\[
                          D=\mathtt{0x0dbd}
\]

has exactly two first-middle occurrences:

\[
 (9801,9805,D),\qquad(9967,9971,D).
\tag{4.1}
\]

The complete Lemma 3.1 catalogue gives:

\[
\begin{array}{c|c}
\text{rank-ten target}&\text{only viable adjacent occurrence pair}\\ \hline
\mathtt{0x0fbd}&
 \mathtt{0x0fb9}@9966\ \longrightarrow\ D@9967\\
\mathtt{0x4dbd}&
 D@9801\ \longrightarrow\ \mathtt{0x4db5}@9802\\
\mathtt{0x2dbd}&
 D@9967\ \longrightarrow\ \mathtt{0x2d9d}@9968.
\end{array}
\tag{4.2}
\]

In particular, `0x0fbd` forces the later occurrence of (D), whereas
`0x4dbd` forces the earlier occurrence.  A transversal may select only one
of them.

### Theorem 4.1 (scoped duplicate-owner compression no-go)

No selection of exactly one existing first-middle occurrence per rank-nine
label in `answers/k17_upper25746.word` represents both `0x0fbd` and
`0x4dbd` as consecutive unions of the selected owner word.

#### Proof

By Lemma 3.2 each target needs a viable adjacent facet pair.  The exhaustive
iff catalogue (4.2) says the former target selects (D@9967), while the
latter selects (D@9801).  This contradicts the one-occurrence choice for
(D). \(\square\)

The core is minimal in its target set: either target alone has the
transversal promised by Lemma 3.1.  The third row of (4.2) independently
reinforces the later choice but is not needed for the contradiction.

The literal word itself has exactly one physical interval for each of these
three targets:

\[
\begin{array}{c|c}
\mathtt{0x0fbd}&[9966,9971]\\
\mathtt{0x4dbd}&[9801,9806]\\
\mathtt{0x2dbd}&[9967,9972].
\end{array}
\tag{4.3}
\]

This explains why the opposite choices occur geometrically; (4.3) is not
needed for the abstract adjacency proof.

## 5. Witness reassignment is not physical deletion

Choosing one occurrence of a repeated label changes only the certificate.
It leaves every letter and every physical interval of the word untouched.
Deleting position (p), by contrast, changes every interval crossing
(p) and creates a new seam between its former neighbours.

A literal example is position (6394), whose value is `0x0368` and which
is the deadline of one occurrence of the repeated label `0x43ee`.  After
deleting that one physical letter, all (24,310) rank-nine labels still
occur.  Nevertheless the shortened word loses exactly

\[
 \{\mathtt{0x0368},\mathtt{0x2369},\mathtt{0x236d},
   \mathtt{0x436a},\mathtt{0x43ea}\}.
\tag{5.1}
\]

So even a deletion invisible to the entire middle-owner set is not a valid
universal-word compression.  Marginal duplicate ownership therefore cannot
be charged one-for-one to removable letters.

## 6. Common-cap consequence and exact boundary

For a fixed owner-subsequence compiler, upper transfer must be established
before lower common caps are chosen.  Theorem 4.1 fails that upper gate on
a two-target core.  Intersecting maximal envelopes with lower-target caps
cannot change which existing owner occurrence was selected and therefore
cannot resolve the opposite choice.

The theorem does **not** exclude a construction which changes the physical
letters or the first-middle chronology so that one of the rank-ten targets
gets a new facet adjacency.  That is exactly the structural operation a
rethreaded (K=17) carrier must perform.  No unrestricted claim about
\(\nu(17)\) follows from this fixed-source obstruction.

## 7. Reproducible audit

The independent audit is

```text
scratch/audit_k17_upper25746_duplicate_owner_opposite_choice_20260731.py
```

and its normalized output is

```text
scratch/k17_upper25746_duplicate_owner_opposite_choice_20260731.audit.json.
```

It reconstructs all first-middle occurrences from the literal word,
enumerates every candidate facet pair for the three rank-ten targets,
applies Lemma 3.1 literally, enumerates their physical interval witnesses,
and replays the deletion example against all (131,071) nonempty masks.

