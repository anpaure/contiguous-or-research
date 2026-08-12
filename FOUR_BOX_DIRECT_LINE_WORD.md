# Direct four-box line trails

## 1. Outcome

Let

\[
 P=[0,a_1]\times[0,a_2]\times[0,a_3]\times[0,a_4]
\]

with coordinatewise maximum, and let

\[
 m_j=\#\{x\in P:|x|=j\}.
\]

There is a direct word, using the rank-\((r-1)\) points as entries, which
covers every point of ranks \(r-1\) and \(r\).  It does not prescribe a
middle row and then factor it.  The factor entries are the construction.

### Theorem 1 (two-rank line word)

For every integer \(2\le r\le a_1+a_2+a_3+a_4\), there is a nonzero word
of length

\[
             m_r+C_r,                                      \tag{1.1}
\]

whose singleton maxima cover rank \(r-1\) and whose singleton or adjacent
pair maxima cover rank \(r\).  Here

\[
 C_r=\#\{(c,d)\in[0,a_3]\times[0,a_4]:
       0\le r-1-c-d\le a_1+a_2\}                         \tag{1.2}
\]

is the number of nonempty transverse rank lines.  In particular,

\[
             C_r\le(a_3+1)(a_4+1).                         \tag{1.3}
\]

For the equal cube \(P_m=[0,m]^4\), with \(m\ge1\), at the middle rank
\(r=2m\),

\[
 C_{2m}=(m+1)^2-1=m^2+2m,                                \tag{1.4}
\]

and the word has the exact length

\[
 \boxed{M_m+m^2+2m},\qquad
 M_m=[z^{2m}](1+z+\cdots+z^m)^4.                          \tag{1.5}
\]

Thus the whole middle layer and its lower neighbor admit a direct
width-plus-surface construction.  This evades the intact-middle-row and
natural-core factor obstructions.

## 2. Construction

Fix \((c,d)\in[0,a_3]\times[0,a_4]\), and put

\[
 K=r-1-c-d,
 \qquad
 L=\max(0,K-a_2),
 \qquad
 U=\min(a_1,K).                                      \tag{2.1}
\]

When \(L\le U\), form the line word

\[
 W_{c,d}=
 (L,K-L,c,d),(L+1,K-L-1,c,d),\ldots,(U,K-U,c,d).    \tag{2.2}
\]

Concatenate all nonempty words \(W_{c,d}\), in any order.  Every
rank-\((r-1)\) point occurs exactly once in this concatenation.

For consecutive letters

\[
 v_t=(t,K-t,c,d),\qquad v_{t+1}=(t+1,K-t-1,c,d),
\]

we have

\[
 v_t\vee v_{t+1}=(t+1,K-t,c,d).                    \tag{2.3}
\]

The right side has rank \(r\) and has positive first and second
coordinates.  Conversely, every rank-\(r\) point
\(z=(z_1,z_2,z_3,z_4)\) with \(z_1,z_2>0\) occurs uniquely in (2.3), by
taking

\[
 c=z_3,\quad d=z_4,\quad K=z_1+z_2-1,\quad t=z_1-1. \tag{2.4}
\]

Append literally every remaining rank-\(r\) point, namely every one with
\(z_1=0\) or \(z_2=0\).  This finishes the construction.

## 3. Exact length proof

Let \(C_r\) be the number of nonempty line words.  Since the line words
partition rank \(r-1\), their total number of letters is \(m_{r-1}\).
Their internal adjacent pairs number

\[
                         m_{r-1}-C_r.                \tag{3.1}
\]

By the bijection (2.3)--(2.4), this is exactly the number of rank-\(r\)
points with positive first and second coordinates.  Therefore the number
of rank-\(r\) points appended literally is

\[
                         m_r-m_{r-1}+C_r.            \tag{3.2}
\]

The total length is consequently

\[
 m_{r-1}+(m_r-m_{r-1}+C_r)=m_r+C_r,                \tag{3.3}
\]

proving Theorem 1.  Cross-line and line-to-literal intervals create only
additional maxima and cannot destroy the displayed witnesses.

For \(P_m\) and \(r=2m\), a line is nonempty exactly when
\(c+d\le2m-1\).  Among the \((m+1)^2\) pairs only \((m,m)\) fails, which
gives (1.4).

The adjacent rank count is also explicit:

\[
 m_{2m-1}=M_m-(m+1).                                \tag{3.4}
\]

This agrees with (3.2): the number of literal middle points is
\(m^2+3m+1\).

## 4. All longer intervals are classified

The construction automatically covers a substantial upper family.

### Theorem 2 (line-interval criterion)

Let \(y=(y_1,y_2,c,d)\in P\) have rank

\[
                         |y|=r-1+s,\qquad s\ge0.     \tag{4.1}
\]

