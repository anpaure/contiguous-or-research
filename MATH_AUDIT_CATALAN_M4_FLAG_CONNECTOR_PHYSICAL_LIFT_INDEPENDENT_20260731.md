# Independent audit of the varied-size \(m=4\) flag/connector physical lift

Date: 2026-07-31  
Status: **PASS**, finite positive certificate only

## 1. Literal object and quantifiers

Let

\[
 \mathcal L=\binom{[8]}3,\qquad
 \mathcal M=\binom{[8]}4,\qquad
 \mathcal U=\binom{[8]}5.
\]

The audited input consists of 56 literal flags \((L,U)\), with
\(L\in\mathcal L\), \(U\in\mathcal U\), and \(L\subset U\), and 14
literal unordered connector pairs in \(\mathcal M\).  The full arrays are
embedded in both the independent replay and its JSON.  They are not the
previous `3^7 7^7` item-2139 fixture.

The flags are a perfect inclusion matching: every member of
\(\mathcal L\) is a first coordinate once and every member of
\(\mathcal U\) is a second coordinate once.  This is a finite statement
about the displayed \(m=4\) object; it does not assert an all-dimension
matching construction.

## 2. Unique physical lift

For each flag \(L\subset U\), write \(U\setminus L=\{a,b\}\).  There is
exactly one unordered Johnson edge with intersection \(L\) and union
\(U\), namely

\[
             \{L\cup\{a\},L\cup\{b\}\}.              \tag{2.1}
\]

The replay also verifies uniqueness by enumerating all pairs of rank-four
sets, rather than merely evaluating (2.1).  The 56 resulting edges are
distinct.  Their graph \(F\subset J(8,4)\) spans all 70 rank-four sets and
has degree histogram

\[
                       1^{28}2^{42}.                    \tag{2.2}
\]

It is a linear forest with fourteen path components of vertex sizes

\[
 21,7,7,6,5,5,4,3,2,2,2,2,2,2.                       \tag{2.3}
\]

Because the flags are a perfect inclusion matching, the forest edges alone
use every lower colour and every upper colour exactly once.

## 3. Endpoint connector cycle

The fourteen displayed connectors are distinct Johnson edges.  Their 28
ends are exactly the 28 degree-one vertices of \(F\), each once, and every
connector joins two different forest components.  Contracting every path
of \(F\), the connectors form one 14-cycle.  With the audit's canonical
component numbering, one orientation of that cycle is

```text
0,4,8,11,2,1,3,5,10,13,12,6,7,9.
```

Consequently \(F\) plus the connectors is connected and two-regular on all
70 vertices: it is a Hamilton cycle in \(J(8,4)\).  Its canonical vertex
order has SHA-256

```text
189ed0e9e0333287a6c5e6b960fa06203564a63370cef27d8f6039481970af78
```

## 4. Exact connector-colour catalogue

The connector lower-colour multiplicities are

```text
13:1  26:1  29:1  2c:2  45:1  49:1  4a:1
52:1  83:1  85:1  91:1  98:1  a2:1
```

The repeated lower colour is literal:

```text
3c--2e and ac--6c both have intersection 2c.
```

The connector upper-colour multiplicities are

```text
3e:1  6d:1  76:2  79:1  b3:1  b5:1
b6:1  c7:1  cd:1  d9:1  da:2  ec:1
```

The two repetitions are

```text
66--36 and 72--56 both have union 76;
9a--d8 and ca--5a both have union da.
```

Since the internal forest already uses every colour once, these connector
repetitions do not destroy coverage.  The full Hamilton cycle has lower
load histogram

\[
                       1^{43}2^{12}3^1                 \tag{4.1}
\]

and upper load histogram

\[
                       1^{44}2^{10}3^2.                \tag{4.2}
\]

Thus both complete colour ranks remain covered.

This is strictly weaker than the frozen item-2139 uniformly directed
fixture.  Its fourteen connector colours are distinct on both shores, so
both of its full load histograms are \(1^{42}2^{14}\).  In particular, the
new frozen connector set cannot itself satisfy the distinct-cut-seam gate:
its connector lower colour `2c` occurs twice.  This does not exclude a
different connector closure of the same forest or a different forest.

## 5. Reproduction and lineage

Run

```bash
python3 scratch/audit_catalan_m4_flag_connector_lift_independent_20260731.py
```

Two independent executions were byte-identical.  Frozen hashes at audit
time are:

```text
independent replay
  7c825136a55e3f0cf12a3b996a9dea32980ff9ecd1262bfd04af1cc979c78a19
independent JSON
  a505dbe4e0d93eca2631b0949ddfe8d650bd71bbaedada2ea135f1d770781174
canonical payload
  3f2eeede08f432d06df74482d599ad3eb07bd65566130227269bbc8c966e1186
item-2139 comparison fixture
  e8eb60cf8401296d73fa7d39739fb85d70e7f921ecd9661548e2a768cb44f899
```

The producer file was observed transiently at
`scratch/audit_catalan_m4_two_sided_hamilton_carrier_20260731.py` with SHA
`e3c595d2...`, then disappeared during the independent audit.  It is not
used as a live dependency.  The authoritative literal arrays for this
audit are the copies frozen in the independent script and JSON.

## 6. Scope

This proves existence of one \(J(8,4)\) Hamilton cycle containing a
perfect lower/upper inclusion transversal and hence having immediate
complete lower and upper coverage.  It proves neither uniform outgoing
repair, a directed split-leave lift, a block-coherent recursion, nor an
all-\(m\) theorem.
