# Exact omitted-colour flag-moment cut for `k=11`

## 1. General identity

Let the selected real graph be a Hamilton path on all rank-six subsets of
`[11]`.  Suppose its 461 edge intersections are all rank-five masks except
one omitted colour `C0`.  For `Q subseteq [11]`, `|Q|=q<=5`, let

```text
e_Q = number of the two real path endpoints containing Q,
H_Q = number of selected real edges (C,U) such that
      |Q minus C|=1 and Q subseteq U.
```

Here an edge has lower and upper flags

```text
C = X intersection Y,   |C|=5,
U = X union Y,          |U|=7.
```

Then

\[
 H_Q=
 2\binom{11-q}{6-q}-e_Q
 -2\left(\binom{11-q}{5-q}-\mathbf1_{Q\subseteq C_0}\right).
 \tag{1}
\]

### Proof

Sum selected degrees over all rank-six vertices containing `Q`.  There are
`binom(11-q,6-q)` such vertices, and a path endpoint among them loses one
unit of degree.  The degree sum is therefore

\[
 2\binom{11-q}{6-q}-e_Q.                 \tag{2}
\]

A selected flag edge `(C,U)` contributes two to this sum when `Q subseteq C`.
It contributes one exactly when `|Q minus C|=1` and `Q subseteq U`, and zero
otherwise.  Since every rank-five lower colour other than `C0` is selected
once, the number contributing two is

\[
 \binom{11-q}{5-q}-\mathbf1_{Q\subseteq C_0}.
\]

Equating this edge contribution with (2) proves (1).

No assumption about the second endpoint containing `C0` is valid or needed.
Indeed, the score-549 checkpoint has endpoints `63` and `504`; only `63`
contains `C0=31`.  Any specialization that writes both endpoints as
`C0 union {x}` is therefore unsound for the current search.

## 2. Cheap strongest specialization

After canonicalization,

```text
C0 = {0,1,2,3,4} = 31.
```

Take `Q=C0`.  The two binomial terms involving selected lower colours cancel:
the only rank-five set containing `C0` is `C0` itself, and it is omitted.
Equation (1) becomes

\[
 H_{C_0}+e_{C_0}=12.                     \tag{3}
\]

There is an even simpler graph proof.  Let `S` be the six rank-six supersets
of `C0`.  Every Johnson edge with both endpoints in `S` has intersection
`C0`, so none is selected.  Thus `S` is independent in the selected path.
Summing the degree-two equations of its six vertices counts exactly:

* once, every selected real edge crossing `S` to its complement; and
* once, every selected dummy edge marking a path endpoint in `S`.

The total is `2|S|=12`.  The crossing real edges are precisely the flags
counted by `H_C0`, proving (3).

The complete Johnson graph has 150 real cut edges at this flag plus six
possible dummy endpoint edges.  An explicit exact-12 counter over these 156
literals is small, while it exposes in one place a consequence otherwise
distributed across six degree encodings and fifteen forbidden internal
`C0` edges.

## 3. Implementation

With canonicalization active, set

```text
RECOMBINE_C0_MOMENT=1
```

to add exact equality (3).  The source constructs the support geometrically:
real selected edges with exactly one endpoint containing `C0`, plus dummy
edges at vertices containing `C0`.  It uses the audited exact truncated unary
counter for both the lower and upper cardinality bounds.

The option is rejected unless `k=11`, `rank=6`, and the WLOG omitted colour
is fixed to `C0=31`.  It is valid in both connected ordered searches and the
weaker degree-two cycle-cover relaxations; connectivity is not used in the
degree-sum proof.