Put \(K=r-1-c-d\) and define \(L,U\) by (2.1).  Then \(y\) is the maximum
of a contiguous interval of \(W_{c,d}\) if and only if

\[
                         L+s\le y_1\le U.            \tag{4.2}
\]

### Proof

For \(L\le p\le q\le U\), direct calculation gives

\[
 \bigvee_{t=p}^{q}(t,K-t,c,d)=(q,K-p,c,d).          \tag{4.3}
\]

To obtain \(y\), the endpoints are forced:

\[
 q=y_1,\qquad p=K-y_2=y_1-s.                        \tag{4.4}
\]

The conditions \(L\le p\le q\le U\) are exactly (4.2), because
\(s\ge0\).  This proves the criterion.  \(\square\)

For the equal cube at \(r=2m\), (4.2) simplifies symmetrically to

\[
                         \boxed{y_1\ge s,\quad y_2\ge s}.   \tag{4.5}
\]

Indeed, the feasible line has

\[
 L=\max(0,K-m),\qquad U=\min(m,K),
\]

and the box constraints together with
\(y_1+y_2=K+s\) turn (4.2) into (4.5).  Hence the same word covers, for
every \(s\ge0\), every rank-\((2m-1+s)\) target whose first two coordinates
are at least \(s\).

Equivalently, a target at depth \(d\ge0\) above the middle rank is covered
whenever

\[
                         y_1,y_2\ge d+1.             \tag{4.6}

This exact family is useful when several coordinate-pair line systems are
superposed or assigned by sectors.

## 5. Boundary size and a shallow-band corollary

At rank \(2m-1+s\), the targets missed by the fixed pair \(\{1,2\}\) lie
in

\[
                         \{y_1<s\}\cup\{y_2<s\}.    \tag{5.1}

For each fixed value of one coordinate, the other three coordinates are
determined by two free coordinates.  Therefore

\[
 \#\{y:|y|=2m-1+s,\ y_1<s\text{ or }y_2<s\}
 \le2s(m+1)^2.                                      \tag{5.2}

Appending these exceptions literally for \(0\le s\le q\) gives a word
covering all targets in those \(q+1\) consecutive ranks, of length at most

\[
 M_m+m^2+2m+q(q+1)(m+1)^2.                         \tag{5.3}

This is width plus \(o(m^3)\) whenever \(q=o(\sqrt m)\).  It is only a
shallow-band result; iterating (5.3) over \(\Theta(m/q)\) bands would repeat
the width-scale core and is not a full four-box construction.

## 6. Relation to hypergraph Euler tours

Let the vertices of a hypergraph be the rank-\((r-1)\) points, and let the
hyperedge indexed by a rank-\(r\) point \(z\) be its set of lower covers.
Choosing two lower covers of every \(z\) and trail-decomposing the resulting
graph is exactly the rank-two universal-cycle or hypergraph-Euler
formulation.

The construction above gives an explicit Euler family for the bulk
hyperedges \(z_1,z_2>0\): its components are precisely the line paths
\(W_{c,d}\).  It therefore obtains the needed \(O(m^2)\) component bound
directly, without invoking a general hypergraph Euler theorem.  The
nonuniform boundary hyperedges are the literal rank-\(r\) exceptions.

## 7. Exact scope

Proved here:

* a direct \(m_r+C_r\) word for two adjacent ranks of every four-chain box;
* exact middle length \(M_m+m^2+2m\) in the equal cube;
* an explicit \(O(m^2)\)-component bulk Euler family; and
* the complete longer-interval criterion (4.2), including the upper family
  (4.6).

Not proved here:

* coverage of the full lower half below rank \(2m-1\);
* coverage of upper targets failing every assigned line-pair condition;
* a superposition of several coordinate-pair line systems without
  repeating a width-scale layer; or
* the desired full estimate \(g_4(P_m)=M_m+o(m^3)\).

The next positive target is a **sector assignment of line directions**:
partition the middle layer among coordinate pairs so that the resulting
monochromatic line segments retain the required upper intervals, while the
same lower-entry word recursively supplies deeper lower ranks.  The theorem
above proves that the first derivative layer and every fixed-pair shallow
upper cone already have the correct width-plus-surface cost.

## 8. Finite audit

The independent enumerator

```
python3 scratch/verify_four_box_direct_line_word.py 4
```

checks every ordered side tuple in \([0,4]^4\) and every rank \(r\ge2\).
For each instance it verifies:

* the line partition of rank \(r-1\);
* the bijection between internal line edges and rank-\(r\) points with
  positive first two coordinates;
* the exact length \(m_r+C_r\);
* coverage of both designated ranks after concatenation;
* equality between all actual within-line interval maxima and criterion
  (4.2); and
* the equal-cube formula (1.5).

The current exhaustive result is

```
PASS: 4376 rectangular-box/rank instances through side 4
```
